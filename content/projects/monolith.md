+++
title = "Monolith"
description = "Local-first AI workbench for testing, comparing, and evaluating local LLMs on real hardware."
weight = 1
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
+++

**Technical Public Alpha · alpha v0.11.9**  
[GitHub Repository](https://github.com/WumboLabs/monolith)

Monolith is a local-first AI workbench for testing, comparing, and evaluating local LLMs on real hardware.

It is built for practical local AI users working with GGUF models, llama.cpp, Linux workstations, constrained VRAM, prompt suites, local evals, context scaling, and agent-backend testing.

**Real hardware. Real testing. No hype.**

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Current Release</span>
    <strong>alpha v0.11.9</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Status</span>
    <strong>Technical Public Alpha</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Audience</span>
    <strong>Technical Linux users</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Setup</span>
    <strong>Manual install</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Local UI</span>
    <strong>127.0.0.1:8765</strong>
  </div>

  <div class="info-card">
    <span class="info-label">License</span>
    <strong>Source-available</strong>
  </div>
</div>

## What It Does

<div class="feature-grid">
  <div class="feature-card">
    <h3>Model Profiles</h3>
    <p>Track local GGUF models, llama.cpp profiles, generated chat profiles, and model metadata.</p>
  </div>

  <div class="feature-card">
    <h3>Local Eval Workflows</h3>
    <p>Browse prompt suites, import local eval results, preserve outputs, and compare practical model behavior.</p>
  </div>

  <div class="feature-card">
    <h3>Context Scaling</h3>
    <p>Scaffold context-size experiments for understanding how models behave beyond short prompts.</p>
  </div>

  <div class="feature-card">
    <h3>Agent Backend Testing</h3>
    <p>Explore conservative agent-backend readiness through prompt suites, review workflows, and read-only scaffolding.</p>
  </div>

  <div class="feature-card">
    <h3>Setup Diagnostics</h3>
    <p>Expose setup state through the UI and terminal-side checks instead of failing silently.</p>
  </div>

  <div class="feature-card">
    <h3>Workstation Visibility</h3>
    <p>Track CPU, memory, root disk, optional NVIDIA GPU stats, and graceful fallback behavior.</p>
  </div>
</div>

## Current Direction

Monolith is becoming a serious local LLM testing suite rather than a generic dashboard.

The design direction is:

- Local AI workbench
- Model lab console
- Terminal-friendly instrument panel
- Practical evaluation suite

The goal is not to chase generic leaderboards. The goal is to understand how local models behave under real constraints.

## Current Roadmap

The roadmap below is synced from Monolith's canonical `docs/ROADMAP.md` public website block.

{{ generated_markdown(path="data/generated/monolith-roadmap.md") }}

## Current Limitations

Monolith is still early and intentionally technical.

Not done yet:

- No clean-clone install validation yet
- No real installer or bootstrap command yet
- No guided setup wizard
- No one-command install
- No bundled llama.cpp installation or build process
- No GPU driver, CUDA, ROCm, or runtime setup
- No full model-profile editor
- No packaged CLI
- No real TUI yet
- No mature eval scoring UI
- No polished model comparison dashboard
- No formal import/export flow
- No CI validation yet
- No packaged desktop app
- No production multi-user or authenticated deployment model

## Licensing Status

Monolith does not currently have an open-source license selected.

The source is public for visibility, review, and technical alpha testing, but broad reuse or redistribution rights are not granted at this stage.

<details>
<summary>Technical Details</summary>

## Canonical Local Usage

Current local web UI:

    http://127.0.0.1:8765/

Canonical start command:

    python scripts/run_webui.py

The local web UI launcher loads `.env` automatically for normal local startup. Direct uvicorn or service wrappers must export environment variables themselves.

## Current Capabilities

### Local Model Testing

- Local FastAPI dashboard
- Local GGUF model profile tracking
- Generated chat profiles from discovered local models
- Basic chat and test run logging
- Prompt and response metadata capture
- Token count tracking
- Speed tracking
- VRAM and performance fields

### Evaluation Workflows

- Local eval prompt suite browsing and imports
- Context-scaling evaluation scaffolding
- Agent-backend evaluation scaffolding
- Agent Lab proposal, review, and read-only workflow scaffolding
- Conservative agent workflow experiments

### Setup and Diagnostics

- Setup diagnostics at `/setup`
- Raw setup diagnostics JSON at `/api/setup/status`
- Terminal-side setup validation through `scripts/setup_check.py`
- First-run empty states for missing setup/configuration
- Release metadata guard for changelog, header, and version consistency

### Workstation Visibility

- CPU monitoring
- Memory monitoring
- Root disk monitoring
- Optional NVIDIA GPU stats
- Graceful fallback when optional machine-specific metrics are unavailable

### Workbench UI

- WumboLabs / WumboCore Monochrome Lime visual system
- Terminal workbench UI shell
- Sidebar and status ticker
- Cards, panels, compact tables, and small technical labels
- Shared table pagination
- Active tab highlighting
- Terminal-readable typography

## Recent Development State

### alpha v0.11.7

Focused on public-alpha cleanup and removing private machine assumptions.

Completed:

- Generalized public-alpha docs and bundled prompt examples
- Removed original-author machine/path assumptions from active public files
- Generalized default model, llama.cpp, inventory, and LLMGauge paths
- Added public-alpha status documentation
- Updated troubleshooting database migration instructions
- Corrected release dates
- Improved repo hygiene for public visibility

### alpha v0.11.8

Focused on first-run setup diagnostics and setup hardening.

Completed:

- Added read-only setup diagnostics at `/setup`
- Added raw setup diagnostics JSON at `/api/setup/status`
- Added `scripts/setup_check.py`
- Improved first-run empty states
- Documented setup diagnostics
- Added release metadata guard
- Established cleaner release validation

### alpha v0.11.9

Focused on the terminal workbench UI shell.

Completed:

- Added terminal workbench UI concept documentation
- Locked local web UI startup to `scripts/run_webui.py`
- Standardized local URL to `http://127.0.0.1:8765/`
- Added `monolith_web_host` and `monolith_web_port`
- Updated install, configuration, and public-alpha docs
- Added terminal workbench CSS shell
- Refined global shell, sidebar, status ticker, cards, panels, and tables
- Added shared table pagination
- Added active tab highlighting
- Preserved existing routes and backend workflows

## Safety Posture

Monolith is designed to run locally on a trusted machine.

The project avoids committing secrets, API keys, private local configs, SQLite databases, raw logs, local model binaries, screenshots with private data, and private prompts.

Agent workflows remain proposal, review, and read-only oriented until proven safe. Automatic write or execution features should remain conservative, explicit, and reversible.

## Longer-Term Direction

The long-term direction includes better model onboarding, safer profile editing, eval scoring, comparison dashboards, global search, run annotations, agent-backend readiness views, and a future CLI/TUI companion.

</details>
