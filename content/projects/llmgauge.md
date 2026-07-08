+++
title = "LLMGauge"
description = "Local-first CLI for practical LLM evaluation on real consumer hardware."
template = "project.html"
weight = 20
[extra]
back_label = "Back to Projects"
back_url = "/projects"
+++

LLMGauge is WumboLabs' local-first CLI for validating practical local LLM testing workflows on real consumer hardware.

It runs local GGUF models through llama.cpp, preserves raw and cleaned artifacts, validates result structure, supports manual scoring with rationale, regenerates reports, captures speed and VRAM context, and exports machine-readable indexes for downstream reporting or import workflows.

<strong>Flagship WumboLabs evidence tool</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Current Tag</span>
    <strong>v0.65</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Focus</span>
    <strong>First-run validation</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Evaluation CLI</strong>
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
    <span class="info-label">Claim Style</span>
    <strong>Local evidence, not rankings</strong>
  </div>
</div>

The v0.65 milestone validates the guided first-run setup and clean-clone workflow. The current phase is product validation: making sure a fresh user can clone LLMGauge, configure llama.cpp and model profiles, run real local models, validate artifacts, manually score outputs, regenerate reports, and export indexes without broken paths, unclear commands, or hidden assumptions.

Model results are still useful evidence, but they are secondary to proving the tool works end-to-end.

## What It Is

LLMGauge is a local-first command-line tool for running practical local LLM evaluations, preserving artifacts, validating results, manually scoring outputs, and generating auditable reports.

It is not a hype benchmark, leaderboard, automatic judge, model downloader, or universal performance authority.

## Workflow

<div class="feature-grid">
  <div class="feature-card">
    <h3>Setup</h3>
    <p>Configure llama.cpp and local GGUF model profiles with guided setup commands.</p>
  </div>

  <div class="feature-card">
    <h3>Dry run</h3>
    <p>Resolve suites, model paths, runtime options, and output locations before launching a model.</p>
  </div>

  <div class="feature-card">
    <h3>Run and validate</h3>
    <p>Run practical prompt suites through llama.cpp, then validate generated result artifacts.</p>
  </div>

  <div class="feature-card">
    <h3>Score and export</h3>
    <p>Apply manual scores with rationale, regenerate reports, and export machine-readable indexes.</p>
  </div>
</div>

<details class="project-details">
<summary>Guided setup in v0.65</summary>

LLMGauge v0.65 adds guided first-run setup:

- `llmgauge setup`
- `llmgauge setup --scan`
- `llmgauge setup --non-interactive`
- explicit `--llama-cli`
- explicit `--model-path`
- explicit `--models-dir`
- explicit `--profile-name`

Setup helps configure the local llama.cpp path and GGUF model profiles.

It does not download models, build llama.cpp, or launch a model during setup.

</details>

<details class="project-details">
<summary>What LLMGauge can do</summary>

- Run local GGUF / llama.cpp models.
- Use practical prompt suites.
- Capture raw model outputs.
- Create cleaned outputs for review.
- Preserve stderr logs.
- Capture prompt-level NVIDIA VRAM telemetry.
- Track prompt eval speed and generation speed.
- Validate result artifact structure.
- Support manual scoring with rationale.
- Regenerate scored reports.
- Create comparison and report artifacts.
- Export machine-readable index JSON for downstream reporting/import workflows.
- Support model profiles for repeated local testing.
- Guard against accidental output directory reuse.
- Validate clean-clone setup and scripted setup checks.

</details>

<details class="project-details">
<summary>Validated v0.65 clean-clone workflow</summary>

The v0.65 workflow validation confirmed:

- fresh GitHub clone works
- `uv sync` works
- `llmgauge --version` reports `0.65.0`
- `llmgauge setup --help` works
- `setup --scan` is read-only
- `setup --non-interactive` creates usable config/profile files
- `doctor` and `smoke` pass after setup
- `run --dry-run` resolves model paths and runtime options without launching
- real model runs launch llama.cpp successfully
- result artifacts are generated correctly
- `validate-result` passes before and after scoring
- `score --init`, `score --check`, and score application work
- `report.md` updates with scoring status and provenance
- `export-index` works with positional artifact paths and includes scoring, artifact, and VRAM metadata

</details>

<details class="project-details">
<summary>Recent real validation artifacts</summary>

Gemma 4 12B IT UD-Q5_K_XL completed, validated, scored, and indexed through the v0.65 workflow.

- Suite: `wumbolabs-practical-v1`
- Context: 8192
- Prompts: 10 / 10 completed
- Manual score average: 4.29 / 5
- Verdicts: 7 pass, 3 mixed
- Peak VRAM: 9631 MiB
- Minimum VRAM headroom: 2596 MiB
- Generation speed: about 60-62 tok/s

Mellum2 12B-A2.5B Instruct Q4_K_M also completed and validated through the same workflow, but was not yet scored in that pass.

- Suite: `wumbolabs-practical-v1`
- Context: 8192
- Prompts: 10 / 10 completed
- Peak VRAM: 8762 MiB
- Minimum VRAM headroom: 3465 MiB
- Generation speed: about 248-264 tok/s

The Mellum2 run validated that adding a second real model profile works, dry-run planning works, existing output directory guards work, and artifacts validate correctly. Its quality appears more mixed and still needs scoring.

</details>

<details class="project-details">
<summary>Example first-run flow</summary>

    uv sync
    uv run llmgauge setup --scan
    uv run llmgauge setup --non-interactive \
      --llama-cli /path/to/llama-cli \
      --model-path /path/to/model.gguf \
      --profile-name my_model

    uv run llmgauge doctor
    uv run llmgauge smoke
    uv run llmgauge run --suite practical --model-profile my_model --dry-run

</details>

<details class="project-details">
<summary>Claim boundaries</summary>

LLMGauge results are local evidence, not universal rankings.

Manual scores are review metadata under a stated rubric. Speed and VRAM results are specific to the tested hardware, runtime, quantization, context size, and settings.

Reports should be read with their publish-readiness notes, scoring provenance, and known failure modes.

LLMGauge exists to make local model testing reproducible, auditable, and grounded in real hardware rather than hype, screenshots, or unverifiable claims.

</details>
