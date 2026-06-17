+++
title = "Building WumboLabs"
description = "Notes on building the WumboLabs website as a public lab record."
date = 2026-06-09
updated = 2026-06-17
[extra]
back_label = "Back to Lab Notes"
back_url = "/lab-notes/"
+++

WumboLabs started as a simple static site for documenting local AI, Linux, homelab, and self-hosting work.

The first version was intentionally conservative:

- Zola static site generator
- Markdown content
- plain CSS
- no npm dependency chain
- no CMS
- no database
- no unnecessary JavaScript

The goal was to build a site that is easy to maintain, easy to deploy, and simple enough to keep writing for.

This first version was not meant to be perfect. It was meant to exist.

## 2026-06-17 Update

The site has moved from a basic project index toward a public lab-console layout.

Recent changes focused on making the site easier to understand quickly:

- homepage simplified around a clear Start Here section
- redundant homepage project grid removed
- project pages compacted with collapsible supporting details
- Monolith quick-start information moved higher on its page
- LLMGauge reframed as the private/internal evaluation engine behind Monolith planning
- benchmark results split into separate dated records instead of overloading the baseline page
- typography shifted toward a restrained terminal/mono feel without making body copy hard to read

The current structure is:

- **Projects** — what exists
- **Benchmarks** — measured local test results
- **Lab Notes** — what changed, why it changed, and what was learned
- **About** — what WumboLabs is

## Current Rule

The site should stay small, readable, and evidence-based.

If a section does not help someone understand what to click, what changed, or what was learned, it probably does not belong on the homepage.
