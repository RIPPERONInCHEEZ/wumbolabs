#!/usr/bin/env python3
"""Validate public content ownership and project-directory boundaries after zola build."""
from __future__ import annotations

import tomllib
from html import unescape as html_unescape
from pathlib import Path

CONTENT = Path("content")
PUBLIC = Path("public")
EXPECTED_PROJECTS = {
    "llmgauge.md": "LLMGauge",
    "wumbos.md": "wumbOS",
    "monolith.md": "Monolith",
}


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
    for path in project_files:
        data = frontmatter(path)
        extra = data.get("extra", {})
        if "public_project" not in extra:
            failures.append(f"{path}: explicit extra.public_project is required")
            continue
        if extra["public_project"]:
            public_projects[path.name] = data["title"]

    if public_projects != EXPECTED_PROJECTS:
        failures.append(f"public projects must be exactly {EXPECTED_PROJECTS}; found {public_projects}")

    projects_index = (CONTENT / "projects" / "_index.md").read_text(encoding="utf-8").lower()
    if "technical notes" in projects_index:
        failures.append("Projects index still contains Technical Notes")

    records_index = frontmatter(CONTENT / "records" / "_index.md")
    if records_index.get("title") != "Lab Records" or records_index.get("template") != "records_index.html":
        failures.append("Lab Records index is not the canonical records surface")

    methodology = (CONTENT / "methodology" / "_index.md").read_text(encoding="utf-8")
    if "Local LLM Baseline" in methodology:
        failures.append("Methodology presents Local LLM Baseline as current method")

    baseline = (CONTENT / "records" / "local-llm-baseline.md").read_text(encoding="utf-8")
    if "historical baseline predates the current welp" not in baseline.lower():
        failures.append("Local LLM Baseline lacks historical/WELP boundary")

    if PUBLIC.is_dir():
        projects_html = (PUBLIC / "projects" / "index.html")
        if not projects_html.is_file():
            failures.append("built Projects index is missing")
        else:
            body = html_unescape(projects_html.read_text(encoding="utf-8"))
            for slug in ("llmgauge", "wumbos", "monolith"):
                if f'/projects/{slug}/' not in body:
                    failures.append(f"built Projects index misses /projects/{slug}/")
            for slug in ("wumbojetsii", "wumbo-core"):
                if f'/projects/{slug}/' in body:
                    failures.append(f"built Projects index leaks /projects/{slug}/")

    if failures:
        print("FAIL")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("PASS: public project and content-ownership contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
