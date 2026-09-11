#!/usr/bin/env python3
"""sync_labs.py — deterministic WumboLabs Labs publication sync.

Reads data/labs-registry.json, consumes each generated record's canonical
website-publication export (schema wumbolabs-labs-publication/1), validates
it, and renders the generated Labs record pages plus machine-readable
generated data. Hand-authored records are verified, never rewritten.

The website is a DERIVATIVE of canonical public evidence. This script never
invents canonical URLs: an export whose canonical_evidence state is
PENDING_HUMAN_GATE renders a record with an explicit evidence-pending state.

Usage (from the repository root):
    python scripts/sync_labs.py --local-exports <dir>
    python scripts/sync_labs.py --local-exports <dir> --check   (verify only, no writes)
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
GENERATED_RECORDS = Path("data/generated/labs-records.json")
GENERATED_FRESHNESS = Path("data/generated/labs-freshness.json")
BASE = Path(".")  # repository root; all repo-relative paths resolve against this

EXPORT_SCHEMA = "wumbolabs-labs-publication/1"
DISPOSITIONS = {"WEBSITE_READY", "WEBSITE_BLOCKED", "NOT_FOR_PUBLICATION", "WEBSITE_PUBLISHED"}
EVIDENCE_STATES = {"PUBLISHED", "PENDING_HUMAN_GATE"}
REGISTRY_PUBLICATION_STATES = {"published", "evidence-pending-human-gate"}
REQUIRED_EXPORT_KEYS = [
    "schema", "campaign", "disposition", "model", "artifact", "runtime",
    "hardware", "welp", "context", "quality", "localmaxxing",
    "canonical_evidence", "public_summary",
]


def fail(message: str) -> "NoReturn":  # type: ignore[valid-type]
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def safe_rel_path(value: Any, what: str, slug: str) -> Path:
    """Validate a registry-provided relative path (no absolute, no '..')."""
    if not isinstance(value, str) or not value:
        fail(f"registry entry {slug!r}: {what} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        fail(f"registry entry {slug!r}: {what} must not be absolute or contain '..': {value!r}")
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
    if not isinstance(registry.get("records"), list) or not registry["records"]:
        fail("registry must contain a non-empty records list")
    return registry


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
    if evidence["state"] == "PUBLISHED" and not evidence.get("url"):
        fail(f"{origin}: canonical_evidence.state PUBLISHED requires url")
    if evidence["state"] == "PENDING_HUMAN_GATE" and evidence.get("url"):
        fail(f"{origin}: PENDING_HUMAN_GATE must not claim a canonical evidence URL")
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
    if kind == "local-export":
        if local_exports is None:
            fail(f"registry entry {entry.get('slug')!r} needs --local-exports DIR to resolve source.file")
        rel = safe_rel_path(source.get("file"), "source.file", entry["slug"])
        path = local_exports / rel
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
        provenance.update({"repo": repo, "ref": ref, "path": path, "url": url,
                           "sha256": sha256_bytes(raw)})
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


def render_record(entry: dict[str, Any], export: dict[str, Any]) -> str:
    """Render a deterministic Zola record page from a validated export."""
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
    if not date:
        fail(f"record {slug!r}: no record_date in the registry entry and no publication_date in the export")

    lines: list[str] = []
    display = fmt(model.get("display_name")).replace('"', "'")
    desc = (export.get("record_description") or export["public_summary"]).replace('"', "'")
    lines.append("+++")
    lines.append(f'title = "{display} Lab Record"')
    lines.append(f'description = "{desc}"')
    lines.append(f"date = {date}")
    lines.append('template = "lab_record.html"')
    weight = entry.get("weight")
    if weight is not None:
        lines.append(f"weight = {weight}")
    lines.append("")
    lines.append("[extra]")
    lines.append(f'model = "{fmt(model.get("display_name"))}"')
    lines.append(f'producer = "{fmt(model.get("producer"))}"')
    lines.append(f'quant = "{fmt(artifact.get("precision"))}"')
    repo_url = evidence.get("url") or ""
    lines.append(f'repo = "{repo_url}"')
    lines.append(f'status = "{fmt(entry.get("welp_status"))}"')
    gpu = fmt(hardware.get("gpu"))
    machine = hardware.get("machine")
    hw = f"{machine} ({gpu})" if machine else gpu
    lines.append(f'hardware = "{hw}"')
    lines.append(f'headline = "{fmt(export.get("record_description") or export["public_summary"])}"')
    lines.append('evidence = "%s"' % ("pending" if pending else "published"))
    lines.append("+++")
    lines.append("")

    if pending:
        proposed = evidence.get("proposed_repo")
        lines.append("> **Evidence publication pending.** Canonical public evidence for this")
        lines.append("> record has not been published yet"
                     + (f" (proposed repository: `{proposed}`)" if proposed else "") + ".")
        lines.append("> This page is a local derivative prepared ahead of publication; no")
        lines.append("> canonical evidence URL is claimed. The listed measurements come from")
        lines.append("> the accepted local WELP campaign named below.")
        lines.append("")

    campaign = export.get("campaign", "")
    lines.append("## Identity")
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

    lines.append("## Runtime and hardware")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f'| Engine | {fmt(runtime.get("engine"))} |')
    lines.append(f'| Runtime version | {fmt(runtime.get("version"))} |')
    if runtime.get("notes"):
        lines.append(f'| Runtime notes | {runtime["notes"]} |')
    lines.append(f'| Hardware | {hw} |')
    if hardware.get("notes"):
        lines.append(f'| Hardware notes | {hardware["notes"]} |')
    lines.append("")

    lines.append("## WELP outcome")
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

    lines.append("## Context profile")
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
        lines.append("## Headline performance")
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

    lines.append("## Quality and capabilities")
    lines.append("")
    lines.append(f'- **Constrained result:** {fmt(quality.get("constrained_result"))}')
    for cap in quality.get("capability_highlights") or []:
        lines.append(f"- {cap}")
    lines.append("")
    lines.append("### Guardrails and limitations")
    lines.append("")
    for guard in quality.get("key_guardrails") or []:
        lines.append(f"- {guard}")
    lines.append("")
    lines.append(f'**Reliability:** {fmt(quality.get("reliability_summary"))}')
    lines.append("")

    lines.append("## LocalMaxxing")
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

    lines.append("## Canonical evidence")
    lines.append("")
    if pending:
        lines.append("State: **PENDING_HUMAN_GATE** — the canonical public evidence repository")
        lines.append("has not been published yet. This record intentionally claims no canonical")
        lines.append("evidence URL. Once the evidence repository is published and the registry is")
        lines.append("updated, this record synchronizes against it and the pending state is removed.")
    else:
        lines.append(f'Canonical public evidence: <{evidence["url"]}>')
    lines.append("")
    lines.append("This Lab Record is a human-readable derivative of the accepted local WELP")
    lines.append("campaign evidence named above; the campaign's REPORT.md is the authoritative")
    lines.append("scientific source. Results are bounded by the tested artifact, runtime,")
    lines.append("hardware, configuration, and protocol snapshot, and are not universal model")
    lines.append("rankings.")
    lines.append("")
    return "\n".join(lines)


def write_if_changed(path: Path, content: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_dataset(registry: dict[str, Any], exports: dict[str, dict[str, Any]],
                  provenance: dict[str, dict[str, Any]]) -> dict[str, Any]:
    records = []
    for entry in registry["records"]:
        slug = entry["slug"]
        export = exports.get(slug)
        item = {
            "slug": slug,
            "model": entry.get("model"),
            "authoring": entry.get("authoring"),
            "record_date": entry.get("record_date"),
            "welp_status": entry.get("welp_status"),
            "publication_state": entry.get("publication_state"),
            "canonical_evidence": entry.get("canonical_evidence"),
            "record_path": entry.get("record_path"),
        }
        if export:
            item["campaign"] = export.get("campaign")
            item["welp_outcome"] = (export.get("welp") or {}).get("outcome")
            item["disposition"] = export.get("disposition")
            item["export_sha256"] = (provenance.get(slug) or {}).get("sha256")
            item["resolved_commit"] = (provenance.get(slug) or {}).get("resolved_commit")
        records.append(item)
    return {
        "version": 1,
        "generated_by": "scripts/sync_labs.py from data/labs-registry.json",
        "records": records,
    }


def run(local_exports: Path | None, check_only: bool) -> int:
    registry = load_registry()

    slugs: list[str] = []
    for entry in registry["records"]:
        slug = entry.get("slug")
        if not slug:
            fail("registry entry missing slug")
        if slug in slugs:
            fail(f"duplicate registry slug: {slug!r}")
        slugs.append(slug)
        if entry.get("publication_state") not in REGISTRY_PUBLICATION_STATES:
            fail(f"registry entry {slug!r}: invalid publication_state {entry.get('publication_state')!r}")
        record_path = safe_rel_path(entry.get("record_path"), "record_path", slug)
        if entry.get("authoring") == "hand-authored":
            page = BASE / record_path
            if not page.is_file():
                fail(f"hand-authored record page missing for {slug!r}: {page}")
        elif entry.get("authoring") != "generated":
            fail(f"registry entry {slug!r}: authoring must be hand-authored or generated")

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
        exports[entry["slug"]] = export
        provenance[entry["slug"]] = prov
        if export["canonical_evidence"]["state"] == "PENDING_HUMAN_GATE":
            blocked.append(entry["slug"])

    changed: list[str] = []
    unchanged: list[str] = []
    outputs: list[Path] = []
    for entry in registry["records"]:
        if entry.get("authoring") != "generated":
            continue
        page_path = BASE / entry["record_path"]
        content = render_record(entry, exports[entry["slug"]])
        if check_only:
            is_changed = not page_path.is_file() or page_path.read_text(encoding="utf-8") != content
        else:
            is_changed = write_if_changed(page_path, content)
            outputs.append(page_path)
        (changed if is_changed else unchanged).append(entry["slug"])

    dataset = build_dataset(registry, exports, provenance)
    freshness = {
        "version": 1,
        "generated_by": "scripts/sync_labs.py",
        "source_identities": {
            slug: {k: v for k, v in prov.items() if k != "kind"} | {"kind": prov.get("kind")}
            for slug, prov in provenance.items()
        },
        "latest_represented_campaigns": [
            {"slug": slug, "campaign": exports[slug].get("campaign")}
            for slug in exports
        ],
        "pending_website_publication": [
            slug for slug in exports
            if registry_entry_publication_state(registry, slug) == "evidence-pending-human-gate"
        ],
        "pending_public_evidence": list(blocked),
        "blocked_records": [],
        "notes": "Publication state is evidence-identity based; no time-based auto-expiration.",
    }
    dataset_serialized = json.dumps(dataset, indent=2, ensure_ascii=False) + "\n"
    freshness_serialized = json.dumps(freshness, indent=2, ensure_ascii=False) + "\n"
    if not check_only:
        for path, serial in ((GENERATED_RECORDS, dataset_serialized),
                             (GENERATED_FRESHNESS, freshness_serialized)):
            if write_if_changed(path, serial):
                changed.append(str(path))
            else:
                unchanged.append(str(path))
            outputs.append(path)

    print("Labs publication sync %s" % ("CHECK" if check_only else "complete"))
    print(f"registry sources:      {len(registry['records'])} entries "
          f"({sum(1 for e in registry['records'] if e.get('authoring') == 'hand-authored')} hand-authored, "
          f"{len(exports)} generated)")
    print(f"records changed:       {len(changed)}" + (f" {sorted(changed)}" if changed else ""))
    print(f"records unchanged:     {len(unchanged)}" + (f" {sorted(unchanged)}" if unchanged else ""))
    print(f"records blocked:       {len(blocked)} (evidence pending) {sorted(blocked)}")
    if outputs:
        print("outputs:")
        for path in outputs:
            print(f"  {path}")
    return 0


def registry_entry_publication_state(registry: dict[str, Any], slug: str) -> str | None:
    for entry in registry["records"]:
        if entry.get("slug") == slug:
            return entry.get("publication_state")
    return None


def selftest() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        export = {
            "schema": EXPORT_SCHEMA,
            "campaign": "selftest-campaign",
            "publication_date": "2026-01-01",
            "disposition": "WEBSITE_READY",
            "model": {"display_name": "SelfTest Model", "producer": "Tester",
                      "official_id": "example/selftest", "license": "Apache-2.0"},
            "artifact": {"tested": "selftest.gguf", "precision": "Q8_0", "sha256": "ab" * 32},
            "runtime": {"engine": "llama.cpp", "version": "b1"},
            "hardware": {"machine": "TestBench", "gpu": "Test GPU 12GB"},
            "welp": {"outcome": "PASS — SELFTEST", "classification": "READY_WITH_GUARDRAILS"},
            "context": {"practical_default_tokens": 32768, "guarded_tokens": 65536,
                        "native_maximum_tokens": 262144, "envelope_complete": False,
                        "native_maximum_disposition": "deferred"},
            "performance": {"short_ttft_s": 0.04, "short_decode_tps": 60.0,
                            "moderate_input_tokens": 3000, "moderate_ttft_s": 0.7,
                            "moderate_prefill_tps": 4000.0, "moderate_decode_tps": 58.0},
            "quality": {"constrained_result": "7/7", "capability_highlights": ["cap one"],
                        "key_guardrails": ["guard one"], "reliability_summary": "20/20"},
            "localmaxxing": {"status": "SUBMITTED", "canonical_context_tokens": 32768,
                             "tok_s_out": 60.0, "ttft_ms": 70.0,
                             "submission_ref": "cmtselftest", "verified_run": False},
            "canonical_evidence": {"state": "PENDING_HUMAN_GATE", "url": None,
                                   "proposed_repo": "eval-selftest"},
            "website_record_slug": "selftest-model",
            "record_description": "Bounded selftest description.",
            "public_summary": "Bounded selftest summary.",
        }
        exports_dir = root / "exports" / "selftest-model"
        exports_dir.mkdir(parents=True)
        export_bytes = (json.dumps(export, indent=2) + "\n").encode()
        (exports_dir / "website-publication.json").write_bytes(export_bytes)

        content_dir = root / "content" / "labs"
        content_dir.mkdir(parents=True)
        (content_dir / "old-model.md").write_text("+++\ntitle = \"Old\"\n+++\nold\n")

        registry = {
            "version": 1,
            "records": [
                {"slug": "old-model", "authoring": "hand-authored",
                 "record_path": "content/labs/old-model.md", "model": "Old",
                 "record_date": "2026-01-01", "welp_status": "READY",
                 "publication_state": "published",
                 "canonical_evidence": {"state": "published", "url": "https://example.com/repo"}},
                {"slug": "selftest-model", "authoring": "generated",
                 "record_path": "content/labs/selftest-model.md", "model": "SelfTest Model",
                 "record_date": "2026-01-01", "welp_status": "READY_WITH_GUARDRAILS",
                 "weight": 7, "publication_state": "evidence-pending-human-gate",
                 "source": {"kind": "local-export", "file": "selftest-model/website-publication.json",
                            "sha256": sha256_bytes(export_bytes)},
                 "canonical_evidence": {"state": "pending-human-gate", "proposed_repo": "eval-selftest"}},
            ],
        }

        failures: list[str] = []

        # Full in-process check using this module's functions against the temp tree.
        global REGISTRY_PATH, GENERATED_RECORDS, GENERATED_FRESHNESS, BASE
        orig_paths = (REGISTRY_PATH, GENERATED_RECORDS, GENERATED_FRESHNESS, BASE)
        BASE = root
        REGISTRY_PATH = root / "data" / "labs-registry.json"
        GENERATED_RECORDS = root / "data" / "generated" / "labs-records.json"
        GENERATED_FRESHNESS = root / "data" / "generated" / "labs-freshness.json"
        REGISTRY_PATH.parent.mkdir(parents=True)
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 1. valid sync
        run(root / "exports", check_only=False)
        page = root / "content" / "labs" / "selftest-model.md"
        if not page.is_file():
            failures.append("selftest: generated page missing")
        first = page.read_text() if page.is_file() else ""
        if "Evidence publication pending" not in first:
            failures.append("selftest: pending banner missing")
        if 'repo = ""' not in first:
            failures.append("selftest: pending record must not claim an evidence URL")
        if not GENERATED_RECORDS.is_file() or not GENERATED_FRESHNESS.is_file():
            failures.append("selftest: generated data files missing")

        # 2. idempotence: second run changes nothing
        before = {p: p.read_text() for p in page.parent.glob("*.md")}
        run(root / "exports", check_only=False)
        after = {p: p.read_text() for p in page.parent.glob("*.md")}
        if before != after:
            failures.append("selftest: second sync is not a no-op")

        # 3. hash mismatch rejected
        bad_registry = json.loads(json.dumps(registry))
        bad_registry["records"][1]["source"]["sha256"] = "0" * 64
        REGISTRY_PATH.write_text(json.dumps(bad_registry, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: hash mismatch not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: hash mismatch exit {exc.code}")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 4. unpinned local export rejected
        bad_registry = json.loads(json.dumps(registry))
        del bad_registry["records"][1]["source"]["sha256"]
        REGISTRY_PATH.write_text(json.dumps(bad_registry, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: unpinned local export not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: unpinned local export exit {exc.code}")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 5. escaping source.file rejected
        bad_registry = json.loads(json.dumps(registry))
        bad_registry["records"][1]["source"]["file"] = "../exports/selftest-model/website-publication.json"
        REGISTRY_PATH.write_text(json.dumps(bad_registry, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: escaping source.file not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: escaping source.file exit {exc.code}")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 6. missing record_path rejected
        bad_registry = json.loads(json.dumps(registry))
        del bad_registry["records"][1]["record_path"]
        REGISTRY_PATH.write_text(json.dumps(bad_registry, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: missing record_path not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: missing record_path exit {exc.code}")
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n")

        # 7. slug mismatch rejected
        bad_export = json.loads(json.dumps(export))
        bad_export["website_record_slug"] = "other-slug"
        (exports_dir / "website-publication.json").write_text(json.dumps(bad_export, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: slug mismatch not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: slug mismatch exit {exc.code}")
        (exports_dir / "website-publication.json").write_bytes(export_bytes)

        # 8. pending export claiming a URL rejected
        bad_export = json.loads(json.dumps(export))
        bad_export["canonical_evidence"]["url"] = "https://example.com/not-real"
        (exports_dir / "website-publication.json").write_text(json.dumps(bad_export, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: pending-with-URL not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: pending-with-URL exit {exc.code}")
        (exports_dir / "website-publication.json").write_bytes(export_bytes)

        # 9. missing model identity rejected
        bad_export = json.loads(json.dumps(export))
        bad_export["model"] = {"producer": "x"}
        (exports_dir / "website-publication.json").write_text(json.dumps(bad_export, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: missing model identity not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: missing model identity exit {exc.code}")
        (exports_dir / "website-publication.json").write_bytes(export_bytes)

        # 10. unsupported schema rejected
        bad_export = json.loads(json.dumps(export))
        bad_export["schema"] = "wumbolabs-labs-publication/99"
        (exports_dir / "website-publication.json").write_text(json.dumps(bad_export, indent=2) + "\n")
        try:
            run(root / "exports", check_only=False)
            failures.append("selftest: unsupported schema not rejected")
        except SystemExit as exc:
            if exc.code != 1:
                failures.append(f"selftest: unsupported schema exit {exc.code}")
        (exports_dir / "website-publication.json").write_bytes(export_bytes)

        REGISTRY_PATH, GENERATED_RECORDS, GENERATED_FRESHNESS, BASE = orig_paths

        if failures:
            print(json.dumps({"pass": False, "failures": failures}, indent=2))
            return 1
        print(json.dumps({"pass": True, "checks": [
            "valid sync renders page + generated data",
            "pending banner present, no evidence URL claimed",
            "second sync is a no-op",
            "hash mismatch rejected",
            "unpinned local export rejected",
            "escaping source.file rejected",
            "missing record_path rejected",
            "slug mismatch rejected",
            "pending export with URL rejected",
            "missing model identity rejected",
            "unsupported schema rejected",
        ]}, indent=2))
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic WumboLabs Labs publication sync")
    parser.add_argument("--local-exports", type=Path, default=None,
                        help="directory that registry source.file entries resolve against")
    parser.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = parser.parse_args()
    if args.local_exports is not None and not args.local_exports.is_dir():
        fail(f"--local-exports directory not found: {args.local_exports}")
    return run(args.local_exports, args.check)


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv and argv[0] == "selftest":
        raise SystemExit(selftest())
    raise SystemExit(main())
