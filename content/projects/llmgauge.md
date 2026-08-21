+++
title = "LLMGauge"
description = "Local-first CLI for practical LLM evaluation on real consumer hardware."
template = "project.html"
weight = 1
[extra]
back_label = "Back to Projects"
back_url = "/projects"
portfolio_status = "FLAGSHIP PROJECT"
release_status = "FORMAL RELEASE · v0.72 · current main toward v0.73"
+++

LLMGauge is the flagship WumboLabs public-evidence tool for practical local LLM evaluation on real consumer hardware.

It is a local-first CLI. The primary runtime is llama.cpp / GGUF. An optional bounded local vLLM adapter is also supported. LLMGauge preserves raw outputs, logs, and evidence; validates artifacts; supports manual and reviewed scoring; generates reports and bounded comparisons; and exports sanitized, machine-readable indexes.

<strong>Flagship WumboLabs evidence tool</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Formal release</span>
    <strong>v0.72</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Package</span>
    <strong>0.72.0</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Current main</span>
    <strong>Unreleased toward v0.73</strong>
  </div>

  <div class="info-card">
    <span class="info-label">v0.73 gate</span>
    <strong>Generic Core</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Evaluator / evidence layer</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Claim style</span>
    <strong>Local evidence, not rankings</strong>
  </div>
</div>

v0.72 is the latest formal release. Current `main` contains substantial validated development beyond that tag. Those capabilities are unreleased work toward the v0.73 Generic Core release gate. **v0.73 has not shipped.**

LLMGauge is not a hype benchmark, leaderboard, automatic judge, model downloader, cloud evaluation service, or autonomous Agent runtime.

## Workflow

<div class="feature-grid">
  <div class="feature-card">
    <h3>Setup</h3>
    <p>Configure llama.cpp and local GGUF model profiles with guided setup, then inspect the environment with doctor and smoke checks.</p>
  </div>

  <div class="feature-card">
    <h3>Dry run</h3>
    <p>Resolve suites, model paths, runtime options, and output locations before launching a model.</p>
  </div>

  <div class="feature-card">
    <h3>Run and validate</h3>
    <p>Run practical and native suites through llama.cpp, preserve artifacts, and validate result structure.</p>
  </div>

  <div class="feature-card">
    <h3>Score and export</h3>
    <p>Apply manual or reviewed scores with rationale, regenerate reports, and export machine-readable indexes.</p>
  </div>
</div>

## Evaluation Surfaces

<div class="feature-grid">
  <div class="feature-card">
    <h3>Practical</h3>
    <p>WumboLabs Practical remains the real-workflow evaluation track. Reviewed practical evidence packages and bounded comparisons exist.</p>
  </div>

  <div class="feature-card">
    <h3>Coding Core</h3>
    <p><code>coding-core-v1</code> 0.1.0 is implemented on current main: eight coding-oriented roles with native run, result, report, manual, structural, hybrid, and bounded live evidence. Generated code is not automatically executed.</p>
  </div>

  <div class="feature-card">
    <h3>Generic Core</h3>
    <p>Current main includes <code>generic-core-v1</code> 0.1.0 as a real discoverable native suite: 13 Core prompts, an exact 4-prompt Smoke profile, and D1–D7 deterministic checks. It is not the completed v0.73 release.</p>
  </div>
</div>

<details class="project-details">
<summary>Generic Core boundaries</summary>

Capability areas include instruction following, structured output, honesty / uncertainty, summarization, extraction, planning, technical explanation, coding, code review, troubleshooting, safety/refusal, tool preparation, and bounded-context reconciliation.

Hybrid and manual review boundaries remain explicit. The D5 generated-code check remains `not_run` and non-executing. A separate containment gate is still required before generated-code execution can be admitted.

</details>

## External Benchmark Interoperability

Current main can import, validate, and report authoritative EleutherAI `lm-evaluation-harness` result evidence. LLMGauge does not recreate those benchmarks as native prompts and does not replace their authoritative scoring implementations.

    llmgauge benchmark import
    llmgauge benchmark validate
    llmgauge benchmark report

Qualified Bundle 1: MMLU, ARC Challenge, HellaSwag, WinoGrande, TruthfulQA MC2, GSM8K, HumanEval, and MBPP.

Pinned qualification baseline: EleutherAI `lm-evaluation-harness` v0.4.12, commit `6d642546f4688648fced259eb3302efd36ece5af`.

Real upstream writer validation has been completed for MMLU, ARC Challenge, HellaSwag, WinoGrande, TruthfulQA MC2, and GSM8K. HumanEval and MBPP remain **import / report only** under the current safety boundary. LLMGauge does not automatically execute candidate code for them.

Future Bundle 2 may add MMLU-Pro, GPQA, and IFEval. Later possible environment tracks include Terminal-Bench / Harbor, SWE-bench, and browser/computer-use / OSWorld. Those remain future work.

## LocalMaxxing

`llmgauge localmaxxing` is the LocalMaxxing speed/performance benchmark integration. It is separate from `llmgauge benchmark ...`, which imports and reports external quality-benchmark evidence.

Current capabilities include a controlled llama.cpp LocalMaxxing performance protocol, enriched hardware/runtime evidence, local validation/export, authenticated dry-run, and explicit public submission with confirmation. Real public validation has occurred with Qwen3.8-27B models.

Where source-backed, evidence may include output TPS, prefill TPS, combined TPS, TTFT, peak VRAM, mean power, runtime/build provenance, and hardware metadata.

LocalMaxxing Bundle-1 quality submission is **not implemented**.

## Runtime and Hardware Provenance

LLMGauge captures reproducible runtime and hardware evidence. Current main also preserves requested and runtime-backed llama.cpp settings such as top-k, seed, independent K/V cache controls, KV offload / parallel evidence, reasoning effort, reasoning budget, fit, reasoning preserve, spec-type, and improved runtime-command evidence.

Requested settings do not automatically prove effective model behavior, effective template behavior, or observed GPU/CPU placement.

The first bounded native llama.cpp runtime-neutral evidence slice is implemented: request wall-time evidence plus classified failures for runtime-environment failure, model-weight-load OOM, KV-cache OOM, and unclassified unknown. Broader Area 4 work remains future.

Current main also includes native multi-turn transcript evidence, retry/recovery/state preservation, read-only WumboLabs OMP Agent Harness session-v3 import, and a dedicated Agent Session Review workflow. LLMGauge remains the evaluator / evidence layer, not an autonomous Agent runtime.

<details class="project-details">
<summary>Mature foundation</summary>

- Local-first CLI with llama.cpp / GGUF as the primary runtime.
- Optional bounded local vLLM adapter.
- Preserved raw outputs, logs, and evidence.
- Model profiles, validation, manual/reviewed scoring, reports, and bounded comparisons.
- Sanitized public export.
- Context ladders and Fit Ladder.
- Provenance and evidence fingerprints.
- Guided setup, doctor, and smoke workflows.

</details>

<details class="project-details">
<summary>Example first-run flow</summary>

    uv tool install git+https://github.com/WumboLabs/llmgauge.git@v0.72
    llmgauge setup --scan
    llmgauge setup --non-interactive \
      --llama-cli /path/to/llama-cli \
      --model-path /path/to/model.gguf \
      --profile-name my_model
    llmgauge doctor
    llmgauge smoke
    llmgauge run --suite practical --model-profile my_model --dry-run

Contributors and unreleased development should use a source checkout with `uv sync` and `uv run llmgauge ...`.

</details>

<details class="project-details">
<summary>Claim boundaries</summary>

LLMGauge results are local evidence, not universal rankings.

Manual scores are review metadata under a stated rubric. They are not objective proof of model quality. Speed and VRAM results are specific to the tested hardware, runtime, quantization, context size, and settings.

Importing a mainstream benchmark does not mean LLMGauge owns or reimplements that benchmark. Generated code is not automatically executed. Unreleased current-main capabilities have not shipped in v0.72.

Reports should be read with their publish-readiness notes, scoring provenance, and known failure modes.

</details>
