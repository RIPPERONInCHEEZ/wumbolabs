#!/usr/bin/env python3
"""sync_labs.py — deterministic WumboLabs publication sync (v3, central source).

Materializes the pinned central registry into data/labs-registry.json, with
stable model_id / profile_id / event_id identity, then consumes each generated
event's canonical website-publication export (schema wumbolabs-labs-publication/1),
validates identity, and renders:

  - exactly ONE canonical Evaluation model page per model_id
    (content/evaluations/<model_id>.md, aggregating all of the model's profiles
    and events, current state first);
  - compatibility redirect stubs for superseded event-style Labs URLs
    (served at /labs/<old-slug>/ via a page path override, meta-refreshing to
    /evaluations/<model_id>/#<event_id>);
  - the Cloudflare Pages _redirects file (static/_redirects) covering retired
    /labs/ URLs and every old model-page URL;
  - a machine-readable route migration map
    (data/generated/route-migration.json);
  - machine-readable generated data (data/generated/labs-models.json,
    labs-events.json for event chronology, and labs-freshness.json
    provenance).

Contract (documented in docs/labs-publication-workflow.md):
    one model_id        = one canonical Evaluation page
    one profile_id      = one materially distinct tested scientific surface
    one event_id        = one dated evidence event on the model page
    one profile may contain many events; one model may contain many profiles

The website is a DERIVATIVE of canonical public evidence. This script never
invents canonical URLs: an export whose canonical_evidence state is
PENDING_HUMAN_GATE renders with an explicit evidence-pending state.

Usage (from the repository root):
    python scripts/sync_labs.py
    python scripts/sync_labs.py --check   (verify only, no writes)
    python scripts/sync_labs.py selftest

Exit codes: 0 ok; 1 structural/data error; 2 usage error.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

REGISTRY_PATH = Path("data/labs-registry.json")
EVENT_BODIES = Path("data")  # hand-authored event bodies resolve under data/
GENERATED_MODELS = Path("data/generated/labs-models.json")
GENERATED_EVENTS = Path("data/generated/labs-events.json")
GENERATED_FRESHNESS = Path("data/generated/labs-freshness.json")
GENERATED_ROUTE_MIGRATION = Path("data/generated/route-migration.json")
EVALUATIONS_PAGES = Path("content/evaluations")
RECORDS_PAGES = Path("content/records")  # hand-maintained technical records
REDIRECTS_FILE = Path("static/_redirects")
BASE = Path(".")  # repository root; all repo-relative paths resolve against this

# Hand-maintained pre-Evaluations redirect lines, preserved verbatim so the
# generated _redirects file stays the single complete source of route
# compatibility (sync rewrites the whole file deterministically).
HISTORICAL_REDIRECT_LINES = [
    "/lab-notes/ /records/ 301",
    "/benchmarks/ /records/ 301",
    "/lab-notes/wumbolabs-first-build/ /records/wumbolabs-first-build/ 301",
    "/benchmarks/local-llm-baseline/ /records/local-llm-baseline/ 301",
    "/benchmarks/mellum2-agent-backend-test/ /records/mellum2-agent-backend-test/ 301",
    "/lab-notes/gemma-12b-practical-use/ /records/gemma-12b-practical-use/ 301",
    "/benchmarks/gemma-12b-practical-use-v1/ /records/gemma-12b-practical-use/ 301",
]

EXPORT_SCHEMA = "wumbolabs-labs-publication/1"
DISPOSITIONS = {"WEBSITE_READY", "WEBSITE_BLOCKED", "NOT_FOR_PUBLICATION", "WEBSITE_PUBLISHED"}
EVIDENCE_STATES = {"PUBLISHED", "PENDING_HUMAN_GATE"}
REGISTRY_PUBLICATION_STATES = {"published", "evidence-pending-human-gate"}
PROFILE_STATUSES = {"current", "current-alternate", "historical", "superseded", "specialized"}
EVENT_TYPES = {
    "initial-evaluation", "welp-recharacterization", "profile-canonical-promotion",
    "context-envelope-completion", "follow-up", "specialized-test",
    "practical-use-comparison", "benchmark-only", "profile-optimization", "integration-test",
}
# Evidence maturity labels (census vocabulary). Required on every registry entry
# since the 2026-09-12 full-evidence census; displayed verbatim on model pages.
MATURITIES = {
    "CURRENT_WELP", "FULL_EVALUATION", "HISTORICAL_EVALUATION", "PARTIAL_EVALUATION",
    "SPECIALIZED_TEST", "BENCHMARK_ONLY", "PRACTICAL_USE", "PROFILE_OPTIMIZATION",
    "CONTEXT_COMPLETION", "RELIABILITY_TEST", "PROTOCOL_BLOCKED", "EARLY_STOP",
    "INTEGRATION_TEST", "UNRESOLVED_HISTORICAL",
}
REQUIRED_EXPORT_KEYS = [
    "schema", "campaign", "disposition", "model", "artifact", "runtime",
    "hardware", "welp", "context", "quality", "localmaxxing",
    "canonical_evidence", "public_summary",
]
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9.-]*$")
EVENT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")

# Evidence surfaces understood by the current-state precedence rule. A later
# event only supersedes the surfaces its evidence_scope declares (context-only
# completions never replace classification/reliability/capabilities).
SURFACES = {
    "model-classification", "reliability", "capabilities", "context",
    "performance", "serving-profile", "localmaxxing", "protocol-development",
    # census additions: bounded testing surfaces that never supersede the
    # canonical WELP surfaces above
    "specialized", "practical-use", "agent-backend",
}


def fail(message: str) -> "NoReturn":  # type: ignore[valid-type]
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def safe_rel_path(value: Any, field: str, slug: str) -> Path:
    if not isinstance(value, str) or not value:
        fail(f"registry entry {slug!r}: {field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        fail(f"registry entry {slug!r}: {field} must not be absolute or contain '..': {value!r}")
    return path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_registry() -> dict[str, Any]:
    registry_path = BASE / REGISTRY_PATH
    if not registry_path.is_file():
        fail(f"registry not found: {registry_path}")
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"registry is invalid JSON: {exc}")
    if registry.get("version") not in (2, 3):
        fail(f"unsupported registry version: {registry.get('version')!r}")
    models = registry.get("models")
    if not isinstance(models, list) or not models:
        fail("registry must contain a non-empty models list")
    if not isinstance(registry.get("records"), list) or not registry["records"]:
        fail("registry must contain a non-empty records list")
    return registry


def validate_registry(registry: dict[str, Any]) -> None:
    model_ids: set[str] = set()
    for model in registry["models"]:
        mid = model.get("model_id")
        if not isinstance(mid, str) or not ID_RE.fullmatch(mid):
            fail(f"registry model has invalid model_id {mid!r}")
        if mid in model_ids:
            fail(f"duplicate registry model_id: {mid!r}")
        if not isinstance(model.get("display_name"), str) or not model["display_name"].strip():
            fail(f"registry model {mid!r}: display_name is required")
        model_ids.add(mid)

    slugs: set[str] = set()
    event_ids: set[str] = set()
    legacy_urls: dict[str, str] = {}
    profile_models: dict[str, str] = {}
    declared_profiles = {p["profile_id"]: p for p in registry.get("profiles", [])}
    for entry in registry["records"]:
        slug = entry.get("slug")
        if not slug or not isinstance(slug, str):
            fail("registry entry missing slug")
        if slug in slugs:
            fail(f"duplicate registry slug: {slug!r}")
        slugs.add(slug)

        eid = entry.get("event_id")
        if not isinstance(eid, str) or not EVENT_ID_RE.fullmatch(eid):
            fail(f"registry entry {slug!r}: invalid event_id {eid!r}")
        if eid in event_ids:
            fail(f"duplicate registry event_id: {eid!r} (slug {slug!r})")
        event_ids.add(eid)

        mid = entry.get("model_id")
        if mid not in model_ids:
            fail(f"registry entry {slug!r}: model_id {mid!r} is not declared in registry models "
                 "(model events must aggregate into a declared model; technical records stay "
                 "out of this registry entirely)")
        pid = entry.get("profile_id")
        if not isinstance(pid, str) or not ID_RE.fullmatch(pid):
            fail(f"registry entry {slug!r}: invalid profile_id {pid!r}")
        if entry.get("event_type") not in EVENT_TYPES:
            fail(f"registry entry {slug!r}: invalid event_type {entry.get('event_type')!r}; "
                 f"expected one of {sorted(EVENT_TYPES)}")
        for field in ("event_date", "record_date"):
            if not isinstance(entry.get(field), str) or not DATE_RE.fullmatch(entry[field]):
                fail(f"registry entry {slug!r}: {field} must be YYYY-MM-DD")
        if entry.get("publication_state") not in REGISTRY_PUBLICATION_STATES:
            fail(f"registry entry {slug!r}: invalid publication_state {entry.get('publication_state')!r}")
        if entry.get("profile_status") is not None and entry["profile_status"] not in PROFILE_STATUSES:
            fail(f"registry entry {slug!r}: invalid profile_status {entry['profile_status']!r}")
        scope = entry.get("evidence_scope")
        if not isinstance(scope, list) or not scope or not all(s in SURFACES for s in scope):
            fail(f"registry entry {slug!r}: evidence_scope must be a non-empty list of {sorted(SURFACES)}")
        maturity = entry.get("evidence_maturity")
        if maturity not in MATURITIES:
            fail(f"registry entry {slug!r}: evidence_maturity must be one of {sorted(MATURITIES)}")

        related_models = entry.get("related_model_ids") or []
        shared_notes = entry.get("shared_model_notes") or {}
        if not isinstance(related_models, list) or \
                any(mid not in model_ids for mid in related_models):
            fail(f"registry entry {slug!r}: related_model_ids must all be declared registry models")
        if set(shared_notes) - set(related_models):
            fail(f"registry entry {slug!r}: shared_model_notes keys must be listed in related_model_ids")
        if related_models and not entry.get("shared_event_id"):
            fail(f"registry entry {slug!r}: related_model_ids entries require a shared_event_id")
        related_profiles = entry.get("related_profile_ids") or []
        if not isinstance(related_profiles, list):
            fail(f"registry entry {slug!r}: related_profile_ids must be a list")

        # Scientific identity is independent of repository topology.
        if profile_models.setdefault(pid, mid) != mid:
            fail(f"profile_id {pid!r} belongs to conflicting models")
        if registry["version"] == 3:
            if pid not in declared_profiles or declared_profiles[pid]["model_id"] != mid:
                fail(f"registry entry {slug!r}: unknown or cross-model profile")
            evidence = entry.get("canonical_evidence") or {}
            if evidence.get("repo") != "WumboLabs/evaluations" or not re.fullmatch(
                    r"[0-9a-f]{40}", str(evidence.get("commit", ""))):
                fail(f"registry entry {slug!r}: canonical evidence requires central repo and full commit")
            safe_rel_path(evidence.get("path"), "canonical_evidence.path", slug)

        authoring = entry.get("authoring")
        if authoring == "hand-authored":
            body_rel = safe_rel_path(entry.get("event_body"), "event_body", slug)
            if not (BASE / EVENT_BODIES / body_rel).is_file():
                fail(f"hand-authored event body missing for {slug!r}: data/{body_rel}")
        elif authoring == "generated":
            if not isinstance(entry.get("source"), dict):
                fail(f"registry entry {slug!r}: generated entries require a source pin")
        else:
            fail(f"registry entry {slug!r}: authoring must be hand-authored or generated")

        for url in entry.get("legacy_urls") or []:
            if url in legacy_urls:
                fail(f"legacy URL {url!r} declared twice ({legacy_urls[url]!r} and {slug!r})")
            seg_match = re.fullmatch(r"/labs/([^/]+)/", url)
            if seg_match and (seg_match.group(1) in model_ids
                              or seg_match.group(1) in {url_slug(m) for m in model_ids}):
                fail(f"legacy URL {url!r} collides with a canonical model page URL")
            legacy_urls[url] = slug


def validate_export(raw: bytes, origin: str) -> dict[str, Any]:
    try:
        export = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"{origin}: export is not valid UTF-8 JSON: {exc}")
    if not isinstance(export, dict):
        fail(f"{origin}: export must be a JSON object")
    if export.get("schema") != EXPORT_SCHEMA:
        fail(f"{origin}: unsupported schema {export.get('schema')!r}; expected {EXPORT_SCHEMA!r}")
    missing = [k for k in REQUIRED_EXPORT_KEYS if k not in export]
    if missing:
        fail(f"{origin}: export missing required keys: {', '.join(missing)}")
    disposition = export.get("disposition")
    if disposition not in DISPOSITIONS:
        fail(f"{origin}: invalid disposition {disposition!r}; expected one of {sorted(DISPOSITIONS)}")
    if disposition in ("WEBSITE_BLOCKED", "NOT_FOR_PUBLICATION") and not export.get("reason"):
        fail(f"{origin}: {disposition} requires a reason")
    display_name = (export.get("model") or {}).get("display_name")
    if not isinstance(display_name, str) or not display_name.strip():
        fail(f"{origin}: model.display_name is required")
    evidence = export.get("canonical_evidence")
    if not isinstance(evidence, dict) or evidence.get("state") not in EVIDENCE_STATES:
        fail(f"{origin}: canonical_evidence.state must be one of {sorted(EVIDENCE_STATES)}")
    current = evidence.get("repo") == "WumboLabs/evaluations" or "path" in evidence
    if current and evidence["state"] == "PUBLISHED":
        if evidence.get("repo") != "WumboLabs/evaluations" or not re.fullmatch(r"[0-9a-f]{40}", evidence.get("commit", "")):
            fail(f"{origin}: current evidence requires central repo and full commit SHA")
        path = evidence.get("path", "")
        if not isinstance(path, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*(/[A-Za-z0-9][A-Za-z0-9._-]*)*", path):
            fail(f"{origin}: current evidence requires a safe relative path")
        url = f"https://github.com/WumboLabs/evaluations/blob/{evidence['commit']}/{path}"
        if evidence.get("url") not in (None, url):
            fail(f"{origin}: current evidence URL disagrees with its immutable citation")
        evidence["url"] = url
    elif evidence["state"] == "PUBLISHED" and not evidence.get("url"):
        fail(f"{origin}: legacy PUBLISHED evidence requires url")
    if evidence["state"] == "PENDING_HUMAN_GATE" and (evidence.get("url") or "commit" in evidence or "path" in evidence):
        fail(f"{origin}: PENDING_HUMAN_GATE must not claim a published citation")
    if current:
        identity = export.get("identity")
        if not isinstance(identity, dict) or any(not identity.get(k) for k in ("model_id", "profile_id", "event_id", "event_type")):
            fail(f"{origin}: current publication requires model/profile/event identity")
    lmx = export.get("localmaxxing")
    if not isinstance(lmx, dict) or not lmx.get("status"):
        fail(f"{origin}: localmaxxing.status is required")
    if not isinstance(export.get("public_summary"), str) or not export["public_summary"].strip():
        fail(f"{origin}: public_summary must be a non-empty string")
    return export


def resolve_source(entry: dict[str, Any], local_exports: Path | None) -> tuple[bytes, dict[str, Any]]:
    """Return (raw export bytes, provenance) for a generated record entry."""
    source = entry.get("source") or {}
    kind = source.get("kind")
    provenance: dict[str, Any] = {"kind": kind}
    if kind in ("local-export", "repository-cache"):
        source_root = BASE if kind == "repository-cache" else local_exports
        if source_root is None:
            fail(f"registry entry {entry.get('slug')!r} needs --local-exports DIR to resolve source.file")
        rel = safe_rel_path(source.get("file"), "source.file", entry["slug"])
        path = source_root / rel
        if not path.is_file():
            fail(f"local export not found for {entry.get('slug')!r}: {path}")
        raw = path.read_bytes()
        expected = source.get("sha256")
        if not expected:
            fail(
                f"registry entry {entry.get('slug')!r}: local-export source requires a "
                "sha256 pin pinning the exact export bytes consumed"
            )
        actual = sha256_bytes(raw)
        if expected != actual:
            fail(
                f"local export hash mismatch for {entry.get('slug')!r}: "
                f"registry pins {expected}, file is {actual} ({path}). "
                "Update the registry pin deliberately, never silently."
            )
        provenance.update({"file": rel.as_posix(), "sha256": actual})
        if kind == "repository-cache":
            if source.get("repo") != "WumboLabs/evaluations" or not re.fullmatch(
                    r"[0-9a-f]{40}", str(source.get("ref", ""))):
                fail(f"registry entry {entry['slug']!r}: invalid central cache pin")
            safe_rel_path(source.get("path"), "source.path", entry["slug"])
            provenance.update({k: source[k] for k in ("repo", "ref", "path")})
            provenance["resolved_commit"] = source["ref"]
            provenance["url"] = f"https://raw.githubusercontent.com/{source['repo']}/{source['ref']}/{source['path']}"
        return raw, provenance
    if kind == "github-raw":
        import urllib.error
        import urllib.request

        repo, ref = source.get("repo"), source.get("ref", "main")
        path = source.get("path")
        if not (repo and path):
            fail(f"registry entry {entry.get('slug')!r}: github-raw source needs repo and path")
        url = f"https://raw.githubusercontent.com/{repo}/{ref}/{path}"
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                if response.status != 200:
                    fail(f"fetch failed for {url} with HTTP status {response.status}")
                raw = response.read()
        except urllib.error.URLError as exc:
            fail(f"fetch failed for {url}: {exc}")
        if source.get("sha256") and sha256_bytes(raw) != source["sha256"]:
            fail(f"github source hash mismatch for {entry['slug']!r}")
        provenance.update({"repo": repo, "ref": ref, "path": path, "url": url,
                           "sha256": sha256_bytes(raw)})
        if re.fullmatch(r"[0-9a-f]{40}", str(ref)):
            # the pin already is the exact commit; no resolution (or API call) needed
            provenance["resolved_commit"] = ref
            return raw, provenance
        api_url = f"https://api.github.com/repos/{repo}/commits/{ref}"
        try:
            req = urllib.request.Request(api_url, headers={"Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=20) as response:
                commit = json.loads(response.read().decode("utf-8"))
            provenance["resolved_commit"] = commit.get("sha")
        except (urllib.error.URLError, json.JSONDecodeError) as exc:
            fail(f"could not resolve commit SHA for {repo}@{ref}: {exc}")
        return raw, provenance
    fail(f"registry entry {entry.get('slug')!r}: unsupported source kind {kind!r}")


def fmt(value: Any, default: str = "not recorded") -> str:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return "YES" if value else "NO"
    return str(value)


def fmt_tokens(value: Any) -> str:
    return f"{value:,} tokens" if isinstance(value, int) else fmt(value)


def url_slug(model_id: str) -> str:
    """Public URL slug for a model page.

    Zola's default path slugification rewrites '.' to '-', so the published
    route of a model page is /labs/<slug(model_id)>/. Verified against the
    live site: /labs/lfm2.5-1.2b/ -> /labs/lfm2-5-1-2b/.
    """
    return model_id.replace(".", "-")


def shift_headings(markdown: str) -> str:
    out = []
    in_fence = False
    for line in markdown.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("#"):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def render_generated_event_body(entry: dict[str, Any], export: dict[str, Any]) -> str:
    """Render the immutable per-event detail (export derivative) for inlining."""
    slug = entry["slug"]
    model = export["model"]
    artifact = export["artifact"]
    runtime = export["runtime"]
    hardware = export["hardware"]
    welp = export["welp"]
    ctx = export["context"]
    perf = export.get("performance") or {}
    quality = export["quality"]
    lmx = export["localmaxxing"]
    evidence = export["canonical_evidence"]
    pending = evidence["state"] == "PENDING_HUMAN_GATE"
    date = entry.get("record_date") or export.get("publication_date") or ""

    lines: list[str] = []
    if pending:
        proposed = evidence.get("proposed_repo")
        lines.append("> **Evidence publication pending.** Canonical public evidence for this")
        lines.append("> record has not been published yet"
                     + (f" (proposed repository: `{proposed}`)" if proposed else "") + ".")
        lines.append("> This section is a local derivative prepared ahead of publication; no")
        lines.append("> canonical evidence URL is claimed. The listed measurements come from")
        lines.append("> the accepted local WELP campaign named below.")
        lines.append("")

    campaign = export.get("campaign", "")
    lines.append("#### Identity")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f'| Model | {fmt(model.get("display_name"))} |')
    lines.append(f'| Producer | {fmt(model.get("producer"))} |')
    if model.get("official_id"):
        lines.append(f'| Official model | {model["official_id"]}'
                     + (f' @ `{model["official_revision"]}`' if model.get("official_revision") else "") + " |")
    lines.append(f'| Tested artifact | {fmt(artifact.get("tested"))} |')
    lines.append(f'| Precision | {fmt(artifact.get("precision"))} |')
    if artifact.get("sha256"):
        sha = artifact["sha256"]
        if re.fullmatch(r"[a-f0-9]{64}", str(sha)):
            lines.append(f'| Artifact SHA-256 | `{sha}` |')
        else:
            lines.append(f'| Artifact hash evidence | {sha} |')
    lines.append(f'| Campaign | `{campaign}` |')
    lines.append(f'| Record date | {date} |')
    lines.append("")

    lines.append("#### Runtime and hardware")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f'| Engine | {fmt(runtime.get("engine"))} |')
    lines.append(f'| Runtime version | {fmt(runtime.get("version"))} |')
    if runtime.get("notes"):
        lines.append(f'| Runtime notes | {runtime["notes"]} |')
    gpu = fmt(hardware.get("gpu"))
    machine = hardware.get("machine")
    hw = f"{machine} ({gpu})" if machine else gpu
    lines.append(f'| Hardware | {hw} |')
    if hardware.get("notes"):
        lines.append(f'| Hardware notes | {hardware["notes"]} |')
    lines.append("")

    lines.append("#### WELP outcome")
    lines.append("")
    lines.append(f'- **Outcome:** {fmt(welp.get("outcome"))}')
    lines.append(f'- **Classification:** {fmt(welp.get("classification"))}')
    if welp.get("artifact_classification"):
        lines.append(f'- **Artifact classification:** {welp["artifact_classification"]}')
    lines.append("")
    lines.append("Publication state: **%s** — %s" % (
        "evidence pending human gate" if pending else "published",
        "canonical public evidence is not yet published; this record shows an explicit pending state"
        if pending else f'canonical evidence: {evidence.get("url")}',
    ))
    lines.append("")

    lines.append("#### Context profile")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f'| Practical default | {fmt(ctx.get("practical_default_tokens"))} tokens |')
    lines.append(f'| Guarded context | {fmt(ctx.get("guarded_tokens"))} tokens |')
    lines.append(f'| Native model-card maximum | {fmt(ctx.get("native_maximum_tokens"))} tokens |')
    lines.append(f'| Model-card envelope complete | {fmt(ctx.get("envelope_complete"))} |')
    lines.append(f'| Native maximum disposition | {fmt(ctx.get("native_maximum_disposition"))} |')
    lines.append("")

    if perf:
        lines.append("#### Headline performance")
        lines.append("")
        lines.append("| Surface | TTFT | Prefill | Decode |")
        lines.append("|---|---|---|---|")
        short_ttft = perf.get("short_ttft_s")
        short_dec = perf.get("short_decode_tps")
        mod = perf.get("moderate_input_tokens")
        lines.append("| Short | %s | — | %s |" % (
            f"{short_ttft:g} s" if isinstance(short_ttft, (int, float)) else "not recorded",
            f"{short_dec:g} tok/s" if isinstance(short_dec, (int, float)) else "not recorded"))
        mod_ttft = perf.get("moderate_ttft_s")
        mod_pre = perf.get("moderate_prefill_tps")
        mod_dec = perf.get("moderate_decode_tps")
        lines.append("| Moderate (%s-token input) | %s | %s | %s |" % (
            fmt(mod, "unspecified"),
            f"{mod_ttft:g} s" if isinstance(mod_ttft, (int, float)) else "not recorded",
            f"{mod_pre:g} tok/s" if isinstance(mod_pre, (int, float)) else "not recorded",
            f"{mod_dec:g} tok/s" if isinstance(mod_dec, (int, float)) else "not recorded"))
        if perf.get("surface_note"):
            lines.append("")
            lines.append(f"<p><small>{perf['surface_note']}</small></p>")
        lines.append("")

    lines.append("#### Quality and capabilities")
    lines.append("")
    lines.append(f'- **Constrained result:** {fmt(quality.get("constrained_result"))}')
    for cap in quality.get("capability_highlights") or []:
        lines.append(f"- {cap}")
    lines.append("")
    lines.append("##### Guardrails and limitations")
    lines.append("")
    for guard in quality.get("key_guardrails") or []:
        lines.append(f"- {guard}")
    lines.append("")
    lines.append(f'**Reliability:** {fmt(quality.get("reliability_summary"))}')
    lines.append("")

    lines.append("#### LocalMaxxing")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f'| Status | {fmt(lmx.get("status"))} |')
    lines.append(f'| Canonical context | {fmt(lmx.get("canonical_context_tokens"))} tokens |')
    lines.append(f'| tok/s out | {fmt(lmx.get("tok_s_out"))} |')
    lines.append(f'| TTFT | %s |' % (f"{lmx['ttft_ms']:g} ms" if isinstance(lmx.get("ttft_ms"), (int, float)) else "not recorded"))
    lines.append(f'| Submission reference | {fmt(lmx.get("submission_ref"))} |')
    lines.append(f'| verifiedRun | {fmt(lmx.get("verified_run"), "null (not claimed)")} |')
    if lmx.get("note"):
        lines.append("")
        lines.append(f"<p><small>{lmx['note']}</small></p>")
    lines.append("")

    lines.append("#### Canonical evidence")
    lines.append("")
    if pending:
        lines.append("State: **PENDING_HUMAN_GATE** — the canonical public evidence repository")
        lines.append("has not been published yet. This section intentionally claims no canonical")
        lines.append("evidence URL. Once the evidence repository is published and the registry is")
        lines.append("updated, this record synchronizes against it and the pending state is removed.")
    else:
        lines.append(f'Canonical public evidence: <{evidence["url"]}>')
    lines.append("")
    lines.append("This event section is a human-readable derivative of the accepted local WELP")
    lines.append("campaign evidence named above; the campaign's REPORT.md is the authoritative")
    lines.append("scientific source. Results are bounded by the tested artifact, runtime,")
    lines.append("hardware, configuration, and protocol snapshot, and are not universal model")
    lines.append("rankings.")
    lines.append("")
    return "\n".join(lines)


def hand_authored_event_body(entry: dict[str, Any]) -> str:
    rel = safe_rel_path(entry.get("event_body"), "event_body", entry["slug"])
    path = BASE / EVENT_BODIES / rel
    return path.read_text(encoding="utf-8").rstrip() + "\n"


def event_body(entry: dict[str, Any], exports: dict[str, dict[str, Any]]) -> str:
    if entry.get("authoring") == "generated":
        # stored heading level is already nested; shift the fresh render once
        return shift_headings(render_generated_event_body(entry, exports[entry["slug"]]))
    return hand_authored_event_body(entry)


def current_event(entries: list[dict[str, Any]], surface: str) -> dict[str, Any] | None:
    """Latest event whose evidence_scope covers `surface`.

    Deterministic precedence: greatest event_date wins; ties break on the
    lexicographically greatest slug. A later event can only supersede the
    surfaces it declares.
    """
    cands = [e for e in entries if surface in (e.get("evidence_scope") or [])]
    if not cands:
        return None
    return max(cands, key=lambda e: (e["event_date"], e["slug"]))


def recommended_profile(entries: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Profile of the latest serving-profile event; fallback: latest practical-use
    event; final fallback: latest event overall. Benchmark-only or specialized
    events must not masquerade as the recommended practical surface."""
    e = current_event(entries, "serving-profile") or \
        current_event(entries, "practical-use") or \
        max(entries, key=lambda e: (e["event_date"], e["slug"]))
    return e


def anchor_link(entry: dict[str, Any]) -> str:
    title = entry.get("event_title") or entry.get("event_id")
    return f'[{title} ({entry["event_date"]})](/evaluations/{url_slug(entry["model_id"])}#{entry["event_id"]})'


def latest_evidence_date(entries: list[dict[str, Any]]) -> str | None:
    """Newest authoritative event date for one model's evidence."""
    return max((e["event_date"] for e in entries), default=None)


def render_model_page(model: dict[str, Any], entries: list[dict[str, Any]],
                      exports: dict[str, dict[str, Any]], catalog_weight: int,
                      shared_for_model: list[dict[str, Any]] | None = None) -> str:
    mid = model["model_id"]
    display = model["display_name"]
    entries_sorted = sorted(entries, key=lambda e: (e["event_date"], e["slug"]), reverse=True)
    cls_event = current_event(entries, "model-classification")
    ctx_event = current_event(entries, "context")
    rec_event = recommended_profile(entries)
    latest = entries_sorted[0]
    profile_events: dict[str, list[dict[str, Any]]] = {}
    for e in entries:
        profile_events.setdefault(e["profile_id"], []).append(e)
        # a shared single event can test several profiles of one model (e.g. a
        # fit test covering an Instruct variant and its Thinking sibling); the
        # related profiles appear as tested surfaces with the same event.
        for rpid in e.get("related_profile_ids") or []:
            profile_events.setdefault(rpid, []).append(e)

    # ordered profiles: current first, then by most recent event
    def profile_sort_key(pid: str) -> tuple[int, str]:
        status = next(e.get("profile_status") or "current" for e in profile_events[pid])
        latest_date = max(e["event_date"] for e in profile_events[pid])
        return (0 if status == "current" else 1, latest_date)

    profile_ids = sorted(profile_events, key=profile_sort_key, reverse=False)
    profile_ids.sort(key=lambda pid: profile_sort_key(pid))
    # stable: profile_sort_key sorts by (status-current, latest_date); reverse=False keeps
    # current first. Do not double-sort (kept explicit for clarity).

    desc = (f"{display} — the current WumboLabs evidence state on one page: tested profiles, "
            "validated context, and the full chronological testing history. Each value is "
            "attributed to the profile and event that measured it.")

    lines: list[str] = []
    lines.append("+++")
    lines.append(f'title = "{display}"')
    lines.append(f'description = "{desc}"')
    lines.append('template = "lab_model.html"')
    lines.append(f"weight = {catalog_weight}")
    lines.append("")
    lines.append("[extra]")
    lines.append("kind = \"model\"")
    lines.append(f'model_id = "{mid}"')
    lines.append(f'vendor = "{fmt(model.get("vendor"))}"')
    if cls_event:
        lines.append(f'classification = "{fmt(cls_event.get("welp_status"))}"')
    if rec_event:
        lines.append(f'recommended_profile_id = "{rec_event["profile_id"]}"')
        lines.append(f'recommended_profile_name = "{fmt(rec_event.get("profile_name"))}"')
    ctx_export = exports.get(ctx_event["slug"]) if ctx_event else None
    if ctx_export and isinstance(ctx_export.get("context"), dict):
        c = ctx_export["context"]
        if isinstance(c.get("practical_default_tokens"), int):
            practical = f"{c['practical_default_tokens']:,} default"
            if isinstance(c.get("guarded_tokens"), int):
                practical += f" / {c['guarded_tokens']:,} guarded"
            lines.append(f'practical_context = "{practical} tokens"')
    lines.append(f"profile_count = {len(profile_ids)}")
    lines.append(f"event_count = {len(entries)}")
    lines.append(f'latest_evidence_date = {latest["event_date"]}')
    lines.append("+++")
    lines.append("")

    lines.append(
        f"WumboLabs tests **{display}** on real consumer hardware. This is the canonical "
        f"model page: current state first, then every tested profile and every evidence "
        "event. Values are attributed to the profile and event that measured them; "
        "historical findings remain the evidence of their tested stack and are never "
        "silently replaced.")
    lines.append("")

    # ---- current state ----
    lines.append("## Current state")
    lines.append("")
    if cls_event:
        lines.append(f'- **Classification:** {fmt(cls_event.get("welp_status"))} '
                     f"— {anchor_link(cls_event)}, profile {cls_event.get('profile_name')}")
    if rec_event:
        repo_url = (rec_event.get("canonical_evidence") or {}).get("url", "")
        lines.append(f'- **Recommended profile:** {fmt(rec_event.get("profile_name"))} '
                     f'(`{rec_event["profile_id"]}`, {rec_event.get("profile_status")})'
                     + (f" — [canonical evidence]({repo_url})" if repo_url else ""))
    if ctx_export and isinstance(ctx_export.get("context"), dict) \
            and isinstance(ctx_export["context"].get("practical_default_tokens"), int):
        c = ctx_export["context"]
        practical = f"{c['practical_default_tokens']:,} default"
        if isinstance(c.get("guarded_tokens"), int):
            practical += f" / {c['guarded_tokens']:,} guarded"
        extra = ""
        if isinstance(c.get("native_maximum_tokens"), int):
            extra = f"; native model-card maximum {c['native_maximum_tokens']:,}"
            if c.get("envelope_complete") is not None:
                extra += f" (envelope complete: {fmt(c['envelope_complete'])})"
        lines.append(f'- **Practical context:** {practical} tokens{extra} — {anchor_link(ctx_event)}')
    lines.append(f'- **Latest evidence:** {latest["event_date"]} — {latest.get("event_title")}')
    lines.append("")

    # ---- tested profiles ----
    lines.append("## Tested profiles")
    lines.append("")
    for pid in profile_ids:
        pevents = sorted(profile_events[pid], key=lambda e: (e["event_date"], e["slug"]), reverse=True)
        first = pevents[0]
        status = first.get("profile_status") or "current"
        lines.append(f'### {fmt(first.get("profile_name"))} — {status.upper()}')
        lines.append("")
        lines.append(f'Profile identity: `{pid}`.')
        lines.append("")
        exports_for_profile = [exports[e["slug"]] for e in pevents if e["slug"] in exports]
        if exports_for_profile:
            ex = exports_for_profile[0]
            art, rt = ex["artifact"], ex["runtime"]
            lines.append("| Field | Value |")
            lines.append("|---|---|")
            lines.append(f'| Runtime | {fmt(rt.get("engine"))}'
                         + (f' {rt.get("version")}' if rt.get("version") else "") + " |")
            lines.append(f'| Artifact | {fmt(art.get("tested"))} |')
            lines.append(f'| Precision | {fmt(art.get("precision"))} |')
            lines.append("")
        else:
            lines.append("Runtime and artifact identity are described inside the event "
                         "sections below (hand-authored records; no machine-readable export).")
            lines.append("")
        status_line = {
            "current": "current canonical/recommended tested surface",
            "current-alternate": "validated alternate tested surface",
            "historical": "historical tested surface; retained evidence, not the recommended profile",
            "superseded": "superseded by a materially different accepted profile",
            "specialized": "specialized tested surface",
        }[status]
        lines.append(f"Status: {status_line}.")
        lines.append("")
        repo_url = (first.get("canonical_evidence") or {}).get("url", "")
        if repo_url:
            lines.append(f"[Canonical Evidence]({repo_url})")
            metadata_url = first.get("profile_metadata_urls", {}).get(pid)
            if metadata_url:
                lines.append(f"[Profile Metadata]({metadata_url})")
        lines.append("")
        lines.append("Events on this profile:")
        lines.append("")
        for e in pevents:
            lines.append(f"- {anchor_link(e)} — {fmt(e.get('welp_status'))}")
        lines.append("")

    # ---- testing history ----
    lines.append("## Testing history")
    lines.append("")
    lines.append("Newest first. Each event is one immutable testing/publication event; the "
                 "exact scientific report lives in the canonical evidence repository linked "
                 "at the top of each event.")
    lines.append("")
    for e in entries_sorted:
        lines.append(f'<a id="{e["event_id"]}"></a>')
        lines.append("")
        lines.append(f'### {e["event_date"]} — {fmt(e.get("event_title"))}')
        lines.append("")
        ev_url = (e.get("canonical_evidence") or {}).get("url", "")
        meta = [f'**{fmt(e.get("event_kicker"))}**', f'profile: {e.get("profile_name")}']
        if e.get("evidence_maturity"):
            meta.append(f'maturity: {e["evidence_maturity"]}')
        if e.get("welp_status"):
            meta.append(f'status: {e["welp_status"]}')
        if e.get("related_profile_ids"):
            meta.append("related profiles: " + ", ".join(f'`{p}`' for p in e["related_profile_ids"]))
        line = " · ".join(meta)
        lines.append(line)
        if ev_url:
            lines.append("")
            lines.append(f"[Canonical Evidence / Full Report]({ev_url})")
            if e.get("model_evidence_url"):
                lines.append(f"[View on GitHub]({e['model_evidence_url']})")
            for pid in e.get("related_profile_ids", []):
                url = e.get("profile_metadata_urls", {}).get(pid)
                if url:
                    lines.append(f"[Profile Metadata: {pid}]({url})")
        report_page = e.get("report_page")
        if report_page:
            report_url = f"/{report_page[:-3]}/" if report_page.endswith(".md") else report_page
            report_title = e.get("report_title") or "Long-form campaign report"
            lines.append("")
            lines.append(f"[Long-form report: {report_title}]({report_url})")
        lines.append("")
        lines.append(event_body(e, exports).rstrip())
        lines.append("")

    if shared_for_model:
        lines.append("## Shared comparison events")
        lines.append("")
        lines.append("This model appears in shared multi-model comparisons. Each report is "
                     "stored once in WumboLabs/evaluations/shared-events/; the model's "
                     "measured entries remain attributed to the same historical event:")
        lines.append("")
        for s in sorted(shared_for_model, key=lambda x: (x["entry"]["event_date"], x["entry"]["slug"])):
            e = s["entry"]
            note = s.get("note")
            lines.append(f"- {anchor_link(e)}"
                         + (f" — {note}" if note else "")
                         + (f" — [Canonical Evidence / Full Report]({e['canonical_evidence']['url']})"
                            if e.get("canonical_evidence", {}).get("url") else ""))
        lines.append("")

    lines.append("## Canonical evidence")
    lines.append("")
    lines.append("All canonical public evidence lives in WumboLabs/evaluations. Each event "
                 "links an immutable full-commit/path citation; each profile remains a "
                 "distinct scientific identity, not a separate repository.")
    lines.append("")
    for pid in profile_ids:
        first = profile_events[pid][0]
        url = first.get("profile_metadata_urls", {}).get(pid) or \
            (first.get("canonical_evidence") or {}).get("url", "")
        if url:
            lines.append(f"- **{pid}**: [Profile Metadata]({url})")
    legacy_sources = {
        (source["repo"], source["commit"], source["path"])
        for e in entries for source in e.get("legacy_sources", [])
    }
    if legacy_sources:
        lines.extend(["", "### Legacy provenance", ""])
        for repo, commit, path in sorted(legacy_sources):
            lines.append(f"- [{repo} @ `{commit}`](https://github.com/{repo}/blob/{commit}/{path})")
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def render_stub(entry: dict[str, Any], old_slug: str) -> str:
    """Compatibility page served at the legacy /labs/<old-slug>/ URL.

    Cloudflare Pages _redirects cannot target fragments, so event-style legacy
    URLs keep real HTML pages (path override) that meta-refresh to the event
    anchor on the canonical Evaluation page.
    """
    target = f"/evaluations/{url_slug(entry['model_id'])}/#{entry['event_id']}"
    display = entry.get("event_title") or entry.get("event_id")
    lines = [
        "+++",
        f'title = "{display} (moved)"',
        'description = "Compatibility page. This evidence event now lives on the canonical '
        'Evaluation page for its model."',
        'template = "redirect.html"',
        f'path = "/labs/{old_slug}/"',
        "",
        "weight = 1000",
        "[extra]",
        "redirect_page = true",
        f'redirect_to = "{target}"',
        "+++",
        "",
        f"This record moved to the canonical Evaluation page: [{display}]({target}).",
        "",
    ]
    return "\n".join(lines)


def write_if_changed(path: Path, content: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_models_data(models: list[dict[str, Any]],
                      page_meta: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "version": 1,
        "generated_by": "scripts/sync_labs.py (model-centric) from data/labs-registry.json",
        "models": [
            {
                "model_id": m["model_id"],
                "display_name": m["display_name"],
                "page": f"/evaluations/{url_slug(m['model_id'])}/",
                **page_meta.get(m["model_id"], {}),
            }
            for m in models
        ],
    }


def build_events_data(registry: dict[str, Any], exports: dict[str, dict[str, Any]]) -> dict[str, Any]:
    models = {m["model_id"]: m for m in registry["models"]}
    events = []
    for entry in registry["records"]:
        export = exports.get(entry["slug"])
        evidence = entry.get("canonical_evidence") or {}
        hardware = entry.get("hardware")
        headline = entry.get("headline")
        if export:
            hw = export["hardware"]
            gpu = fmt(hw.get("gpu"))
            machine = hw.get("machine")
            hardware = f"{machine} ({gpu})" if machine else gpu
            headline = export.get("record_description") or export["public_summary"]
        events.append({
            "event_id": entry["event_id"],
            "slug": entry["slug"],
            "model_id": entry["model_id"],
            "model": models[entry["model_id"]]["display_name"],
            "event_type": entry.get("event_type"),
            "event_kicker": entry.get("event_kicker"),
            "event_title": entry.get("event_title"),
            "profile_id": entry.get("profile_id"),
            "profile_name": entry.get("profile_name"),
            "date": entry.get("record_date"),
            "event_date": entry.get("event_date"),
            "status": entry.get("welp_status"),
            "evidence_maturity": entry.get("evidence_maturity"),
            "shared_event_id": entry.get("shared_event_id"),
            "related_model_ids": entry.get("related_model_ids"),
            "hardware": hardware,
            "headline": headline,
            "evidence_url": evidence.get("url"),
            "evidence_state": evidence.get("state"),
            "model_url": f"/evaluations/{url_slug(entry['model_id'])}/",
            "report_page": entry.get("report_page"),
        })
    return {
        "version": 1,
        "generated_by": "scripts/sync_labs.py (model-centric) from data/labs-registry.json",
        "events": events,
    }


def build_redirects(models: list[dict[str, Any]], registry: dict[str, Any]) -> str:
    """Deterministic Cloudflare Pages _redirects content.

    The retired /labs/ section root and every old canonical model-page URL are
    permanent redirects here. Event-style legacy URLs are NOT listed: they keep
    real HTML stub pages so the fragment in their compatibility target
    (/evaluations/<model>/#<event>) survives — _redirects cannot express fragments.
    """
    lines = [
        "# Generated by scripts/sync_labs.py — legacy route compatibility.",
        "# Do not edit by hand; changes belong in the sync script/registry.",
        "# Historical (pre-2026-09) address changes:",
        *HISTORICAL_REDIRECT_LINES,
        "# 2026-09-12 Evaluations consolidation (/labs/ -> /evaluations/):",
        "/labs/ /evaluations/ 301",
    ]
    for model in sorted(models, key=lambda m: (m.get("weight") or 0, m["model_id"])):
        slug = url_slug(model["model_id"])
        lines.append(f"/labs/{slug}/ /evaluations/{slug}/ 301")
    return "\n".join(lines) + "\n"


def technical_record_slugs() -> list[str]:
    """Hand-maintained technical record pages (URLs preserved, no redirects)."""
    if not (BASE / RECORDS_PAGES).is_dir():
        return []
    return sorted(p.stem for p in (BASE / RECORDS_PAGES).glob("*.md") if p.name != "_index.md")


def build_route_migration(models: list[dict[str, Any]],
                          registry: dict[str, Any]) -> dict[str, Any]:
    """Machine-readable old-URL -> new-URL map (see handoff contract §15)."""
    mappings: list[dict[str, Any]] = [
        {"old_url": "/labs/", "content_type": "section-index", "model_id": None,
         "event_id": None, "new_url": "/evaluations/",
         "mechanism": "cloudflare-redirects", "http_status": 301},
    ]
    for model in sorted(models, key=lambda m: (m.get("weight") or 0, m["model_id"])):
        slug = url_slug(model["model_id"])
        mappings.append({
            "old_url": f"/labs/{slug}/", "content_type": "model-page",
            "model_id": model["model_id"], "event_id": None,
            "new_url": f"/evaluations/{slug}/",
            "mechanism": "cloudflare-redirects", "http_status": 301,
        })
    for entry in registry["records"]:
        for url in entry.get("legacy_urls") or []:
            mappings.append({
                "old_url": url, "content_type": "event-url",
                "model_id": entry["model_id"], "event_id": entry["event_id"],
                "new_url": (f"/evaluations/{url_slug(entry['model_id'])}/"
                            f"#{entry['event_id']}"),
                "mechanism": "html-stub-meta-refresh", "http_status": 200,
            })
    # /records/ is the canonical Reports index and remains a normal Zola route.
    for slug in technical_record_slugs():
        mappings.append({
            "old_url": f"/records/{slug}/", "content_type": "technical-record",
            "model_id": None, "event_id": None, "new_url": f"/records/{slug}/",
            "mechanism": "url-preserved", "http_status": 200,
        })
    return {
        "version": 1,
        "generated_by": "scripts/sync_labs.py (model-centric) from data/labs-registry.json",
        "mappings": mappings,
    }


def run(local_exports: Path | None, check_only: bool) -> int:
    registry = load_registry()
    validate_registry(registry)

    exports: dict[str, dict[str, Any]] = {}
    provenance: dict[str, dict[str, Any]] = {}
    blocked: list[str] = []
    for entry in registry["records"]:
        if entry.get("authoring") != "generated":
            continue
        raw, prov = resolve_source(entry, local_exports)
        export = validate_export(raw, f"record {entry['slug']!r}")
        export_slug = export.get("website_record_slug")
        if export_slug != entry["slug"]:
            fail(
                f"record {entry['slug']!r}: export website_record_slug {export_slug!r} "
                "does not match the registry slug (invalid evidence relationship)"
            )
        ident = export.get("identity")
        if isinstance(ident, dict):
            for key, reg_key in (("model_id", "model_id"), ("profile_id", "profile_id"),
                                 ("event_id", "event_id")):
                if ident.get(key) and ident[key] != entry.get(reg_key):
                    fail(
                        f"record {entry['slug']!r}: export identity {key}={ident.get(key)!r} "
                        f"does not match the registry ({entry.get(reg_key)!r})"
                    )
        if registry["version"] == 3:
            # Legacy export bytes remain immutable. Only the rendered citation topology changes.
            export["canonical_evidence"] = dict(entry["canonical_evidence"], state="PUBLISHED")
        exports[entry["slug"]] = export
        provenance[entry["slug"]] = prov
        if export["canonical_evidence"]["state"] == "PENDING_HUMAN_GATE":
            blocked.append(entry["slug"])

    models_by_id = {m["model_id"]: m for m in registry["models"]}
    entries_by_model: dict[str, list[dict[str, Any]]] = {}
    for entry in registry["records"]:
        entries_by_model.setdefault(entry["model_id"], []).append(entry)
    shared_by_model: dict[str, list[dict[str, Any]]] = {}
    for entry in registry["records"]:
        for mid in entry.get("related_model_ids") or []:
            shared_by_model.setdefault(mid, []).append({
                "entry": entry,
                "note": (entry.get("shared_model_notes") or {}).get(mid),
            })

    changed: list[str] = []
    unchanged: list[str] = []
    outputs: list[Path] = []

    def record_output(path: Path, content: str) -> None:
        if check_only:
            is_changed = not path.is_file() or path.read_text(encoding="utf-8") != content
        else:
            is_changed = write_if_changed(path, content)
            outputs.append(path)
        (changed if is_changed else unchanged).append(str(path))

    page_meta: dict[str, dict[str, Any]] = {}
    for model in registry["models"]:
        mid = model["model_id"]
        entries = entries_by_model.get(mid) or []
        related_pids = {rp for e in entries for rp in (e.get("related_profile_ids") or [])}
        page_meta[mid] = {
            "classification": (current_event(entries, "model-classification") or {}).get("welp_status"),
            "profile_count": len({e["profile_id"] for e in entries} | related_pids),
            "event_count": len(entries),
            "latest_evidence_date": latest_evidence_date(entries),
        }

    dated_models = [
        model for model in registry["models"]
        if page_meta[model["model_id"]]["latest_evidence_date"] is not None
    ]
    dated_models.sort(key=lambda model: model["display_name"].casefold())
    dated_models.sort(
        key=lambda model: page_meta[model["model_id"]]["latest_evidence_date"],
        reverse=True,
    )
    undated_models = sorted(
        (model for model in registry["models"]
         if page_meta[model["model_id"]]["latest_evidence_date"] is None),
        key=lambda model: model["display_name"].casefold(),
    )
    catalog_models = dated_models + undated_models

    for catalog_weight, model in enumerate(catalog_models, start=1):
        mid = model["model_id"]
        entries = entries_by_model.get(mid) or []
        record_output(BASE / EVALUATIONS_PAGES / f"{url_slug(mid)}.md",
                      render_model_page(model, entries, exports, catalog_weight,
                                        shared_by_model.get(mid)))

    for entry in registry["records"]:
        for url in entry.get("legacy_urls") or []:
            old_slug = url.rstrip("/").rsplit("/", 1)[-1]
            record_output(BASE / EVALUATIONS_PAGES / f"{old_slug}.md", render_stub(entry, old_slug))

    redirects_content = build_redirects(registry["models"], registry)
    migration_data = build_route_migration(registry["models"], registry)

    models_data = build_models_data(catalog_models, page_meta)
    events_data = build_events_data(registry, exports)
    freshness = {
        "version": 2,
        "generated_by": "scripts/sync_labs.py (model-centric)",
        "source_identities": {
            slug: {k: v for k, v in prov.items() if k != "kind"} | {"kind": prov.get("kind")}
            for slug, prov in provenance.items()
        },
        "latest_represented_campaigns": [
            {"slug": slug, "campaign": exports[slug].get("campaign")}
            for slug in sorted(exports)
        ],
        "pending_public_evidence": list(blocked),
        "models": len(registry["models"]),
        "model_events": len(registry["records"]),
    }

    outputs_list = (
        (GENERATED_MODELS, json.dumps(models_data, indent=2, ensure_ascii=False) + "\n"),
        (GENERATED_EVENTS, json.dumps(events_data, indent=2, ensure_ascii=False) + "\n"),
        (GENERATED_FRESHNESS, json.dumps(freshness, indent=2, ensure_ascii=False) + "\n"),
        (GENERATED_ROUTE_MIGRATION, json.dumps(migration_data, indent=2, ensure_ascii=False) + "\n"),
        (REDIRECTS_FILE, redirects_content),
    )
    for path, serial in outputs_list:
        record_output(BASE / path, serial)

    print("Labs publication sync (model-centric) %s" % ("CHECK" if check_only else "complete"))
    print(f"models:                {len(registry['models'])}")
    print(f"model events:          {len(registry['records'])} "
          f"({sum(1 for e in registry['records'] if e.get('authoring') == 'hand-authored')} hand-authored, "
          f"{len(exports)} generated)")
    print(f"outputs changed:       {len(changed)}" + (f" {sorted(changed)}" if changed else ""))
    print(f"outputs unchanged:     {len(unchanged)}")
    print(f"records blocked:       {len(blocked)} (evidence pending) {sorted(blocked)}")
    if outputs:
        print("outputs:")
        for path in outputs:
            print(f"  {path}")
    return 1 if check_only and changed else 0


def registry_entry_publication_state(registry: dict[str, Any], slug: str) -> str | None:
    for entry in registry["records"]:
        if entry.get("slug") == slug:
            return entry.get("publication_state")
    return None


def selftest() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        failures: list[str] = []

        def mk_export(slug: str, campaign: str, *, engine: str, artifact: str, precision: str,
                      classification: str, default: int, guarded: int, disposition: str,
                      summary: str) -> dict[str, Any]:
            return {
                "schema": EXPORT_SCHEMA,
                "campaign": campaign,
                "publication_date": "2026-01-02",
                "disposition": "WEBSITE_READY",
                "model": {"display_name": slug, "producer": "Tester"},
                "artifact": {"tested": artifact, "precision": precision},
                "runtime": {"engine": engine, "version": "v1"},
                "hardware": {"machine": "TestBench", "gpu": "Test GPU 12GB"},
                "welp": {"outcome": "PASS — SELFTEST", "classification": classification},
                "context": {"practical_default_tokens": default, "guarded_tokens": guarded,
                            "native_maximum_tokens": 262144, "envelope_complete": disposition,
                            "native_maximum_disposition": "test"},
                "quality": {"constrained_result": "7/7", "capability_highlights": ["cap"],
                            "key_guardrails": ["guard"], "reliability_summary": "20/20"},
                "localmaxxing": {"status": "NOT_ELIGIBLE", "reason": "selftest"},
                "canonical_evidence": {"state": "PUBLISHED", "url": f"https://example.com/{slug}"},
                "website_record_slug": slug,
                "record_description": summary,
                "public_summary": summary,
            }

        def write_export(exports_dir: Path, slug: str, export: dict[str, Any]) -> dict[str, Any]:
            (exports_dir / slug).mkdir(parents=True, exist_ok=True)
            data = json.dumps(export, indent=2) + "\n"
            (exports_dir / slug / "website-publication.json").write_text(data)
            return {"kind": "local-export", "file": f"{slug}/website-publication.json",
                    "sha256": sha256_bytes(data.encode())}

        exports_dir = root / "exports"

        # model-a: TWO profiles (qwen38-like). hand-authored profile-a1 event;
        # generated full-characterization (p2) + later context-only completion (p2).
        hand_body = "### Hand-authored identity\n\nBounded hand-authored evidence body.\n"
        (root / "data" / "labs-events").mkdir(parents=True)
        (root / "data" / "labs-events" / "initial-evaluation.md").write_text(hand_body)

        base_a2 = mk_export("a2-baseline", "a2-baseline-campaign", engine="llama.cpp",
                            artifact="a2.gguf", precision="Q8",
                            classification="READY_WITH_GUARDRAILS", default=32768, guarded=65536,
                            disposition=False, summary="A2 baseline characterization.")
        ctx_a2 = mk_export("a2-context", "a2-context-campaign", engine="llama.cpp",
                           artifact="a2.gguf", precision="Q8",
                           classification="MODEL-CARD CONTEXT ENVELOPE COMPLETE",
                           default=32768, guarded=98304, disposition=True,
                           summary="A2 context envelope completion.")
        src_a2_base = write_export(exports_dir, "a2-baseline", base_a2)
        src_a2_ctx = write_export(exports_dir, "a2-context", ctx_a2)

        # model-b: single profile, two generated events, record_date preserved (qwen35-like)
        base_b = mk_export("b1-baseline", "b1-baseline-campaign", engine="llama.cpp",
                           artifact="b1.gguf", precision="BF16",
                           classification="READY_WITH_GUARDRAILS", default=32768, guarded=65536,
                           disposition=False, summary="B1 baseline characterization.")
        ctx_b = mk_export("b1-context", "b1-context-campaign", engine="llama.cpp",
                          artifact="b1.gguf", precision="BF16",
                          classification="MODEL-CARD CONTEXT ENVELOPE COMPLETE",
                          default=32768, guarded=98304, disposition=True,
                          summary="B1 context envelope completion.")
        src_b_base = write_export(exports_dir, "b1-baseline", base_b)
        # the qwen35-style public record was updated in place: the record keeps
        # its original slug while consuming the completion export
        ctx_b["website_record_slug"] = "b1"
        src_b_ctx = write_export(exports_dir, "b1-context", ctx_b)

        registry = {
            "version": 2,
            "models": [
                {"model_id": "model-a", "display_name": "Model A", "vendor": "V", "weight": 1},
                {"model_id": "model-b", "display_name": "Model B", "vendor": "V", "weight": 2},
            ],
            "records": [
                {"slug": "a1", "event_id": "initial-evaluation-2026-01-01", "event_type": "initial-evaluation",
                 "event_date": "2026-01-01", "record_date": "2026-01-01", "model_id": "model-a",
                 "profile_id": "model-a-p1", "profile_name": "P1 legacy", "profile_status": "historical",
                 "profile_repo": "WumboLabs/eval-model-a-p1", "event_kicker": "Initial Evaluation",
                 "event_title": "Initial evaluation", "welp_status": "COMPLETED_DEEP_EVALUATION",
                 "evidence_maturity": "FULL_EVALUATION",
                 "evidence_scope": ["model-classification", "reliability", "capabilities", "context", "performance"],
                 "authoring": "hand-authored", "event_body": "labs-events/initial-evaluation.md",
                 "publication_state": "published",
                 "canonical_evidence": {"state": "published", "url": "https://example.com/a1"}},
                {"slug": "a2-baseline", "event_id": "profile-canonical-promotion-2026-01-02",
                 "event_type": "profile-canonical-promotion", "event_date": "2026-01-02",
                 "record_date": "2026-01-02", "model_id": "model-a", "profile_id": "model-a-p2",
                 "profile_name": "P2 current", "profile_status": "current",
                 "profile_repo": "WumboLabs/eval-model-a-p2", "event_kicker": "Profile promotion",
                 "event_title": "Profile promotion", "welp_status": "CURRENT_CANONICAL_PROFILE",
                 "evidence_maturity": "CURRENT_WELP",
                 "evidence_scope": ["serving-profile", "performance", "localmaxxing"],
                 "authoring": "generated", "source": src_a2_base, "publication_state": "published",
                 "canonical_evidence": {"state": "published", "url": "https://example.com/a2-baseline"}},
                {"slug": "a2-context", "event_id": "context-envelope-completion-2026-01-03",
                 "event_type": "context-envelope-completion", "event_date": "2026-01-03",
                 "record_date": "2026-01-03", "model_id": "model-a", "profile_id": "model-a-p2",
                 "profile_name": "P2 current", "profile_status": "current",
                 "profile_repo": "WumboLabs/eval-model-a-p2", "event_kicker": "Context Envelope",
                 "event_title": "Context envelope completion", "welp_status": "GUARDED",
                 "evidence_maturity": "CONTEXT_COMPLETION",
                 "evidence_scope": ["context"],
                 "authoring": "generated", "source": src_a2_ctx, "publication_state": "published",
                 "canonical_evidence": {"state": "published", "url": "https://example.com/a2-context"},
                 "legacy_urls": ["/labs/a2-context/"]},
                {"slug": "b1", "event_id": "context-envelope-completion-2026-01-02-b1",
                 "event_type": "context-envelope-completion", "event_date": "2026-01-02",
                 "record_date": "2026-01-01", "model_id": "model-b", "profile_id": "model-b-p1",
                 "profile_name": "B profile", "profile_status": "current",
                 "profile_repo": "WumboLabs/eval-model-b", "event_kicker": "Context Envelope",
                 "event_title": "Context envelope completion", "welp_status": "READY_WITH_GUARDRAILS",
                 "evidence_maturity": "CONTEXT_COMPLETION",
                 "evidence_scope": ["context"],
                 "authoring": "generated", "source": src_b_ctx, "publication_state": "published",
                 "canonical_evidence": {"state": "published", "url": "https://example.com/b1"}},
            ],
        }

        # technical-record exclusion fixture: an entry without a declared model must be rejected
        def run_and_expect_failure(label: str, mutate) -> None:
            bad = json.loads(json.dumps(registry))
            mutate(bad)
            REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
            REGISTRY_PATH.write_text(json.dumps(bad, indent=2) + "\n")
            try:
                run(root / "exports", check_only=False)
                failures.append(f"selftest: {label} not rejected")
            except SystemExit as exc:
                if exc.code != 1:
                    failures.append(f"selftest: {label} exit {exc.code}")
            REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        global REGISTRY_PATH, GENERATED_MODELS, GENERATED_EVENTS, GENERATED_FRESHNESS, EVALUATIONS_PAGES, BASE
        global GENERATED_ROUTE_MIGRATION, REDIRECTS_FILE
        orig = (REGISTRY_PATH, GENERATED_MODELS, GENERATED_EVENTS, GENERATED_FRESHNESS,
                EVALUATIONS_PAGES, GENERATED_ROUTE_MIGRATION, REDIRECTS_FILE, BASE)
        BASE = root
        REGISTRY_PATH = root / "data" / "labs-registry.json"
        GENERATED_MODELS = root / "data" / "generated" / "labs-models.json"
        GENERATED_EVENTS = root / "data" / "generated" / "labs-events.json"
        GENERATED_FRESHNESS = root / "data" / "generated" / "labs-freshness.json"
        GENERATED_ROUTE_MIGRATION = root / "data" / "generated" / "route-migration.json"
        EVALUATIONS_PAGES = root / "content" / "evaluations"
        REDIRECTS_FILE = root / "static" / "_redirects"
        (root / "content" / "evaluations").mkdir(parents=True)
        (root / "content" / "records").mkdir(parents=True)
        (root / "static").mkdir(parents=True)
        REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 1. valid sync: one Evaluation page per model, profiles grouped, events inlined
        run(root / "exports", check_only=False)
        page_a = root / "content" / "evaluations" / "model-a.md"
        page_b = root / "content" / "evaluations" / "model-b.md"
        generated_pages = sorted(p.name for p in (root / "content" / "evaluations").glob("*.md"))
        if not page_a.is_file() or not page_b.is_file():
            failures.append("selftest: model pages missing")
        if generated_pages != ["a2-context.md", "model-a.md", "model-b.md"]:
            failures.append(f"selftest: unexpected evaluations outputs {generated_pages} "
                            "(must be exactly one page per model + legacy stubs)")
        a_text = page_a.read_text() if page_a.is_file() else ""
        a_front = a_text.split("+++")[1] if a_text.startswith("+++") else ""
        if "model-a-p1" not in a_text or "model-a-p2" not in a_text:
            failures.append("selftest: multi-profile grouping missing on model page")
        for anchor in ("initial-evaluation-2026-01-01", "profile-canonical-promotion-2026-01-02",
                       "context-envelope-completion-2026-01-03"):
            if f'<a id="{anchor}"></a>' not in a_text:
                failures.append(f"selftest: event anchor {anchor} missing on model page")
        if "/labs/" in a_text:
            failures.append("selftest: canonical model page must not link legacy /labs/ URLs")
        if "\npath = " in a_front:
            failures.append("selftest: canonical model page must live at its /evaluations/ route")

        # 2. current-state precedence: classification from the full-characterization
        #    hand-authored event; context from the later context-only completion.
        if "- **Classification:** COMPLETED_DEEP_EVALUATION" not in a_text:
            failures.append("selftest: classification must come from the classification-scope event")
        if "98,304 default" in a_text or "32,768 default / 98,304 guarded" not in a_text:
            failures.append("selftest: practical context must come from the context-scope event")

        # 3. redirect stub content: served at the legacy /labs/ URL, targets the
        #    /evaluations/ model page + event anchor
        stub = root / "content" / "evaluations" / "a2-context.md"
        if stub.is_file():
            s = stub.read_text()
            if 'redirect_to = "/evaluations/model-a/#context-envelope-completion-2026-01-03"' not in s:
                failures.append("selftest: legacy URL stub does not target Evaluation page + anchor")
            if 'path = "/labs/a2-context/"' not in s:
                failures.append("selftest: legacy stub must keep serving at its /labs/ URL")
        else:
            failures.append("selftest: legacy URL stub missing")

        # 4. events dataset: chronology + model context + report merge field
        events = json.loads(GENERATED_EVENTS.read_text())["events"]
        if len(events) != 4:
            failures.append("selftest: events dataset must contain every model event exactly once")
        if [e["date"] for e in sorted(events, key=lambda x: x["date"])] != \
           ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-03"]:
            failures.append("selftest: record_date chronology not preserved")
        b_events = [e for e in events if e["model_id"] == "model-b"]
        if len(b_events) != 1 or b_events[0]["headline"] != "B1 context envelope completion.":
            failures.append("selftest: qwen35-style in-place record must stay one event row")
        if any(not e["model_url"].startswith("/evaluations/") for e in events):
            failures.append("selftest: events dataset model_url must be the /evaluations/ page")

        # 5. generated _redirects: Labs section root + model pages 301; event-style
        # URLs stay HTML stubs (not listed)
        redirects = (root / "static" / "_redirects").read_text()
        for required in ("/labs/ /evaluations/ 301",
                         "/labs/model-a/ /evaluations/model-a/ 301",
                         "/labs/model-b/ /evaluations/model-b/ 301"):
            if required not in redirects:
                failures.append(f"selftest: _redirects missing {required!r}")
        if any(line.startswith("/records/ ") for line in redirects.splitlines()):
            failures.append("selftest: /records/ must remain the Reports index")
        if "/labs/a2-context/ " in redirects:
            failures.append("selftest: event-style legacy URL must stay an HTML stub, not _redirects")

        # 6. route migration map covers migrated and preserved routes
        migration = json.loads((root / "data" / "generated" / "route-migration.json").read_text())
        by_old = {m["old_url"]: m for m in migration["mappings"]}
        if by_old.get("/labs/model-a/", {}).get("new_url") != "/evaluations/model-a/":
            failures.append("selftest: route map missing model-page migration")
        event_map = by_old.get("/labs/a2-context/", {})
        if event_map.get("event_id") != "context-envelope-completion-2026-01-03" or \
           event_map.get("new_url") != "/evaluations/model-a/#context-envelope-completion-2026-01-03":
            failures.append("selftest: route map missing event-URL mapping")
        if "/records/" in by_old:
            failures.append("selftest: /records/ must not be a migration source")

        # 7. idempotence: second run is a no-op
        before = {p: p.read_text() for p in (root / "content" / "evaluations").glob("*.md")}
        before_data = {p: p.read_text() for p in (root / "data" / "generated").glob("*.json")}
        before_data[root / "static" / "_redirects"] = \
            (root / "static" / "_redirects").read_text()
        run(root / "exports", check_only=False)
        after = {p: p.read_text() for p in (root / "content" / "evaluations").glob("*.md")}
        after_data = {p: p.read_text() for p in (root / "data" / "generated").glob("*.json")}
        after_data[root / "static" / "_redirects"] = (root / "static" / "_redirects").read_text()
        if before != after or before_data != after_data:
            failures.append("selftest: second sync is not a no-op")

        # 8. --check passes on a synced tree
        if run(root / "exports", check_only=True) != 0:
            failures.append("selftest: --check failed on a synced tree")

        # 9. duplicate event_id rejected
        run_and_expect_failure("duplicate event_id", lambda r: r["records"].append(
            dict(r["records"][3], slug="b1-dup", event_id="initial-evaluation-2026-01-01")))
        # 10. duplicate model_id rejected
        run_and_expect_failure("duplicate model_id", lambda r: r["models"].append(dict(r["models"][0])))
        # 11. a scientific profile cannot silently move between models
        run_and_expect_failure("profile/model collision", lambda r: r["records"][3].update(
            profile_id="model-a-p1"))
        # 12. entry without declared model (technical record) rejected
        run_and_expect_failure("technical record without model", lambda r: r["records"].append(
            {"slug": "tech-note", "event_id": "tech-event-2026-01-01", "event_type": "initial-evaluation",
             "event_date": "2026-01-01", "record_date": "2026-01-01", "model_id": None,
             "profile_id": "tech-p", "profile_repo": "WumboLabs/eval-tech", "authoring": "hand-authored",
             "event_body": "labs-events/initial-evaluation.md", "publication_state": "published",
             "evidence_maturity": "BENCHMARK_ONLY", "evidence_scope": ["performance"]}))
        # 13. unknown model_id rejected
        run_and_expect_failure("unknown model_id", lambda r: r["records"][0].update(model_id="model-z"))
        # 14. duplicate legacy URL rejected
        run_and_expect_failure("duplicate legacy URL", lambda r: r["records"][0].update(
            legacy_urls=["/labs/a2-context/"]))
        # 15. legacy URL colliding with a model page rejected
        run_and_expect_failure("legacy/model URL collision", lambda r: r["records"][0].update(
            legacy_urls=["/labs/model-b/"]))
        # 16. export-bytes mutation without updating the pin rejected
        def export_mutation_case(label: str, mutate_export) -> None:
            mutated = json.loads(json.dumps(ctx_a2))
            mutate_export(mutated)
            data = json.dumps(mutated, indent=2) + "\n"
            (exports_dir / "a2-context" / "website-publication.json").write_text(data)
            bad = json.loads(json.dumps(registry))
            bad["records"][2]["source"]["sha256"] = sha256_bytes(data.encode())
            REGISTRY_PATH.write_text(json.dumps(bad, indent=2) + "\n")
            try:
                run(root / "exports", check_only=False)
                failures.append(f"selftest: {label} not rejected")
            except SystemExit as exc:
                if exc.code != 1:
                    failures.append(f"selftest: {label} exit {exc.code}")
            REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")
            (exports_dir / "a2-context" / "website-publication.json").write_text(
                json.dumps(ctx_a2, indent=2) + "\n")

        bad = json.loads(json.dumps(registry))
        bad["records"][2]["source"]["sha256"] = "0" * 64
        REGISTRY_PATH.write_text(json.dumps(bad, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: hash mismatch not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: hash mismatch exit {exc.code}")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")
        # 17. export slug mismatch rejected
        export_mutation_case("slug mismatch", lambda e: e.update(website_record_slug="other"))
        # 18. pending export claiming a URL rejected
        export_mutation_case(
            "pending-with-URL",
            lambda e: e.update(canonical_evidence={"state": "PENDING_HUMAN_GATE",
                                                   "url": "https://example.com/x"}))
        # 19. export identity conflicting with the registry rejected
        export_mutation_case(
            "conflicting export identity",
            lambda e: e.update(identity={"model_id": "model-zzz", "profile_id": "model-a-p2",
                                         "event_id": "context-envelope-completion-2026-01-03",
                                         "event_type": "context-envelope-completion"}))
        # 20. hand-authored body must stay present; matching export identity accepted
        (root / "data" / "labs-events" / "initial-evaluation.md").write_text(hand_body)
        ok_export = json.loads(json.dumps(ctx_a2))
        ok_export["identity"] = {"model_id": "model-a", "profile_id": "model-a-p2",
                                 "event_id": "context-envelope-completion-2026-01-03",
                                 "event_type": "context-envelope-completion"}
        ok_data = json.dumps(ok_export, indent=2) + "\n"
        (exports_dir / "a2-context" / "website-publication.json").write_text(ok_data)
        ok_registry = json.loads(json.dumps(registry))
        ok_registry["records"][2]["source"]["sha256"] = sha256_bytes(ok_data.encode())
        REGISTRY_PATH.write_text(json.dumps(ok_registry, indent=2) + "\n")
        if run(root / "exports", check_only=False) != 0:
            failures.append("selftest: matching export identity not accepted")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")
        (exports_dir / "a2-context" / "website-publication.json").write_text(
            json.dumps(ctx_a2, indent=2) + "\n")

        REGISTRY_PATH, GENERATED_MODELS, GENERATED_EVENTS, GENERATED_FRESHNESS, \
            EVALUATIONS_PAGES, GENERATED_ROUTE_MIGRATION, REDIRECTS_FILE, BASE = orig

        if failures:
            print(json.dumps({"pass": False, "failures": failures}, indent=2))
            return 1
        print(json.dumps({"pass": True, "checks": [
            "one Evaluation page per model at /evaluations/; legacy event stubs served from /labs/ URLs",
            "generated _redirects (section roots + model pages) and route-migration map",
            "multi-profile/multi-event aggregation with anchors",
            "per-surface current-state precedence (classification vs context)",
            "legacy URL stub targets model page + event anchor",
            "events dataset preserves record_date chronology",
            "second sync is a no-op; --check passes",
            "duplicate event_id rejected",
            "duplicate model_id rejected",
            "profile_id/model collision rejected",
            "technical record without declared model rejected",
            "unknown model_id rejected",
            "duplicate legacy URL rejected",
            "legacy URL colliding with model page rejected",
            "hash mismatch rejected",
            "slug mismatch rejected",
            "pending export with URL rejected",
            "conflicting export identity rejected; matching identity accepted",
        ]}, indent=2))
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic WumboLabs Labs publication sync (model-centric)")
    parser.add_argument("--local-exports", type=Path, default=None,
                        help="directory that registry source.file entries resolve against")
    parser.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = parser.parse_args()
    from evaluations_source import synchronize
    try:
        synchronize(BASE, args.check)
    except (ValueError, OSError) as exc:
        fail(str(exc))
    return run(args.local_exports, args.check)


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv and argv[0] == "selftest":
        raise SystemExit(selftest())
    raise SystemExit(main())
