#!/usr/bin/env python3
"""Validate public content ownership after zola build."""
from __future__ import annotations

import tomllib
from html import unescape as html_unescape
from pathlib import Path

CONTENT = Path("content")
PUBLIC = Path("public")
LEGACY_PROJECTS = (
    "llmgauge.md",
    "wumbos.md",
    "monolith.md",
    "wumbojetsii.md",
    "wumbo-core.md",
)


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        raise ValueError(f"{path}: missing TOML frontmatter")
    _, raw, _ = text.split("+++", 2)
    return tomllib.loads(raw)


def main() -> int:
    failures: list[str] = []
    project_files = sorted(path for path in (CONTENT / "projects").glob("*.md") if path.name != "_index.md")
    public_projects: dict[str, str] = {}
    seen = set()
    for path in project_files:
        data = frontmatter(path)
        extra = data.get("extra", {})
        seen.add(path.name)
        if "public_project" not in extra:
            failures.append(f"{path}: explicit extra.public_project is required")
            continue
        if extra["public_project"]:
            public_projects[path.name] = data["title"]
        if data.get("in_search", True):
            failures.append(f"{path}: compatibility project pages must set in_search = false")
    if seen != set(LEGACY_PROJECTS):
        failures.append(f"project compatibility pages must be exactly {LEGACY_PROJECTS}; found {sorted(seen)}")
    if public_projects:
        failures.append(f"no project page may be a public directory entry; found {public_projects}")

    projects_index = (CONTENT / "projects" / "_index.md").read_text(encoding="utf-8").lower()
    if "technical notes" in projects_index:
        failures.append("Projects index still contains Technical Notes")

    records_index = frontmatter(CONTENT / "records" / "_index.md")
    if records_index.get("title") != "Research" or records_index.get("template") != "records_index.html":
        failures.append("Research index is not the canonical /records/ surface")

    methodology = (CONTENT / "methodology" / "_index.md").read_text(encoding="utf-8")
    if "Under Construction" not in methodology:
        failures.append("Methodology is not the WELP under-construction holding page")
    if "S00" in methodology or "Model Configuration Authority" in methodology:
        failures.append("Methodology still presents detailed current WELP protocol")

    baseline = (CONTENT / "records" / "local-llm-baseline.md").read_text(encoding="utf-8")
    if "historical baseline predates the current welp" not in baseline.lower():
        failures.append("Local LLM Baseline lacks historical/WELP boundary")

    if PUBLIC.is_dir():
        projects_html = PUBLIC / "projects" / "index.html"
        if not projects_html.is_file():
            failures.append("built project compatibility index is missing")
        else:
            body = html_unescape(projects_html.read_text(encoding="utf-8"))
            if ">Projects<" in body:
                failures.append("built /projects/ still uses the Projects navigation label")
            for slug in ("llmgauge", "wumbos", "monolith", "wumbojetsii", "wumbo-core"):
                if f'/projects/{slug}/' in body:
                    failures.append(f"compatibility index lists /projects/{slug}/")
                leaf = PUBLIC / "projects" / slug / "index.html"
                if not leaf.is_file():
                    failures.append(f"compatibility page missing: /projects/{slug}/")
        home = html_unescape((PUBLIC / "index.html").read_text(encoding="utf-8"))
        for banned in ("LLMGauge", "wumbOS", "flagship", "/projects/"):
            if banned in home:
                failures.append(f"homepage still promotes {banned}")
        evaluations = html_unescape((PUBLIC / "evaluations" / "index.html").read_text(encoding="utf-8"))
        if "Historical evaluation notice" not in evaluations:
            failures.append("evaluations catalog missing historical notice")
        if "Not every entry was produced by WELP" not in evaluations:
            failures.append("evaluations notice implies every result was WELP")
        method = html_unescape((PUBLIC / "methodology" / "index.html").read_text(encoding="utf-8"))
        if "Under Construction" not in method:
            failures.append("built methodology page is not the holding page")

    if failures:
        print("FAIL")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("PASS: research-site content ownership contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
