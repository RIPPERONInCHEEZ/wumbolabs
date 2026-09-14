# WumboLabs

WumboLabs is a static website for public projects, model-evaluation evidence, long-form technical reports, and methodology on local AI and Linux systems.

The site is built with Zola and deployed with Cloudflare Pages.

## Live Site

- https://wumbolabs.dev
- https://wumbolabs.pages.dev

## Stack

- Zola
- Markdown
- Plain CSS
- GitHub
- Cloudflare Pages

## Local Development

Start the local development server:

    zola serve

Or on WumboJetsII, use the local alias:

    weblab

Then open:

    http://127.0.0.1:1111

## Build

    zola build

The static site is generated into:

    public/

## Content ownership

- **Projects** lists only public WumboLabs projects and derives from explicit project metadata.
- **Evaluations** is the registry-backed model catalog and current evidence surface.
- **Reports** keeps long-form reports, benchmarks, experiments, fit tests, and historical baselines.
- **Methodology** is the canonical public explanation of WELP, review rules, claim boundaries, and publication process.

See [docs/site-content-ownership.md](docs/site-content-ownership.md) for the operational contract.

## Updating Evaluations

Each tested model has exactly one canonical Evaluation page under `/evaluations/`,
generated from an immutable `WumboLabs/evaluations` registry pin by deterministic sync.
Reports retain direct `/records/<slug>/` URLs for long-form evidence. See
[docs/labs-publication-workflow.md](docs/labs-publication-workflow.md).

`data/evaluations-source.json` is the website's source pin. The local registry,
cached exports, model pages, and indexes are generated derivatives, not separate
publication authorities. Never create an `eval-*` repository or hand-edit generated
registry entries. Public citations use central repository + full commit SHA + path.

Canonical sync command:

    python scripts/sync_labs.py

## Validation

    python3 scripts/check_site_content.py
    python3 scripts/sync_labs.py --check
    zola build
    python3 scripts/check_evaluations_site.py

## Deployment

Deployments are handled automatically by Cloudflare Pages when changes are pushed to the main branch.

## Project Goals

- No npm dependency chain
- Markdown-first content
- Simple static deployment
- Low maintenance
- Project-centric structure
- Practical documentation over polish-first design
