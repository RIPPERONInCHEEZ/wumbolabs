+++
title = "LLMGauge"
description = "Local-first CLI for practical LLM evaluation on real consumer hardware."
template = "project.html"
weight = 1
[extra]
back_label = "Back to Projects"
back_url = "/projects"
portfolio_status = "FLAGSHIP PROJECT"
release_status = "FORMAL RELEASE · v0.75 · PyPI 0.75.0"
+++

LLMGauge is the flagship WumboLabs public-evidence tool for practical local LLM evaluation on real consumer hardware.

It is a local-first CLI. The primary runtime is llama.cpp / GGUF. An optional bounded local vLLM adapter is also supported. LLMGauge preserves raw outputs, logs, and evidence; validates artifacts; supports manual and reviewed scoring; generates reports and bounded comparisons; and exports sanitized, machine-readable indexes.

<strong>Flagship WumboLabs evidence tool</strong>

## Current Checkpoint

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Formal release</span>
    <strong>v0.75</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Package</span>
    <strong>0.75.0</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Distribution</span>
    <strong>PyPI · uv tool install</strong>
  </div>

  <div class="info-card">
    <span class="info-label">v0.75 focus</span>
    <strong>Profiles + Bundle 2</strong>
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

v0.75 is the latest formal release, published to production PyPI as `llmgauge` 0.75.0 and covered by over 1,100 automated tests. It adds named reasoning / sampling profiles, requested `--min-p` capture, a derived peak-VRAM metric, and read-only Bundle 2 benchmark qualification. Schemas and artifact contracts evolve additively: previously valid v0.74 result directories remain valid.

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
    <p><code>coding-core-v1</code> 0.1.0 ships in the released CLI: eight coding-oriented roles with native run, result, report, manual, structural, hybrid, and bounded live evidence. Generated code is not automatically executed.</p>
  </div>

  <div class="feature-card">
    <h3>Generic Core</h3>
    <p>The released CLI ships <code>generic-core-v1</code> 0.1.0 as a real discoverable native suite: 13 Core prompts, an exact 4-prompt Smoke profile, and D1–D7 deterministic checks with explicit manual-review boundaries.</p>
  </div>
</div>

<details class="project-details">
<summary>Generic Core boundaries</summary>

Capability areas include instruction following, structured output, honesty / uncertainty, summarization, extraction, planning, technical explanation, coding, code review, troubleshooting, safety/refusal, tool preparation, and bounded-context reconciliation.

Hybrid and manual review boundaries remain explicit. The D5 generated-code check remains `not_run` and non-executing. A separate containment gate is still required before generated-code execution can be admitted.

</details>

## Reasoning and Sampling Profiles

v0.75 makes generation controls a named, versioned, reproducible part of every run. `llmgauge run --sampling-profile PROFILE_ID` attaches a profile to a run; the selected profile, its content identity, and its provenance are recorded in run metadata, reports, and comparisons.

    llmgauge profiles list
    llmgauge profiles show qwen3-thinking-v1

The released CLI ships one controlled profile (`controlled-deterministic-v1`) and four primary-source-qualified vendor-aligned profiles (`qwen3-thinking-v1`, `qwen3-nonthinking-v1`, `gemma-4-instruct-v1`, `deepseek-r1-v1`), each with documented source and scope provenance.

A profile records the controls a run requested. It does not prove semantic model reasoning, effective template behavior, or equivalent behavior to vendor-hosted inference. Vendor alignment is operator-declared, not vendor endorsement.

Comparison reports now treat every captured reasoning / sampling / control setting as runtime-mixing evidence, disclose reasoning mode in Comparison Scope, and add a limited-claims notice when effective reasoning mode is unknown, unspecified, or differs across runs.

## External Benchmark Interoperability

The released CLI imports, validates, and reports authoritative EleutherAI `lm-evaluation-harness` result evidence. LLMGauge does not recreate those benchmarks as native prompts and does not replace their authoritative scoring implementations.

    llmgauge benchmark import
    llmgauge benchmark validate
    llmgauge benchmark report

Qualified Bundle 1: MMLU, ARC Challenge, HellaSwag, WinoGrande, TruthfulQA MC2, GSM8K, HumanEval, and MBPP.

Qualified Bundle 2 (`llmgauge.bundle2.v0`): MMLU-Pro, GPQA (n-shot), and IFEval, at the same pin.

Pinned qualification baseline: EleutherAI `lm-evaluation-harness` v0.4.12, commit `6d642546f4688648fced259eb3302efd36ece5af`.

Real upstream writer validation has been completed for MMLU, ARC Challenge, HellaSwag, WinoGrande, TruthfulQA MC2, and GSM8K. HumanEval and MBPP remain **import / report only** under the current safety boundary. LLMGauge does not automatically execute candidate code for them. Bundle 2 qualification is likewise read-only import evidence, not an LLMGauge-native quality score.

Later possible environment tracks include Terminal-Bench / Harbor, SWE-bench, and browser/computer-use / OSWorld. Those remain future work.

## LocalMaxxing

`llmgauge localmaxxing` is the LocalMaxxing speed/performance benchmark integration. It is separate from `llmgauge benchmark ...`, which imports and reports external quality-benchmark evidence.

Current capabilities include a controlled llama.cpp LocalMaxxing performance protocol, enriched hardware/runtime evidence, local validation/export, authenticated dry-run, and explicit public submission with confirmation. Real public validation has occurred with Qwen3.8-27B models.

Where source-backed, evidence may include output TPS, prefill TPS, combined TPS, TTFT, peak VRAM, mean power, runtime/build provenance, and hardware metadata.

LocalMaxxing Bundle-1 quality submission is **not implemented**.

## Runtime and Hardware Provenance

LLMGauge captures reproducible runtime and hardware evidence. The released CLI preserves requested and runtime-backed llama.cpp settings such as top-k, `--min-p`, seed, independent K/V cache controls, KV offload / parallel evidence, reasoning effort, reasoning budget, fit, reasoning preserve, spec-type, and improved runtime-command evidence.

Requested settings do not automatically prove effective model behavior, effective template behavior, or observed GPU/CPU placement.

Runtime-neutral evidence now includes request wall-time plus classified failures for runtime-environment failure, model-weight-load OOM, KV-cache OOM, and unclassified unknown — and, for native llama.cpp results, a derived device-scoped peak-VRAM metric (`llmgauge.metric.v1.peak_vram`) computed from preserved per-prompt VRAM samples with calculated provenance and validator recomputation. Results without capture remain unchanged; no cross-runtime VRAM equivalence is implied.

The released CLI also includes native multi-turn transcript evidence, retry/recovery/state preservation, read-only WumboLabs OMP Agent Harness session-v3 import, and a dedicated Agent Session Review workflow. LLMGauge remains the evaluator / evidence layer, not an autonomous Agent runtime.

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
- PyPI distribution via Trusted Publishing with build-once/publish-exact-artifacts release automation.

</details>

<details class="project-details">
<summary>Example first-run flow</summary>

    uv tool install llmgauge
    llmgauge --version
    llmgauge setup --scan
    llmgauge setup --non-interactive \
      --llama-cli /path/to/llama-cli \
      --model-path /path/to/model.gguf \
      --profile-name my_model
    llmgauge doctor
    llmgauge smoke
    llmgauge run --suite practical --model-profile my_model --dry-run

For a pinned install: `uv tool install "llmgauge==0.75.0"`. Contributors and unreleased development should use a source checkout with `uv sync` and `uv run llmgauge ...`.

</details>

<details class="project-details">
<summary>Links</summary>

- PyPI: <https://pypi.org/project/llmgauge/>
- GitHub: <https://github.com/WumboLabs/llmgauge>
- Changelog: <https://github.com/WumboLabs/llmgauge/blob/main/CHANGELOG.md>

</details>

<details class="project-details">
<summary>Claim boundaries</summary>

LLMGauge results are local evidence, not universal rankings.

Manual scores are review metadata under a stated rubric. They are not objective proof of model quality. Speed and VRAM results are specific to the tested hardware, runtime, quantization, context size, and settings.

Importing a mainstream benchmark does not mean LLMGauge owns or reimplements that benchmark, and imported external benchmark evidence is not an LLMGauge-native quality score. Generated code is not automatically executed. Sampling-profile selection records requested controls only, and vendor-profile alignment is operator-declared rather than vendor-endorsed.

Reports should be read with their publish-readiness notes, scoring provenance, and known failure modes.

</details>
