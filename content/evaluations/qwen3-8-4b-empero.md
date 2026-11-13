+++
title = "Qwen3.8-4B (Empero)"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 19

[extra]
kind = "model"
model_id = "qwen3.8-4b-empero"
vendor = "empero-ai (Qwen3.8 derivative)"
findings_first = true
recommended_profile_id = "qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver"
recommended_profile_name = "llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane)"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-09-01
+++

## Overview

empero-ai (Qwen3.8 derivative) · 2 tested configurations · 2 evidence events · newest evidence 2026-09-01.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane) (specialized): [event result](#qwen38-empero-4b-distill-wumboserver-2026-09-01).
- **Latest evidence:** 2026-09-01: [event result](#qwen38-empero-4b-distill-wumboserver-2026-09-01)
- **2026-09-01** · llama.cpp · RTX 2060 SUPER: classification BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result). [Event result](#qwen38-empero-4b-distill-wumboserver-2026-09-01)
- **2026-08-18** · llama.cpp/vLLM · RTX 5070: classification SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY. [Event result](#qwen38-empero-4b-vendor-battery-2026-08-18)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen38-empero-4b-distill-wumboserver-2026-09-01"></a>

### 2026-09-01: WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M

**Benchmark Only: WumboServer hardware lane** · config llama.cpp · RTX 2060 SUPER · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

Configuration: llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-4b-empero/events/qwen38-empero-4b-distill-wumboserver-2026-09-01/REPORT.md)


empero-ai/Qwen3.8-4B-Distill-GGUF Q4_K_M on WumboServer RTX 2060S: 97.14 tok/s out, 2145.66 tok/s prefill, 3.0 GB peak VRAM, 172 W. Hardware-lane benchmark; not a WumboJetsII WELP result.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver`: llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboServer (RTX 2060 SUPER 8GB)

<a id="qwen38-empero-4b-vendor-battery-2026-08-18"></a>

### 2026-08-18: LLMGauge vendor-alignment battery (4B bf16/q4)

**Specialized Test: vendor alignment** · config llama.cpp/vLLM · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

Configuration: LLMGauge vendor-alignment battery (bf16/q4).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-4b-empero/events/qwen38-empero-4b-vendor-battery-2026-08-18/REPORT.md)


LLMGauge vendor-alignment qualification battery on empero-ai Qwen3.8-4B (BF16 + Q4).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3.8-4b-empero-vendor-battery`: LLMGauge vendor-alignment battery (bf16/q4)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, performance
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| llama.cpp/vLLM · RTX 5070 | not recorded | llama.cpp/vLLM | RTX 5070 | not recorded | 1 (2026-08-18) |
| llama.cpp · RTX 2060 SUPER | not recorded | llama.cpp | RTX 2060 SUPER | not recorded | 1 (2026-09-01) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp/vLLM · RTX 5070</summary>

- Full profile name: LLMGauge vendor-alignment battery (bf16/q4).
- Profile identity: `qwen3.8-4b-empero-vendor-battery`.
- Status: current tested surface; not the recommended profile.
- Artifact (as recorded): empero-ai/Qwen3.8-4B-GGUF (BF16 + Q4)
- Runtime (as recorded): llama.cpp/vLLM.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.8-4b-empero/profiles/qwen3.8-4b-empero-vendor-battery/profile.json)

Events on this configuration:

- [LLMGauge vendor-alignment battery (4B bf16/q4) (2026-08-18)](/evaluations/qwen3-8-4b-empero#qwen38-empero-4b-vendor-battery-2026-08-18); status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

</details>

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 2060 SUPER</summary>

- Full profile name: llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane).
- Profile identity: `qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver`.
- Status: specialized tested surface.
- Artifact (as recorded): empero-ai/Qwen3.8-4B-Distill-GGUF Q4_K_M
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.8-4b-empero/profiles/qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver/profile.json)

Events on this configuration:

- [WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M (2026-09-01)](/evaluations/qwen3-8-4b-empero#qwen38-empero-4b-distill-wumboserver-2026-09-01); status: BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-01 | [WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M](#qwen38-empero-4b-distill-wumboserver-2026-09-01) | llama.cpp · RTX 2060 SUPER | BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result) |
| 2026-08-18 | [LLMGauge vendor-alignment battery (4B bf16/q4)](#qwen38-empero-4b-vendor-battery-2026-08-18) | llama.cpp/vLLM · RTX 5070 | SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.8-4b-empero)

### Legacy provenance

- [WumboLabs/eval-qwen3.8-4b-empero @ `891dec8a5bd371cf50660efbbee98924f6d4e768`](https://github.com/WumboLabs/eval-qwen3.8-4b-empero/blob/891dec8a5bd371cf50660efbbee98924f6d4e768/events/qwen38-empero-4b-vendor-battery-2026-08-18.md)
- [WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver @ `5b942eee8bb028b7a4f154b2aaee3026b57b6671`](https://github.com/WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver/blob/5b942eee8bb028b7a4f154b2aaee3026b57b6671/events/qwen38-empero-4b-distill-wumboserver-2026-09-01.md)
