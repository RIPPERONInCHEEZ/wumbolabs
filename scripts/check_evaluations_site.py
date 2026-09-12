#!/usr/bin/env python3
"""check_evaluations_site.py — post-build public-route validation.

Validates the consolidated public Evaluations contract against the built site
(public/) and the generated datasets (data/generated/). Run after
`zola build` from the repository root:

    python scripts/check_evaluations_site.py

Checks:
  - one Evaluations index; exactly one canonical page per registry model;
  - primary navigation is Projects / Evaluations / Methodology / About /
    Contact (no Labs / Lab Records / Records destinations);
  - retired /labs/ + /records/ section roots are covered by _redirects;
  - event-style legacy stubs still serve at their /labs/ URLs and target the
    /evaluations/<model>/#<event> anchors;
  - technical records keep their URLs and stay discoverable;
  - /records/ no longer renders a standalone archive index;
  - the Qwen3.8-27B multi-profile fixture (profiles, events, anchors, context
    state, canonical profile repositories);
  - all local links in built HTML resolve (built pages, redirects, or
    fragment-only).

Exit codes: 0 PASS; 1 FAIL.
"""
from __future__ import annotations

import json
import re
import sys
from html import unescape as html_unescape
from pathlib import Path
from urllib.parse import unquote

PUBLIC = Path("public")
REGISTRY = Path("data/labs-registry.json")
REDIRECTS_FILE = Path("static/_redirects")
EVENTS_DATA = Path("data/generated/labs-events.json")
ROUTE_MIGRATION = Path("data/generated/route-migration.json")

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


def main() -> int:
    if not PUBLIC.is_dir():
        print("ERROR: public/ not found — run `zola build` first")
        return 1

    registry = load_json(REGISTRY)
    models = registry["models"]
    events = load_json(EVENTS_DATA)["events"]
    migration = load_json(ROUTE_MIGRATION)["mappings"]
    redirects = redirect_sources()

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

    # 2. navigation: Evaluations present; Labs / Lab Records / Records absent
    home = html(PUBLIC / "index.html")
    for label, dest in (("Evaluations", "/evaluations/"), ("Projects", "/projects/"),
                        ("Methodology", "/methodology/"), ("About", "/about/"),
                        ("Contact", "/contact/")):
        check(f'href="{dest}"' in home, f"primary navigation missing {label} ({dest})")
    for dest in ("/labs/", "/records/"):
        check(dest not in home, f"homepage still links retired destination {dest}")
    for page in PUBLIC.glob("*/index.html"):
        body = html(page)
        for dest in ("/labs/", "/records/"):
            if f'href="{dest}"' in body or f'href="{dest}"' in body:
                failures.append(f"{page}: links retired destination {dest}")
                break
    # direct nav-label check: no visible ">Labs<"/">Lab Records<"/">Records<" anchors
    for label in ("Labs", "Lab Records", "Records"):
        check(not re.search(rf">{''.join(label)}<", home),
              f"homepage renders a nav anchor labeled {label!r}")

    # 3. retired section roots covered by _redirects
    for source in ("/labs/", "/records/"):
        check(source in redirects, f"_redirects missing entry for {source}")
    for m in models:
        source = f"/labs/{url_slug(m['model_id'])}/"
        check(source in redirects, f"_redirects missing entry for {source}")

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

    # 5. /records/: no competing archive; technical records keep URLs
    records_index = PUBLIC / "records" / "index.html"
    if records_index.is_file():
        body = html(records_index)
        check("COMPATIBILITY REDIRECT" in body,
              "/records/ still renders a standalone index (must be a redirect)")
        check("All records" not in body, "/records/ still renders the records archive list")
    for m in migration:
        if m["mechanism"] != "url-preserved":
            continue
        check((PUBLIC / m["new_url"].strip("/") / "index.html").is_file(),
              f"preserved technical record missing: {m['new_url']}")
    projects_page = html(PUBLIC / "projects" / "index.html")
    for slug in ("wumbolabs-first-build", "local-llm-baseline",
                 "mellum2-agent-backend-test", "gemma-12b-practical-use"):
        check(f'href="/records/{slug}/"' in projects_page,
              f"technical record /records/{slug}/ not discoverable from Projects")
    qwen_eval = html(PUBLIC / "evaluations" / "qwen38-27b" / "index.html")
    check('href="/records/qwen38-27b-rtx5070-evaluation/"' in qwen_eval,
          "Qwen3.8 long-form campaign report not linked from its Evaluation page")

    # 6. Qwen3.8 multi-profile/multi-event fixture
    for needle in ("eval-qwen3.8-27b-llamacpp", "eval-qwen3.8-27b-exl3-h1",
                   "initial-evaluation-2026-08-21", "h1-canonical-promotion-2026-09-09",
                   "context-envelope-completion-2026-09-12",
                   "65,536", "98,304", "262,144", "1,000,000", "INTEGRATION_BLOCKED",
                   "MODEL-CARD CONTEXT ENVELOPE COMPLETE"):
        check(needle in qwen_eval, f"Qwen3.8 evaluation page missing {needle!r}")
    for m in models:
        page = PUBLIC / "evaluations" / url_slug(m["model_id"]) / "index.html"
        if page.is_file():
            body = html(page)
            for e in [ev for ev in events if ev["model_id"] == m["model_id"]]:
                check(f'id="{e["event_id"]}"' in body,
                      f"{m['model_id']}: event anchor {e['event_id']} missing")

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

    # 8. every local link in built HTML resolves
    html_files = sorted(PUBLIC.rglob("*.html"))
    for path in html_files:
        body = html(path)
        for href in re.findall(r'(?:href|src)="(/[^"]*)"', body):
            href = unquote(href)
            if href.startswith("//"):
                continue
            target = href.split("#", 1)[0]
            if not target or target == "/":
                continue
            fs_path = PUBLIC / target.lstrip("/")
            resolved = fs_path if fs_path.is_file() else fs_path / "index.html"
            if resolved.is_file() or target in redirects:
                continue
            failures.append(f"{path.relative_to(PUBLIC)}: broken local link {href}")

    print(json.dumps({
        "status": "PASS" if not failures else "FAIL",
        "checks_run": checks,
        "html_files_scanned": len(html_files),
        "failures": failures,
    }, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
