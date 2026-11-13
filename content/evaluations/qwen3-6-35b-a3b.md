+++
title = "Qwen3.6-35B-A3B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 11

[extra]
kind = "model"
model_id = "qwen3.6-35b-a3b"
vendor = "Alibaba (Qwen team)"
findings_first = true
classification = "LIMITED_ROLE_ONLY"
recommended_profile_id = "qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv"
recommended_profile_name = "llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile)"
practical_context = "32,768 default / 16,384 guarded tokens"
profile_count = 2
event_count = 3
latest_evidence_date = 2026-09-15
+++

## Overview

Alibaba (Qwen team) · 2 tested configurations · 3 evidence events · newest evidence 2026-09-15.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: LIMITED_ROLE_ONLY** - attributed to the [2026-09-15 event](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15), configuration UD-IQ2_M · llama.cpp · RTX 5070.
- **Recommended configuration:** llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile) (current): [event result](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15).
- **Practical context:** 32,768 default / 16,384 guarded tokens; native model-card maximum 262,144 (envelope complete: YES); source: [event result](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15)
- **Context limit outcome:** FIT_LIMIT on this RTX 5070 12GB/current q8_0-KV text profile: measured ~12.9 KiB/token KV growth and frozen 512 MiB reserve exceed available VRAM; nearest measured validated boundary is 32,768. This is profile/hardware scoped, not a universal model limit.; source: [event result](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15)
- **Latest evidence:** 2026-09-15: [event result](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15)
- **2026-09-15** · UD-IQ2_M · llama.cpp · RTX 5070: classification LIMITED_ROLE_ONLY; 11/12 frozen mechanical quality screen; sole miss was the lexical no-letter-e constraint. [Event result](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15)
- **2026-07-22** · llama.cpp · RTX 5070: classification BENCHMARK_ONLY (TOOL_VERSION_RERUN). [Event result](#qwen36-35b-practical-v071-2026-07-22)
- **2026-07-15** · llama.cpp · RTX 5070: classification SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION. [Event result](#qwen36-35b-fit-ladder-e2e-2026-07-15)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15"></a>

### 2026-09-15: Current-WELP recharacterization

**WELP Recharacterization: llama.cpp UD-IQ2_M q8_0 KV** · config UD-IQ2_M · llama.cpp · RTX 5070 · maturity: CURRENT_WELP · status: LIMITED_ROLE_ONLY

Configuration: llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)

#### WELP outcome

- **Outcome:** PASS
- **Classification:** LIMITED_ROLE_ONLY

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; sole miss was the lexical no-letter-e constraint.
- coding: PASS
- tool formatting: PASS
- reasoning: frozen 1,500-token probe did not finalize; a separate 4,096-token operational probe correctly completed 17 × 23 = 391 with coherent reasoning

##### Guardrails and limitations

- reliability 9/20 at seed 42 and 9/20 at seed 314159
- Git safety 0/1 at both seeds
- substantive factual errors, hallucination-related failures, sycophancy and uncertainty weaknesses, plus repeated length truncation constrain use to LIMITED_ROLE_ONLY
- official model is multimodal but this --no-mmproj text profile is SUPPORTED_NOT_CHARACTERIZED for vision

**Reliability:** Strict interfaces 3/3 at both seeds; the replicated 9/20 reliability result is classification-determining. Reasoning is operational with sufficient output budget, not an unconditional frozen-cap PASS.

#### LocalMaxxing

- Status: MEASURED_NOT_SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>local canonical-profile benchmark pp512 3571.96 ± 151.06 tok/s / tg128 157.62 ± 0.43 tok/s; no external submission or fabricated verification fields; service mutation requires separate authorization.</small></p>

**Tested condition:** artifact UD-IQ2_M · llama.cpp · RTX 5070 · context 32,768 default / 16,384 guarded · native model-card maximum 262,144 tokens · envelope complete: YES.

**Context limit outcome:** FIT_LIMIT on this RTX 5070 12GB/current q8_0-KV text profile: measured ~12.9 KiB/token KV growth and frozen 512 MiB reserve exceed available VRAM; nearest measured validated boundary is 32,768. This is profile/hardware scoped, not a universal model limit.

**Context boundaries:** 8K, 16K, and 32K are VALIDATED. Canonical measured maximum 32K is tight-fit only (about 433 MiB remaining after near-full request; no concurrent GPU workload). Two required 32K seeds pass useful-context depths 2/25/50/75/95%, with 31,961-31,964 usable tokens (99.48-99.49%). Official static-YaRN 1,010,000 is FIT_LIMIT on this hardware/profile.

**Hardware conditions:** requested full GPU placement -ngl 99; q8_0 K/V; one heavy CUDA workload at a time; --no-cache-prompt; --no-mmproj

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv` |
| Model | Qwen3.6-35B-A3B |
| Producer | Alibaba Qwen team |
| Official model | Qwen/Qwen3.6-35B-A3B @ `995ad96eacd98c81ed38be0c5b274b04031597b0` |
| Tested artifact | UD-IQ2_M local GGUF; SHA-256 verified |
| Precision | UD-IQ2_M |
| Artifact SHA-256 | `2be7ef1ed7e1af8b10d3829102cf9a6c2bd5ddb64d675b4ece23a60799403d43` |
| Campaign | `qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15` |
| Record date | 2026-09-15 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp 0.1.0-dev build 10449 (0d9ceae1e), CUDA |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | requested full GPU placement -ngl 99; q8_0 K/V; one heavy CUDA workload at a time; --no-cache-prompt; --no-mmproj |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 16384 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT on this RTX 5070 12GB/current q8_0-KV text profile: measured ~12.9 KiB/token KV growth and frozen 512 MiB reserve exceed available VRAM; nearest measured validated boundary is 32,768. This is profile/hardware scoped, not a universal model limit. |

<p><small>8K, 16K, and 32K are VALIDATED. Canonical measured maximum 32K is tight-fit only (about 433 MiB remaining after near-full request; no concurrent GPU workload). Two required 32K seeds pass useful-context depths 2/25/50/75/95%, with 31,961-31,964 usable tokens (99.48-99.49%). Official static-YaRN 1,010,000 is FIT_LIMIT on this hardware/profile.</small></p>

</details>

<a id="qwen36-35b-practical-v071-2026-07-22"></a>

### 2026-07-22: LLMGauge v0.71 practical re-run

**Benchmark Only: tool-version re-run** · config llama.cpp · RTX 5070 · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (TOOL_VERSION_RERUN)

Configuration: llama.cpp Unsloth UD-IQ2_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)


Same artifact/suite re-run under LLMGauge v0.71 for tool-version continuity.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`: llama.cpp Unsloth UD-IQ2_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="qwen36-35b-fit-ladder-e2e-2026-07-15"></a>

### 2026-07-15: Fit-ladder E2E (LLMGauge feature validation)

**Specialized Test: fit ladder** · config llama.cpp · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

Configuration: llama.cpp Unsloth UD-IQ2_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-fit-ladder-e2e-2026-07-15/REPORT.md)


Fit-ladder E2E (32k/16k/8k attempts) used Qwen3.6-35B-A3B UD-IQ2_M as payload; primary subject is LLMGauge behavior.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`: llama.cpp Unsloth UD-IQ2_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

## Limitations

- reliability 9/20 at seed 42 and 9/20 at seed 314159 Source events: [2026-09-15](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15).
- Git safety 0/1 at both seeds Source events: [2026-09-15](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15).
- substantive factual errors, hallucination-related failures, sycophancy and uncertainty weaknesses, plus repeated length truncation constrain use to LIMITED_ROLE_ONLY Source events: [2026-09-15](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15).
- official model is multimodal but this --no-mmproj text profile is SUPPORTED_NOT_CHARACTERIZED for vision Source events: [2026-09-15](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| UD-IQ2_M · llama.cpp · RTX 5070 | UD-IQ2_M | llama.cpp | RTX 5070 | 32,768 default / 16,384 guarded | 1 (2026-09-15) |
| llama.cpp · RTX 5070 | not recorded | llama.cpp | RTX 5070 | not recorded | 2 (2026-07-15, 2026-07-22) |

<details class="lab-findings-configs">
<summary>Configuration details: UD-IQ2_M · llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile).
- Profile identity: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU llama.cpp CUDA text-generation serving on RTX 5070 12GB: -ngl 99, -c 32768, -np 1, q8_0 K/V, batch 256/64, --no-cache-prompt, reasoning off, --no-mmproj, --jinja
- Artifact (as recorded): Qwen3.6-35B-A3B-UD-IQ2_M.gguf (11,522,702,304-byte UD-IQ2_M; sha256 2be7ef1ed7e1af8b10d3829102cf9a6c2bd5ddb64d675b4ece23a60799403d43)
- Runtime (as recorded): llama.cpp 0.1.0-dev build 10449 (0d9ceae1e), CUDA.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv/profile.json)

Events on this configuration:

- [Current-WELP recharacterization (2026-09-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15); status: LIMITED_ROLE_ONLY

</details>

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp Unsloth UD-IQ2_M.
- Profile identity: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`.
- Status: historical tested surface; retained evidence, not the recommended profile.
- Artifact (as recorded): unsloth Qwen3.6-35B-A3B UD-IQ2_M GGUF (11,522,702,304-byte fingerprint)
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/profile.json)

Events on this configuration:

- [LLMGauge v0.71 practical re-run (2026-07-22)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-practical-v071-2026-07-22); status: BENCHMARK_ONLY (TOOL_VERSION_RERUN)
- [Fit-ladder E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-fit-ladder-e2e-2026-07-15); status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-15 | [Current-WELP recharacterization](#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15) | UD-IQ2_M · llama.cpp · RTX 5070 | LIMITED_ROLE_ONLY |
| 2026-07-22 | [LLMGauge v0.71 practical re-run](#qwen36-35b-practical-v071-2026-07-22) | llama.cpp · RTX 5070 | BENCHMARK_ONLY (TOOL_VERSION_RERUN) |
| 2026-07-15 | [Fit-ladder E2E (LLMGauge feature validation)](#qwen36-35b-fit-ladder-e2e-2026-07-15) | llama.cpp · RTX 5070 | SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3.6-35b-a3b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-15 WELP Recharacterization: llama.cpp UD-IQ2_M q8_0 KV</summary>

- Campaign: `qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15`
- Export disposition: WEBSITE_READY; publication date 2026-09-15
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md`
- Export identity: event_date `2026-09-15`, event_id `qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15`, event_type `current-welp-recharacterization`, evidence_scope `['host-preflight', 'identity', 'artifact-provenance', 'performance', 'quality', 'capabilities', 'reliability', 'context', 'useful-context']`, model_id `qwen3.6-35b-a3b`, profile_id `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `3e9292e40ce307e58219d0b962f4c9a9360a73cd` path models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/website-publication.json sha256 `fd1553a960b207f9ccee8d80e0bb6b116c3af6331dd590acfda08896737e7d30`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; historical profile/events retained and no eval-* repository created.</small></p>

</details>

### Legacy provenance

- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-fit-ladder-e2e-2026-07-15.md)
- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-practical-v071-2026-07.md)

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04): UD-IQ2_M scored 233.9/300 (3.9 avg); tight 12GB fit (676 MiB minimum headroom). [Canonical evidence / full report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
