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
