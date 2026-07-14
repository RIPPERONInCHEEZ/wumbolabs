# Lab Records migration plan

Status: canonical architecture and content contract. This document defines the migration; it does not implement it.

## Decision

WumboLabs will consolidate the current `/lab-notes/` and `/benchmarks/` sections into one section at `/records/`.

- Canonical section name: **Lab Records**
- Primary navigation label: **Records**
- Section source: `content/records/_index.md`
- Public section URL: `/records/`
- Sort order: publication date, newest first, preserving every existing `date`
- Architecture: static Zola content rendered by the existing record templates

“Lab Records” is the public evidence archive for dated reports, baselines, fit tests, and working notes. Projects continue to explain what exists; Lab Records document what was tested, observed, changed, or learned. LLMGauge remains the flagship project and the local-first evidence tool behind applicable model-testing records. The section is not a leaderboard, automatic judge, or universal model-ranking system.

The shorter navigation label keeps the accepted operator-console header compact. Page headings, back links, homepage copy, footer copy, and prose use the canonical name “Lab Records.”

## Scope and content contract

The migration changes information architecture, not the evidence standard or visual direction.

Each migrated record must:

- retain its original publication date and any existing `updated` date;
- retain the existing evidence, measurements, runtime settings, limitations, and claim boundaries;
- keep hardware-, runtime-, model-, quantization-, context-, suite-, and scoring-specific language where present;
- describe manual scores as manual review metadata or judgments, not objective proof;
- remain readable as a long-form document without client-side filtering or search;
- render through the existing operator-console record design in `templates/section.html`, `templates/page.html`, and `static/css/style.css`;
- use `/records/` as its back-link destination with the label “Back to Lab Records”; and
- add one restrained record type in front matter as `[extra] record_type`.

The section index should introduce Lab Records as dated, bounded evidence and working history. It should explain the four current types without promising future content lanes.

## Record type vocabulary

Use exactly these initial display values:

| Type | Current justification | Definition |
|---|---|---|
| `REPORT` | The scored Gemma practical-use comparison | A bounded interpretation of a completed test with measured evidence, manual review context, and conclusions. |
| `BASELINE` | The local LLM baseline | A reference record defining the test bench, evaluation expectations, or comparison starting point. |
| `FIT TEST` | The Mellum2 agent-backend test | A test focused on whether specified models, contexts, or runtime paths fit and complete on named hardware; it is not a quality verdict. |
| `LAB NOTE` | The WumboLabs build note | A dated record of changes, decisions, breakage, repairs, or lessons that is not primarily a measured test result. |

Store the value in each page’s existing `[extra]` table, for example:

```toml
[extra]
record_type = "FIT TEST"
back_label = "Back to Lab Records"
back_url = "/records/"
```

This is display metadata, not a new Zola taxonomy. Do not add categories, tags, filters, or speculative types during the migration. `REPORT` does not create a separate `/reports/` section.

## Current inventory and disposition

The two section indexes are containers, not records. They are replaced by `content/records/_index.md` and both old section URLs redirect to `/records/`.

Every current Lab Note and Benchmark page is accounted for below.

| Current source | Current public URL | Date | Final type | Relationship and disposition | Final source | Final public URL |
|---|---|---:|---|---|---|---|
| `content/lab-notes/wumbolabs-first-build.md` | `/lab-notes/wumbolabs-first-build/` | 2026-06-09 | `LAB NOTE` | Independent. Move without dropping its build history or `updated = 2026-06-17`. Update only stale section/back-link wording required by the new information architecture. | `content/records/wumbolabs-first-build.md` | `/records/wumbolabs-first-build/` |
| `content/benchmarks/local-llm-baseline.md` | `/benchmarks/local-llm-baseline/` | 2026-06-09 | `BASELINE` | Independent. Preserve the WumboJetsII test bench, practical-use criteria, tracking checklist, and anti-leaderboard boundary. | `content/records/local-llm-baseline.md` | `/records/local-llm-baseline/` |
| `content/benchmarks/mellum2-agent-backend-test.md` | `/benchmarks/mellum2-agent-backend-test/` | 2026-06-17 | `FIT TEST` | Independent. Preserve both variants, context ladder, 64k measurements, fit-only limitation, and manual-review requirements. | `content/records/mellum2-agent-backend-test.md` | `/records/mellum2-agent-backend-test/` |
| `content/lab-notes/2026-06-21-gemma-12b-practical-use.md` | `/lab-notes/gemma-12b-practical-use/` | 2026-06-21 | `REPORT` | Companion summary of the benchmark below. Merge into one canonical record; do not retain as an independent page. | `content/records/gemma-12b-practical-use.md` | `/records/gemma-12b-practical-use/` |
| `content/benchmarks/gemma-12b-practical-use-v1.md` | `/benchmarks/gemma-12b-practical-use-v1/` | 2026-06-21 | `REPORT` | Detailed evidence page for the same test as the Lab Note above. Use as the structural base of the canonical merged record. | `content/records/gemma-12b-practical-use.md` | `/records/gemma-12b-practical-use/` |

The final section contains four records: one report, one baseline, one fit test, and one lab note.

## Gemma practical-use merge

The Gemma pages are not byte-for-byte duplicates, but they are not complementary independent records either. They have the same title and publication date, describe the same three models, LLMGauge v0.24 run, Practical Use Suite, RTX 5070 12GB hardware, result, and limitations. The Lab Note is a short editorial companion that points readers to the detailed Benchmark. Keeping both in one unified index would create two identities for one evidence event.

Use `content/benchmarks/gemma-12b-practical-use-v1.md` as the structural base and publish the merged record at:

- source: `content/records/gemma-12b-practical-use.md`
- URL: `/records/gemma-12b-practical-use/`
- type: `REPORT`
- date: `2026-06-21`

The merged record must preserve:

1. all three exact model/quantization identities;
2. WumboJetsII and RTX 5070 12GB hardware scope;
3. LLMGauge v0.24, `wumbolabs-practical-use-v1`, llama.cpp, context, generation settings, and completion status;
4. per-model manual scores, speed, VRAM, and headroom values;
5. per-prompt score detail and the statement that scores are manual local-context judgments, not universal rankings;
6. the practical-use-test boundary and the six tested task areas;
7. the finding that Gemma 4 12B IT QAT UD-Q4_K_XL had the strongest balance in this specific comparison;
8. the finding that the heavier UD-Q5 did not justify its added hardware cost in this run;
9. the Gemmable MTP model’s action-oriented or incomplete-answer failure mode, its successful fit/run, and the need for further prompt-template or MTP runtime investigation; and
10. the concise Lab Note rationale that quantization weight alone did not determine practical value.

Consolidate repeated prose rather than stacking the Lab Note above the Benchmark verbatim. No score, setting, limitation, or claim boundary may be lost. Both old Gemma URLs must permanently redirect to the canonical merged URL.

## Required presentation and link updates

### Section and page templates

Keep the current record-list and long-form page structure. Extend the existing templates only enough to expose the new metadata:

- `templates/section.html`: show `page.extra.record_type` alongside each record date; retain title, description, date sorting, and `open →` behavior.
- `templates/page.html`: show `page.extra.record_type` near the publication date; retain the current readable content width, tables, details blocks, and record-console framing.
- `static/css/style.css`: reuse `.record-row-kicker`, `.page-record-date`, and the accepted operator-console styles. Add no new layout system; change CSS only if a minimal spacing rule is required after real browser validation.

### Primary navigation

In `templates/base.html`, replace the separate “Lab Notes” and “Benchmarks” entries with one **Records** link to `/records/`. Its active-state condition must cover `/records/` and every descendant record URL. Keep Projects first and About/Contact after Records.

### Homepage

In `templates/index.html`:

- keep the three-target operator evidence layout and LLMGauge as target 01;
- change target 02 from “Lab notes and benchmarks” to “Lab Records”;
- describe reports, baselines, fit tests, and lab notes as bounded records from local testing and lab work;
- replace the separate Lab Notes and Benchmarks links with one “Lab Records” link to `/records/` while retaining the Projects link;
- change the `FIELD NOTES` side panel to a Lab Records/index treatment, with copy covering all four record types rather than only notes; and
- change “Open lab notes →” to “Open Lab Records →” linking to `/records/`.

The recent-activity log and its claims do not need restructuring. The working-rule lines “benchmarks need context” and “notes beat memory” are principles rather than navigation labels and may remain.

### Footer

In `templates/base.html`:

- replace the Lab Notes footer link with **Lab Records** linking to `/records/`; and
- change “Notes, benchmarks, and project pages…” to “Lab records and project pages…” without changing the conservative disclaimer.

### Record-local and prose references

- Set every migrated page’s back link to `/records/` with “Back to Lab Records.”
- Remove the Gemma Lab Note’s cross-link as part of the merge.
- In `wumbolabs-first-build.md`, replace the obsolete separate Benchmarks/Lab Notes structure bullets with one Lab Records bullet. Preserve the rest of the article and its dates.
- Do not rewrite generic uses of “benchmark,” “note,” or “report” when they describe a test or document type rather than an old section.
- `docs/site-backlog.md` contains the superseded Benchmarks-versus-Reports proposal. Do not silently treat it as the migration contract: during implementation, add a concise note that this plan supersedes that information-architecture proposal, without expanding the implementation into a backlog rewrite.

Current source links that require migration are:

| Source | Current reference | Required result |
|---|---|---|
| `templates/base.html` | two primary-nav links and one Lab Notes footer link | one `/records/` navigation link and one `/records/` footer link |
| `templates/index.html` | two target-02 links and one field-notes link | `/records/` links using Lab Records wording |
| `content/benchmarks/*.md` | three `back_url = "/benchmarks/"` values | `/records/` |
| `content/lab-notes/wumbolabs-first-build.md` | `back_url = "/lab-notes/"` | `/records/` |
| `content/lab-notes/2026-06-21-gemma-12b-practical-use.md` | link to the Gemma Benchmark | removed by the documented merge |

Untracked historical files under `temp/` are review artifacts, not public site links, and must not be edited merely to erase historical URLs.

## Old URL treatment and redirect feasibility

All published old section and record URLs receive permanent HTTP redirects. Use explicit mappings rather than broad wildcards so an unknown old URL does not acquire a misleading destination.

| Old URL | Permanent destination |
|---|---|
| `/lab-notes/` | `/records/` |
| `/benchmarks/` | `/records/` |
| `/lab-notes/wumbolabs-first-build/` | `/records/wumbolabs-first-build/` |
| `/benchmarks/local-llm-baseline/` | `/records/local-llm-baseline/` |
| `/benchmarks/mellum2-agent-backend-test/` | `/records/mellum2-agent-backend-test/` |
| `/lab-notes/gemma-12b-practical-use/` | `/records/gemma-12b-practical-use/` |
| `/benchmarks/gemma-12b-practical-use-v1/` | `/records/gemma-12b-practical-use/` |

Redirects are feasible in the current deployment without JavaScript, a framework, or a dependency. The repository builds static files with Zola and deploys them to Cloudflare Pages. Cloudflare Pages supports a root `_redirects` file, and Zola copies files from `static/` to the generated root. The implementation milestone should therefore add `static/_redirects` with the seven explicit `301` rules above.

There is no redirect configuration in the current repository, so this is a new deployment artifact. `zola build` can confirm that `public/_redirects` is emitted, but it cannot prove Cloudflare’s live HTTP behavior. After deployment, verify every old URL returns a permanent redirect with the exact expected `Location`; do not replace redirects with client-side JavaScript or an HTML-only fallback.

## Migration acceptance criteria

The implementation is accepted only when all of the following are true:

1. `/records/` is the only current public section index for Lab Records and contains exactly the four planned records, sorted by preserved publication date.
2. The canonical name is “Lab Records”; the primary navigation label is “Records.”
3. Every row and record page exposes exactly one justified type from the four-value vocabulary.
4. The three independent records retain their substantive content, dates, evidence boundaries, and limitations.
5. The Gemma material is one canonical report containing every item in the merge-preservation list; neither old page remains as a second record.
6. LLMGauge remains the homepage flagship and is described as the local-first evidence tool, not a leaderboard or automatic judge.
7. The primary navigation, homepage target 02, homepage side panel, footer, back links, and stale structure prose all point to or describe Lab Records consistently.
8. The existing operator-console styling and readable long-form layout remain intact at desktop and mobile widths; tables, details blocks, headings, focus states, and links remain usable.
9. `static/_redirects` contains the seven explicit permanent mappings, `zola build` copies it to `public/_redirects`, and no old source section continues to generate conflicting HTML.
10. A repository-wide search finds no live content/template link to `/lab-notes/` or `/benchmarks/`; expected occurrences are limited to redirect sources, historical documentation, this plan, and untracked review artifacts.
11. `zola build` and `git diff --check` pass, and localhost browser validation covers `/`, `/records/`, all four record pages, and representative old URL behavior where the local server supports it.
12. The complete tracked diff contains no generated `public/` output, dependency, JavaScript filter/search, unrelated article rewrite, or unrelated design change.

## Out of scope for this planning milestone

This document does not:

- move, delete, merge, or rewrite content files;
- create `content/records/`;
- modify templates, CSS, navigation, homepage, footer, or internal links;
- implement or test redirects;
- add JavaScript filters, search, taxonomies, frameworks, dependencies, build steps, analytics, or dynamic fetches;
- add new records or publish unpublished model results;
- revise the wider report methodology or create a separate Reports section; or
- stage, commit, merge, push, tag, release, or delete branches.

## Exact next implementation milestone

Implement **Lab Records static migration** as one bounded milestone:

1. Create `content/records/_index.md` with the canonical title, bounded introduction, date sorting, and existing `section.html`/`page.html` templates.
2. Move the three independent records to the exact final paths in the inventory, preserving their bodies and dates; add `extra.record_type` and Lab Records back-link metadata.
3. Merge the two Gemma pages into the one exact destination using the detailed Benchmark as the base and the preservation checklist as the content contract; remove both old source pages after the merge.
4. Remove the old Lab Notes and Benchmarks indexes after all record content is accounted for.
5. Update `templates/section.html` and `templates/page.html` to display record types with existing presentation primitives.
6. Apply only the navigation, homepage, footer, back-link, internal-link, stale structure prose, and backlog-status updates enumerated in this plan.
7. Add `static/_redirects` with exactly the seven permanent mappings.
8. Run `zola build`, confirm `public/_redirects`, run `git diff --check`, repeat the repository-wide legacy-URL search, inspect the complete tracked diff, and perform desktop/mobile localhost browser validation of the changed routes.
9. Leave all changes unstaged and uncommitted for human review and write the milestone review report under `temp/` as the final file-writing action.

Do not combine that milestone with new report content, methodology expansion, a separate `/reports/` route, visual redesign, filtering, search, or dependency work.
