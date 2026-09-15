+++
title = "Qwen3.6-35B-A3B"
description = "Qwen3.6-35B-A3B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 14

[extra]
kind = "model"
model_id = "qwen3.6-35b-a3b"
vendor = "Alibaba (Qwen team)"
recommended_profile_id = "qwen3.6-35b-a3b-llamacpp-ud-iq2-m"
recommended_profile_name = "llama.cpp Unsloth UD-IQ2_M"
profile_count = 1
event_count = 2
latest_event_date = 2026-07-22
+++

WumboLabs tests **Qwen3.6-35B-A3B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Unsloth UD-IQ2_M (`qwen3.6-35b-a3b-llamacpp-ud-iq2-m`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
- **Latest evidence:** 2026-07-22 — LLMGauge v0.71 practical re-run

## Tested profiles

### llama.cpp Unsloth UD-IQ2_M — CURRENT

Profile identity: `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/profile.json)

Events on this profile:

- [LLMGauge v0.71 practical re-run (2026-07-22)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-practical-v071-2026-07-22) — BENCHMARK_ONLY (TOOL_VERSION_RERUN)
- [Fit-ladder E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-6-35b-a3b#qwen36-35b-fit-ladder-e2e-2026-07-15) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen36-35b-practical-v071-2026-07-22"></a>

### 2026-07-22 — LLMGauge v0.71 practical re-run

**Benchmark Only — tool-version re-run** · profile: llama.cpp Unsloth UD-IQ2_M · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (TOOL_VERSION_RERUN)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.6-35b-a3b/events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/qwen3.6-35b-a3b)

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
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/qwen3.6-35b-a3b)

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

- **qwen3.6-35b-a3b-llamacpp-ud-iq2-m**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/qwen3.6-35b-a3b/profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-fit-ladder-e2e-2026-07-15.md)
- [WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m @ `d89df9bc26227247b858033742048bc6ccede901`](https://github.com/WumboLabs/eval-qwen3.6-35b-a3b-ud-iq2-m/blob/d89df9bc26227247b858033742048bc6ccede901/events/qwen36-35b-practical-v071-2026-07.md)
