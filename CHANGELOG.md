# Changelog

## v0.07 - Monolith Roadmap Sync

### Added
- Added website-side Monolith roadmap sync script.
- Added generated local roadmap content from Monolith's canonical `docs/ROADMAP.md`.
- Added Zola shortcode for rendering generated Markdown content.
- Added developer documentation for the manual Monolith roadmap sync workflow.

### Changed
- Updated the Monolith project page to render synced roadmap content instead of hardcoded roadmap text.
- Updated visible footer version to v0.07.

### Notes
- The website remains static and deterministic.
- The sync is manual for now via `python scripts/sync_monolith_roadmap.py`.
- The website only consumes the public marker block from Monolith's roadmap.
- There is no browser-side GitHub fetch, no GitHub Actions requirement, and no write access to the Monolith repo.

## v0.06 - Project Pages Pass

### Added
- Expanded LLMGauge project page with scan-first project structure.
- Expanded Wumbo Core project page as the home network and homelab infrastructure layer.
- Expanded WumboJetsII project page as the Linux workstation and local AI test rig.
- Added WumboJetsII to the homepage featured projects section.
- Added old project URL aliases for LLMGauge.

### Changed
- Added contextual back links for project, section, About, and Contact pages.
- Removed duplicate top-level content headings now handled by page templates.
- Renamed the public-facing Quant Lab project to LLMGauge.
- Updated active website references from Quant Lab and WumboGauge to LLMGauge.
- Updated Projects index to remove duplicate project card rendering.
- Updated project page descriptions for cleaner automatic project cards.
- Updated visible footer version to v0.06.

### Notes
- The local/internal quant-lab directory name remains unchanged outside the website.
- Old public URLs for Quant Lab and WumboGauge are preserved through page aliases.

## v0.05 - Monolith Project Page

### Added
- Expanded the Monolith project page into a scan-first public project overview.
- Added alpha v0.11.9 status and current project positioning.
- Added At a Glance status cards for release, status, audience, setup, local UI, and license.
- Added capability cards for model profiles, local eval workflows, context scaling, agent-backend testing, setup diagnostics, and workstation visibility.
- Added current roadmap summary for alpha v0.11.10 through alpha v0.11.13.
- Added collapsible Technical Details section for deeper project information.

### Changed
- Reworked the Monolith page to reduce long-scroll friction while preserving technical detail.
- Updated homepage Monolith card copy.
- Added reusable CSS for project info cards, feature cards, roadmap rows, and details panels.
- Clarified Monolith as a technical public alpha and source-available project, not open source.

### Notes
- Monolith currently has no open-source license selected.
- The page intentionally prioritizes fast scanning first, with deeper technical detail available on demand.

## v0.04 - Brand Identity Pass

### Added
- Added WumboLabs logo assets
- Added favicon
- Added branded Open Graph image
- Added header logo mark
- Added footer logo mark
- Updated homepage tagline to "Real hardware. Real testing. No hype."

### Changed
- Updated CSS palette to locked WumboLabs brand colors
- Tuned links, cards, buttons, footer, and contact cards around restrained lime accents
- Updated visible footer version to v0.04

### Notes
This release applies the locked WumboLabs Monochrome Lime identity to the public site.

## v0.03 - Public Launch Polish

### Added
- Updated About page with clearer WumboLabs origin story
- Updated Contact page with public email, X/Twitter, and GitHub cards
- Updated footer navigation
- Bumped visible site version to v0.03

### Infrastructure
- Verified Cloudflare Email Routing for contact@wumbocore.com
- Confirmed contact@wumbocore.com forwards to Proton Mail
- Kept Cloudflare Pages deployment flow unchanged

### Notes
This release polishes the public launch version of WumboLabs after confirming the site, custom domain, GitHub repository, and email routing are working.

## v0.02 - Contact and Footer

### Added
- Contact page
- contact@wumbocore.com email routing
- X/Twitter contact link
- Footer versioning

## v0.01 - Initial Baseline

### Added
- Zola static site foundation
- GitHub repository
- Cloudflare Pages deployment
- Custom domain setup
- Initial homepage, project pages, lab notes, benchmarks, and about page
