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

It runs practical prompt suites, captures raw prompts and model outputs, validates result artifacts, supports context ladder tests, captures VRAM behavior, and writes import-ready JSON and Markdown outputs.

<strong>Private alpha / internal evaluation engine</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Status</span>
    <strong>Private alpha</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Current Tag</span>
    <strong>v0.20</strong>
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
    <strong>Batch, VRAM, and import workflows</strong>
  </div>

  <div class="info-card">
    <span class="info-label">UI Layer</span>
    <strong>Monolith</strong>
  </div>
</div>

LLMGauge has moved beyond its v0.13 importer-readiness checkpoint. The current v0.20 line adds model batch runs, batch validation, batch export-index support, VRAM metadata, deterministic baseline checks, and scored comparison summaries.

This is not a polished public release. LLMGauge remains an internal WumboLabs evaluation engine unless a separate public-release and licensing decision is made.

## How It Fits

LLMGauge and Monolith have separate responsibilities.

LLMGauge runs prompt suites, creates result folders, validates artifacts, captures performance/VRAM data, and writes portable files.

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
    <p>Keeps raw prompts, raw model outputs, stderr logs, Markdown reports, machine-readable result JSON, and VRAM samples.</p>
  </div>

  <div class="feature-card">
    <h3>Validates results</h3>
    <p>Checks single-run, context-ladder, model-batch, and export-index artifacts before downstream tools import or compare them.</p>
  </div>

  <div class="feature-card">
    <h3>Tests context behavior</h3>
    <p>Runs the same evaluation across bounded context sizes, with explicit opt-in required for extreme context tests.</p>
  </div>
</div>

</details>

<details class="project-details">
<summary>Current capabilities</summary>

- Run local GGUF / llama.cpp model evaluations from controlled prompt suites.
- Preserve raw prompts, raw outputs, logs, reports, and JSON summaries.
- Capture prompt-level NVIDIA VRAM usage through `nvidia-smi`.
- Report peak VRAM, total VRAM, headroom, initial usage, final usage, GPU name, and sample count.
- Validate single-run artifacts.
- Validate context-ladder artifacts.
- Run manifest-driven model batches across existing model profiles.
- Validate model-batch parent artifacts and completed child result directories.
- Generate export indexes for run, ladder, and batch artifacts.
- Include validation and VRAM metadata in export indexes.
- Run deterministic baseline checks against completed result artifacts.
- Support manual scoring and scored comparison summaries.
- Document artifact schemas and the Monolith bridge contract.

</details>

<details class="project-details">
<summary>Artifact model</summary>

A single LLMGauge run produces a result directory with:

- `llmgauge-result.json`
- `report.md`
- raw prompt and output artifacts
- logs
- optional VRAM sample artifacts

A context ladder produces a ladder directory with:

- `ladder-summary.json`
- `ladder-report.md`
- one child run directory per context size

A model batch produces a batch directory with:

- `batch-summary.json`
- `batch-report.md`
- one child run directory per model/profile run

Export indexes use:

- `llmgauge-index.json`

</details>

<details class="project-details">
<summary>Recent work and guardrails</summary>

Recent LLMGauge work focused on making evaluation outputs more complete, safer to import, and easier to compare.

The v0.20 line adds manifest-driven model batches, batch validation, batch export-index support, warning-only VRAM guardrails, VRAM metadata in export indexes, baseline checks, and scored comparison summaries.

Batch manifests reference existing model profile names rather than accepting arbitrary model paths. VRAM capture is read-only and non-fatal if `nvidia-smi` is unavailable.

LLMGauge is not presented as a hosted service, polished UI, public ranking product, or substitute for Monolith. Its value comes from preserving what was actually run, making outputs auditable, and giving Monolith clean files to import.

</details>
