# Site content ownership

Keep one authoritative public surface for each kind of fact.

| Surface | Owns | Source and maintenance rule |
|---|---|---|
| Project page | Public project facts | `content/projects/*.md`; add `public_project = true` only for a public WumboLabs project. The Projects index derives its listing from this flag. Infrastructure may keep a compatibility page with `public_project = false`; it is never a directory project. |
| Projects | Public project directory | `templates/section.html` renders only `public_project = true`. Do not list infrastructure, internal work, or technical records here. |
| Evaluations | Model catalog and current evidence state | Pinned `WumboLabs/evaluations` registry → `data/labs-registry.json` → `scripts/sync_labs.py` → generated model pages. Never hand-maintain a second catalog or copy evidence facts into client JavaScript. |
| Reports | Long-form reports, experiments, fit tests, baselines, and technical findings | `content/records/*.md`; preserve historical context and routes. Link model-specific reports from their canonical Evaluation page. |
| Methodology | WELP, review/scoring rules, claim boundaries, and publication process | `content/methodology/_index.md` and the canonical WELP publication documentation. Do not restate it as current process elsewhere. |
| Homepage | Concise orientation | `templates/index.html`; link to canonical surfaces and avoid detailed status copies. |

## Required checks

Run `python3 scripts/check_site_content.py`, `python3 scripts/sync_labs.py --check`, `zola build`, and `python3 scripts/check_evaluations_site.py` before publishing content-architecture changes. The content checker protects the public-project contract and canonical surface boundaries; the evaluation sync and site checker protect the pinned evidence projection.
