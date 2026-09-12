# Labs Publication Workflow

How WumboLabs model evidence gets onto this website after a WELP campaign
closes. The website is a **derivative** of canonical public evidence — never a
second independent source of model facts. If a page ever conflicts with
campaign evidence, the campaign evidence governs and the page is
stale/defective.

## Identity contract (2026-09-12, model/profile/event architecture)

    one MODEL ID        = one canonical Evaluation page   (/evaluations/<model-id>/)
    one PROFILE ID      = one canonical public eval repository
    one EVENT ID        = one dated evidence event on the model page
    one profile may contain many events; one model may contain many profiles

Public presentation (2026-09-12 Evaluations consolidation): the primary
navigation is Projects / Evaluations / Methodology / About / Contact. There is
one public model-evaluation section — **Evaluations** — listing one entry per
tested model, with exactly one canonical page per model containing the current
state, tested profiles, results, chronological testing history (events with
anchors), and canonical evidence links. The underlying model/profile/event
evidence architecture is unchanged.

- `data/labs-registry.json` (v2) is EVENT-oriented: one entry per published
  evidence event, carrying `model_id`, `profile_id`, `event_id`, `event_type`,
  `event_date`, `record_date`, `profile_repo`, `profile_status`, and
  `evidence_scope`.
- `scripts/sync_labs.py` renders exactly ONE Evaluation page per model
  (`content/evaluations/<model-id>.md`), aggregating all of the model's profiles
  and events with the current state first. Per-surface currency follows
  `evidence_scope`: a later context-only event supersedes only the surfaces it
  declares (it can never silently replace classification, reliability, or
  capability evidence).
- A PROFILE ID maps to exactly one canonical public eval repository, and every
  canonical eval repository carries a `profile.json` descriptor (schema
  `wumbolabs-eval-profile/1`). A repository that mixed two materially distinct
  profiles (eval-qwen3.8-27b: historical llama.cpp vs ExLlamaV3 H1) was split
  into profile-specific canonical repositories; the original remains a
  preserved historical archive with a README notice. Profile-pure repositories
  keep their original names.
- Legacy route compatibility (generated deterministically by sync):
  `/labs/`, `/labs/atom.xml`, every `/labs/<model-id>/`, and `/records/`
  permanent-redirect (301) to their Evaluations destinations via
  `static/_redirects` (generated — do not edit by hand). Superseded
  event-style Labs URLs keep real HTML stub pages served at `/labs/<old-slug>/`
  (page path override) that meta-refresh to
  `/evaluations/<model-id>/#<event-id>`, because `_redirects` cannot target
  fragments. A machine-readable map of every old → new route is written to
  `data/generated/route-migration.json`. Hand-maintained technical records
  keep their direct `/records/<slug>/` URLs and are listed under
  Projects → Technical notes.
- Each canonical eval repository used to pin website exports stores the export
  at a pinned commit with a SHA-256 pin in the registry. Where evidence was
  migrated, `MIGRATION.md` in the new repository records per-file provenance
  (original repo/commit/path, SHA-256 equality); migrated exports are
  byte-identical, so existing pins resolve unchanged in their new home.

## Source-of-truth chain

    WELP campaign closes (local scientific evidence, canonical)
      -> public-safe publication export (summaries/website-publication.json)
      -> canonical public evidence reviewed + published (human Git gate)
      -> website publication registry entry (data/labs-registry.json)
      -> deterministic Labs sync (scripts/sync_labs.py)
      -> site build + validation
      -> human website Git gate
      -> deploy (Cloudflare Pages)

Key rule: a record whose canonical evidence is not yet published renders with
an explicit **Evidence publication pending** state and claims no canonical
evidence URL. The registry stores no machine-local absolute paths; local
exports are resolved through the `--local-exports` argument at sync time and
pinned by SHA-256.

## Public presentation: Evaluations

`/evaluations/` is the single public model catalog: one entry per tested model
(model name, classification, recommended profile, practical context, profile
and event counts, latest evidence date). Event chronology is not duplicated on
the catalog; it lives in each model page's **Testing history** section, where
every event keeps its stable anchor (`#<event-id>`), its canonical evidence
link, and — where one exists — a link to the long-form campaign report.

`/records/` is no longer a standalone public archive. Its index address
permanent-redirects to `/evaluations/`. The hand-maintained technical records
(`content/records/`) keep their direct `/records/<slug>/` URLs and are
discoverable through the **Technical notes** block on the Projects index; a
long-form report describing a model event (for example
`records/qwen38-27b-rtx5070-evaluation.md`) is additionally linked from that
event's section on the model's Evaluation page. No public Records/Labs
navigation label remains, and no old published route returns 404.

Archive position of technical records uses the original front-matter `date`,
descending. `weight`, `updated`, type, and status do not affect chronology.
Every record needs a trustworthy explicit date. Later substantive evidence
belongs in a new dated record rather than moving an older event.

When a technical report and an evaluation describe the **same evidence event**,
the report is linked from the event section on the model's Evaluation page
(registry `report_page` field). This is an explicit event relationship, not
model-name deduplication. All existing detail URLs remain available.

Type, lifecycle/status, hardware, and publication state are entry metadata,
not separate browsing sections. No public testing-status dashboard or research
queue is maintained.

## Publication dispositions (defined in canonical WELP)

Every full WELP campaign records exactly one disposition in
`summaries/website-publication.json`:

| Disposition | Meaning |
|---|---|
| `WEBSITE_READY` | Campaign closed with sufficient public-safe material to publish. |
| `WEBSITE_BLOCKED` | Intended for publication; blocked (missing evidence, unresolved concern). Reason required. |
| `NOT_FOR_PUBLICATION` | Intentionally excluded. Reason required. |
| `WEBSITE_PUBLISHED` | Public evidence + website record published and verified. |

Scientific classification (e.g. `READY_WITH_GUARDRAILS`) and publication state
are independent axes. The campaign validator (`R07`/`R08`, snapshot dates from
2026-09-12) makes the disposition mandatory for new campaigns.

## Standard update sequence (exact commands)

Work inside the website repository root unless noted. Staging, commits,
pushes, and deployment are always human actions.

1. **Close the WELP campaign.** Campaign completion produces
   `summaries/website-publication.json` (schema `wumbolabs-labs-publication/1`)
   with the disposition, the LocalMaxxing summary, and the canonical-evidence
   state (`PUBLISHED` + URL, or `PENDING_HUMAN_GATE` + proposed repo).
2. **Review the export** for public-safe content: no credentials, no local
   absolute paths, no raw prompt logs; negative results retained.
3. **Publish canonical public evidence (human gate).** Create/update the
   `WumboLabs/eval-*` repository (or push the prepared follow-up package) and
   commit the `website-publication.json` file there.
4. **Update the website registry** (`data/labs-registry.json`): switch the
   record's `source` to `kind: "github-raw"` with `repo`/`ref`/`path`,
   set `publication_state: "published"` and `canonical_evidence.state:
   "published"` with the URL — or, for a new local export, add its relative
   `source.file` + SHA-256 pin. Add the campaign to the campaign-side
   registry used by the gap checker.
5. **Run the Labs sync** (deterministic; fetches only from raw.githubusercontent.com):

       python scripts/sync_labs.py

   Omit `--local-exports` when every generated entry consumes `github-raw`
   sources. Sync renders one Evaluation page per model_id, legacy compatibility
   stubs and the generated `_redirects`, the generated datasets, and the route
   migration map, then exits nonzero on schema, hash, slug, identity, or
   evidence-relationship errors. A second run must change nothing (idempotence).

       python scripts/sync_labs.py --local-exports <exports-dir>   # first pass
       python scripts/sync_labs.py --local-exports <exports-dir>   # verify: 0 changed

   To verify without writing anything (used for review and stale-output
   checks), add `--check`:

       python scripts/sync_labs.py --local-exports <exports-dir> --check

   The sync tool also carries a selftest covering its reject paths
   (unpinned or mismatched export hash, escaping source path, missing
   record path, slug mismatch, pending export claiming a URL, missing
   model identity, unsupported schema):

       python scripts/sync_labs.py selftest

6. **Check the publication gap** (answers: is any publication-worthy closed
   campaign missing from the website registry?):

       python scripts/check_labs_publication_status.py --campaign-registry <campaign-registry.json>

7. **Build:**

       zola build

8. **Validate:** inspect generated routes under `public/evaluations/`, run
   `python scripts/check_evaluations_site.py` (route/navigation/legacy-link
   validation), confirm no localhost URLs, no local filesystem paths, no
   secrets in changed files, and run `git diff --check`. Review the complete
   diff.
9. **Human Git gate:** stage, review, and commit the changes; push.
10. **Deployment verification:** confirm the Cloudflare Pages deployment and
    that every published record resolves to live canonical evidence. Then set
    the campaign's disposition to `WEBSITE_PUBLISHED` in the export/registry
    lineage.

## Reference sync used to establish this workflow

The 2026-09-11 backfill (Qwen3.5-4B, Qwen3.5-9B, MiniCPM5-2B, Gemma 4 E4B,
Qwen3.8-27B H1 follow-up) was produced end-to-end through this exact chain,
with Gemma 4 E4B as the designated end-to-end proof. All five records were in
`evidence-pending-human-gate` state at creation; the human publication gates
listed above are the remaining steps.
