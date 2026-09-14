+++
title = "Qwen3-14B"
description = "Qwen3-14B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 13

[extra]
kind = "model"
model_id = "qwen3-14b"
vendor = "Alibaba (Qwen team)"
recommended_profile_id = "qwen3-14b-ollama-q4km-wumbo"
recommended_profile_name = "Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver)"
profile_count = 2
event_count = 3
latest_event_date = 2026-07-15
+++

WumboLabs tests **Qwen3-14B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver) (`qwen3-14b-ollama-q4km-wumbo`, historical) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)
- **Latest evidence:** 2026-07-15 — Fit-ladder success-fallback E2E (LLMGauge feature validation)

## Tested profiles

### llama.cpp Q4_K_M (unsloth) — CURRENT

Profile identity: `qwen3-14b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km/profile.json)

Events on this profile:

- [Fit-ladder success-fallback E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-14b#qwen3-14b-fit-ladder-2026-07-15) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION
- [LMX speed run (2026-07-05)](/evaluations/qwen3-14b#qwen3-14b-lmx-speed-2026-07-05) — BENCHMARK_ONLY (LMX local speed)

### Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver) — HISTORICAL

Profile identity: `qwen3-14b-ollama-q4km-wumbo`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b/profiles/qwen3-14b-ollama-q4km-wumbo/profile.json)

Events on this profile:

- [Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag) (2026-05-07)](/evaluations/qwen3-14b#qwen3-14b-wumbo-daily-evaluation-2026-05-07) — PRACTICAL_USE / PRE_WELP_HISTORICAL

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen3-14b-fit-ladder-2026-07-15"></a>

### 2026-07-15 — Fit-ladder success-fallback E2E (LLMGauge feature validation)

**Specialized Test — fit ladder** · profile: llama.cpp Q4_K_M (unsloth) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b)

### Identity and scope

- Profile: `qwen3-14b-llamacpp-q4km` — llama.cpp Q4_K_M (unsloth)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge fit-ladder feature E2E used Qwen3-14B Q4_K_M as payload (32k -> 8k fallback). Primary subject: LLMGauge feature behavior; retained as model-adjacent evidence.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen3-14b-lmx-speed-2026-07-05"></a>

### 2026-07-05 — LMX speed run

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M (unsloth) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-lmx-speed-2026-07-05/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b)

### Identity and scope

- Profile: `qwen3-14b-llamacpp-q4km` — llama.cpp Q4_K_M (unsloth)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: 66.57 tok/s out (llama.cpp Q4_K_M). Archaeology retention review separately records 63.74 tok/s full-CUDA-offload in the May-era recorded benchmark.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen3-14b-wumbo-daily-evaluation-2026-05-07"></a>

### 2026-05-07 — Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag)

**Practical Use — historical daily driver** · profile: Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / PRE_WELP_HISTORICAL

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b)

### Identity and scope

- Profile: `qwen3-14b-ollama-q4km-wumbo` — Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Historical May 2026 Ollama-era evaluation of the custom qwen3-14b-wumbo tag: 'Good enough for daily local technical assistant use'; strengths in Docker/systemd/Arch tooling with mandatory command review; 4096-context guidance. Pre-WELP practical-use evidence, not a WELP verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — Q4_K_M scored 228.4/300 (3.81 avg). — [Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen3-14b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km/profile.json)
- **qwen3-14b-ollama-q4km-wumbo**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/b58445a028ae7f8fffe444c3349de7928e57b01c/models/qwen3-14b/profiles/qwen3-14b-ollama-q4km-wumbo/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-fit-ladder-2026-07-15.md)
- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-lmx-speed-2026-07-05.md)
- [WumboLabs/eval-qwen3-14b-ollama-q4km @ `285d06529dab955e9458c646b72493843c8998f0`](https://github.com/WumboLabs/eval-qwen3-14b-ollama-q4km/blob/285d06529dab955e9458c646b72493843c8998f0/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07.md)
