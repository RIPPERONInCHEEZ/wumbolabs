# Evaluation publication workflow

The website is a derivative of accepted public scientific evidence, never a second
source of model facts. The canonical operating contract lives in
[WELP publication documentation](https://github.com/WumboLabs/welp/blob/main/docs/publication.md).

## Four layers and scientific identity

- **Website** `https://wumbolabs.dev/evaluations/`: human discovery and ordinary sharing.
- **WumboLabs/evaluations**: canonical public registry, reports, profile metadata,
  public-safe supporting artifacts, and exact scientific citations.
- **Local `research/model-evaluations/`**: working/raw science and authoritative
  campaign evidence. Resolve conflicts there and publish attributed corrections.
- **NAS model archive**: large model artifacts, not website or Git content.

One `model_id` identifies one Evaluation page; `profile_id` identifies a materially
distinct tested artifact/runtime/deployment surface; `event_id` identifies an
immutable dated event. A profile is **not** a repository boundary. Never create an
`eval-*` repository. Multiple profiles and events live in WumboLabs/evaluations.
Shared comparisons are stored once under `shared-events/<shared_event_id>/`, with
related model/profile IDs and no fabricated scientific owner. Website display
attribution preserves existing model-page placement and per-surface precedence.

## One registry; deterministic derivatives

The central `registry.json` is authoritative for publication topology and identity.
`data/evaluations-source.json` pins its repository, **full 40-character commit SHA**,
relative path, and SHA-256. Each event's report and source have independent immutable
commit/path pins; structured and narrative sources additionally pin SHA-256.

`scripts/evaluations_source.py` fetches that exact registry and verifies every source
hash before materializing:

- `data/labs-registry.json` v3 — generated; never hand-edit.
- `data/generated/evaluations-exports/*.json` — byte-identical frozen source exports.
- `data/labs-events/*.md` — narrative derivatives with migrated evidence links.

`scripts/sync_labs.py` consumes those derivatives, renders one page per model, and
writes the model/event/freshness datasets, compatibility stubs, `_redirects`, and
route map. There are no browser fetches or runtime dependencies: committed static
artifacts are built by Zola. A second sync must change zero files; `--check` writes
nothing and exits nonzero if either the central projection or rendered outputs are stale.

Historical exports retain optional identity, legacy `profile_repo`, and original
canonical URLs unchanged. Only the in-memory rendered derivative overlays the new
central citation. Legacy v2/local-export and GitHub-raw consumers remain supported
for frozen fixtures; they are not the current publication path. GitHub-raw sources
must match their hash pins too. Never hand-edit cached exports to resolve a conflict.

Current findings follow each event's `evidence_scope`, not merely the latest date.
A context-only event must not replace classification, reliability, or capabilities.
Human model pages show current findings, tested profiles, testing history, exact
**Canonical Evidence / Full Report** links, profile metadata, and clearly labelled
legacy provenance. No independent public research backlog is generated.

## Update sequence

1. Complete the authorized WELP campaign and its publication disposition. Preserve
   measured values, limitations, dates, source attribution, and negative results.
2. Follow the WELP contract to publish public-safe event files and update the existing
   central registry/indexes. Use the event-file commit in registry citations; then
   push the registry commit under explicit human authorization. Never fabricate a
   future commit or publish pending evidence as if it exists.
3. Set `data/evaluations-source.json` to the pushed central registry commit and hash.
   Add the campaign to the local campaign-side publication-gap registry if applicable.
4. Run from this website repository:

   ```sh
   python3 scripts/check_site_content.py
   python3 scripts/sync_labs.py
   python3 scripts/sync_labs.py
   python3 scripts/sync_labs.py --check
   python3 scripts/sync_labs.py selftest
   python3 scripts/check_labs_publication_status.py --campaign-registry CAMPAIGN_REGISTRY
   zola build
   python3 scripts/check_evaluations_site.py
   ```

5. Review scoped working and staged diffs, public safety, exact report/profile links,
   model scientific state, and every compatibility route. Git push and deployment
   require explicit human authorization; a local export does not authorize them.
6. Push the accepted website main commit for Cloudflare Pages deployment, then verify
   the **actual live** homepage, Evaluation index, model pages, report/profile links,
   and old routes. Mark `WEBSITE_PUBLISHED` only after verification.
7. Close local publication bookkeeping without changing scientific priorities.
   Legacy repositories may be archived only after replacement publication and live
   verification; retain README migration notices, original histories, and old URLs.

## Compatibility routes and chronology

`/evaluations/` is the only public model catalog. `/labs/`, `/labs/atom.xml`, and
old model URLs permanently redirect through generated `static/_redirects`. Old
event-style Labs URLs retain HTML meta-refresh stubs to model-page event anchors
because Cloudflare redirect rules cannot target fragments. The exact map is
`data/generated/route-migration.json`.

`/records/` is the Lab Records index. Hand-maintained technical records retain their
`/records/<slug>/` URLs, preserving original front-matter dates and `record_date`
chronology. A model-specific long-form report remains linked from the corresponding
model event via `report_page`; historical baselines remain Lab Records rather than
current methodology.

## Sharing

Share the website model URL for ordinary discussion, central model/profile indexes
for navigation, and `https://github.com/WumboLabs/evaluations/blob/FULL_SHA/PATH` for
an exact scientific claim. Branch links are discovery, not immutable citations.
Legacy links are historical provenance, never future publication targets.
