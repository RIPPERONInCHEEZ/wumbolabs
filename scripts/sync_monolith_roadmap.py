#!/usr/bin/env python3
from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/ROADMAP.md"
OUTPUT_PATH = Path("data/generated/monolith-roadmap.md")

START_MARKER = "<!-- website-roadmap:start -->"
END_MARKER = "<!-- website-roadmap:end -->"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def fetch_source(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            if response.status != 200:
                fail(f"fetch failed with HTTP status {response.status}")
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        fail(f"fetch failed with HTTP {exc.code}: {exc.reason}")
    except urllib.error.URLError as exc:
        fail(f"fetch failed: {exc.reason}")
    except UnicodeDecodeError as exc:
        fail(f"source file is not valid UTF-8: {exc}")


def extract_block(source: str) -> str:
    start_count = source.count(START_MARKER)
    end_count = source.count(END_MARKER)

    if start_count != 1:
        fail(f"expected exactly one start marker, found {start_count}")

    if end_count != 1:
        fail(f"expected exactly one end marker, found {end_count}")

    start_index = source.find(START_MARKER)
    end_index = source.find(END_MARKER)

    if end_index < start_index:
        fail("end marker appears before start marker")

    block_start = start_index + len(START_MARKER)
    block = source[block_start:end_index].strip()

    if not block:
        fail("extracted roadmap block is empty")

    return block + "\n"


def write_output(path: Path, content: str) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        fail(f"failed to write output file {path}: {exc}")


def main() -> int:
    source = fetch_source(SOURCE_URL)
    block = extract_block(source)
    write_output(OUTPUT_PATH, block)

    line_count = len(block.splitlines())

    print("Monolith roadmap sync complete")
    print(f"source: {SOURCE_URL}")
    print(f"output: {OUTPUT_PATH}")
    print(f"lines:  {line_count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
