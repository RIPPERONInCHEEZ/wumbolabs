# Site content ownership

Keep one authoritative public surface for each kind of fact.

| Surface | Owns | Source and maintenance rule |
|---|---|---|
| Project page | Unlisted compatibility record | `content/projects/*.md`; `public_project` must be false and `in_search` must be false. Direct URLs remain. Do not add these pages to navigation or the homepage. |
| Projects index | Compatibility notice only | `/projects/` explains that the directory is retired from navigation. It must not list project pages. |
| Evaluations | Model catalog and historical evidence | Pinned `WumboLabs/evaluations` registry → `data/labs-registry.json` → `scripts/sync_labs.py` → generated model pages. `latest_evidence_date` is derived as the maximum authoritative `event_date` for that model; never use presentation, Git, filesystem, or deployment timestamps. Never hand-maintain a second catalog or copy evidence facts into client JavaScript. Display a protocol snapshot only when the registry or export already records one. |
| Research | Long-form reports, experiments, fit tests, baselines, and technical findings | `content/records/*.md` at `/records/`. Navigation label is Research. Preserve historical context and routes. |
| Methodology | Current WELP framework and scientific boundaries | `content/methodology/_index.md`; link to the public specification and canonical results. Preserve earlier results under their original methodology; never reinterpret legacy scores as v1.0. |
| Homepage | Research orientation | `templates/index.html`; link to Evaluations, Research, and Methodology. Do not promote software projects. |

The homepage keeps normal global navigation and one prominent destination set;
its footer does not repeat those routes. The catalog exposes model, producer,
tested artifact/configuration, latest evidence and event links, not internal
classifications. Classification values remain in source records and attributed
model-event results, but are not catalog search metadata.

All model pages share the findings-first generator documented in
[the publication workflow](labs-publication-workflow.md). Presentation changes
must not edit source pins, frozen exports, narrative evidence, scores or event
identities.

## Required checks

Run `python3 scripts/sync_labs.py --check`, `python3 scripts/sync_labs.py selftest`, `zola build`, `python3 scripts/check_site_content.py`, `python3 scripts/check_evaluations_site.py`, and `node scripts/test_evaluations_catalog.js` before publishing content-architecture changes. The content checker protects the research-site contract and canonical surface boundaries; the evaluation sync and site checker protect the pinned evidence projection and all-model presentation, including objective results, negative findings, event anchors, provenance and media.
