#!/usr/bin/env python3
"""labs_findings_render.py — findings-first Evaluation page renderer (website only).

Renders every canonical model Evaluation page (one per model_id) from the same
frozen registry entries and canonical exports ``sync_labs.render_model_page``
already consumes. It changes presentation only:

  - reading order per event: outcome, independent section results and measured
    performance come first; a compact tested-condition attribution line stays
    visible; hashes, full identity, runtime and context metadata collapse into
    native ``<details>`` blocks that keep correct Markdown rendering (blank
    lines around the body); empty sections are omitted;
  - exactly one full-report link per event. Findings bullets and the
    recommendation point at the event anchor, never at a second copy of the
    canonical report URL; a hand-authored narrative body keeps its authored
    text, except that a Markdown link repeating that event's canonical report
    URL verbatim is reduced to its link text (all facts and other links stay);
  - hand-authored narrative bodies keep their authored Markdown verbatim apart
    from two mechanical, text-preserving transforms: every heading is demoted
    three levels (clamped at H6) so the body nests under its event H3 — heading
    text is unchanged, so Zola's generated inbound heading IDs keep resolving —
    and the known purely technical identity/deployment section is moved after
    the findings content, still fully visible. Narrative events are never
    labeled WELP;
  - the page overview stays minimal (producer, configuration/event counts,
    newest evidence date, section navigation); classification remains
    event-attributed: the frontmatter keeps the scientific classification
    value and the ``findings_first`` validator marker, and the header renders
    only the latest evidence date;
  - profile identities collapse to short labels derived mechanically from each
    profile's own fields — its own export when it has events with one, its own
    registry metadata otherwise (never another profile's export); collisions
    are resolved by appending deployment-topology segments from the registry;
    exact identities stay in the configuration details;
  - optional metrics are never fabricated: missing values render as "not
    recorded"/"Not recorded"; the ``/ 100 normalized`` denominator is printed
    only for a recorded score under a recorded helicopterbench methodology;
    Counter check-count derivations are the only zero-defaulted values.

Every rendered value is either verbatim source text or a mechanical derivation
(counts, min/max ranges, sums, identifiers). No scores, summaries or runtime
preferences are invented, and no registry/source/evidence data is modified.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from typing import Any

_RUNTIME_TAG_RE = re.compile(r"tag ([A-Za-z0-9][A-Za-z0-9._+-]*)")
_RUNTIME_BUILD_RE = re.compile(r"^(b[0-9]+)")
# Neutral hardware shortening: one mechanical rule set for every vendor string.
# Prefer a parenthesised GPU segment over the machine name, cut recorded lane
# suffixes, strip vendor prefixes and standalone memory sizes.
_GPU_PAREN_RE = re.compile(r"\(([^)]+)\)")
_GPU_LANE_SPLIT_RE = re.compile(r"\s*/\s*")
_GPU_VENDOR_RE = re.compile(
    r"^(?:NVIDIA\s+GeForce|AMD\s+Radeon|NVIDIA|AMD|Intel\s+Arc|Intel|Apple)\s+",
    re.IGNORECASE,
)
_GPU_MEMORY_RE = re.compile(r"\s+\d+\s*GB\b", re.IGNORECASE)
# Section-count highlight lines ("helicopterbench: 1 recorded identities")
# are superseded by the derived section summaries; matched mechanically.
_COUNT_HIGHLIGHT_RE = re.compile(r"^[A-Za-z0-9-]+: [0-9]+ recorded identit(y|ies)$")
_NARRATIVE_HEADING_RE = re.compile(r"^(#{1,6})(\s+\S.*?)(\s+#+\s*)?$")
_NARRATIVE_FENCE_PREFIXES = ("```", "~~~")
# Known purely technical narrative headings whose section may move after the
# findings content; heading text itself is never rewritten.
_NARRATIVE_IDENTITY_HEADINGS = {"identity", "identity and scope",
                                "identity and deployment"}

_STATUS_LINES = {
    "current": "current tested surface; not the recommended profile",
    "current-alternate": "validated alternate tested surface",
    "historical": "historical tested surface; retained evidence, not the recommended profile",
    "superseded": "superseded by a materially different accepted profile",
    "specialized": "specialized tested surface",
}


# ---------------------------------------------------------------------------
# mechanical, source-derived identity helpers
# ---------------------------------------------------------------------------

def _precision_short(precision: Any) -> str:
    """``Q6_K (official publisher GGUF)`` -> ``Q6_K``; verbatim when no suffix."""
    if isinstance(precision, str) and precision:
        return precision.split(" (", 1)[0].strip() or precision
    return ""


def _runtime_short(engine: Any, version: Any) -> str:
    """``llama.cpp (upstream)`` + ``... (tag b10999, ...)`` -> ``llama.cpp b10999``."""
    eng = ((engine or "").replace(" (upstream)", "").strip()) if isinstance(engine, str) else ""
    if isinstance(version, str) and version:
        m = _RUNTIME_TAG_RE.search(version) or _RUNTIME_BUILD_RE.match(version)
        if m:
            return f"{eng} {m.group(1)}".strip()
    return eng

def _runtime_values(runtime: dict[str, Any],
                    profile: dict[str, Any] | None = None) -> tuple[Any, Any]:
    """Read both frozen export schemas before falling back to profile metadata."""
    profile = profile or {}
    return (
        runtime.get("engine") or runtime.get("name") or profile.get("runtime_family"),
        runtime.get("version") or runtime.get("tag") or runtime.get("commit")
        or profile.get("runtime_version"),
    )


def _gpu_short(text: Any) -> str:
    """Neutral GPU shortening applied identically to every vendor string.

    ``WumboJetsII (NVIDIA GeForce RTX 5070 12GB)`` -> ``RTX 5070``;
    ``AMD Radeon AI PRO R9700 32 GB / gfx1201 / HIP`` -> ``AI PRO R9700``;
    ``UNKNOWN`` stays ``UNKNOWN``.
    """
    if not isinstance(text, str) or not text.strip():
        return ""
    s = text.strip()
    inner = _GPU_PAREN_RE.search(s)
    if inner and inner.group(1).strip():
        s = inner.group(1).strip()
    else:
        s = _GPU_LANE_SPLIT_RE.split(s, maxsplit=1)[0].strip()
    prev = None
    while prev != s and s:
        prev = s
        s = _GPU_VENDOR_RE.sub("", s, count=1).strip()
        s = _GPU_MEMORY_RE.sub("", s, count=1).strip()
    return re.sub(r"\s{2,}", " ", s)


def profile_short_labels(entries: list[dict[str, Any]],
                         exports: dict[str, dict[str, Any]],
                         profiles: dict[str, dict[str, Any]] | None) -> dict[str, str]:
    """Short config label per profile_id, derived from that profile's own
    fields: the export of one of its own events when one exists, otherwise the
    profile's own registry metadata (never another profile's export).

    Labels that would collide on one page are disambiguated mechanically by
    appending ``; ``-separated deployment-topology segments (registry profile
    field, verbatim) until unique. Full identities stay in the details blocks.
    """
    labels: dict[str, str] = {}
    by_profile: dict[str, list[dict[str, Any]]] = {}
    for entry in entries:
        by_profile.setdefault(entry["profile_id"], []).append(entry)
    for pid, pevents in by_profile.items():
        pair = next(((e, exports.get(e.get("slug") or "")) for e in pevents
                     if exports.get(e.get("slug") or "")), None)
        if pair is None:
            profile = (profiles or {}).get(pid) or {}
            parts = [
                _precision_short(profile.get("artifact_precision")),
                _runtime_short(*_runtime_values({}, profile)),
                _gpu_short(profile.get("hardware_scope")),
            ]
            labels[pid] = " · ".join(p for p in parts if p) \
                or pevents[0].get("profile_name") or pid
            continue
        entry, export = pair
        artifact = export.get("artifact") or {}
        runtime = export.get("runtime") or {}
        hardware = export.get("hardware") or {}
        gpu = hardware.get("gpu") or entry.get("hardware") or ""
        parts = [
            _precision_short(artifact.get("precision")) or entry.get("profile_name") or pid,
            _runtime_short(*_runtime_values(runtime, (profiles or {}).get(pid)))
            or "runtime not recorded",
            _gpu_short(gpu) or "GPU not recorded",
        ]
        labels[pid] = " · ".join(p for p in parts if p)
    related_profiles = {pid for e in entries for pid in e.get("related_profile_ids", [])}
    for pid, profile in (profiles or {}).items():
        if pid not in related_profiles:
            continue
        if pid in labels:
            continue  # covered above; this loop covers related-only surfaces
        parts = [
            _precision_short(profile.get("artifact_precision"))
            or profile.get("profile_display_name") or pid,
            _runtime_short(*_runtime_values({}, profile))
            or "runtime not recorded",
            _gpu_short(profile.get("hardware_scope")) or "GPU not recorded",
        ]
        labels[pid] = " · ".join(p for p in parts if p)

    duplicates = {pid for pid, label in labels.items()
                  if sum(1 for v in labels.values() if v == label) > 1}
    for pid in sorted(duplicates):
        topology = ((profiles or {}).get(pid) or {}).get("deployment_topology") or ""
        segments = [s.strip().rstrip(".") for s in topology.split(";") if s.strip()]
        # Walk the recorded topology from its most distinctive (last) segment.
        for segment in reversed(segments):
            if segment in labels[pid]:
                continue
            candidate = f"{labels[pid]} · {segment}"
            labels[pid] = candidate
            if sum(1 for v in labels.values() if v == candidate) == 1:
                break
        if sum(1 for v in labels.values() if v == labels[pid]) > 1:
            labels[pid] = f"{labels[pid]} · {pid}"
    return labels


# ---------------------------------------------------------------------------
# mechanical derivations of results and failures
# ---------------------------------------------------------------------------

def _num(value: Any) -> str:
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def _check_result(subcheck: dict[str, Any]) -> str:
    if subcheck.get("unevaluable") or subcheck.get("pass") is None:
        return "UNEVALUABLE"
    return "PASS" if subcheck.get("pass") else "FAIL"


def fmt_or(value: Any, default: str = "not recorded") -> str:
    """Local fmt with the shared vocabulary; None/empty renders as the default."""
    if value is None or value == "":
        return default
    return str(value)


def objective_summary(score: dict[str, Any]) -> dict[str, Any]:
    """Mechanical rollup of one objective_benchmark block (no judgment)."""
    counts: Counter[str] = Counter()
    for category in (score.get("categories") or {}).values():
        for subcheck in (category.get("subchecks") or {}).values():
            counts[_check_result(subcheck)] += 1
    return {
        "final_score": score.get("final_score"),
        "class": score.get("class"),
        "mechanical_points": score.get("mechanical_points"),
        "mechanical_max": score.get("mechanical_max"),
        "counts": counts,
        "generation_outcome": score.get("generation_outcome"),
    }


def _objective_headline(score: dict[str, Any]) -> str:
    """Score phrase for a recorded objective_benchmark block.

    The ``/ 100 normalized`` denominator is printed only for a recorded score
    under a recorded helicopterbench methodology; unknown values stay unknown.
    """
    fs = score.get("final_score")
    normalized = str(score.get("methodology") or "").startswith("helicopterbench")
    if fs is None:
        head = "score not recorded"
    elif normalized:
        head = f"{_num(fs)} / 100 normalized"
    else:
        head = _num(fs)
    if score.get("class") is not None:
        head += f" ({score['class']})"
    return head


def objective_lines(score: dict[str, Any]) -> list[str]:
    """Human-readable objective result: score, categories, then per-check rows.
    Missing optional metrics render as "Not recorded"; nothing is invented."""
    summary = objective_summary(score)
    counts = summary["counts"]
    pts, mx = summary["mechanical_points"], summary["mechanical_max"]
    if pts is not None and mx is not None:
        points_phrase = f" From {_num(pts)}/{_num(mx)} mechanical points."
    else:
        points_phrase = " Mechanical points not recorded."
    lines = [f"- Objective result: {_objective_headline(score)}.{points_phrase}",
             "- Check results: "
             + (" / ".join(f"{counts[k]} {k}"
                           for k in ("PASS", "FAIL", "UNEVALUABLE") if counts[k])
                or "not recorded")
             + "."]
    if summary["generation_outcome"] is not None:
        lines.append(f"- Generation outcome: {summary['generation_outcome']}.")
        if score.get("generation_reason") is not None:
            lines.append(f"- Generation reason (as recorded): {score['generation_reason']}.")
        lines.append("- Generation PASS means a completed submission, not a functioning "
                     "game. Failed gameplay checks remain part of the objective result.")

    categories = score.get("categories") or {}
    if categories:
        lines.append("")
        lines.append("| Category | Points | Max |")
        lines.append("|---|---|---|")
        for name, category in categories.items():
            lines.append(f"| {name} | {fmt_or(category.get('points'), 'Not recorded')} "
                         f"| {fmt_or(category.get('max'), 'Not recorded')} |")
        lines.append(f"| Total | {fmt_or(pts, 'Not recorded')} "
                     f"| {fmt_or(mx, 'Not recorded')} |")
        lines.append("")

    check_rows = [(name, check_id, subcheck)
                  for name, category in categories.items()
                  for check_id, subcheck in (category.get("subchecks") or {}).items()]
    if check_rows:
        lines.append("| Category | Check | Result | Points |")
        lines.append("|---|---|---|---|")
        for name, check_id, subcheck in check_rows:
            lines.append(f"| {name} | {check_id} | {_check_result(subcheck)} "
                         f"| {fmt_or(subcheck.get('points'), 'Not recorded')} |")
        lines.append("")
    return lines


def coverage_lines(coverage: dict[str, Any]) -> list[str]:
    """Per-category pass/fail table exactly as recorded in the coverage block.
    Missing optional counts render as "Not recorded"; nothing is invented."""
    lines: list[str] = []
    if coverage.get("status"):
        lines.append(f"- Coverage status: {coverage['status']}.")
    if coverage.get("rule"):
        lines.append(f"- Coverage rule (as recorded): {coverage['rule']}.")
    if coverage.get("advancement"):
        lines.append(f"- Coverage advancement: {coverage['advancement']}.")
    categories = coverage.get("categories") or {}
    if categories:
        lines.append("")
        lines.append("| Category | Pass | Fail | Measured | Scored | Status |")
        lines.append("|---|---|---|---|---|---|")
        for name, c in categories.items():
            lines.append(f"| {name} | {fmt_or(c.get('pass'), 'Not recorded')} "
                         f"| {fmt_or(c.get('fail'), 'Not recorded')} "
                         f"| {fmt_or(c.get('measured'), 'Not recorded')} "
                         f"| {fmt_or(c.get('scored'), 'Not recorded')} "
                         f"| {fmt_or(c.get('status'))} |")
        lines.append("")
    return lines


def section_lines(section: dict[str, Any]) -> list[str]:
    """Derived, source-faithful summary of one WELP section (bullet facts,
    tables separated by blank lines so Markdown renders them standalone)."""
    lines: list[str] = []
    units = section.get("units") or []
    if units:
        counts = Counter(u.get("outcome") or "UNSPECIFIED" for u in units)
        ordered = [k for k in ("PASS", "FAIL") if k in counts] + \
            sorted(k for k in counts if k not in ("PASS", "FAIL"))
        summary = ", ".join(f"{counts[k]} {k}" for k in ordered)
        lines.append(f"- Units: {len(units)} recorded ({summary}). Per-unit outcomes are "
                     "retained in the section provenance below.")
        negative_units = [u for u in units if u.get("outcome") != "PASS"
                          or u.get("reason")]
        if negative_units:
            lines.extend(["", "| Unit | Outcome | Completion / execution | Limits | Reason |",
                          "|---|---|---|---|---|"])
            for unit in negative_units:
                limits = unit.get("limits")
                if isinstance(limits, dict):
                    limits = "; ".join(f"{k}: {v}" for k, v in limits.items())
                lines.append(
                    f"| {fmt_or(unit.get('unit_id'))} | {fmt_or(unit.get('outcome'))} "
                    f"| {fmt_or(unit.get('completion'))} / {fmt_or(unit.get('execution'))} "
                    f"| {fmt_or(limits)} | {fmt_or(unit.get('reason'))} |")
            lines.append("")
    advancement = (section.get("advancement") or {}).get("decision")
    if advancement:
        lines.append(f"- Advancement: {advancement}.")
    if section.get("coverage"):
        lines.extend(coverage_lines(section["coverage"]))
    memory = section.get("memory") or {}
    if memory:
        vram = memory.get("sampled_vram_used_max_bytes")
        if isinstance(vram, int):
            lines.append(f"- Memory sample (boundary samples are not true peaks): VRAM used "
                         f"max {vram:,} bytes (~{vram / 2**30:.2f} GiB); host available min: "
                         f"{fmt_or(memory.get('sampled_host_available_min_bytes'), 'UNKNOWN')}.")
    observations = section.get("performance_observations") or []
    if observations:
        by_unit: dict[str, list[dict[str, Any]]] = {}
        for obs in observations:
            by_unit.setdefault(str(obs.get("unit_id")), []).append(obs)
        parts = []
        for unit_id, samples in sorted(by_unit.items()):
            rates = [s.get("timings", {}).get("tokens_per_second", {}).get("generation")
                     for s in samples]
            rates = [r for r in rates if isinstance(r, (int, float))]
            prompt = next((s.get("timings", {}).get("usage", {}).get("prompt_tokens")
                           for s in samples), None)
            piece = f"{unit_id}: {len(samples)} samples"
            if isinstance(prompt, int):
                piece += f" ({prompt:,}-token prompts)"
            if rates:
                piece += f": generation {_num(min(rates))}-{_num(max(rates))} tok/s"
            parts.append(piece + ".")
        if parts:
            lines.append("- Timed samples: " + " ".join(parts) + " Full per-sample timings "
                         "are retained in the section provenance below.")
    score = section.get("objective_benchmark")
    if score:
        if lines and lines[-1] != "":
            lines.append("")
        lines.extend(objective_lines(score))
    return lines


# ---------------------------------------------------------------------------
# collapsible <details> blocks with correct Markdown rendering
# ---------------------------------------------------------------------------

def details_block(summary: str, body: list[str], css_class: str | None = None) -> list[str]:
    """Native details/summary around Markdown body lines.

    Blank lines after <summary> and before </details> keep the body inside a
    Markdown context, so fences and tables inside render correctly.
    """
    attrs = f' class="{css_class}"' if css_class else ""
    return [f"<details{attrs}>", f"<summary>{summary}</summary>", "", *body, "", "</details>"]


def json_provenance_details(export: dict[str, Any]) -> list[str] | None:
    """The immutable section findings/provenance JSON, collapsed.

    The JSON payload stays byte-content-equivalent to the previous renderer.
    """
    sections = export.get("welp_sections")
    if not sections:
        return None
    payload = json.dumps({"sections": sections,
                          "profile_conditions": export.get("profile_conditions", [])},
                         ensure_ascii=False, sort_keys=True, indent=2)
    return details_block(
        "Raw section findings and provenance (JSON: outcomes, hashes, manifest and "
        "sampling conditions)",
        ["```json", payload, "```"],
        css_class="lab-findings-provenance",
    )


# ---------------------------------------------------------------------------
# hand-authored narrative bodies: two mechanical, text-preserving transforms
# ---------------------------------------------------------------------------

def _in_fence(line: str, fence: bool) -> bool:
    """Update and return the fenced-block state after ``line``."""
    if line.lstrip().startswith(_NARRATIVE_FENCE_PREFIXES):
        return not fence
    return fence


def _dedupe_report_links(body: list[str], ev_url: str) -> list[str]:
    """Reduce Markdown links that repeat this event's canonical report URL
    verbatim to their link text. Facts stay; other links stay untouched."""
    if not ev_url:
        return body
    pattern = re.compile(r"\[([^\]]+)\]\(" + re.escape(ev_url) + r"\)")
    return [pattern.sub(r"\1", line) for line in body]


def _narrative_restructure(body: list[str]) -> tuple[list[str], list[str]]:
    """Split one narrative body into ``(main, identity)``.

    ``identity`` is the known purely technical identity/deployment section —
    its heading plus the contiguous list/table block under it (a following
    loose paragraph stays where the author put it, so results and framing
    prose keep their reading position). Moving a section never rewrites its
    heading text, so Zola's generated inbound heading IDs keep resolving.
    """
    start = end = None
    fence = False
    for i, line in enumerate(body):
        fence = _in_fence(line, fence)
        if line.lstrip().startswith(_NARRATIVE_FENCE_PREFIXES) or fence:
            continue
        m = _NARRATIVE_HEADING_RE.match(line)
        if not m:
            continue
        text = re.sub(r"\s+", " ", m.group(2).strip()).casefold()
        if text not in _NARRATIVE_IDENTITY_HEADINGS:
            continue
        start = i
        end = start + 1
        while end < len(body):
            nxt = body[end]
            if _NARRATIVE_HEADING_RE.match(nxt):
                break
            stripped = nxt.strip()
            if stripped and not stripped.startswith(("-", "|")) \
                    and not re.match(r"^\d+\.\s", stripped):
                break  # loose prose belongs where the author put it
            end += 1
        while end > start and not body[end - 1].strip():
            end -= 1
        break
    if start is None:
        return body, []
    identity = body[start:end]
    main = body[:start] + body[end:]
    while main and not main[-1].strip():
        main.pop()
    return main, identity


def _demote_headings(lines: list[str]) -> list[str]:
    """Shift every Markdown heading three levels deeper, clamped at H6, so a
    narrative body nests under its event H3 without ever exceeding H6.

    Heading text is unchanged, so Zola's generated inbound heading IDs (slugs
    of the unchanged text) survive the level change. Fenced blocks are
    untouched.
    """
    out: list[str] = []
    fence = False
    for line in lines:
        fence_after = _in_fence(line, fence)
        m = None if fence else _NARRATIVE_HEADING_RE.match(line)
        if m:
            level = min(6, len(m.group(1)) + 3)
            out.append("#" * level + m.group(2).rstrip() + (m.group(3) or ""))
        else:
            out.append(line)
        fence = fence_after
    return out


# ---------------------------------------------------------------------------
# per-event rendering
# ---------------------------------------------------------------------------

def findings_bullet(entry: dict[str, Any], export: dict[str, Any] | None,
                    label: str) -> str:
    """One concise, source-grounded finding line for the Findings section.

    Labels stay short (date + config label); exact identities, full titles and
    complete values live in the event result the line links to.
    """
    head = f"- **{entry['event_date']}** · {label}"
    bits: list[str] = []
    if entry.get("welp_status"):
        bits.append(f"classification {entry['welp_status']}")
    if export:
        quality = export.get("quality") or {}
        if quality.get("constrained_result"):
            bits.append(str(quality["constrained_result"]))
        for section in export.get("welp_sections") or []:
            score = section.get("objective_benchmark")
            if score:
                summary = objective_summary(score)
                counts = summary["counts"]
                bit = f"objective {section['section']} {_objective_headline(score)}"
                if summary["mechanical_points"] is not None \
                        and summary["mechanical_max"] is not None:
                    bit += (f", {summary['mechanical_points']}/"
                            f"{summary['mechanical_max']} mechanical")
                if counts:
                    bit += ("; checks " + " / ".join(f"{counts[k]} {k}"
                                                     for k in ("PASS", "FAIL", "UNEVALUABLE")
                                                     if counts[k]))
                bits.append(bit)
            units = section.get("units") or []
            if units and not score:
                counts = Counter(u.get("outcome") or "UNSPECIFIED" for u in units)
                ordered = [k for k in ("PASS", "FAIL") if k in counts] + \
                    sorted(k for k in counts if k not in ("PASS", "FAIL"))
                adv = (section.get("advancement") or {}).get("decision")
                bits.append(f"{section['section']} {len(units)} units: "
                            + ", ".join(f"{counts[k]} {k}" for k in ordered)
                            + (f" ({adv})" if adv else ""))
            coverage = section.get("coverage") or {}
            failures = [f"{name.replace('_', ' ')} {fmt_or(c.get('pass'))} pass / "
                        f"{fmt_or(c.get('fail'))} fail"
                        for name, c in (coverage.get("categories") or {}).items()
                        if c.get("fail")]
            if failures:
                bits.append("coverage failures retained: " + "; ".join(failures))
    body = ("; ".join(str(b).rstrip(".") for b in bits) + ".") if bits \
        else "recorded outcome; details in the event result."
    return f"{head}: {body} [Event result](#{entry['event_id']})"


def _event_header(entry: dict[str, Any], label: str, full_profile_name: str,
                  fmt) -> list[str]:
    """Anchor, heading, compact condition-attribution header and the single
    full-report link block shared by generated and narrative events."""
    lines: list[str] = [f'<a id="{entry["event_id"]}"></a>', ""]
    lines.append(f'### {entry["event_date"]}: {fmt(entry.get("event_title"))}')
    lines.append("")
    meta = [f'**{fmt(entry.get("event_kicker"))}**', f"config {label}"]
    if entry.get("evidence_maturity"):
        meta.append(f'maturity: {entry["evidence_maturity"]}')
    if entry.get("welp_status"):
        meta.append(f'status: {entry["welp_status"]}')
    lines.append(" · ".join(meta))
    lines.append("")
    recorded = entry.get("welp") if isinstance(entry.get("welp"), dict) else {}
    snapshot = recorded.get("snapshot")
    if isinstance(snapshot, str) and snapshot.strip():
        provenance = f"Methodology snapshot: `{snapshot.strip()}`"
        welp_commit = recorded.get("welp_commit")
        if isinstance(welp_commit, str) and re.fullmatch(r"[0-9a-f]{40}", welp_commit):
            provenance += f" · WELP commit `{welp_commit}`"
        lines.extend([provenance, ""])
    lines.append(f"Configuration: {full_profile_name}.")
    lines.append("")

    ev_url = (entry.get("canonical_evidence") or {}).get("url", "")
    linked = False
    if ev_url:
        lines.append(f"[Full report (REPORT.md)]({ev_url})")
        linked = True
    report_page = entry.get("report_page")
    if report_page:
        report_url = f"/{report_page[:-3]}/" if report_page.endswith(".md") else report_page
        report_title = entry.get("report_title") or "Long-form campaign report"
        lines.extend(["", f"[Long-form report: {report_title}]({report_url})"])
        linked = True
    related = entry.get("related_profile_ids") or []
    if related:
        urls = entry.get("profile_metadata_urls") or {}
        rendered = [f"[{p}]({urls[p]})" if urls.get(p) else f"`{p}`" for p in related]
        lines.extend(["", "Related tested profiles: " + ", ".join(rendered)])
        linked = True
    if linked:
        lines.append("")
    return lines


def event_section_lines(entry: dict[str, Any], export: dict[str, Any] | None,
                        label: str, full_profile_name: str,
                        fmt, narrative_body: list[str] | None = None) -> list[str]:
    """Full event result section: results first, then a compact tested-condition
    attribution line, then collapsed identity/runtime/config metadata.

    ``fmt`` is sync_labs.fmt (the shared "not recorded" vocabulary). Raw JSON
    and lengthy provenance render collapsed; scores, failures and limitations
    stay visible. Exactly one full-report link per event.

    Hand-authored narrative records (``narrative_body``) keep their authored
    Markdown verbatim under the structured header, apart from the mechanical
    heading demotion and identity-section move described in the module
    docstring. No WELP framing is appended to narrative events.
    """
    lines = _event_header(entry, label, full_profile_name, fmt)

    if narrative_body is not None:
        ev_url = (entry.get("canonical_evidence") or {}).get("url", "")
        main_body, identity_body = _narrative_restructure(
            _dedupe_report_links(narrative_body, ev_url))
        lines.extend(_demote_headings(main_body))
        if identity_body:
            lines.append("")
            lines.extend(_demote_headings(identity_body))
        lines.append("")
        if export:
            provenance = json_provenance_details(export)
            if provenance:
                lines.extend(provenance)
                lines.append("")
        return lines

    model = export.get("model") or {}
    artifact = export.get("artifact") or {}
    runtime = export.get("runtime") or {}
    hardware = export.get("hardware") or {}
    welp = export.get("welp") or {}
    ctx = export.get("context") or {}
    quality = export.get("quality") or {}
    lmx = export.get("localmaxxing") or {}
    perf = export.get("performance") or {}
    pending = (export.get("canonical_evidence") or {}).get("state") == "PENDING_HUMAN_GATE"
    date = entry.get("record_date") or export.get("publication_date") or ""
    condition = next((c for c in (export.get("profile_conditions") or [])
                      if c.get("profile_id") == entry["profile_id"]), None)

    if pending:
        proposed = (export.get("canonical_evidence") or {}).get("proposed_repo")
        lines.extend([
            "> **Evidence publication pending.** Canonical public evidence for this",
            "> record has not been published yet"
            + (f" (proposed repository: `{proposed}`)" if proposed else "") + ".",
            "> This section is a local derivative prepared ahead of publication; no",
            "> canonical evidence URL is claimed. The listed measurements come from",
            "> the accepted local WELP campaign named below.",
            "",
        ])

    # ---- results first ----
    lines.extend([
        "#### WELP outcome", "",
        f'- **Outcome:** {fmt(welp.get("outcome"))}',
        f'- **Classification:** {fmt(welp.get("classification"))}',
    ])
    if welp.get("artifact_classification"):
        lines.append(f'- **Artifact classification:** {welp["artifact_classification"]}')
    if welp.get("snapshot"):
        lines.append(f'- **Methodology snapshot:** {welp["snapshot"]}')
    if welp.get("contract"):
        lines.append(f'- **Classification contract:** {welp["contract"]}')
    lines.append("")
    lines.append("Publication state: **%s**; %s" % (
        "evidence pending human gate" if pending else "published",
        "canonical public evidence is not yet published; this record shows an explicit "
        "pending state" if pending else "canonical evidence linked above",
    ))
    lines.append("")

    sections = export.get("welp_sections") or []
    if sections:
        lines.extend(["#### Section results", "",
                      "Each section retains its own profile, methodology, outcomes and "
                      "manifest. Performance observations are not model-quality scores; "
                      "null/UNKNOWN metrics remain unavailable.", ""])
        for section in sections:
            lines.append(f"##### {fmt(section.get('section'))} ({fmt(section.get('methodology'))})")
            lines.append("")
            lines.extend(section_lines(section))
            lines.append("")

    if perf:
        lines.extend(["#### Headline performance", "",
                      "| Surface | TTFT | Prefill | Decode |", "|---|---|---|---|"])
        short_ttft = perf.get("short_ttft_s")
        short_dec = perf.get("short_decode_tps")
        mod = perf.get("moderate_input_tokens")
        lines.append("| Short | %s | Not recorded | %s |" % (
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
            lines.extend(["", f"<p><small>{perf['surface_note']}</small></p>"])
        lines.append("")

    lines.extend([
        "#### Quality and capabilities", "",
        f'- **Constrained result:** {fmt(quality.get("constrained_result"))}',
    ])
    for cap in quality.get("capability_highlights") or []:
        if _COUNT_HIGHLIGHT_RE.match(str(cap)):
            continue  # section counts; superseded by the derived section results
        lines.append(f"- {cap}")
    lines.extend(["", "##### Guardrails and limitations", ""])
    for guard in quality.get("key_guardrails") or []:
        lines.append(f"- {guard}")
    lines.extend(["", f'**Reliability:** {fmt(quality.get("reliability_summary"))}', ""])

    if lmx:
        lines.extend(["#### LocalMaxxing", "",
                      f'- Status: {fmt(lmx.get("status"))}'])
        if isinstance(lmx.get("canonical_context_tokens"), int):
            lines.append(f'- Canonical context: {lmx["canonical_context_tokens"]:,} tokens')
        if lmx.get("tok_s_out") is not None:
            lines.append(f"- tok/s out: {_num(lmx['tok_s_out'])}")
        if isinstance(lmx.get("ttft_ms"), (int, float)):
            lines.append(f"- TTFT: {_num(lmx['ttft_ms'])} ms")
        lines.append(f'- Submission reference: {fmt(lmx.get("submission_ref"))}')
        lines.append(f'- verifiedRun: {fmt(lmx.get("verified_run"), "null (not claimed)")}')
        if lmx.get("note"):
            lines.append(f"<p><small>{lmx['note']}</small></p>")
        lines.append("")

    media = export.get("gameplay_media")
    if media:
        lines.extend([
            "#### Independently captured gameplay", "",
            "Actual independently executed gameplay from the evaluated generated artifact.",
            "Supplementary evidence only; objective scoring remains authoritative.", "",
            f'<video controls preload="metadata" width="{int(media["width"])}" '
            f'height="{int(media["height"])}">',
            f'<source src="{media["url"]}" type="video/mp4">',
            f'<a href="{media["url"]}">Download the captured H.264 MP4</a>',
            "</video>", "",
            f'Video SHA-256: `{media["sha256"]}`. Methodology: `{media["methodology"]}`.',
            "Historical /1 scores and videos retain their separate attribution.", "",
        ])
    elif export.get("gameplay_unavailable_reason"):
        lines.extend(["#### Gameplay footage", "",
                      export["gameplay_unavailable_reason"], ""])

    # ---- compact condition attribution ----
    attribution: list[str] = []
    precision = _precision_short(artifact.get("precision"))
    if precision:
        attribution.append(f"artifact {precision}")
    rt_short = _runtime_short(*_runtime_values(runtime))
    if rt_short:
        attribution.append(rt_short)
    gpu_short = _gpu_short(hardware.get("gpu"))
    if gpu_short:
        attribution.append(gpu_short)
    if isinstance(ctx.get("practical_default_tokens"), int):
        piece = f"context {ctx['practical_default_tokens']:,} default"
        if isinstance(ctx.get("guarded_tokens"), int):
            piece += f" / {ctx['guarded_tokens']:,} guarded"
        attribution.append(piece)
    if isinstance(ctx.get("useful_context_max_tokens"), int):
        attribution.append(
            f"useful context maximum {ctx['useful_context_max_tokens']:,} tokens")
    if isinstance(ctx.get("native_maximum_tokens"), int):
        attribution.append(f"native model-card maximum {ctx['native_maximum_tokens']:,} tokens")
    if isinstance(ctx.get("envelope_complete"), bool):
        attribution.append(f"envelope complete: {fmt(ctx['envelope_complete'])}")
    if condition:
        reasoning = condition.get("reasoning") or {}
        if reasoning.get("arm"):
            attribution.append(f"reasoning {reasoning['arm']}")
        if isinstance(condition.get("context_capacity"), int):
            attribution.append(f"capacity {condition['context_capacity']:,} tokens")
    if attribution:
        lines.extend(["**Tested condition:** " + " · ".join(attribution) + ".", ""])
    if ctx.get("native_maximum_disposition"):
        lines.extend([f"**Context limit outcome:** {ctx['native_maximum_disposition']}", ""])
    for title, record in (("Context boundaries", ctx), ("Runtime conditions", runtime),
                          ("Hardware conditions", hardware)):
        if record.get("notes"):
            lines.extend([f"**{title}:** {record['notes']}", ""])
    provenance = json_provenance_details(export)
    if provenance:
        lines.extend(provenance)
        lines.append("")

    # ---- collapsed identity, runtime and context metadata ----
    detail: list[str] = [
        "#### Identity", "",
        "| Field | Value |", "|---|---|",
        f'| Profile identity | `{entry["profile_id"]}` |',
        f'| Model | {fmt(model.get("display_name"))} |',
        f'| Producer | {fmt(model.get("producer"))} |',
    ]
    if model.get("official_id"):
        detail.append(f'| Official model | {model["official_id"]}'
                      + (f' @ `{model["official_revision"]}`' if model.get("official_revision")
                         else "") + " |")
    detail.extend([
        f'| Tested artifact | {fmt(artifact.get("tested"))} |',
        f'| Precision | {fmt(artifact.get("precision"))} |',
    ])
    if artifact.get("sha256"):
        sha = artifact["sha256"]
        if re.fullmatch(r"[a-f0-9]{64}", str(sha)):
            detail.append(f"| Artifact SHA-256 | `{sha}` |")
        else:
            detail.append(f"| Artifact hash evidence | {sha} |")
    detail.extend([
        f'| Campaign | `{fmt(export.get("campaign"))}` |',
        f"| Record date | {date} |", "",
        "#### Runtime and hardware", "",
        "| Field | Value |", "|---|---|",
        f'| Engine | {fmt(_runtime_values(runtime)[0])}'
        + (f' {_runtime_values(runtime)[1]}' if _runtime_values(runtime)[1] else "") + " |",
    ])
    for key in ("tag", "commit", "build", "backend"):
        if runtime.get(key):
            detail.append(f"| Runtime {key} | `{runtime[key]}` |")
    if hardware.get("machine") or hardware.get("gpu"):
        gpu = fmt(hardware.get("gpu"))
        machine = hardware.get("machine")
        detail.append(f'| Hardware | {f"{machine} ({gpu})" if machine else gpu} |')
    if runtime.get("notes"):
        detail.append(f'| Runtime notes | {runtime["notes"]} |')
    if hardware.get("notes"):
        detail.append(f'| Hardware notes | {hardware["notes"]} |')
    if ctx:
        detail.extend(["", "#### Context profile", "",
                       "| Field | Value |", "|---|---|",
                       f'| Practical default | {fmt(ctx.get("practical_default_tokens"))} tokens |',
                       f'| Guarded context | {fmt(ctx.get("guarded_tokens"))} tokens |'])
        if isinstance(ctx.get("useful_context_max_tokens"), int):
            detail.append(f'| Useful context maximum '
                          f'| {ctx["useful_context_max_tokens"]:,} tokens |')
        detail.extend([
            f'| Native model-card maximum | {fmt(ctx.get("native_maximum_tokens"))} tokens |',
            f'| Model-card envelope complete | {fmt(ctx.get("envelope_complete"))} |',
            f'| Native maximum disposition | {fmt(ctx.get("native_maximum_disposition"))} |',
        ])
        if ctx.get("notes"):
            detail.extend(["", f"<p><small>{ctx['notes']}</small></p>"])
    lines.extend(details_block(
        "Full tested identity, runtime and context details (exact hashes, versions "
        "and configuration)",
        detail, css_class="lab-findings-configs"))
    lines.append("")
    return lines


# ---------------------------------------------------------------------------
# page assembly
# ---------------------------------------------------------------------------

def render_findings_first_page(*, model, entries, entries_sorted, profile_ids,
                               profile_events, cls_event, ctx_event, rec_event, latest,
                               exports, catalog_weight, shared_for_model=None,
                               profiles=None, fmt, anchor_link, event_body,
                               editorial_presentation) -> str:
    """Findings-first presentation for one model page (same outputs contract as
    sync_labs.render_model_page: one deterministic Markdown page string)."""
    mid = model["model_id"]
    display = model["display_name"]
    labels = profile_short_labels(entries, exports, profiles)
    profile_names = {e["profile_id"]: e.get("profile_name") for e in entries}
    for pid, profile in (profiles or {}).items():
        profile_names.setdefault(pid, profile.get("profile_display_name"))
    guard_sources: dict[str, list[dict[str, Any]]] = {}
    for entry in entries_sorted:
        quality = (exports.get(entry["slug"]) or {}).get("quality") or {}
        for guard in quality.get("key_guardrails") or []:
            guard_sources.setdefault(guard, []).append(entry)

    desc = ("Published evaluation evidence and testing history. Results remain "
            "attributed to their original configurations and methods.")

    lines: list[str] = []
    lines.extend(["+++", f'title = "{display}"', f'description = "{desc}"',
                  'template = "lab_model.html"', f"weight = {catalog_weight}", "",
                  "[extra]", 'kind = "model"', f'model_id = "{mid}"',
                  f'vendor = "{fmt(model.get("vendor"))}"',
                  'findings_first = true'])
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
    lines.extend([f"profile_count = {len(profile_ids)}",
                  f"event_count = {len(entries)}",
                  f'latest_evidence_date = {latest["event_date"]}',
                  "+++", ""])

    # ---- overview ----
    lines.extend([
        "## Overview", "",
        f"{fmt_or(model.get('vendor'), 'producer not recorded')} · "
        f"{len(profile_ids)} tested configuration{'s' if len(profile_ids) != 1 else ''} · "
        f"{len(entries)} evidence event{'s' if len(entries) != 1 else ''} · "
        f'newest evidence {latest["event_date"]}.',
        "",
        "Contents: [Findings](#current-state) · [Event results](#testing-history) · "
        + ("[Limitations](#limitations) · " if guard_sources else "")
        + "[Tested configurations](#tested-profiles) · "
        "[Chronology](#chronology) · [Technical provenance](#canonical-evidence)",
        "",
    ])

    # ---- findings ----
    lines.extend(['<a id="current-state"></a>', "", "## Findings", "",
                  "Each finding is attributed to the event and tested configuration "
                  "that measured it; exact values, failures and limitations are in the "
                  "[event results](#testing-history). A historical event's recorded "
                  "status describes that event's own sections at its date and is not a "
                  "verdict on newer sections.", ""])
    if cls_event:
        label = labels.get(cls_event["profile_id"], cls_event["profile_id"])
        lines.append(f'- **Model classification: {fmt(cls_event.get("welp_status"))}** '
                     f"- attributed to the [{cls_event['event_date']} event]"
                     f"(#{cls_event['event_id']}), configuration {label}.")
    if rec_event:
        lines.append(f'- **Recommended configuration:** {fmt(rec_event.get("profile_name"))} '
                     f"({rec_event.get('profile_status')}) "
                     f"— [event result](#{rec_event['event_id']}).")
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
        lines.append(f'- **Practical context:** {practical} tokens{extra}; '
                     f"source: [event result](#{ctx_event['event_id']})")
        if c.get("native_maximum_disposition"):
            lines.append(f'- **Context limit outcome:** {c["native_maximum_disposition"]}; '
                         f"source: [event result](#{ctx_event['event_id']})")
    lines.append(f'- **Latest evidence:** {latest["event_date"]} — '
                 f'[event result](#{latest["event_id"]})')
    for entry in entries_sorted:
        lines.append(findings_bullet(entry, exports.get(entry.get("slug") or ""),
                                     labels.get(entry["profile_id"],
                                                entry["profile_id"])))
    lines.append("")

    # ---- full event results ----
    lines.extend(['<a id="testing-history"></a>', "", "## Event results", "",
                  "Newest first. Each event is one independent testing/publication "
                  "event with its full report linked once at the top of its section; "
                  "scores, failures and limitations stay visible and raw "
                  "section-provenance JSON stays collapsed.", ""])
    for entry in entries_sorted:
        export = exports.get(entry.get("slug") or "")
        narrative = entry.get("authoring") != "generated"
        narrative_body = (event_body(entry, exports).rstrip().splitlines()
                          if narrative else None)
        lines.extend(event_section_lines(
            entry, export,
            labels.get(entry["profile_id"], entry["profile_id"]),
            fmt(profile_names.get(entry["profile_id"]), default=entry["profile_id"]),
            fmt, narrative_body=narrative_body))

    # ---- source-attributed limitations; no empty boilerplate section ----
    if guard_sources:
        lines.extend(["## Limitations", ""])
        for guard, sources in guard_sources.items():
            links = ", ".join(f'[{e["event_date"]}](#{e["event_id"]})' for e in sources)
            lines.append(f"- {guard} Source events: {links}.")
        lines.append("")

    # ---- compact tested configurations ----
    lines.extend(['<a id="tested-profiles"></a>', "", "## Tested configurations", "",
                  "Exact profile identities, sampling conditions and provenance are in "
                  "each configuration's details below.", "",
                  "| Configuration | Artifact / precision | Runtime | Hardware | "
                  "Context / reasoning | Events |",
                  "|---|---|---|---|---|---|"])
    for pid in profile_ids:
        pevents = sorted(profile_events[pid],
                         key=lambda e: (e["event_date"], e["slug"]), reverse=True)
        registry_profile = (profiles or {}).get(pid) or {}
        export = next((exports.get(e.get("slug") or "") for e in pevents
                       if e["profile_id"] == pid and exports.get(e.get("slug") or "")),
                      None)
        artifact = (export or {}).get("artifact") or {}
        runtime = (export or {}).get("runtime") or {}
        hardware = (export or {}).get("hardware") or {}
        ctx = (export or {}).get("context") or {}
        condition = next((c for c in ((export or {}).get("profile_conditions") or [])
                          if c.get("profile_id") == pid), None)
        artifact_cell = (_precision_short(artifact.get("precision"))
                         or _precision_short(registry_profile.get("artifact_precision"))
                         or "not recorded")
        runtime_cell = (_runtime_short(*_runtime_values(runtime, registry_profile))
                        or "not recorded")
        hardware_cell = (_gpu_short(hardware.get("gpu"))
                         or _gpu_short(registry_profile.get("hardware_scope"))
                         or "not recorded")
        context_bits: list[str] = []
        if isinstance(ctx.get("practical_default_tokens"), int):
            piece = f"{ctx['practical_default_tokens']:,} default"
            if isinstance(ctx.get("guarded_tokens"), int):
                piece += f" / {ctx['guarded_tokens']:,} guarded"
            context_bits.append(piece)
        if isinstance(ctx.get("useful_context_max_tokens"), int):
            context_bits.append(f"useful max {ctx['useful_context_max_tokens']:,}")
        reasoning = (condition or {}).get("reasoning") or {}
        if reasoning.get("arm"):
            context_bits.append(f"reasoning {reasoning['arm']}")
        if isinstance((condition or {}).get("context_capacity"), int):
            context_bits.append(f"capacity {condition['context_capacity']:,}")
        dates = ", ".join(e["event_date"] for e in sorted(pevents,
                                                          key=lambda e: e["event_date"]))
        lines.append(f"| {labels.get(pid, pid)} | {artifact_cell} | {runtime_cell} "
                     f"| {hardware_cell} | {' · '.join(context_bits) or 'not recorded'} "
                     f"| {len(pevents)} ({dates}) |")
    lines.append("")
    for pid in profile_ids:
        pevents = sorted(profile_events[pid],
                         key=lambda e: (e["event_date"], e["slug"]), reverse=True)
        first = pevents[0]
        registry_profile = (profiles or {}).get(pid) or {}
        own = [e for e in pevents if e["profile_id"] == pid]
        status_source = own[0] if own else first
        status = status_source.get("profile_status") or "current"
        export = next((exports.get(e.get("slug") or "") for e in pevents
                       if e["profile_id"] == pid and exports.get(e.get("slug") or "")),
                      None)
        status_line = "current canonical/recommended tested surface" \
            if status == "current" and rec_event and pid == rec_event["profile_id"] \
            else _STATUS_LINES.get(status, status)
        full_name = (registry_profile.get("profile_display_name")
                     or (own[0].get("profile_name") if own else None)
                     or first.get("profile_name") or pid)
        body: list[str] = [
            f"- Full profile name: {fmt(full_name)}.",
            f"- Profile identity: `{pid}`.",
            f"- Status: {status_line}.",
        ]
        if registry_profile.get("deployment_topology"):
            body.append(f"- Deployment topology (as recorded): "
                        f"{registry_profile['deployment_topology']}")
        if registry_profile.get("artifact"):
            body.append(f"- Artifact (as recorded): {registry_profile['artifact']}")
        artifact = (export or {}).get("artifact") or {}
        if artifact.get("revision"):
            body.append(f"- Artifact revision: {artifact['revision']}.")
        if artifact.get("format"):
            body.append(f"- Artifact format: {artifact['format']}.")
        runtime = (export or {}).get("runtime") or {}
        rt_engine, rt_version = _runtime_values(runtime, registry_profile)
        if rt_engine:
            body.append(f"- Runtime (as recorded): {rt_engine}"
                        + (f" {rt_version}" if rt_version else "") + ".")
        hardware = (export or {}).get("hardware") or {}
        if hardware.get("machine") or hardware.get("gpu"):
            gpu = fmt(hardware.get("gpu"))
            machine = hardware.get("machine")
            body.append(f"- Hardware (as recorded): "
                        f"{f'{machine} ({gpu})' if machine else gpu}.")
        # Sampling/reasoning conditions come only from a condition record that
        # names this profile_id — never from another profile's attribution.
        condition = next((c for e in pevents
                          for c in ((exports.get(e.get("slug") or "") or {})
                                    .get("profile_conditions") or [])
                          if c.get("profile_id") == pid), None)
        if condition:
            sampling = condition.get("sampling") or {}
            if sampling:
                rendered = ", ".join(f"{k} {sampling[k]}" for k in sorted(sampling))
                body.append(f"- Sampling (as recorded): {rendered}.")
            reasoning = condition.get("reasoning") or {}
            if reasoning.get("arm"):
                body.append(f"- Reasoning arm: {reasoning['arm']}.")
            if isinstance(condition.get("context_capacity"), int):
                body.append(f"- Configured capacity: "
                            f"{condition['context_capacity']:,} tokens.")
        metadata_url = (first.get("profile_metadata_urls") or {}).get(pid)
        if metadata_url:
            body.append(f"- [Profile Metadata]({metadata_url})")
        body.extend(["", "Events on this configuration:", ""])
        for e in pevents:
            body.append(f"- {anchor_link(e)}; status: {fmt(e.get('welp_status'))}")
        lines.extend(details_block(f"Configuration details: {labels.get(pid, pid)}",
                                   body, css_class="lab-findings-configs"))
        lines.append("")

    # ---- compact chronology ----
    lines.extend(["## Chronology", "",
                  "Compact index; full results are in [Event results](#testing-history).",
                  "",
                  '| Date | Event | Configuration | Status |',
                  "|---|---|---|---|"])
    for entry in entries_sorted:
        lines.append(f'| {entry["event_date"]} '
                     f'| [{fmt(entry.get("event_title"))}](#{entry["event_id"]}) '
                     f"| {labels.get(entry['profile_id'], entry['profile_id'])} "
                     f"| {fmt(entry.get('welp_status'))} |")
    lines.append("")

    # ---- collapsible technical provenance ----
    lines.extend(['<a id="canonical-evidence"></a>', "", "## Technical provenance", "",
                  "Publication, acceptance and source-pin provenance for each event, "
                  "collapsed; the scientific content above never depends on it.", ""])
    tree_urls = sorted({e.get("model_evidence_url") for e in entries_sorted
                        if e.get("model_evidence_url")})
    for tree in tree_urls:
        lines.extend([f"[Model evidence tree (GitHub)]({tree})", ""])
    for entry in entries_sorted:
        export = exports.get(entry.get("slug") or "")
        body = []
        if export:
            evidence = export.get("canonical_evidence") or {}
            welp = export.get("welp") or {}
            acceptance = export.get("scientific_acceptance") or {}
            if export.get("campaign"):
                body.append(f"- Campaign: `{export['campaign']}`")
            if export.get("disposition"):
                disposition = export["disposition"]
                if export.get("publication_date"):
                    disposition += f"; publication date {export['publication_date']}"
                body.append(f"- Export disposition: {disposition}")
            if evidence.get("url"):
                body.append(f"- Canonical citation (immutable commit/path pin): "
                            f"`{evidence['url']}`")
            for key, title in (("snapshot", "Methodology snapshot"),
                               ("contract", "Classification contract"),
                               ("rule", "Classification rule"),
                               ("review_adjudication", "Review adjudication"),
                               ("setup_revalidation", "Setup revalidation")):
                if welp.get(key):
                    body.append(f"- {title}: {welp[key]}")
            if acceptance:
                body.append(f"- Scientific acceptance: schema {acceptance.get('schema')}, "
                            f"decision {acceptance.get('decision')}"
                            + (f", reviewed {acceptance['reviewed_at']}"
                               if acceptance.get("reviewed_at") else ""))
            if acceptance.get("basis"):
                body.append(f"- Acceptance basis (as recorded): {acceptance['basis']}")
            if acceptance.get("review_source_sha256"):
                body.append(f"- Review source SHA-256: "
                            f"`{acceptance['review_source_sha256']}`")
            manifests = acceptance.get("section_manifests") or {}
            if manifests:
                body.append("")
                body.append("| Section | Manifest SHA-256 |")
                body.append("|---|---|")
                for name, manifest in sorted(manifests.items()):
                    body.append(f"| {name} | `{manifest}` |")
                body.append("")
            artifact = export.get("artifact") or {}
            if artifact.get("revision"):
                body.append(f"- Artifact revision: {artifact['revision']}")
            if artifact.get("format"):
                body.append(f"- Artifact format: {artifact['format']}")
            runtime = export.get("runtime") or {}
            if runtime.get("backend"):
                body.append(f"- Runtime backend: {runtime['backend']}")
            identity = export.get("identity") or {}
            if identity:
                body.append("- Export identity: " + ", ".join(
                    f"{k} `{identity[k]}`" for k in sorted(identity) if identity[k]))
            source = entry.get("source") or {}
            if source:
                pin = (f"{source.get('kind')} {source.get('repo', '')}"
                       + (f" @ `{source['ref']}`" if source.get("ref") else "")
                       + (f" path {source['path']}" if source.get("path") else "")
                       + (f" sha256 `{source['sha256']}`" if source.get("sha256") else ""))
                body.append(f"- Export source pin: {pin.strip()}")
                if source.get("url"):
                    body.append(f"- Source URL: `{source['url']}`")
            note = (entry.get("publication_provenance") or {}).get("note")
            if note:
                body.append("")
                body.append(f"<p><small>Publication provenance note (as recorded): "
                            f"{note}</small></p>")
        if body:
            lines.extend(details_block(
                f"Event provenance: {entry['event_date']} "
                f"{fmt(entry.get('event_kicker'))}",
                body, css_class="lab-findings-provenance"))
            lines.append("")

    legacy_sources = {
        (source["repo"], source["commit"], source["path"])
        for e in entries for source in e.get("legacy_sources", [])
    }
    if legacy_sources:
        lines.extend(["### Legacy provenance", ""])
        for repo, commit, path in sorted(legacy_sources):
            lines.append(f"- [{repo} @ `{commit}`](https://github.com/{repo}/blob/{commit}/{path})")
        lines.append("")

    if shared_for_model:
        lines.extend([
            "## Shared comparison events", "",
            "This model appears in shared multi-model comparisons. Each report is "
            "stored once in WumboLabs/evaluations/shared-events/; the model's "
            "measured entries remain attributed to the same historical event:", "",
        ])
        for s in sorted(shared_for_model,
                        key=lambda x: (x["entry"]["event_date"], x["entry"]["slug"])):
            e = s["entry"]
            note = s.get("note")
            shared_url = (e.get("canonical_evidence") or {}).get("url", "")
            # Own-model events already carry their single full-report link in
            # the event result above; only foreign-model events need the link
            # repeated here.
            link = ""
            if e.get("model_id") != mid and shared_url:
                link = f" [Canonical evidence / full report]({shared_url})"
            lines.append(f"- {anchor_link(e)}"
                         + (f": {note}" if note else "")
                         + link)
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    return editorial_presentation("\n".join(lines) + "\n")
