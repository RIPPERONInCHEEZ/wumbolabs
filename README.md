# WumboLabs

WumboLabs is a static website for documenting local AI, Linux, homelab, self-hosting, and infrastructure projects.

The site is built with Zola and deployed with Cloudflare Pages.

## Live Site

- https://wumbocore.com
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

## Deployment

Deployments are handled automatically by Cloudflare Pages when changes are pushed to the main branch.

## Project Goals

- No npm dependency chain
- Markdown-first content
- Simple static deployment
- Low maintenance
- Project-centric structure
- Practical documentation over polish-first design
