# WumboLabs

WumboLabs is a static website for local language-model evaluations, technical reports, and methodology notes.

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

- **Evaluations** is the registry-backed model catalog and historical evidence surface.
- **Research** keeps long-form reports, benchmarks, experiments, fit tests, and investigations at `/records/`.
- **Methodology** is a temporary WELP holding page while the evaluation framework is revised.
- **Project URLs** under `/projects/` are unlisted compatibility pages. They are not primary navigation.

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

    python3 scripts/sync_labs.py

## Validation

    python3 scripts/check_site_content.py
    python3 scripts/sync_labs.py --check
    zola build
    python3 scripts/check_evaluations_site.py

## Brand assets

Furnace Plum color roles live in `static/css/style.css`. Status colors remain
independent from brand emphasis; evaluation classification text is authoritative.

`static/img/brand/` contains the three approved, unchanged PNG masters and their
locally cropped/resized derivatives. `mark.png` serves the compact header/footer;
`favicon-32.png`, `favicon-192.png`, and `apple-touch-icon.png` use the mark alone.
`og-card.png` is the 1200×630 horizontal-lockup social image. The stacked master
is retained without adding redundant page branding. Metadata lives in
`templates/base.html`; the canonical release value remains
`zola.toml` → `[extra].site_version`.

## Deployment

Deployments are handled automatically by Cloudflare Pages when changes are pushed to the main branch.

## Project Goals

- No npm dependency chain
- Markdown-first content
- Simple static deployment
- Low maintenance
- Project-centric structure
- Practical documentation over polish-first design
