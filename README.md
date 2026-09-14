# WumboLabs

WumboLabs is a static website for documenting local AI, Linux, homelab, self-hosting, and infrastructure projects.

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

## Updating Evaluations

Each tested model has exactly one canonical Evaluation page under `/evaluations/`,
generated from an immutable `WumboLabs/evaluations` registry pin by deterministic sync. The
old `/labs/` and `/records/` addresses redirect to the Evaluations destinations.
Hand-maintained technical records keep their direct `/records/<slug>/` URLs and
are listed under Projects → Technical notes. See
[docs/labs-publication-workflow.md](docs/labs-publication-workflow.md).

`data/evaluations-source.json` is the website's source pin. The local registry,
cached exports, model pages, and indexes are generated derivatives, not separate
publication authorities. Never create an `eval-*` repository or hand-edit generated
registry entries. Public citations use central repository + full commit SHA + path.

Canonical sync command:

    python scripts/sync_labs.py

## Deployment

Deployments are handled automatically by Cloudflare Pages when changes are pushed to the main branch.

## Project Goals

- No npm dependency chain
- Markdown-first content
- Simple static deployment
- Low maintenance
- Project-centric structure
- Practical documentation over polish-first design
