#!/usr/bin/env python3
"""check_labs_publication_status.py — WumboLabs Labs publication-gap checker.

Answers one question: are there closed/publication-worthy WELP campaigns that
are not represented in the website publication registry, and which records are
blocked on pending public evidence?

The comparison is deliberately EXPLICIT: it consumes a campaign-side registry
file (campaigns list with website_disposition fields) rather than guessing
from directory scans. The website-side side is data/labs-registry.json.

Usage (from the website repository root):
    python scripts/check_labs_publication_status.py \
        --campaign-registry <path-to-campaign-registry.json>

Exit codes: 0 no publication gap; 1 gap or structural problem; 2 usage error.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REGISTRY_PATH = Path("data/labs-registry.json")
TRACKED_DISPOSITIONS = {"WEBSITE_READY", "WEBSITE_PUBLISHED"}


def load_json(path: Path) -> dict:
    if not path.is_file():
        fail(f"file not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is invalid JSON: {exc}")


def fail(message: str) -> "NoReturn":  # type: ignore[valid-type]
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Labs publication-gap checker")
    parser.add_argument("--campaign-registry", type=Path, required=True,
                        help="explicit campaign registry JSON with a campaigns[] list")
    args = parser.parse_args()

    website = load_json(Path("data") / "labs-registry.json")
    campaigns = load_json(args.campaign_registry)
    entries = website.get("records")
    if not isinstance(entries, list):
        fail("data/labs-registry.json must contain a records list")
    campaign_list = campaigns.get("campaigns")
    if not isinstance(campaign_list, list):
        fail("campaign registry must contain a campaigns list")

    by_slug = {}
    for entry in entries:
        slug = entry.get("slug")
        if slug in by_slug:
            fail(f"duplicate registry slug: {slug!r}")
        by_slug[slug] = entry

    missing = []
    matched = []
    for campaign in campaign_list:
        slug = campaign.get("website_record_slug")
        disposition = campaign.get("website_disposition")
        if disposition in TRACKED_DISPOSITIONS and slug not in by_slug:
            missing.append({"model": campaign.get("model"), "campaign": campaign.get("campaign"),
                            "website_record_slug": slug})
        elif slug:
            matched.append(slug)

    stale = [
        {"slug": e.get("slug"), "note": "registry entry with no matching campaign-registry entry"}
        for e in entries if e.get("authoring") == "generated" and e.get("slug") not in matched
    ]
    pending_evidence = [
        {"slug": e.get("slug"), "model": e.get("model"),
         "publication_state": e.get("publication_state"),
         "proposed_repo": (e.get("canonical_evidence") or {}).get("proposed_repo")}
        for e in entries if e.get("publication_state") != "published"
    ]

    print(json.dumps({
        "status": "GAP" if missing else "OK",
        "campaigns_tracked": len(campaign_list),
        "missing_from_website_registry": missing,
        "records_pending_public_evidence": pending_evidence,
        "generated_records_without_campaign_entry": stale,
        "notes": "A GAP status means a publication-worthy closed campaign is not represented in the website registry. evidence-pending states are visible, not hidden.",
    }, indent=2))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
