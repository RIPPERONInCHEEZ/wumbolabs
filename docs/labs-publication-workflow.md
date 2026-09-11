# Labs Publication Workflow

How WumboLabs Lab Records get onto this website after a WELP campaign closes.
The website is a **derivative** of canonical public evidence — never a second
independent source of model facts. If a page ever conflicts with campaign
evidence, the campaign evidence governs and the page is stale/defective.

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

       python scripts/sync_labs.py --local-exports <exports-dir>

   Omit `--local-exports` when every generated entry consumes `github-raw`
   sources. The command prints sources, records changed/unchanged/blocked,
   and output paths; it exits nonzero on schema, hash, slug, or evidence
   relationship errors. A second run must change nothing (idempotence).

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

8. **Validate:** inspect generated routes under `public/labs/`, confirm no
   localhost URLs, no local filesystem paths, no secrets in changed files,
   and run `git diff --check`. Review the complete diff.
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
