# Monolith Roadmap Sync

The WumboLabs website renders a public Monolith roadmap section from Monolith's canonical roadmap.

## Source of Truth

The canonical source is:

    WumboLabs/monolith
    docs/ROADMAP.md

The website fetches the raw file from:

    https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/ROADMAP.md

## Public Marker Block

The website only consumes the Markdown between these exact markers:

    <!-- website-roadmap:start -->
    <!-- website-roadmap:end -->

The Monolith roadmap must contain exactly one start marker and exactly one end marker.

The sync script fails if:

- the start marker is missing
- the end marker is missing
- either marker is duplicated
- the end marker appears before the start marker
- the extracted block is empty
- the fetch fails
- the output file cannot be written

## Manual Sync Command

From the website repo root:

    python scripts/sync_monolith_roadmap.py

The script writes the extracted roadmap block to:

    data/generated/monolith-roadmap.md

The website renders that local generated file. It does not fetch GitHub from the browser.

## Current Policy

This is intentionally manual for now.

There is no browser-side GitHub fetch, no write access to the Monolith repo, no GitHub Actions requirement, and no automatic deployment behavior.

Automation may be added later from the website repo after the manual sync flow is proven stable.
