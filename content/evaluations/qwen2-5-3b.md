+++
title = "Qwen2.5-3B Instruct"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 25

[extra]
kind = "model"
model_id = "qwen2.5-3b"
vendor = "Alibaba (Qwen team)"
findings_first = true
recommended_profile_id = "qwen2.5-3b-vllm-bf16"
recommended_profile_name = "vLLM BF16 (cross-runtime lane)"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-07-15
+++

## Overview

Alibaba (Qwen team) · 2 tested configurations · 2 evidence events · newest evidence 2026-07-15.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** vLLM BF16 (cross-runtime lane) (current): [event result](#qwen25-3b-vllm-fingerprint-smoke-2026-07-15).
- **Latest evidence:** 2026-07-15: [event result](#qwen25-3b-vllm-fingerprint-smoke-2026-07-15)
- **2026-07-15** · vLLM · RTX 5070: classification SPECIALIZED_TEST / RUNTIME_FINGERPRINT. [Event result](#qwen25-3b-vllm-fingerprint-smoke-2026-07-15)
- **2026-07-15** · llama.cpp · RTX 5070: classification BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE. [Event result](#qwen25-3b-cross-runtime-2026-07-15)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen25-3b-vllm-fingerprint-smoke-2026-07-15"></a>

### 2026-07-15: vLLM fingerprint live smoke

**Specialized Test: runtime fingerprint** · config vLLM · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / RUNTIME_FINGERPRINT

Configuration: vLLM BF16 (cross-runtime lane).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-vllm-fingerprint-smoke-2026-07-15/REPORT.md)


vLLM runtime-fingerprint smoke using Qwen2.5-3B as payload.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen2.5-3b-vllm-bf16`: vLLM BF16 (cross-runtime lane)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="qwen25-3b-cross-runtime-2026-07-15"></a>

### 2026-07-15: Cross-runtime comparison: llama.cpp F16 vs vLLM BF16

**Benchmark Only: cross-runtime methodology lane** · config llama.cpp · RTX 5070 · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE

Configuration: llama.cpp F16 (comparison reference).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-cross-runtime-2026-07-15/REPORT.md)


LLMGauge cross-runtime methodology study with model-specific results: Qwen2.5-3B Instruct as F16 llama.cpp vs BF16 vLLM agent-backend comparison incl. failed-command-recovery probes. Primary subject is cross-runtime methodology; the Qwen2.5-3B results are retained as its benchmark-only evidence. Archaeology separately cites a full Qwen2.5-3B quant-lab record set (F16/Q8_0/Q6_K/Q5_K_M/Q4_K_M/IQ4_XS) from the Arch era.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen2.5-3b-llamacpp-f16`: llama.cpp F16 (comparison reference)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| llama.cpp · RTX 5070 | not recorded | llama.cpp | RTX 5070 | not recorded | 1 (2026-07-15) |
| vLLM · RTX 5070 | not recorded | vLLM | RTX 5070 | not recorded | 1 (2026-07-15) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp F16 (comparison reference).
- Profile identity: `qwen2.5-3b-llamacpp-f16`.
- Status: current tested surface; not the recommended profile.
- Artifact (as recorded): Qwen2.5-3B-Instruct F16 GGUF (6,178,317,312-byte fingerprint)
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen2.5-3b/profiles/qwen2.5-3b-llamacpp-f16/profile.json)

Events on this configuration:

- [Cross-runtime comparison: llama.cpp F16 vs vLLM BF16 (2026-07-15)](/evaluations/qwen2-5-3b#qwen25-3b-cross-runtime-2026-07-15); status: BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE

</details>

<details class="lab-findings-configs">
<summary>Configuration details: vLLM · RTX 5070</summary>

- Full profile name: vLLM BF16 (cross-runtime lane).
- Profile identity: `qwen2.5-3b-vllm-bf16`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): Qwen/Qwen2.5-3B-Instruct BF16
- Runtime (as recorded): vLLM.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen2.5-3b/profiles/qwen2.5-3b-vllm-bf16/profile.json)

Events on this configuration:

- [vLLM fingerprint live smoke (2026-07-15)](/evaluations/qwen2-5-3b#qwen25-3b-vllm-fingerprint-smoke-2026-07-15); status: SPECIALIZED_TEST / RUNTIME_FINGERPRINT

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-07-15 | [vLLM fingerprint live smoke](#qwen25-3b-vllm-fingerprint-smoke-2026-07-15) | vLLM · RTX 5070 | SPECIALIZED_TEST / RUNTIME_FINGERPRINT |
| 2026-07-15 | [Cross-runtime comparison: llama.cpp F16 vs vLLM BF16](#qwen25-3b-cross-runtime-2026-07-15) | llama.cpp · RTX 5070 | BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen2.5-3b)

### Legacy provenance

- [WumboLabs/eval-qwen2.5-3b-llamacpp-f16 @ `651bbea8c5d1e9c1c5dfa21a538a6922f2bf60a8`](https://github.com/WumboLabs/eval-qwen2.5-3b-llamacpp-f16/blob/651bbea8c5d1e9c1c5dfa21a538a6922f2bf60a8/shared/compare-qwen25-3b-f16-vs-vllm-bf16-8k.md)
- [WumboLabs/eval-qwen2.5-3b-vllm-bf16 @ `92e975e31a46b1e84e21b838f7a79e5c91cd7e86`](https://github.com/WumboLabs/eval-qwen2.5-3b-vllm-bf16/blob/92e975e31a46b1e84e21b838f7a79e5c91cd7e86/events/qwen25-3b-vllm-fingerprint-smoke-2026-07.md)
