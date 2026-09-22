+++
title = "Qwen3.6-35B-A3B"
description = "Qwen3.6-35B-A3B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 4

[extra]
kind = "model"
model_id = "qwen3.6-35b-a3b"
vendor = "Alibaba (Qwen team)"
classification = "LIMITED_ROLE_ONLY"
recommended_profile_id = "qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv"
recommended_profile_name = "llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile)"
practical_context = "32,768 default / 16,384 guarded tokens"
profile_count = 2
event_count = 3
latest_evidence_date = 2026-09-15
+++

WumboLabs tests **Qwen3.6-35B-A3B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** LIMITED_ROLE_ONLY — [Current-WELP recharacterization (2026-09-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15), profile llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile)
- **Recommended profile:** llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile) (`qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
- **Practical context:** 32,768 default / 16,384 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Current-WELP recharacterization (2026-09-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15)
- **Latest evidence:** 2026-09-15 — Current-WELP recharacterization

## Tested profiles

### llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile) — CURRENT

Profile identity: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv`.

| Field | Value |
|---|---|
| Runtime | llama.cpp 0.1.0-dev build 10449 (0d9ceae1e), CUDA |
| Artifact | UD-IQ2_M local GGUF; SHA-256 verified |
| Precision | UD-IQ2_M |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15) — LIMITED_ROLE_ONLY

### llama.cpp Unsloth UD-IQ2_M — HISTORICAL

Profile identity: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/profile.json)

Events on this profile:

- [LLMGauge v0.71 practical re-run (2026-07-22)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-practical-v071-2026-07-22) — BENCHMARK_ONLY (TOOL_VERSION_RERUN)
- [Fit-ladder E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-fit-ladder-e2e-2026-07-15) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15"></a>

### 2026-09-15 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp UD-IQ2_M q8_0 KV** · profile: llama.cpp UD-IQ2_M q8_0 KV (32K text-generation profile) · maturity: CURRENT_WELP · status: LIMITED_ROLE_ONLY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3.6-35B-A3B |
| Producer | Alibaba Qwen team |
| Official model | Qwen/Qwen3.6-35B-A3B @ `995ad96eacd98c81ed38be0c5b274b04031597b0` |
| Tested artifact | UD-IQ2_M local GGUF; SHA-256 verified |
| Precision | UD-IQ2_M |
| Artifact SHA-256 | `2be7ef1ed7e1af8b10d3829102cf9a6c2bd5ddb64d675b4ece23a60799403d43` |
| Campaign | `qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15` |
| Record date | 2026-09-15 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build 10449 (0d9ceae1e), CUDA |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | requested full GPU placement -ngl 99; q8_0 K/V; one heavy CUDA workload at a time; --no-cache-prompt; --no-mmproj |

##### WELP outcome

- **Outcome:** PASS
- **Classification:** LIMITED_ROLE_ONLY

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 16384 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT on this RTX 5070 12GB/current q8_0-KV text profile: measured ~12.9 KiB/token KV growth and frozen 512 MiB reserve exceed available VRAM; nearest measured validated boundary is 32,768. This is profile/hardware scoped, not a universal model limit. |

##### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; sole miss was the lexical no-letter-e constraint.
- coding: PASS
- tool formatting: PASS
- reasoning: frozen 1,500-token probe did not finalize; a separate 4,096-token operational probe correctly completed 17 × 23 = 391 with coherent reasoning

###### Guardrails and limitations

- reliability 9/20 at seed 42 and 9/20 at seed 314159
- Git safety 0/1 at both seeds
- substantive factual errors, hallucination-related failures, sycophancy and uncertainty weaknesses, plus repeated length truncation constrain use to LIMITED_ROLE_ONLY
- official model is multimodal but this --no-mmproj text profile is SUPPORTED_NOT_CHARACTERIZED for vision

**Reliability:** Strict interfaces 3/3 at both seeds; the replicated 9/20 reliability result is classification-determining. Reasoning is operational with sufficient output budget, not an unconditional frozen-cap PASS.

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>local canonical-profile benchmark pp512 3571.96 ± 151.06 tok/s / tg128 157.62 ± 0.43 tok/s; no external submission or fabricated verification fields; service mutation requires separate authorization.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/7009751ff83088b435eba61730e94b511f1103c4/models/qwen3.6-35b-a3b/events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen36-35b-practical-v071-2026-07-22"></a>

### 2026-07-22 — LLMGauge v0.71 practical re-run

**Benchmark Only — tool-version re-run** · profile: llama.cpp Unsloth UD-IQ2_M · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (TOOL_VERSION_RERUN)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b)

### Identity and scope

- Profile: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m` — llama.cpp Unsloth UD-IQ2_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Same artifact/suite re-run under LLMGauge v0.71 for tool-version continuity.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen36-35b-fit-ladder-e2e-2026-07-15"></a>

### 2026-07-15 — Fit-ladder E2E (LLMGauge feature validation)

**Specialized Test — fit ladder** · profile: llama.cpp Unsloth UD-IQ2_M · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-fit-ladder-e2e-2026-07-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b)

### Identity and scope

- Profile: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m` — llama.cpp Unsloth UD-IQ2_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

Fit-ladder E2E (32k/16k/8k attempts) used Qwen3.6-35B-A3B UD-IQ2_M as payload; primary subject is LLMGauge behavior.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — UD-IQ2_M scored 233.9/300 (3.9 avg); tight 12GB fit (676 MiB minimum headroom). — [Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv/profile.json)
- **qwen3.6-35b-a3b-llamacpp-ud-iq2-m**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-fit-ladder-e2e-2026-07-15.md)
- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-practical-v071-2026-07.md)
