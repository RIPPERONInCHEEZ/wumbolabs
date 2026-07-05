+++
title = "LLMGauge"
description = "Local LLM evaluation bench for real consumer hardware."
template = "project.html"
weight = 20
[extra]
back_label = "Back to Projects"
back_url = "/projects"
+++

LLMGauge is WumboLabs' local LLM evaluation bench for real consumer hardware.

It runs reproducible prompt suites against local GGUF models through llama.cpp, preserves raw and cleaned artifacts, captures runtime metrics and VRAM behavior, validates results, supports reviewable scoring, and compares practical model usefulness without leaderboard hype.

<strong>Flagship WumboLabs evidence engine</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Current Tag</span>
    <strong>v0.42</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Evaluation bench</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Backend</span>
    <strong>llama.cpp / GGUF</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Hardware</span>
    <strong>Consumer GPUs</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Core Output</span>
    <strong>Artifacts and reports</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Claim Style</span>
    <strong>Conservative / evidence-backed</strong>
  </div>
</div>

LLMGauge has advanced well beyond the older v0.20 website description. The current v0.42 line includes setup diagnostics, model profile onboarding, dry-run preflight, cleaned output artifacts, manual scoring validation, assisted score drafts, scoring provenance, Fit Ladder artifact workflows, comparison reports, and export indexes.

The goal is not to crown universal benchmark winners. The goal is to preserve enough evidence to answer practical local model questions: what fits, what runs, what fails, what is useful, and what claims the artifacts actually support.

## What LLMGauge Measures

<div class="feature-grid">
  <div class="feature-card">
    <h3>Usefulness</h3>
    <p>Does the model complete practical Linux, coding, config, local AI, and workflow tasks?</p>
  </div>

  <div class="feature-card">
    <h3>Honesty and safety</h3>
    <p>Does it avoid invented tools, unsafe commands, fake packages, and overconfident unsupported claims?</p>
  </div>

  <div class="feature-card">
    <h3>Fit and performance</h3>
    <p>How fast does it run, how much VRAM does it use, and how much headroom remains?</p>
  </div>

  <div class="feature-card">
    <h3>Reproducibility</h3>
    <p>Can the run be validated, reviewed, scored, compared, and understood later from preserved artifacts?</p>
  </div>
</div>

<details class="project-details">
<summary>Current capabilities</summary>

- Check local setup readiness with `doctor`.
- Create ignored local config files with `init-config`.
- Inspect configured model profiles with `list-model-profiles`.
- Validate built-in and custom prompt suites.
- Run one prompt, one category, or a full suite.
- Preview run plans with `run --dry-run`.
- Preview context ladders with `run-ladder --dry-run`.
- Run explicit context fallback tests with `fit-ladder`.
- Validate result, ladder, batch, and Fit Ladder artifacts.
- Preserve raw prompts and raw model outputs.
- Generate cleaned output previews for easier review.
- Capture stderr logs, runtime metadata, speed metrics, and prompt-level NVIDIA VRAM samples.
- Generate Markdown reports and machine-readable JSON result files.
- Initialize, validate, and apply manual scoring files.
- Create deterministic assisted score drafts with review-required provenance.
- Surface scoring provenance and review warnings in reports.
- Compare scored result directories.
- Generate export indexes for downstream reporting/import workflows.

</details>

<details class="project-details">
<summary>Artifact model</summary>

A single LLMGauge run can include:

- raw prompt
- raw model output
- cleaned output preview
- stderr log
- runtime metadata
- speed metrics
- VRAM samples
- `llmgauge-result.json`
- `report.md`
- optional `scores.yaml`
- optional `auto-scores.yaml`

Higher-level artifacts include:

- context ladder summaries
- Fit Ladder summaries and reports
- model batch summaries and reports
- export indexes for run, ladder, batch, and fit-ladder artifacts

</details>

<details class="project-details">
<summary>Scoring and review</summary>

LLMGauge supports structured manual scoring through `scores.yaml`.

The standard scoring workflow is explicit:

    llmgauge score RESULT_DIR --init
    llmgauge score RESULT_DIR --scores RESULT_DIR/scores.yaml --check
    llmgauge score RESULT_DIR --scores RESULT_DIR/scores.yaml

Assisted score drafts are supported, but they are not treated as final human judgment:

    llmgauge score RESULT_DIR --auto-draft

Auto-drafts are deterministic local-rule drafts. They preserve provenance, require review, and do not mutate result artifacts until deliberately validated and applied.

</details>

<details class="project-details">
<summary>Fit Ladder</summary>

Fit Ladder tests whether a model fits at a requested context size and falls back through smaller contexts when needed.

It is designed for practical questions:

- Does this model fit at 64k?
- If not, does it fit at 32k, 16k, or 8k?
- Which context actually works?
- What failed, and why?
- What VRAM headroom remains?

Fit Ladder preserves failed attempt directories and selected working attempts instead of hiding failures.

</details>

<details class="project-details">
<summary>Claim boundaries</summary>

LLMGauge is not a model downloader, automatic judge, synthetic benchmark leaderboard, or universal performance authority.

It complements synthetic benchmarks by testing whether a model is actually useful, honest, safe, complete, and practical on the hardware people really own.

Public claims should stay tied to artifacts, hardware, quantization, runtime settings, context size, scoring status, and known failure modes.

</details>
