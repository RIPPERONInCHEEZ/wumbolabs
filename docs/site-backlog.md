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

### 1. Finish LLMGauge v0.42 refresh

Status: in progress.

Update the LLMGauge project page and homepage activity/status from the old v0.20-era framing to the current v0.42-era framing.

The page should describe LLMGauge as a local LLM evaluation bench for real consumer hardware, with preserved artifacts, cleaned output, validation, scoring, reports, VRAM/performance capture, Fit Ladder testing, and comparison workflows.

Do not frame LLMGauge primarily as an agent benchmark, synthetic leaderboard, automatic judge, or model downloader.

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

Status: planned.

The current Benchmarks section already contains report-like practical-use pages. Do not rush a migration.

Preferred long-term split:

    Reports = curated public conclusions
    Benchmarks = dated evidence records
    LLMGauge = tool / evidence engine
    Lab Notes = process, decisions, and change history

Do not rename or restructure the section until the first curated report format is clear.

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
