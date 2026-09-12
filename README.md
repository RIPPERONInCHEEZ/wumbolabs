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
generated from the publication registry by the deterministic sync pipeline. The
old `/labs/` and `/records/` addresses redirect to the Evaluations destinations.
Hand-maintained technical records keep their direct `/records/<slug>/` URLs and
are listed under Projects → Technical notes. See
[docs/labs-publication-workflow.md](docs/labs-publication-workflow.md).

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
