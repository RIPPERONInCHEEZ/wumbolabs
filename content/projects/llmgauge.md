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

LLMGauge is designed to act as the evaluation backend for Monolith while keeping the boundary clean: LLMGauge produces portable artifacts, and Monolith imports, displays, and manages them.

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
    <span class="info-label">Target Backend</span>
    <strong>llama.cpp / GGUF</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Current Focus</span>
    <strong>Monolith importer readiness</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Artifact Style</span>
    <strong>Filesystem-first</strong>
  </div>

  <div class="info-card">
    <span class="info-label">UI Layer</span>
    <strong>Monolith</strong>
  </div>
</div>

LLMGauge is currently at the v0.13 readiness checkpoint for Monolith importer planning. That means the project has a stable file-based bridge contract, validation commands, artifact schema documentation, context ladder validation, and export indexes that downstream tools can inspect before importing.

This checkpoint should not be read as a polished public release. The project remains an internal WumboLabs evaluation engine unless a separate public-release and licensing decision is made.

## What It Does

<div class="feature-grid">
  <div class="feature-card">
    <h3>Runs controlled prompt suites</h3>
    <p>LLMGauge executes curated local evaluation suites against configured model profiles instead of relying on ad hoc one-off prompts.</p>
  </div>

  <div class="feature-card">
    <h3>Preserves raw artifacts</h3>
    <p>Runs keep raw prompts, raw model outputs, stderr logs, Markdown reports, and machine-readable result JSON.</p>
  </div>

  <div class="feature-card">
    <h3>Validates results</h3>
    <p>Run directories, context ladder outputs, and export indexes can be checked before downstream tools import or compare them.</p>
  </div>

  <div class="feature-card">
    <h3>Tests context behavior</h3>
    <p>Context ladders run the same evaluation across bounded context sizes, with explicit opt-in required for extreme context tests.</p>
  </div>

  <div class="feature-card">
    <h3>Supports manual scoring</h3>
    <p>Evaluation stays practical and inspectable: raw outputs remain available while scoring and comparison reports add structure.</p>
  </div>

  <div class="feature-card">
    <h3>Exports for Monolith</h3>
    <p>LLMGauge writes portable JSON and Markdown artifacts that Monolith can import into its own UI, database, and dashboards.</p>
  </div>
</div>

## Boundary With Monolith

LLMGauge and Monolith have separate responsibilities.

LLMGauge is the evaluation engine. It runs prompt suites, creates result folders, validates artifacts, and writes portable files.

Monolith is the operator and interface layer. It keeps UI state, dashboards, annotations, task state, imported rows, caches, and database-backed views.

That boundary is intentional. LLMGauge should not own the Monolith database. Monolith should not be required to execute every evaluation directly. The file-based bridge lets LLMGauge remain inspectable and portable while Monolith becomes the place where results are imported, reviewed, compared, and managed.

## Artifact Model

A single LLMGauge run produces a result directory with:

- `llmgauge-result.json`
- `report.md`
- raw prompt and output artifacts
- logs

A context ladder produces a ladder directory with:

- `ladder-summary.json`
- `ladder-report.md`
- one child run directory per context size

Each context child directory is a normal single-run result directory.

Export indexes use:

- `llmgauge-index.json`

These indexes can describe one or more run or ladder artifacts and can include validation metadata for import workflows.

## Current Capabilities

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

## Recent Work

Recent LLMGauge work focused on making evaluation outputs safer and easier for Monolith to import.

The current readiness checkpoint includes automatic timestamped result directory naming, export indexes, validated index metadata, ladder validation, artifact schema documentation, and a documented bridge contract for Monolith.

This work shifts the next major implementation step toward Monolith: importing LLMGauge result directories, ladder directories, and export indexes while keeping older Quant Lab and local evaluation data readable.

## Guardrails

LLMGauge is not presented as a hosted service, polished UI, public ranking product, or substitute for Monolith.

It is a local-first, artifact-based evaluation engine for practical model testing on real hardware. Its value comes from preserving what was actually run, making outputs auditable, and giving Monolith clean files to import rather than hidden state to guess from.
