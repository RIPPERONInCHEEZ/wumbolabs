+++
title = "Qwen3.8-2B (Empero)"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 24

[extra]
kind = "model"
model_id = "qwen3.8-2b-empero"
vendor = "empero-ai (Qwen3.8 derivative)"
findings_first = true
recommended_profile_id = "qwen3.8-2b-empero-vllm-bf16"
recommended_profile_name = "vLLM BF16 vendor-alignment battery"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-08-18
+++

## Overview

empero-ai (Qwen3.8 derivative) · 1 tested configuration · 1 evidence event · newest evidence 2026-08-18.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** vLLM BF16 vendor-alignment battery (current): [event result](#qwen38-empero-2b-vendor-battery-2026-08-18).
- **Latest evidence:** 2026-08-18: [event result](#qwen38-empero-2b-vendor-battery-2026-08-18)
- **2026-08-18** · vLLM/llama.cpp · RTX 5070: classification SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY. [Event result](#qwen38-empero-2b-vendor-battery-2026-08-18)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen38-empero-2b-vendor-battery-2026-08-18"></a>

### 2026-08-18: LLMGauge vendor-alignment battery (2B bf16)

**Specialized Test: vendor alignment** · config vLLM/llama.cpp · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

Configuration: vLLM BF16 vendor-alignment battery.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-2b-empero/events/qwen38-empero-2b-vendor-battery-2026-08-18/REPORT.md)


LLMGauge vendor-alignment qualification battery on empero-ai Qwen3.8-2B (BF16/GGUF): full suites at vendor 8192 plus configured-context default probing up to 262144. Primary subject is LLMGauge vendor alignment; model results retained.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3.8-2b-empero-vllm-bf16`: vLLM BF16 vendor-alignment battery
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, performance, context
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| vLLM/llama.cpp · RTX 5070 | not recorded | vLLM/llama.cpp | RTX 5070 | not recorded | 1 (2026-08-18) |

<details class="lab-findings-configs">
<summary>Configuration details: vLLM/llama.cpp · RTX 5070</summary>

- Full profile name: vLLM BF16 vendor-alignment battery.
- Profile identity: `qwen3.8-2b-empero-vllm-bf16`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): empero-ai/Qwen3.8-2B-GGUF (+ BF16)
- Runtime (as recorded): vLLM/llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.8-2b-empero/profiles/qwen3.8-2b-empero-vllm-bf16/profile.json)

Events on this configuration:

- [LLMGauge vendor-alignment battery (2B bf16) (2026-08-18)](/evaluations/qwen3-8-2b-empero#qwen38-empero-2b-vendor-battery-2026-08-18); status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-08-18 | [LLMGauge vendor-alignment battery (2B bf16)](#qwen38-empero-2b-vendor-battery-2026-08-18) | vLLM/llama.cpp · RTX 5070 | SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.8-2b-empero)

### Legacy provenance

- [WumboLabs/eval-qwen3.8-2b-empero @ `e09ed632fe835dac69eb05f9e37f7b57485923fd`](https://github.com/WumboLabs/eval-qwen3.8-2b-empero/blob/e09ed632fe835dac69eb05f9e37f7b57485923fd/events/qwen38-empero-2b-vendor-battery-2026-08-18.md)
