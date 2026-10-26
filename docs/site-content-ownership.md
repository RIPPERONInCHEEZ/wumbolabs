# Site content ownership

Keep one authoritative public surface for each kind of fact.

| Surface | Owns | Source and maintenance rule |
|---|---|---|
| Project page | Unlisted compatibility record | `content/projects/*.md`; `public_project` must be false and `in_search` must be false. Direct URLs remain. Do not add these pages to navigation or the homepage. |
| Projects index | Compatibility notice only | `/projects/` explains that the directory is retired from navigation. It must not list project pages. |
| Evaluations | Model catalog and historical evidence | Pinned `WumboLabs/evaluations` registry → `data/labs-registry.json` → `scripts/sync_labs.py` → generated model pages. `latest_evidence_date` is derived as the maximum authoritative `event_date` for that model; never use presentation, Git, filesystem, or deployment timestamps. Never hand-maintain a second catalog or copy evidence facts into client JavaScript. Display a protocol snapshot only when the registry or export already records one. |
| Research | Long-form reports, experiments, fit tests, baselines, and technical findings | `content/records/*.md` at `/records/`. Navigation label is Research. Preserve historical context and routes. |
| Methodology | Temporary WELP holding page | `content/methodology/_index.md`. Do not present the previous detailed protocol as the current authoritative method. Do not restate internal development status elsewhere. |
| Homepage | Research orientation | `templates/index.html`; link to Evaluations, Research, and Methodology. Do not promote software projects. |

## Required checks

Run `python3 scripts/check_site_content.py`, `python3 scripts/sync_labs.py --check`, `zola build`, and `python3 scripts/check_evaluations_site.py` before publishing content-architecture changes. The content checker protects the research-site contract and canonical surface boundaries; the evaluation sync and site checker protect the pinned evidence projection.
