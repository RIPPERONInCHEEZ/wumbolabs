# Monolith Website Sync

The WumboLabs website renders selected public Monolith project information from the Monolith repository.

## Source of Truth

The canonical source repository is:

    WumboLabs/monolith

The website currently consumes:

    docs/website/public_status.json
    docs/ROADMAP.md

Raw source URLs:

    https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/website/public_status.json
    https://raw.githubusercontent.com/WumboLabs/monolith/main/docs/ROADMAP.md

## Generated Website Files

The sync script writes:

    data/generated/monolith-status.json
    data/generated/monolith-roadmap.md

The website renders those local generated files. It does not fetch GitHub from the browser.

## Public Roadmap Marker Block

The website only consumes roadmap Markdown between these exact markers:

    <!-- website-roadmap:start -->
    <!-- website-roadmap:end -->

The Monolith roadmap must contain exactly one start marker and exactly one end marker.

The sync script fails if:

- the start marker is missing
- the end marker is missing
- either marker is duplicated
- the end marker appears before the start marker
- the extracted block is empty
- the roadmap fetch fails

## Public Status Metadata

The website also consumes:

    docs/website/public_status.json

Required keys:

    project
    status
    current_release
    repository_url
    license_status
    canonical_local_url
    canonical_start_command
    summary
    audience
    positioning
    capabilities
    caveats
    current_focus

The sync script validates that required keys exist and that expected list fields are non-empty lists.

## Manual Sync Command

From the website repo root:

    python scripts/sync_monolith.py

Legacy compatibility command:

    python scripts/sync_monolith_roadmap.py

The legacy command currently runs the broader Monolith sync.

## Current Policy

This is intentionally manual for now.

There is no browser-side GitHub fetch, no write access to the Monolith repo, no GitHub Actions requirement, and no automatic deployment behavior.

Automation may be added later from the website repo after the manual sync flow is proven stable.
