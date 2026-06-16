+++
title = "LLMGauge"
description = "Practical local LLM evaluation on real hardware."
template = "project.html"
weight = 20
[extra]
back_label = "Back to Projects"
back_url = "/projects"
+++

LLMGauge is WumboLabs' local-first evaluation engine for testing GGUF models through llama.cpp on real hardware.

It runs practical prompt suites, captures raw prompts and model outputs, validates result artifacts, supports context ladder tests, and writes import-ready JSON and Markdown outputs.

<strong>Private alpha / internal evaluation engine</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Status</span>
    <strong>Private alpha</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Evaluation engine</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Backend</span>
    <strong>llama.cpp / GGUF</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Focus</span>
    <strong>Monolith importer readiness</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Artifacts</span>
    <strong>Filesystem-first</strong>
  </div>

  <div class="info-card">
    <span class="info-label">UI Layer</span>
    <strong>Monolith</strong>
  </div>
</div>

LLMGauge is currently at the v0.13 readiness checkpoint for Monolith importer planning. It has a stable file-based bridge contract, validation commands, artifact schema documentation, context ladder validation, and export indexes for downstream import workflows.

This is not a polished public release. LLMGauge remains an internal WumboLabs evaluation engine unless a separate public-release and licensing decision is made.

## How It Fits

LLMGauge and Monolith have separate responsibilities.

LLMGauge runs prompt suites, creates result folders, validates artifacts, and writes portable files.

Monolith is the operator and interface layer. It imports, displays, annotates, compares, and manages those results.

<details class="project-details">
<summary>What LLMGauge does</summary>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Runs controlled prompt suites</h3>
    <p>Executes curated local evaluation suites against configured model profiles instead of relying on ad hoc one-off prompts.</p>
  </div>

  <div class="feature-card">
    <h3>Preserves raw artifacts</h3>
    <p>Keeps raw prompts, raw model outputs, stderr logs, Markdown reports, and machine-readable result JSON.</p>
  </div>

  <div class="feature-card">
    <h3>Validates results</h3>
    <p>Checks run directories, context ladder outputs, and export indexes before downstream tools import or compare them.</p>
  </div>

  <div class="feature-card">
    <h3>Tests context behavior</h3>
    <p>Runs the same evaluation across bounded context sizes, with explicit opt-in required for extreme context tests.</p>
  </div>
</div>

</details>

<details class="project-details">
<summary>Artifact model</summary>

A single LLMGauge run produces a result directory with:

- `llmgauge-result.json`
- `report.md`
- raw prompt and output artifacts
- logs

A context ladder produces a ladder directory with:

- `ladder-summary.json`
- `ladder-report.md`
- one child run directory per context size

Export indexes use:

- `llmgauge-index.json`

</details>

<details class="project-details">
<summary>Current capabilities</summary>

- Run local GGUF / llama.cpp model evaluations from controlled prompt suites.
- Preserve raw prompts, raw outputs, logs, reports, and JSON summaries.
- Validate single-run artifacts.
- Validate context-ladder artifacts.
- Generate export indexes for downstream tools.
- Include validation metadata in export indexes.
- Run bounded context ladders.
- Require explicit opt-in for extreme context tests above normal limits.
- Generate synthetic long-context prompts.
- Support manual scoring and comparison workflows.
- Document artifact schemas.
- Document the Monolith bridge contract.

</details>

<details class="project-details">
<summary>Recent work and guardrails</summary>

Recent LLMGauge work focused on making evaluation outputs safer and easier for Monolith to import.

The current readiness checkpoint includes automatic timestamped result directory naming, export indexes, validated index metadata, ladder validation, artifact schema documentation, and a documented bridge contract for Monolith.

LLMGauge is not presented as a hosted service, polished UI, public ranking product, or substitute for Monolith. Its value comes from preserving what was actually run, making outputs auditable, and giving Monolith clean files to import.

</details>
