# WumboLabs Website Backlog

Small follow-up items for the public WumboLabs / WumboCore website.

> **Note (2026-09-12):** the Evaluations consolidation changed the public
> information architecture. The canonical public model-evaluation route is now
> `/evaluations/` (one page per tested model); the `/labs/` route and the
> "Labs" / "Lab Records" naming are retired concepts with legacy redirects.
> `/records/` itself remains the live canonical archive, now titled
> **Technical Reports**. Backlog entries below that reference Labs / Lab
> Records as live routes are historical.
>
> **Note (2026-10-13):** later entries describing an active **RTX 5070 12GB**
> or "current 12GB" configuration are historical boundaries, not current
> state. Do not restore them as active claims; current per-model evidence
> lives under `/evaluations/`.

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

LLMGauge is the flagship public evidence tool. wumbOS is the main active development focus. Monolith remains an important supporting project as the interface, operator, and import layer.

### 1. Finish LLMGauge v0.42 / v0.65 site framing

Status: done (superseded by the August 2026 public-status pass).

The LLMGauge project page and homepage activity/status were moved off the old v0.20-era framing through a v0.42 public-proof pass, then updated for v0.65 product-validation, later v0.70 metadata, and the August 2026 consistency pass.

Current site framing treats LLMGauge as the flagship local-first CLI/evidence tool. Formal release is v0.78. Current main is unreleased post-v0.78 development: multi-runtime model identity (model source kinds, checkpoint-directory provenance, vLLM checkpoint binding) plus the accepted EXL/ExLlama runtime-qualification contract — a project-scoped qualification target in LLMGauge's development architecture, not a WELP runtime preference, with no EXL execution promised. The earlier "development is paused pending an RTX 5070 EXL3 baseline" rationale is historical; current compute context is documented on [Methodology](/methodology/) and the site's WumboJetsII infrastructure page. It is not an agent benchmark, synthetic leaderboard, automatic judge, or model downloader.

Further LLMGauge copy updates should track real releases versus unreleased main; they are not the active next website content task.

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

Status: historical. Superseded in compact form by the Technical Reports snapshot (`/records/`); the hardware it described is no longer the active evaluation configuration.

The August 2026 public-status pass added a compact **Current 12GB Reference** and tested/blocked snapshot to `/records/` instead of restoring a homepage model feed.

Historical 12GB reference from that pass (WumboJetsII / RTX 5070 12GB, 2026-08 framing):

- Qwen3.8-27B UD-Q2_K_XL was then the 12GB reference: a strong reviewed coding/technical assistant, not ready for unguarded daily use.
- Gemma 4 12B GGUF, Mellum2, Grug-12B, and earlier Qwen3 / Qwen3.6 results remain historical baselines.
- Do not treat producer claims, queued models, or blocked admissions as completed quality verdicts.

Retain these as dated, hardware-scoped historical boundaries. Do not present them as current state, and do not restore Recent Lab Activity or add a homepage research queue; current per-model evidence lives under `/evaluations/`.

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

Status: superseded — do not implement as written. The canonical long-form surface is `/records/` (Technical Reports) per `docs/lab-records-migration.md`, and the methodology page exists. Any future landing-page idea must build on `/records/`, not a new `/reports/` section.

Create:

    /reports/

Purpose:

    Real Hardware Model Reports

This page should explain that WumboLabs turns LLMGauge artifacts into readable, conservative, hardware-aware model reports.

It should link to methodology, LLMGauge, and the best current practical-use comparison.

### 6. Publish first curated comparison report

Status: superseded as written. The working target `/reports/practical-local-models-rtx-5070-12gb/` predates the records consolidation and its RTX 5070 / 12GB scope is a dated hardware boundary, not the active configuration. Any future comparison content belongs under the canonical `/records/` or `/evaluations/` surfaces.

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

Status: historical framing; superseded by the August 2026 public-status pass (then formal v0.72, with main toward v0.73). This is dated history, not the current release status.

This section records the earlier v0.65 product-validation pass.

Historical website emphasis at that time:

- LLMGauge is a local-first CLI/evidence tool for validating local LLM testing workflows on real consumer hardware.
- The then-current phase was clean-clone and first-run workflow validation.
- Model results remain useful evidence, but the priority then was proving the tool works end-to-end for a fresh user.
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

Those workflow steps remain part of the mature foundation. Current public pages should describe formal v0.78 plus unreleased main, not treat v0.65/v0.70 as the live release line.

## Future expanded Lab experience

Status: later concept. Do not implement a competing `/labs/` route while `/records/` is the canonical evidence archive.

A future expanded Lab experience may eventually organize:

- historical 12GB reference (dated RTX 5070 boundary)
- published reports
- tested models
- blocked/failed experiments
- upcoming tests
- runtime research
- hardware platforms
- methodology

Canonical public route today remains `/records/`.
