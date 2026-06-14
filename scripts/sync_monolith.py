#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

STATUS_URL = "https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/website/public_status.json"
ROADMAP_URL = "https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/ROADMAP.md"

STATUS_OUTPUT = Path("data/generated/monolith-status.json")
ROADMAP_OUTPUT = Path("data/generated/monolith-roadmap.md")

START_MARKER = "<!-- website-roadmap:start -->"
END_MARKER = "<!-- website-roadmap:end -->"

REQUIRED_STATUS_KEYS = {
    "project",
    "status",
    "current_release",
    "repository_url",
    "license_status",
    "canonical_local_url",
    "canonical_start_command",
    "summary",
    "audience",
    "positioning",
    "capabilities",
    "caveats",
    "current_focus",
}

REQUIRED_LIST_KEYS = {
    "positioning",
    "capabilities",
    "caveats",
    "current_focus",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def fetch_text(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            if response.status != 200:
                fail(f"fetch failed for {url} with HTTP status {response.status}")
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        fail(f"fetch failed for {url} with HTTP {exc.code}: {exc.reason}")
    except urllib.error.URLError as exc:
        fail(f"fetch failed for {url}: {exc.reason}")
    except UnicodeDecodeError as exc:
        fail(f"source file is not valid UTF-8 for {url}: {exc}")


def validate_status_json(raw: str) -> dict[str, Any]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"public_status.json is invalid JSON: {exc}")

    if not isinstance(data, dict):
        fail("public_status.json root must be a JSON object")

    missing = sorted(REQUIRED_STATUS_KEYS - data.keys())
    if missing:
        fail("public_status.json missing required keys: " + ", ".join(missing))

    for key in REQUIRED_STATUS_KEYS - REQUIRED_LIST_KEYS:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            fail(f"public_status.json key '{key}' must be a non-empty string")

    for key in REQUIRED_LIST_KEYS:
        value = data.get(key)
        if not isinstance(value, list) or not value:
            fail(f"public_status.json key '{key}' must be a non-empty list")
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                fail(f"public_status.json key '{key}' item {index} must be a non-empty string")

    return data


def extract_roadmap_block(source: str) -> str:
    start_count = source.count(START_MARKER)
    end_count = source.count(END_MARKER)

    if start_count != 1:
        fail(f"expected exactly one roadmap start marker, found {start_count}")

    if end_count != 1:
        fail(f"expected exactly one roadmap end marker, found {end_count}")

    start_index = source.find(START_MARKER)
    end_index = source.find(END_MARKER)

    if end_index < start_index:
        fail("roadmap end marker appears before start marker")

    block_start = start_index + len(START_MARKER)
    block = source[block_start:end_index].strip()

    if not block:
        fail("extracted roadmap block is empty")

    return block + "\n"


def write_text(path: Path, content: str) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        fail(f"failed to write {path}: {exc}")


def main() -> int:
    status_raw = fetch_text(STATUS_URL)
    status_data = validate_status_json(status_raw)
    status_output = json.dumps(status_data, indent=2, ensure_ascii=False) + "\n"
    write_text(STATUS_OUTPUT, status_output)

    roadmap_raw = fetch_text(ROADMAP_URL)
    roadmap_block = extract_roadmap_block(roadmap_raw)
    write_text(ROADMAP_OUTPUT, roadmap_block)

    print("Monolith website sync complete")
    print(f"status source:  {STATUS_URL}")
    print(f"status output:  {STATUS_OUTPUT}")
    print(f"roadmap source: {ROADMAP_URL}")
    print(f"roadmap output: {ROADMAP_OUTPUT}")
    print(f"roadmap lines:  {len(roadmap_block.splitlines())}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
