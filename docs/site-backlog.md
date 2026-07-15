# WumboLabs Website Backlog

Small follow-up items for the public WumboLabs / WumboCore website.

## Translation / language accessibility

Status: planned, not urgent.

Add a small English-only/browser-translation note to the footer or About page in a future patch.

Recommended first version:

    This site is written in English. Browser translation should work for most pages.

Do not build a full multilingual language switcher yet.

Revisit proper multilingual/i18n support only if the site gets meaningful non-English readership or if major pages become stable enough to maintain translated versions.

## Website roadmap — July 4, 2026

Current direction: WumboLabs should become publicly legible as a practical local AI testing source.

The site should support the core thesis:

    Real Hardware. Real Testing. No Hype.

LLMGauge is the flagship public wedge. The website is the public proof layer. Monolith remains important, but it is secondary for now as the later interface, operator, and import layer.

### 1. Finish LLMGauge v0.42 / v0.65 site framing

Status: done (superseded by v0.65).

The LLMGauge project page and homepage activity/status were moved off the old v0.20-era framing through a v0.42 public-proof pass, then updated again for v0.65 product-validation and first-run workflow validation.

Current site framing treats LLMGauge as a local-first CLI/evidence tool for validating local LLM testing workflows on real consumer hardware (setup, dry run, real run, validation, scoring, report generation, export-index), not as an agent benchmark, synthetic leaderboard, automatic judge, or model downloader.

Further LLMGauge copy updates should track real releases; they are not the active next website content task.

### 2. Add methodology and claim boundaries

Status: next recommended content patch.

Create a concise methodology page or section:

    How WumboLabs Tests Local Models

This should explain:

- tests run on real consumer hardware
- models are local GGUF files through llama.cpp
- raw outputs are preserved for auditability
- cleaned outputs improve review readability but do not replace raw artifacts
- scores are manual or clearly marked as assisted/review-required
- speed and VRAM results are hardware-specific
- verdicts are practical-use judgments, not universal rankings
- claims should stay tied to hardware, quantization, context, suite, scoring status, and known failure modes

This is the trust bridge between LLMGauge artifacts and public WumboLabs reports.

### 3. Add a current practical baseline summary

Status: near-term.

Add a compact baseline summary to the homepage, Benchmarks index, or future Reports landing page.

Current practical-use baseline on WumboJetsII / RTX 5070 12GB:

- Gemma 4 12B IT QAT UD-Q4_K_XL is the current best overall practical-use baseline.
- Mellum2 Instruct remains the strongest speed candidate.
- Grug-12B Q4_K_M is viable enough to keep as a public comparison entry.
- Qwen3.6 35B-A3B is capable but less comfortable as a 12GB default because of VRAM headroom, completion, and safety tradeoffs.
- Qwen3 14B fits better than Qwen3.6 35B but does not clearly beat Gemma QAT overall.

Keep this short and clearly hardware-scoped.

### 4. Decide Benchmarks vs Reports structure

Status: superseded by `docs/lab-records-migration.md`.

The current Benchmarks section already contains report-like practical-use pages. Do not rush a migration.

Preferred long-term split:

    Reports = curated public conclusions
    Benchmarks = dated evidence records
    LLMGauge = tool / evidence engine
    Lab Notes = process, decisions, and change history

Do not rename or restructure the section until the first curated report format is clear.

The canonical Lab Records plan replaces this split proposal with one `/records/` section for reports, baselines, fit tests, and lab notes.

### 5. Add Real Hardware Model Reports landing page

Status: planned after methodology.

Create:

    /reports/

Purpose:

    Real Hardware Model Reports

This page should explain that WumboLabs turns LLMGauge artifacts into readable, conservative, hardware-aware model reports.

It should link to methodology, LLMGauge, and the best current practical-use comparison.

### 6. Publish first curated comparison report

Status: planned.

Create a public comparison page from the existing practical-use LLMGauge result set.

Working target:

    /reports/practical-local-models-rtx-5070-12gb/

This should answer:

- what was tested
- what hardware was used
- what won
- what failed
- what is actually practical
- what should be tested next
- what claims the evidence supports

Keep it simple before making it exhaustive.

### 7. Add repeatable model report template

Status: later.

Only add individual model report pages after the first comparison report works.

Each model report should include:

- model name
- quantization
- hardware tested
- runtime/backend
- context size
- prompt eval speed
- generation speed
- peak VRAM
- VRAM headroom
- suite/test context
- qualitative strengths
- failure modes
- safety/honesty issues
- practical verdict
- comparison against current baseline
- reproducible artifact links when available

Avoid making per-model pages before the report format is proven.

### 8. Revisit theme and palette after content direction is stable

Status: parallel design work, not blocking content.

A new color theme or palette can improve the site, but it should not distract from the public-proof loop.

Theme work should support:

- readability
- credibility
- report clarity
- no-hype technical identity
- fast scanning of model results

Avoid visual polish that delays methodology, baseline summaries, and the first curated model report.

### Current operating rule

When considering website work, ask:

    Does this create public proof or just private progress?

Prefer work that supports:

- publishing LLMGauge-backed results
- improving report clarity
- increasing credibility
- explaining methodology
- improving reproducibility
- making the WumboLabs thesis clearer
- helping readers understand practical local model tradeoffs

Challenge work that mainly adds internal structure, broad project sprawl, generic portfolio polish, or private-progress infrastructure.

## LLMGauge v0.65 website direction

Status: current content update.

LLMGauge has moved from v0.42 public-proof framing to v0.65 product-validation framing.

Current website emphasis:

- LLMGauge is a local-first CLI/evidence tool for validating local LLM testing workflows on real consumer hardware.
- The current phase is clean-clone and first-run workflow validation.
- Model results remain useful evidence, but the priority is proving the tool works end-to-end for a fresh user.
- Avoid framing the project as a hype benchmark, leaderboard, automatic judge, or “best model” site.

Validated v0.65 workflow:

    fresh clone
    uv sync
    llmgauge setup / setup --scan / setup --non-interactive
    doctor
    smoke
    run --dry-run
    real llama.cpp run
    validate-result
    score --init
    score --check
    apply score
    regenerate report
    export-index

Near-term site implications:

- Update homepage and LLMGauge project page to v0.65.
- Emphasize guided setup, clean-clone validation, and end-to-end product workflow.
- Add methodology / claim-boundary page before expanding reports.
- Do not restructure Benchmarks or Reports in this patch.
- Keep model-result claims scoped as evidence from local runs, not universal recommendations.
