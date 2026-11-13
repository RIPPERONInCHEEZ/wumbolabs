#!/usr/bin/env python3
"""check_evaluations_site.py — post-build public-route validation.

Validates the consolidated Evaluations, Research, and compatibility-page
contracts against the built site (public/) and generated datasets
(data/generated/). Run after `zola build` from the repository root:

    python scripts/check_evaluations_site.py

Checks:
  - one Evaluations index; exactly one canonical page per registry model;
  - catalog rows are a five-column static index (no Status column, no
    status/classification or placeholder advertisement in data-search) that
    derives latest evidence from canonical event dates and sorts deterministically;
  - homepage links each research destination exactly twice (global nav + one
    main route set), without a homepage hardware inventory;
  - primary navigation exposes Evaluations, Research, and Methodology, not Projects;
  - retired /labs/ routes and event stubs preserve their model-page targets;
  - /records/ remains the Research archive and each technical-record URL;
  - former project URLs remain as unlisted compatibility pages;
  - model pages share one findings-first structure (Overview, Findings, Event
    results, Limitations, Tested configurations, Chronology, Technical
    provenance) with no page-wide classification in the page header;
  - every generated event result keeps its recorded WELP outcome,
    classification, constrained result, highlights, guardrails, reliability,
    context/performance notes, section counts/outcomes/coverage/objective
    scores and subchecks visible outside collapsed <details>, and its raw
    section JSON decodes back to the recorded export sections and
    profile_conditions; narrative events keep their hand-authored bodies;
  - every event keeps its anchor, canonical report link, long-form secondary
    report, profile identities and profile metadata links, and gameplay
    media controls/source/hash;
  - all local links in built HTML resolve, including #fragment targets
    (redirect routes resolve through the recorded route mappings).

Exit codes: 0 PASS; 1 FAIL.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from html import escape as html_escape, unescape as html_unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


from sync_labs import editorial_presentation

PUBLIC = Path("public")
REGISTRY = Path("data/labs-registry.json")
REDIRECTS_FILE = Path("static/_redirects")
EVENTS_DATA = Path("data/generated/labs-events.json")
MODELS_DATA = Path("data/generated/labs-models.json")
ROUTE_MIGRATION = Path("data/generated/route-migration.json")
EVALUATION_EXPORTS = Path("data/generated/evaluations-exports")

# Shared findings-first structure every model page must expose (Zola slugged
# heading ids / explicit anchor ids).
REQUIRED_MODEL_SECTIONS = (
    "overview", "findings", "event-results", "limitations",
    "tested-configurations", "chronology", "technical-provenance",
)
CATALOG_COLUMNS = 5
STATUS_PLACEHOLDER = "evidence in progress"  # retired catalog status placeholder

failures: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(message)


def url_slug(model_id: str) -> str:
    return model_id.replace(".", "-")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def html(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def redirect_sources() -> set[str]:
    sources = set()
    for line in REDIRECTS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        sources.add(line.split()[0])
    return sources


def redirect_targets() -> dict[str, str]:
    """Path-only redirect destinations usable for fragment resolution.

    Cloudflare splat/placeholder targets (":splat", ":path") cannot be resolved
    statically and are omitted; the path itself is still validated elsewhere.
    """
    targets: dict[str, str] = {}
    for line in REDIRECTS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cols = line.split()
        if len(cols) >= 2 and ":" not in cols[1]:
            targets[cols[0]] = cols[1]
    return targets


def data_attr(attrs: str, name: str) -> str | None:
    match = re.search(rf'\b{name}="([^"]*)"', attrs)
    return match.group(1) if match else None


# ---------------------------------------------------------------------------
# HTML text separation: visible prose vs collapsed <details> technical text
# ---------------------------------------------------------------------------

_BLOCK_TAGS = frozenset({
    "address", "article", "aside", "blockquote", "body", "details", "dd", "div",
    "dl", "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2",
    "h3", "h4", "h5", "h6", "header", "hr", "html", "li", "main", "nav", "ol",
    "p", "pre", "section", "summary", "table", "tbody", "td", "tfoot", "th",
    "thead", "tr", "ul", "video", "source", "br",
})


def _normalize(text: str) -> str:
    """Fold formatting/punctuation so mechanical copyedits don't mask content."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _alnum_len(text: str) -> int:
    return len(re.sub(r"[^A-Za-z0-9]", "", text))


class _PageParser(HTMLParser):
    """Collect positioned runs, links, ids and media from one built page.

    Text inside closed <details> blocks (collapsed raw provenance/configuration)
    is captured for raw checks but marked not visible: consumer-visible results
    must appear outside those blocks.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.raw = ""
        self.line_starts = [0]
        self.runs: list[tuple[int, str, bool, bool]] = []  # offset, text, visible, in_pre
        self.links: list[tuple[int, str, bool]] = []       # offset, href/src, visible
        self.ids: dict[str, int] = {}
        self.videos: list[tuple[int, dict[str, str]]] = []
        self._detail_depth = 0
        self._pre_depth = 0

    def feed_html(self, raw: str) -> None:
        self.raw = raw
        self.line_starts = [0] + [m.end() for m in re.finditer("\n", raw)]
        self.feed(raw)
        self.close()

    def _offset(self) -> int:
        line, col = self.getpos()
        return self.line_starts[line - 1] + col

    def _visible(self) -> bool:
        return self._detail_depth == 0

    def _separator(self, where: int) -> None:
        if self._pre_depth == 0:
            self.runs.append((where, "\n", self._visible(), False))

    def handle_starttag(self, tag, attrs):
        where = self._offset()
        attr_map = {key: value or "" for key, value in attrs}
        for key in ("id", "name"):
            if attr_map.get(key):
                self.ids.setdefault(attr_map[key], where)
        if tag == "a" and attr_map.get("href"):
            self.links.append((where, attr_map["href"], self._visible()))
        elif tag in ("video", "source", "img") and attr_map.get("src"):
            self.links.append((where, attr_map["src"], self._visible()))
        if tag == "video":
            self.videos.append((where, attr_map))
        if tag == "details":
            self._detail_depth += 1
        if tag == "pre":
            self._pre_depth += 1
        if tag in _BLOCK_TAGS:
            self._separator(where)

    def handle_endtag(self, tag):
        where = self._offset()
        if tag == "details":
            self._detail_depth = max(0, self._detail_depth - 1)
        if tag == "pre":
            self._pre_depth = max(0, self._pre_depth - 1)
        if tag in _BLOCK_TAGS:
            self._separator(where)

    def handle_data(self, data):
        if not data:
            return
        self.runs.append((self._offset(), data, self._visible(), self._pre_depth > 0))


class PageText:
    """Positioned text view of one built page."""

    def __init__(self, raw: str) -> None:
        self.parser = _PageParser()
        self.parser.feed_html(raw)

    @property
    def raw(self) -> str:
        return self.parser.raw

    @property
    def ids(self) -> dict[str, int]:
        return self.parser.ids

    @property
    def links(self) -> list[tuple[int, str, bool]]:
        return self.parser.links

    @property
    def videos(self) -> list[tuple[int, dict[str, str]]]:
        return self.parser.videos

    def visible_text(self, lo: int = 0, hi: int | None = None) -> str:
        hi = len(self.raw) if hi is None else hi
        return "".join(text for off, text, visible, _ in self.parser.runs
                       if visible and lo <= off < hi)

    def raw_text(self, lo: int = 0, hi: int | None = None) -> str:
        hi = len(self.raw) if hi is None else hi
        return "".join(text for off, text, _, _ in self.parser.runs
                       if lo <= off < hi)

    def pre_runs(self, lo: int = 0, hi: int | None = None) -> list[tuple[int, str]]:
        hi = len(self.raw) if hi is None else hi
        return [(off, text) for off, text, _, in_pre in self.parser.runs
                if in_pre and lo <= off < hi]

    def locate(self, lo: int, hi: int, needle: str,
               normalized_ok: bool = True) -> int | None:
        """Raw offset of the first visible occurrence of `needle` in [lo, hi).

        Falls back to punctuation/whitespace-folded matching for longer values
        (mechanical copyedits may reflow punctuation without changing content).
        """
        if not needle:
            return None
        needle = str(needle)
        runs = [(off, text) for off, text, visible, _ in self.parser.runs
                if visible and lo <= off < hi]
        joined = "".join(text for _, text in runs)
        idx = joined.find(needle)
        if idx >= 0:
            return self._run_offset(runs, idx)
        if normalized_ok and _alnum_len(needle) > 5:
            norm_joined = "".join(_normalize(text) + " " for _, text in runs)
            pos = norm_joined.find(_normalize(needle))
            if pos >= 0:
                acc = 0
                for off, text in runs:
                    if pos < acc + len(_normalize(text)) + 1:
                        return off
                    acc += len(_normalize(text)) + 1
        return None

    @staticmethod
    def _run_offset(runs: list[tuple[int, str]], idx: int) -> int:
        acc = 0
        offset = runs[0][0] if runs else 0
        for off, text in runs:
            if idx < acc + len(text):
                return off
            acc += len(text)
            offset = off
        return offset

    def anchor_offsets(self) -> list[int]:
        return sorted(set(self.parser.ids.values()))


# ---------------------------------------------------------------------------
# source-normalized narrative comparison
# ---------------------------------------------------------------------------

def _source_normalized(markdown: str) -> str:
    """Normalize hand-authored Markdown for presence matching in built HTML.

    Markdown link/image targets and inline HTML render as link text or plain
    content on the page, so source-side markup that does not survive as text is
    dropped; everything else folds through _normalize on both sides.
    """
    text = re.sub(r"(?ms:^```.*?^```[^\n]*$)|`[^`\n]*`",
                  lambda m: html_escape(m.group(), quote=False), markdown)
    text = re.sub(r"\]\([^)\s]*\)", " ", text)
    text = re.sub(r"</?[A-Za-z][^>\n]*>", " ", text)
    return _normalize(html_unescape(text))


def _narrative_gaps(dom: PageText, lo: int, hi: int, body: str) -> list[str]:
    """Every authored paragraph/table remains readable after reordering."""
    page_norm = _normalize(dom.visible_text(lo, hi))
    return [block[:100] for paragraph in re.split(r"\n\s*\n", editorial_presentation(body))
            if (block := _source_normalized(paragraph)) and block not in page_norm]


# ---------------------------------------------------------------------------
# export/registry helpers
# ---------------------------------------------------------------------------

_EXPORT_CACHE: dict[str, dict] = {}


def export_for(entry: dict) -> dict | None:
    """The recorded machine export backing one registry record."""
    source = entry.get("source") or {}
    file_rel = source.get("file") or ""
    if not file_rel:
        return None
    if file_rel not in _EXPORT_CACHE:
        path = PUBLIC.parent / file_rel
        _EXPORT_CACHE[file_rel] = load_json(path) if path.is_file() else {}
    return _EXPORT_CACHE[file_rel] or None


def fmt_num(value) -> str:
    """Mirror the renderer's mechanical number formatting."""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)


def value_forms(value) -> list[str]:
    """Acceptable rendered forms of one source value (floats keep both the
    compact and the exact-precision form so either presentation verifies)."""
    if isinstance(value, float):
        return sorted({f"{value:g}", str(value)})
    return [str(value)]


def check_raw_sections(label: str, export: dict, dom: PageText,
                       lo: int, hi: int) -> int | None:
    """Round-trip every raw section value, including narrative-attached exports."""
    for off, text in dom.pre_runs(lo, hi):
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict) or "sections" not in payload:
            continue
        expected = {"sections": export["welp_sections"],
                    "profile_conditions": export.get("profile_conditions", [])}
        check(payload == expected, f"{label}: raw section JSON differs from source")
        check(not any(visible for pos, _, visible, _ in dom.parser.runs if pos == off),
              f"{label}: raw JSON must be in expandable technical details")
        return off
    check(False, f"{label}: raw section findings/provenance JSON missing")
    return None


# Section-count highlight lines are superseded by the derived section summaries
# in the shared renderer; they are mechanically matched, never judged.
_COUNT_HIGHLIGHT_RE = re.compile(r"^[A-Za-z0-9-]+: [0-9]+ recorded identit(y|ies)$")


def _front_matter(path: Path) -> dict:
    """Flatten the simple `key = "value"` front matter of one content page."""
    block = re.match(r"\+\+\+\n([\s\S]*?)\n\+\+\+", path.read_text(encoding="utf-8"))
    fields: dict[str, str] = {}
    if not block:
        return fields
    for line in block.group(1).split("\n"):
        pair = re.match(r"^([A-Za-z0-9_]+) = (.*)$", line)
        if pair:
            value = pair.group(2).strip()
            fields[pair.group(1)] = value[1:-1] if re.fullmatch(r'".*"', value, re.S) else value
    return fields


def main() -> int:
    if not PUBLIC.is_dir():
        print("ERROR: public/ not found — run `zola build` first")
        return 1

    registry = load_json(REGISTRY)
    models = registry["models"]
    events = load_json(EVENTS_DATA)["events"]
    generated_models = {m["model_id"]: m for m in load_json(MODELS_DATA)["models"]}
    migration = load_json(ROUTE_MIGRATION)["mappings"]
    redirects = redirect_sources()
    records = registry["records"]

    # 1. canonical Evaluations routes: one index, one page dir per model
    eval_index = PUBLIC / "evaluations" / "index.html"
    check(eval_index.is_file(), "missing /evaluations/ index page")
    model_slugs = {url_slug(m["model_id"]) for m in models}
    built_dirs = {p.parent.name for p in (PUBLIC / "evaluations").glob("*/index.html")}
    check(model_slugs <= built_dirs,
          f"missing model pages under /evaluations/: {sorted(model_slugs - built_dirs)}")
    extra_dirs = built_dirs - model_slugs
    check(not extra_dirs,
          f"unexpected directories under /evaluations/ (route collisions?): {sorted(extra_dirs)}")
    check(len(built_dirs) == len(model_slugs),
          "model page count mismatch under /evaluations/")

    # 1b. The catalog is a static, status-free evidence index before JavaScript.
    front_by_model: dict[str, dict] = {}
    for source in Path("content/evaluations").glob("*.md"):
        fields = _front_matter(source)
        if fields.get("model_id") and fields.get("redirect_page") != "true":
            front_by_model[fields["model_id"]] = fields
    if eval_index.is_file():
        catalog = html_unescape(html(eval_index))
        rows = re.findall(
            r"<tr data-evaluation-row\b(?P<attrs>[^>]*)>(?P<body>.*?)</tr>",
            catalog,
            flags=re.DOTALL,
        )
        row_ids = [data_attr(attrs, "data-model-id") for attrs, _ in rows]
        check(len(rows) == len(models),
              f"catalog row count {len(rows)} does not match registry models {len(models)}")
        check(all(row_ids) and len(set(row_ids)) == len(row_ids),
              "catalog rows must have one unique data-model-id each")
        check(set(row_ids) == {m["model_id"] for m in models},
              "catalog rows omit or add registry models")
        thead = re.search(r"<thead>(.*?)</thead>", catalog, flags=re.DOTALL)
        columns = re.findall(r'<th scope="col">(.*?)</th>', thead.group(1)) if thead else []
        check(len(columns) == CATALOG_COLUMNS,
              f"catalog must expose exactly {CATALOG_COLUMNS} columns; found {columns}")
        check(not any(col.strip().lower() == "status" for col in columns),
              "catalog still renders a Status column")
        check(STATUS_PLACEHOLDER not in catalog.lower(),
              "catalog still advertises the retired status placeholder "
              f"{STATUS_PLACEHOLDER!r}")
        check("<th scope=\"col\">Latest evidence</th>" in catalog,
              "catalog lacks a Latest evidence column")
        check('id="evaluation-sort"' in catalog,
              "catalog lacks the Sort control")
        for option in ("Newest evidence", "Oldest evidence", "Model A–Z", "Producer A–Z"):
            check(f">{option}</option>" in catalog, f"catalog sort option missing: {option}")
        check("<noscript" in catalog,
              "catalog lost its no-JavaScript fallback notice")

        events_by_model: dict[str, list[dict]] = {}
        for event in events:
            events_by_model.setdefault(event["model_id"], []).append(event)
        model_by_id = {m["model_id"]: m for m in models}
        expected_order: list[tuple[str, str]] = []
        for model in sorted(models, key=lambda item: item["display_name"].casefold()):
            latest = max(e["event_date"] for e in events_by_model.get(model["model_id"], []))
            expected_order.append((latest, model["model_id"]))
        expected_order.sort(key=lambda item: item[0], reverse=True)
        expected_ids = [model_id for _, model_id in expected_order]
        check(row_ids == expected_ids,
              "catalog static rows must sort newest event_date first, then Model A–Z")

        all_classifications = sorted({str(m["classification"]).lower()
                                      for m in generated_models.values()
                                      if m.get("classification")})
        for attrs, body in rows:
            model_id = data_attr(attrs, "data-model-id")
            assert model_id is not None
            model = model_by_id[model_id]
            front = front_by_model.get(model_id, {})
            latest = max(e["event_date"] for e in events_by_model[model_id])
            check(data_attr(attrs, "data-model") == model["display_name"].lower(),
                  f"{model_id}: data-model disagrees with display name")
            check(data_attr(attrs, "data-producer") == model["vendor"].lower(),
                  f"{model_id}: data-producer disagrees with canonical producer")
            check(data_attr(attrs, "data-latest-evidence") == latest,
                  f"{model_id}: data-latest-evidence disagrees with event_date")
            check(generated_models.get(model_id, {}).get("latest_evidence_date") == latest,
                  f"{model_id}: generated latest_evidence_date disagrees with event_date")
            check(f"<td>{latest}</td>" in body,
                  f"{model_id}: rendered Latest evidence does not match event_date")
            cells = re.findall(r"<t[dh]\b", body)
            check(len(cells) == CATALOG_COLUMNS,
                  f"{model_id}: catalog row must have exactly {CATALOG_COLUMNS} cells")
            # data-search mirrors the page front matter verbatim (title, identifier,
            # producer, recommended profile, practical context) and nothing else.
            profile = front.get("recommended_profile_name") or "No recommended profile recorded"
            context = front.get("practical_context") or "Not recorded"
            expected_search = " ".join(
                (front.get("title") or model["display_name"],
                 model_id, model["vendor"], profile, context)).lower()
            actual_search = data_attr(attrs, "data-search") or ""
            check(actual_search == expected_search,
                  f"{model_id}: data-search must mirror the five front-matter fields "
                  f"(got {actual_search!r}, expected {expected_search!r})")
            classification = generated_models.get(model_id, {}).get("classification")
            leaks = [c for c in all_classifications if c in actual_search.lower()]
            check(not leaks,
                  f"{model_id}: data-search leaks status/classification text: {leaks}")
            if isinstance(classification, str) and classification:
                for variant in (classification.lower(), classification.replace("_", " ").lower()):
                    check(variant not in actual_search.lower(),
                          f"{model_id}: data-search leaks the classification {variant!r}")
            check(model_id in actual_search,
                  f"{model_id}: data-search omits model identifier")
    # 2. navigation: canonical public surfaces are discoverable; Labs is retired.
    home = html(PUBLIC / "index.html")
    for label, dest in (("Evaluations", "/evaluations/"), ("Research", "/records/"),
                        ("Methodology", "/methodology/"),
                        ("About", "/about/"), ("Links", "/contact/")):
        check(re.search(rf'<a\b[^>]*href="{re.escape(dest)}"[^>]*>{label}</a>', home),
              f"primary navigation missing {label} ({dest})")
    check(">Projects<" not in home, "primary navigation still exposes Projects")
    for page in PUBLIC.glob("*/index.html"):
        body = html(page)
        if 'href="/labs/"' in body:
            failures.append(f"{page}: links retired destination /labs/")

    # 2b. homepage: each research destination exactly twice (global nav + one
    # main route set — a duplicated route panel would re-expose the destination).
    main_block = re.search(r"<main\b[^>]*>(.*)</main>", home, flags=re.DOTALL)
    check(main_block is not None, "homepage lost its main content landmark")
    if main_block is not None:
        main_html = main_block.group(1)
        chrome = home[:main_block.start()]
        for label, dest in (("Evaluations", "/evaluations/"),
                            ("Research", "/records/"),
                            ("Methodology", "/methodology/")):
            total = sum(urlsplit(h).path.rstrip("/") == dest.rstrip("/")
                        for h in re.findall(r'href="([^"]+)"', home))
            check(total == 2,
                  f"homepage must link {label} exactly twice (global nav + one main "
                  f"route set); found {total}")
            in_main = sum(urlsplit(h).path.rstrip("/") == dest.rstrip("/")
                          for h in re.findall(r'href="([^"]+)"', main_html))
            check(in_main == 1,
                  f"homepage main content must expose exactly one {label} route "
                  f"(duplicate route panel?); found {in_main}")
            in_chrome = sum(urlsplit(h).path.rstrip("/") == dest.rstrip("/")
                            for h in re.findall(r'href="([^"]+)"', chrome))
            check(in_chrome == 1,
                  f"homepage global navigation must expose {label} exactly once; "
                  f"found {in_chrome}")
        check('id="systems"' not in main_html and 'class="inventory-list"' not in main_html,
              "homepage still exposes a hardware inventory")

    # 3. retired Labs section root and model routes remain covered by _redirects.
    check("/labs/" in redirects, "_redirects missing entry for /labs/")
    for m in models:
        source = f"/labs/{url_slug(m['model_id'])}/"
        check(source in redirects, f"_redirects missing entry for {source}")
    check("/records/" not in redirects, "/records/ must remain the Reports index")

    # 4. event-style legacy stubs: served from /labs/, targeting /evaluations/ anchors
    for m in migration:
        if m["mechanism"] != "html-stub-meta-refresh":
            continue
        old = m["old_url"].strip("/")
        stub = PUBLIC / old / "index.html"
        check(stub.is_file(), f"missing legacy stub page at {m['old_url']}")
        if stub.is_file():
            body = html_unescape(html(stub))
            check(f"0; url={m['new_url']}" in body,
                  f"stub {m['old_url']} does not meta-refresh to {m['new_url']}")
            check(f'href="{m["new_url"]}"' in body,
                  f"stub {m['old_url']} does not link {m['new_url']}")
    labs_built = {p.parent.name for p in (PUBLIC / "labs").glob("*/index.html")} \
        if (PUBLIC / "labs").is_dir() else set()
    stub_slugs = {m["old_url"].rstrip("/").rsplit("/", 1)[-1]
                  for m in migration if m["mechanism"] == "html-stub-meta-refresh"}
    check(labs_built == stub_slugs,
          f"/labs/ must contain only legacy event stubs; found {sorted(labs_built)} "
          f"expected {sorted(stub_slugs)}")
    check(not (PUBLIC / "labs" / "index.html").exists(),
          "/labs/ index page must not be built (covered by _redirects)")

    # 5. Reports is the canonical archive for long-form evidence.
    records_index = PUBLIC / "records" / "index.html"
    check(records_index.is_file(), "missing /records/ Reports index")
    if records_index.is_file():
        body = html_unescape(html(records_index))
        check("Research" in body, "/records/ does not render the Research archive")
        check("COMPATIBILITY REDIRECT" not in body, "/records/ still renders a redirect")
    for m in migration:
        if m["mechanism"] != "url-preserved":
            continue
        check((PUBLIC / m["new_url"].strip("/") / "index.html").is_file(),
              f"preserved technical record missing: {m['new_url']}")
    for source in sorted(path for path in Path("content/records").glob("*.md") if path.name != "_index.md"):
        record_url = f'/records/{source.stem}/'
        check(record_url in html_unescape(html(records_index)),
              f"Reports index does not link {record_url}")

    projects_page = html_unescape(html(PUBLIC / "projects" / "index.html"))
    check("not a project directory" in projects_page,
          "/projects/ is not a compatibility notice")
    for slug in ("llmgauge", "wumbos", "monolith", "wumbojetsii", "wumbo-core"):
        check(f'/projects/{slug}/' not in projects_page,
              f"compatibility index lists /projects/{slug}/")
        check((PUBLIC / "projects" / slug / "index.html").is_file(),
              f"missing compatibility page /projects/{slug}/")
    check("Technical notes" not in projects_page.lower(),
          "Projects still renders a Technical Notes section")
    eval_page = html_unescape(html(PUBLIC / "evaluations" / "index.html"))
    check("Historical evaluation notice" in eval_page, "missing historical evaluation notice")
    granite = html(PUBLIC / "evaluations" / "granite-4-2-8b" / "index.html")
    check("welp-next-snapshot-2026-09-24-context-outcome-repair" in granite,
          "granite event missing recorded methodology snapshot")
    lfm = html(PUBLIC / "evaluations" / "lfm2-5-8b-a1b" / "index.html")
    check("welp-next-snapshot-2026-09-24-review-and-setup-hardening" in lfm,
          "LFM adjudication event missing recorded export snapshot")

    qwen_eval = html(PUBLIC / "evaluations" / "qwen38-27b" / "index.html")
    check('href="/records/qwen38-27b-rtx5070-evaluation/"' in qwen_eval,
          "Qwen3.8 long-form campaign report not linked from its Evaluation page")

    # 6. Qwen3.8 multi-profile/multi-event fixture
    for needle in ("qwen38-27b-llamacpp-ud-q2-k-xl", "qwen38-27b-exl3-h1",
                   "initial-evaluation-2026-08-21", "h1-canonical-promotion-2026-09-09",
                   "context-envelope-completion-2026-09-12",
                   "65,536", "98,304", "262,144", "1,000,000", "INTEGRATION_BLOCKED"):
        check(needle in qwen_eval, f"Qwen3.8 evaluation page missing {needle!r}")
    for m in models:
        page = PUBLIC / "evaluations" / url_slug(m["model_id"]) / "index.html"
        if page.is_file():
            body = html(page)
            for e in [ev for ev in events if ev["model_id"] == m["model_id"]]:
                check(f'id="{e["event_id"]}"' in body,
                      f"{m['model_id']}: event anchor {e['event_id']} missing")
            for entry in registry["records"]:
                if m["model_id"] not in [entry["model_id"], *entry.get("related_model_ids", [])]:
                    continue
                evidence = entry["canonical_evidence"]
                check(evidence.get("repo") == "WumboLabs/evaluations"
                      and bool(re.fullmatch(r"[0-9a-f]{40}", evidence.get("commit", ""))),
                      f"{entry['event_id']}: canonical evidence must use central full-commit pin")
                check(f'href="{evidence["url"]}"' in body,
                      f"{m['model_id']}: immutable report link missing for {entry['event_id']}")
                if entry["model_id"] == m["model_id"]:
                    for url in entry.get("profile_metadata_urls", {}).values():
                        check(f'href="{url}"' in body,
                              f"{m['model_id']}: profile metadata link missing: {url}")

    # 7. events dataset points at canonical Evaluations routes
    for e in events:
        check(e["model_url"].startswith("/evaluations/"),
              f"events dataset model_url for {e['event_id']} is not /evaluations/: "
              f"{e['model_url']}")

    # 7b. 2026-09-12 census: maturity labels, specialized/benchmark-only
    # representation, shared multi-model events, orphan rejection
    for e in events:
        check(bool(e.get("evidence_maturity")),
              f"event {e['event_id']} has no evidence_maturity label")
    by_model: dict[str, list[dict]] = {}
    for e in events:
        by_model.setdefault(e["model_id"], []).append(e)
    # required census fixtures: previously omitted models now represented
    census_fixtures = {
        "mellum2-12b-a2.5b": "Mellum2 Agent Backend Test",
        "gemma-4-12b": "Gemma 4 12B",
        "gemmable-4-12b": "Gemmable",
        "grug-12b": "Grug",
        "qwen3-14b": "Qwen3-14B",
        "qwen3.6-35b-a3b": "Qwen3.6-35B",
        "qwen2.5-3b": "Qwen2.5-3B",
        "bonsai-27b": "Bonsai",
    }
    for mid, needle in census_fixtures.items():
        check(mid in {m["model_id"] for m in models},
              f"census model {mid} missing from the registry catalog")
        page = PUBLIC / "evaluations" / url_slug(mid) / "index.html"
        check(page.is_file(), f"census model page missing: /evaluations/{url_slug(mid)}/")
        if page.is_file():
            body = html_unescape(html(page))
            check(needle in body, f"model page {mid} missing identity text {needle!r}")
            check("SPECIALIZED_TEST" in body or "BENCHMARK_ONLY" in body or "PRACTICAL_USE" in body,
                  f"model page {mid} displays no bounded maturity label")
    # maturity labels rendered on every model page event
    for m in models:
        page = PUBLIC / "evaluations" / url_slug(m["model_id"]) / "index.html"
        if not page.is_file():
            continue
        body = html_unescape(html(page))
        for e in by_model.get(m["model_id"], []):
            if e.get("evidence_maturity"):
                check(f"maturity: {e['evidence_maturity']}" in body,
                      f"{m['model_id']}: event {e['event_id']} missing its maturity label")
    # shared multi-model events attached to every related model page
    registry_by_event = {r["event_id"]: r for r in registry["records"]}
    for r in registry["records"]:
        for mid in r.get("related_model_ids") or []:
            page = PUBLIC / "evaluations" / url_slug(mid) / "index.html"
            check(page.is_file(), f"shared-event related model page missing: {mid}")
            if page.is_file():
                body = html_unescape(html(page))
                check("Shared comparison events" in body,
                      f"{mid}: shared comparison section missing")
                check(f"/evaluations/{url_slug(r['model_id'])}#{r['event_id']}" in body,
                      f"{mid}: shared event {r['event_id']} not linked on the model page")
        # canonical shared events must declare their shared_event_id
        if r.get("related_model_ids"):
            check(bool(r.get("shared_event_id")),
                  f"event {r['event_id']} has related_model_ids but no shared_event_id")
    # model-specific orphan rejection: the long-form model reports must be
    # linked from their canonical Evaluation pages (no model evidence whose
    # only discoverable home is a /records/ URL)
    for record_slug, model_slug in (
            ("mellum2-agent-backend-test", "mellum2-12b-a2-5b"),
            ("gemma-12b-practical-use", "gemma-4-12b")):
        record_page = PUBLIC / "records" / record_slug / "index.html"
        check(record_page.is_file(), f"record page missing: /records/{record_slug}/")
        if record_page.is_file():
            body = html_unescape(html(record_page))
            check(f"/evaluations/{model_slug}/" in body,
                  f"/records/{record_slug}/ does not link its canonical Evaluation page")
        model_page = PUBLIC / "evaluations" / model_slug / "index.html"
        if model_page.is_file():
            body = html_unescape(html(model_page))
            check(f"/records/{record_slug}/" in body,
                  f"/evaluations/{model_slug}/ does not link its long-form record /records/{record_slug}/")
    # exactly one canonical page per model: no dotted-slug duplicates outside
    # generated legacy stubs
    dotted = [p.name for p in (PUBLIC / "evaluations").glob("*.*.html*")]
    check(not dotted, f"unexpected dotted files under /evaluations/: {dotted}")

    # 8. shared findings-first model-page structure with source-grounded event
    # results; values outside closed <details>, raw JSON inside them.
    records_by_model: dict[str, list[dict]] = {}
    for entry in records:
        records_by_model.setdefault(entry["model_id"], []).append(entry)
    for m in models:
        mid = m["model_id"]
        page = PUBLIC / "evaluations" / url_slug(mid) / "index.html"
        if not page.is_file():
            continue
        dom = PageText(html(page))
        entries = records_by_model.get(mid, [])
        raw = dom.raw

        for section_id in REQUIRED_MODEL_SECTIONS:
            if section_id == "limitations" and not any(
                ((export_for(e) or {}).get("quality") or {}).get("key_guardrails")
                for e in entries
            ):
                continue
            check(section_id in dom.ids,
                  f"{mid}: shared model structure missing the {section_id!r} section")

        # page header stays classification-free; the date line carries evidence
        header_start = raw.find('<header class="page-record-header"')
        check(header_start >= 0, f"{mid}: model page lacks its page-record header")
        if header_start >= 0:
            header_end = raw.find("</header>", header_start)
            header_text = dom.visible_text(header_start, header_end).lower()
            latest_date = max((e["event_date"] for e in entries), default="")
            check(f"latest evidence {latest_date}" in header_text,
                  f"{mid}: page header must carry the latest evidence date")
            classification = generated_models.get(mid, {}).get("classification")
            if isinstance(classification, str) and classification:
                for variant in (classification.lower(),
                                classification.replace("_", " ").lower()):
                    check(variant not in header_text,
                          f"{mid}: page header must not advertise the page-wide "
                          f"classification {variant!r}")

        def section_bounds(start_ids: tuple[str, ...], end_ids: tuple[str, ...]) -> tuple[int, int]:
            starts = [dom.ids[s] for s in start_ids if s in dom.ids]
            lo = min(starts) if starts else 0
            ends = [dom.ids[e] for e in end_ids if e in dom.ids and dom.ids[e] > lo]
            return lo, (min(ends) if ends else len(raw))

        overview_lo, overview_hi = section_bounds(("overview",),
                                                  ("current-state", "findings"))
        overview_text = dom.visible_text(overview_lo, overview_hi)
        profile_ids = {e["profile_id"] for e in entries} | {
            rp for e in entries for rp in (e.get("related_profile_ids") or [])}
        check(str(len(profile_ids)) in overview_text and str(len(entries)) in overview_text,
              f"{mid}: overview must state the tested configuration and event counts")

        # every profile identity stays available on the page
        page_visible = dom.raw_text()
        for pid in sorted(profile_ids):
            check(pid in page_visible, f"{mid}: profile identity {pid!r} not available")

        # Findings keeps the event-attributed classification and latest evidence
        findings_lo, findings_hi = section_bounds(("findings",),
                                                  ("testing-history", "event-results"))
        findings_text = dom.visible_text(findings_lo, findings_hi)
        classification = generated_models.get(mid, {}).get("classification")
        if isinstance(classification, str) and classification:
            check(classification in findings_text,
                  f"{mid}: findings must attribute the classification to its event")
        for e in entries:
            check(any(urlsplit(href).fragment == e["event_id"] for _, href, _ in dom.links),
                  f"{mid}: findings/chronology must link event {e['event_id']}")

        # chronology: one compact row per event
        chron_lo, chron_hi = section_bounds(("chronology",),
                                            ("canonical-evidence", "technical-provenance"))
        chron_text = dom.visible_text(chron_lo, chron_hi)
        for e in entries:
            check(e["event_date"] in chron_text,
                  f"{mid}: chronology missing event date {e['event_date']}")
            title = e.get("event_title") or e["event_id"]
            check(_normalize(str(title)) in _normalize(chron_text),
                  f"{mid}: chronology missing event title for {e['event_id']}")

        # tested configurations: every profile listed with its full identity
        conf_lo, conf_hi = section_bounds(("tested-profiles", "tested-configurations"),
                                          ("chronology",))
        conf_text = dom.raw_text(conf_lo, conf_hi)
        names = {p["profile_id"]: p.get("profile_display_name")
                 for p in registry.get("profiles", [])}
        for e in entries:
            names.setdefault(e["profile_id"], e.get("profile_name"))
        for pid in sorted(profile_ids):
            check(pid in conf_text, f"{mid}: tested configurations missing profile {pid!r}")
            if names.get(pid):
                check(_normalize(names[pid]) in _normalize(conf_text),
                      f"{mid}: tested configurations missing full profile name for {pid!r}")

        # Event slices run from one event anchor to the next *structural*
        # boundary: another event anchor or a shared section anchor. Ids Zola
        # derives from the event's own headings (slugified titles, subsections)
        # must not truncate the slice.
        boundary_ids = ({e["event_id"] for e in events}
                        | {e["event_id"] for e in records}
                        | set(REQUIRED_MODEL_SECTIONS)
                        | {"current-state", "testing-history", "tested-profiles",
                           "chronology", "canonical-evidence"})
        boundary_offsets = sorted(off for name, off in dom.ids.items()
                                  if name in boundary_ids)
        for entry in entries:
            event_id = entry["event_id"]
            anchor = dom.ids.get(event_id)
            check(anchor is not None,
                  f"{mid}: event anchor {event_id} missing (per-event checks skipped)")
            if anchor is None:
                continue
            following = [off for off in boundary_offsets if off > anchor]
            lo, hi = anchor, (min(following) if following else len(raw))
            label = f"{mid} event {event_id}"
            export = export_for(entry)
            narrative = entry.get("authoring") != "generated"

            # every event keeps its identity header and citation links
            check(dom.locate(lo, hi, entry.get("event_kicker") or event_id) is not None,
                  f"{label}: event kicker not visible")
            if entry.get("evidence_maturity"):
                check(dom.locate(lo, hi, entry["evidence_maturity"]) is not None,
                      f"{label}: maturity label not visible")
            if entry.get("welp_status"):
                check(dom.locate(lo, hi, entry["welp_status"]) is not None,
                      f"{label}: recorded status not visible")
            check(entry["profile_id"] in dom.raw_text(lo, hi),
                  f"{label}: exact profile identity not available")
            if entry.get("related_profile_ids"):
                for pid in entry["related_profile_ids"]:
                    check(dom.locate(lo, hi, pid) is not None,
                          f"{label}: related profile {pid!r} not visible")
            recorded_welp = entry.get("welp") if isinstance(entry.get("welp"), dict) else {}
            if isinstance(recorded_welp.get("snapshot"), str) and recorded_welp["snapshot"].strip():
                check(dom.locate(lo, hi, recorded_welp["snapshot"].strip()) is not None,
                      f"{label}: recorded methodology snapshot not visible")
            evidence = entry.get("canonical_evidence") or {}
            ev_url = evidence.get("url")
            if ev_url:
                report_links = [1 for off, href, visible in dom.links
                                if lo <= off < hi and visible and href == ev_url]
                check(len(report_links) == 1,
                      f"{label}: expected exactly one visible canonical report link, "
                      f"found {len(report_links)}")
            report_page = entry.get("report_page")
            if report_page:
                long_url = f"/{report_page[:-3]}/" if report_page.endswith(".md") else report_page
                long_links = [1 for off, href, visible in dom.links
                              if lo <= off < hi and visible and href == long_url]
                check(len(long_links) == 1,
                      f"{label}: expected exactly one visible long-form report link, "
                      f"found {len(long_links)}")
            for pid, url in (entry.get("profile_metadata_urls") or {}).items():
                if pid == entry["profile_id"]:
                    # the own profile's metadata link lives in the configuration
                    # details; it must survive somewhere on the page
                    check(any(href == url for _, href, _ in dom.links),
                          f"{label}: profile metadata link missing: {url}")
                else:
                    check(any(href == url and visible and lo <= off < hi
                              for off, href, visible in dom.links),
                          f"{label}: related profile metadata link not visible: {url}")

            if narrative or not export:
                body_rel = entry.get("event_body")
                if narrative and body_rel:
                    body_path = Path("data") / body_rel
                    check(body_path.is_file(),
                          f"{label}: hand-authored body file missing: {body_rel}")
                    if body_path.is_file():
                        body = body_path.read_text(encoding="utf-8").rstrip()
                        gaps = _narrative_gaps(dom, lo, hi, body)
                        check(not gaps,
                              f"{label}: hand-authored narrative dropped or altered, "
                              f"e.g. {gaps[:2]}")
                # narrative attached exports must still preserve media evidence
                media = (export or {}).get("gameplay_media")
                if media:
                    slice_text = dom.raw_text(lo, hi)
                    check(media["url"] in slice_text and media["sha256"] in slice_text,
                          f"{label}: narrative event lost attached gameplay "
                          f"source/hash evidence")
                reason = (export or {}).get("gameplay_unavailable_reason")
                if reason:
                    check(reason in dom.raw_text(lo, hi),
                          f"{label}: gameplay availability statement missing")
                if export and export.get("welp_sections"):
                    check_raw_sections(label, export, dom, lo, hi)
                continue

            check_generated_event(label, entry, export, dom, lo, hi)

    # 9. every local link in built HTML resolves, including #fragment targets
    # (redirect routes resolve through the recorded route mappings)
    html_files = sorted(PUBLIC.rglob("*.html"))
    ids_by_file: dict[Path, frozenset[str]] = {}

    def fragment_ids(file_path: Path) -> frozenset[str]:
        cached = ids_by_file.get(file_path)
        if cached is None:
            cached = frozenset(re.findall(r'\b(?:id|name)="([^"]+)"',
                                          file_path.read_text(encoding="utf-8")))
            ids_by_file[file_path] = cached
        return cached

    redirect_target = redirect_targets()
    for m in migration:
        dest_path = urlsplit(m["new_url"]).path
        if ":" not in dest_path:
            redirect_target.setdefault(m["old_url"], dest_path)

    for path in html_files:
        body = html(path)
        own_ids = fragment_ids(path)
        for match in re.finditer(r'(?:href|src)="([^"]+)"', body):
            href = html_unescape(match.group(1))
            if href.startswith("//"):
                continue
            if href.startswith("#"):
                fragment = unquote(href[1:])
                if fragment and fragment not in own_ids:
                    failures.append(f"{path.relative_to(PUBLIC)}: broken local link {href}")
                continue
            parts = urlsplit(href)
            if parts.scheme and parts.hostname != "wumbolabs.dev":
                continue
            target = unquote(parts.path)
            fragment = unquote(parts.fragment)
            if not target or target == "/":
                continue
            fs_path = PUBLIC / target.lstrip("/")
            resolved = fs_path if fs_path.is_file() else fs_path / "index.html"
            if not resolved.is_file() and target in redirects:
                dest_path = redirect_target.get(target)
                if dest_path:
                    dest_fs = PUBLIC / dest_path.lstrip("/")
                    resolved = dest_fs if dest_fs.is_file() else dest_fs / "index.html"
            if not resolved.is_file():
                failures.append(f"{path.relative_to(PUBLIC)}: broken local link {href}")
                continue
            if fragment and fragment not in fragment_ids(resolved):
                failures.append(
                    f"{path.relative_to(PUBLIC)}: broken local link {href} "
                    f"(fragment target not found)")

    print(json.dumps({
        "status": "PASS" if not failures else "FAIL",
        "checks_run": checks,
        "html_files_scanned": len(html_files),
        "failures": failures,
    }, indent=2))
    return 0 if not failures else 1


def check_generated_event(label: str, entry: dict, export: dict,
                          dom: PageText, lo: int, hi: int) -> None:
    """One generated event's structured result: recorded values visible, raw
    JSON collapsed. Only consumer-visible presence is asserted; phrasing is
    never pinned."""
    ordered_offsets: list[int] = []

    def present(value, what: str, *, before_json: bool = True) -> int | None:
        if value in (None, ""):
            return None
        forms = list(value) if isinstance(value, (list, tuple)) else [value]
        forms = [str(form) for form in forms]
        off = next((dom.locate(lo, hi, form,
                               normalized_ok=_alnum_len(form) > 5)
                    for form in forms if dom.locate(lo, hi, form,
                                                    normalized_ok=_alnum_len(form) > 5) is not None),
                   None)
        check(off is not None,
              f"{label}: recorded {what} {forms[0][:70]!r} not visible")
        if off is not None and before_json:
            ordered_offsets.append(off)
        return off

    def available(value, what: str) -> None:
        """Exact secondary identity remains accessible, including in details."""
        if value is None or value == "":
            return
        text = dom.raw_text(lo, hi)
        check(_normalize(str(value)) in _normalize(text),
              f"{label}: recorded {what} not available")

    model = export.get("model") or {}
    artifact = export.get("artifact") or {}
    runtime = export.get("runtime") or {}
    hardware = export.get("hardware") or {}
    welp = export.get("welp") or {}
    ctx = export.get("context") or {}
    quality = export.get("quality") or {}
    perf = export.get("performance") or {}
    lmx = export.get("localmaxxing") or {}

    # Exact identities may be collapsed; scientific boundaries remain visible.
    available(model.get("display_name"), "model display name")
    available(model.get("producer"), "producer")
    available(artifact.get("tested"), "tested artifact")
    available(artifact.get("precision"), "artifact precision")
    available(artifact.get("sha256"), "artifact hash")
    available(export.get("campaign"), "campaign identifier")
    available(entry.get("record_date") or export.get("publication_date"), "record date")
    for key in ("engine", "name", "version", "tag", "commit", "build"):
        available(runtime.get(key), f"runtime {key}")
    available(hardware.get("machine"), "hardware machine")
    available(hardware.get("gpu"), "hardware GPU")
    present(runtime.get("notes"), "runtime notes")
    present(hardware.get("notes"), "hardware notes")

    # WELP outcome and classification
    present(welp.get("outcome"), "WELP outcome")
    present(welp.get("classification"), "WELP classification")
    present(welp.get("artifact_classification"), "artifact classification")
    present(welp.get("snapshot"), "methodology snapshot")
    present(welp.get("contract"), "classification contract")
    recorded_welp = entry.get("welp") if isinstance(entry.get("welp"), dict) else {}
    welp_commit = recorded_welp.get("welp_commit")
    if isinstance(welp_commit, str) and re.fullmatch(r"[0-9a-f]{40}", welp_commit):
        present(welp_commit, "recorded WELP commit pin")

    # context profile
    present(ctx.get("practical_default_tokens") and
            f"{ctx['practical_default_tokens']:,}", "practical default tokens")
    present(ctx.get("guarded_tokens") and f"{ctx['guarded_tokens']:,}",
            "guarded context tokens")
    present(ctx.get("useful_context_max_tokens") and
            f"{ctx['useful_context_max_tokens']:,}", "useful context maximum")
    present(ctx.get("native_maximum_tokens") and
            f"{ctx['native_maximum_tokens']:,}", "native model-card maximum")
    present(("YES" if ctx.get("envelope_complete") else "NO")
            if isinstance(ctx.get("envelope_complete"), bool)
            else ctx.get("envelope_complete"), "envelope completion")
    present(ctx.get("native_maximum_disposition"), "native maximum disposition")
    present(ctx.get("notes"), "context notes")

    # headline performance
    for key, what_key in (("short_ttft_s", "short-context TTFT"),
                          ("short_decode_tps", "short-context decode rate"),
                          ("moderate_input_tokens", "moderate input size"),
                          ("moderate_ttft_s", "moderate TTFT"),
                          ("moderate_prefill_tps", "moderate prefill rate"),
                          ("moderate_decode_tps", "moderate decode rate")):
        value = perf.get(key)
        present(value_forms(value) if isinstance(value, float) else value, what_key)
    present(perf.get("surface_note"), "performance surface note")

    # quality and capabilities
    present(quality.get("constrained_result"), "constrained result")
    for cap in quality.get("capability_highlights") or []:
        if _COUNT_HIGHLIGHT_RE.match(str(cap)):
            continue  # superseded by the derived section summaries
        present(cap, "capability highlight")
    for guard in quality.get("key_guardrails") or []:
        present(guard, "key guardrail")
    present(quality.get("reliability_summary"), "reliability summary")

    # section results: units, outcomes, coverage, objective scores, subchecks
    sections = export.get("welp_sections") or []
    for section in sections:
        what = str(section.get("section"))
        present(section.get("section"), f"{what} section name")
        present(section.get("methodology"), f"{what} methodology")
        units = section.get("units") or []
        if units:
            counts = Counter(u.get("outcome") or "UNSPECIFIED" for u in units)
            present(f"{len(units)} recorded", f"{what} unit count")
            for outcome, count in sorted(counts.items()):
                present(f"{count} {outcome}", f"{what} unit outcome counts")
            # negative and unevaluable unit outcomes stay readable with their
            # recorded reasons and budgets, not just in the collapsed JSON
            for unit in units:
                if (unit.get("outcome") or "UNSPECIFIED") in ("PASS", ""):
                    continue
                uid = str(unit.get("unit_id"))
                present(unit.get("unit_id"), f"{what} failed unit identity {uid}")
                present(unit.get("outcome"), f"{what} unit {uid} outcome")
                present(unit.get("reason"), f"{what} unit {uid} reason")
                limits = unit.get("limits")
                if isinstance(limits, dict):
                    for key, bound in limits.items():
                        present(key, f"{what} unit {uid} limit {key}")
                        if isinstance(bound, (int, float)) and not isinstance(bound, bool):
                            present(value_forms(bound), f"{what} unit {uid} budget {key}")
                elif limits not in (None, ""):
                    present(limits, f"{what} unit {uid} limits")
        advancement = (section.get("advancement") or {}).get("decision")
        present(advancement, f"{what} advancement decision")
        coverage = section.get("coverage") or {}
        present(coverage.get("status"), f"{what} coverage status")
        present(coverage.get("rule"), f"{what} coverage rule")
        present(coverage.get("advancement"), f"{what} coverage advancement")
        for name, c in (coverage.get("categories") or {}).items():
            present(name, f"{what} coverage category {name}")
            if c.get("status"):
                present(c.get("status"), f"{what} coverage status for {name}")
            if c.get("fail"):
                # important failures stay visible in the section coverage table
                present(name.replace("_", " "), f"{what} coverage failure {name}")
        memory = section.get("memory") or {}
        vram = memory.get("sampled_vram_used_max_bytes")
        if isinstance(vram, int):
            present(f"{vram:,}", f"{what} sampled VRAM maximum")
        for obs in section.get("performance_observations") or []:
            present(obs.get("unit_id"), f"{what} timed sample unit")
        score = section.get("objective_benchmark")
        if score:
            present(value_forms(score["final_score"])
                    if isinstance(score.get("final_score"), float)
                    else score.get("final_score"), f"{what} objective final score")
            present(score.get("class"), f"{what} objective class")
            points = score.get("mechanical_points")
            maximum = score.get("mechanical_max")
            if points is not None and maximum is not None:
                present([f"{fmt_num(points)}/{fmt_num(maximum)}",
                         f"{points}/{maximum}"], f"{what} mechanical points")
            results = Counter()
            for category in (score.get("categories") or {}).values():
                for subcheck in (category.get("subchecks") or {}).values():
                    if subcheck.get("unevaluable") or subcheck.get("pass") is None:
                        results["UNEVALUABLE"] += 1
                    else:
                        results["PASS" if subcheck.get("pass") else "FAIL"] += 1
            for outcome, count in sorted(results.items()):
                if count:
                    present(f"{count} {outcome}", f"{what} objective check counts")
            present(score.get("generation_outcome"), f"{what} generation outcome")
            for name, category in (score.get("categories") or {}).items():
                present(name, f"{what} objective category {name}")
                if category.get("points") is not None:
                    present(fmt_num(category.get("points")),
                            f"{what} objective points for {name}")
                for check_id, subcheck in (category.get("subchecks") or {}).items():
                    # every subcheck (failures and unevaluable checks included)
                    # stays visible with its recorded outcome
                    present(check_id, f"{what} objective subcheck {check_id}")
                    if subcheck.get("unevaluable") or subcheck.get("pass") is None:
                        present("UNEVALUABLE", f"{what} subcheck {check_id} outcome")
                    else:
                        present("PASS" if subcheck.get("pass") else "FAIL",
                                f"{what} subcheck {check_id} outcome")

    payload_off = check_raw_sections(label, export, dom, lo, hi) if sections else None
    if payload_off is not None:
        for off in ordered_offsets:
            check(off < payload_off,
                  f"{label}: scientific results must precede collapsed raw JSON")

    # gameplay evidence: controls, source and hash preserved
    media = export.get("gameplay_media")
    if media:
        video_hits = [attrs for off, attrs in dom.videos if lo <= off < hi]
        check(any("controls" in attrs for attrs in video_hits),
              f"{label}: gameplay video must keep native controls")
        media_links = [1 for off, href, _ in dom.links
                       if lo <= off < hi and href == media["url"]]
        check(len(media_links) >= 2,
              f"{label}: gameplay video source and download links missing")
        present(media.get("sha256"), "gameplay video SHA-256", before_json=False)
        present(media.get("methodology"), "gameplay methodology", before_json=False)
    elif export.get("gameplay_unavailable_reason"):
        present(export["gameplay_unavailable_reason"], "gameplay availability "
                "statement", before_json=False)

    # LocalMaxxing record
    present(lmx.get("status"), "LocalMaxxing status", before_json=False)
    present(lmx.get("canonical_context_tokens") and
            f"{lmx['canonical_context_tokens']:,}", "LocalMaxxing canonical context",
            before_json=False)
    present(lmx.get("tok_s_out"), "LocalMaxxing tok/s out", before_json=False)
    present(lmx.get("ttft_ms"), "LocalMaxxing TTFT", before_json=False)
    present(lmx.get("submission_ref"), "LocalMaxxing submission reference",
            before_json=False)
    if lmx.get("verified_run") is not None:
        present("YES" if lmx.get("verified_run") else "NO",
                "LocalMaxxing verifiedRun", before_json=False)
    present(lmx.get("note"), "LocalMaxxing note", before_json=False)


if __name__ == "__main__":
    raise SystemExit(main())
