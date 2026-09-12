+++
title = "Gemma 4 12B IT"
description = "Gemma 4 12B IT — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 11

[extra]
kind = "model"
model_id = "gemma-4-12b"
vendor = "Google"
recommended_profile_id = "gemma-4-12b-llamacpp-qat-q4-0"
recommended_profile_name = "llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)"
profile_count = 4
event_count = 5
latest_event_date = 2026-07-04
+++

WumboLabs tests **Gemma 4 12B IT** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) (`gemma-4-12b-llamacpp-qat-q4-0`, current) — [canonical evidence](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4)
- **Latest evidence:** 2026-07-04 — 12B practical pool comparison v025 + Grug

## Tested profiles

### llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) — CURRENT

Profile identity: `gemma-4-12b-llamacpp-qat-q4-0`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4>

Events on this profile:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [Honesty ladder smoke (QAT Q4) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-honesty-ladder-2026-06-21) — SPECIALIZED_TEST / UNSCORED_SMOKE
- [Early core-v1 + agent-backend-v1 scored runs (QAT Q4) (2026-06-16)](/evaluations/gemma-4-12b#gemma4-12b-core-agent-v016-2026-06-16) — BENCHMARK_ONLY

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-gemma-4-12b-q4km>

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-ud-q5-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-gemma-4-12b-q4km>

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-ud-q6-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-gemma-4-12b-q4km>

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="gemma4-12b-practical-pool-v025-2026-07-04"></a>

### 2026-07-04 — 12B practical pool comparison v025 + Grug

**Practical Use — shared comparison (canonical)** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0` — llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Second shared multi-model practical-use comparison: the incumbent QAT Q4 practical default (259.2/300 from the v024 suite) against five additional tested models on wumbolabs-practical-use-v1 at 8k — Grug-12B 243.6, Mellum2 Instruct 239.9, Mellum2 Thinking 232.8, Qwen3.6-35B-A3B 233.9, Qwen3-14B 228.4 (all /300 manual practical scores). One immutable shared report; each related model page lists this event with its own score.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Shared comparison: `practical-use-comparison-2026-07-04` — one immutable shared report; related model pages list
this event with their own measured entries.

<a id="gemma4-12b-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LMX speed runs across four Gemma 4 12B quants

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M (ggml-org) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed) · related profiles: `gemma-4-12b-llamacpp-qat-q4-0`, `gemma-4-12b-llamacpp-ud-q5-k-xl`, `gemma-4-12b-llamacpp-ud-q6-k-xl`

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemma-4-12b-q4km)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-q4km` — llama.cpp Q4_K_M (ggml-org)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: Q4_K_M 72.11, UD-Q5_K_XL 62.76, UD-Q6_K_XL 51.26 tok/s out (llama.cpp). Archaeology additionally cites Q8_0 test and NVFP4 conversion-attempt records (weights since removed).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="gemma4-12b-practical-use-family-2026-06-21"></a>

### 2026-06-21 — 12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)

**Practical Use — LLMGauge wumbolabs-practical-use-v1** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4)

[Long-form report: 12B Gemma-Based Practical Use Test](/records/gemma-12b-practical-use/)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0` — llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite — that model carries its own Evaluation page.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Shared comparison: `practical-use-comparison-2026-06-21` — one immutable shared report; related model pages list
this event with their own measured entries.

<a id="gemma4-12b-honesty-ladder-2026-06-21"></a>

### 2026-06-21 — Honesty ladder smoke (QAT Q4)

**Specialized Test — honesty ladder** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_SMOKE

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0` — llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, reliability
- Hardware: WumboJetsII (RTX 5070 12GB)

Honesty-ladder smoke runs against the QAT Q4 practical profile.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="gemma4-12b-core-agent-v016-2026-06-16"></a>

### 2026-06-16 — Early core-v1 + agent-backend-v1 scored runs (QAT Q4)

**Benchmark Only — LLMGauge v0.16 era** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0` — llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, capabilities
- Hardware: WumboJetsII (RTX 5070 12GB)

QAT Q4 completed core-v1 (8/8, manual score 308/400) and agent-backend-v1 (2048 ctx) during LLMGauge v0.16 validation.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)** (`gemma-4-12b-llamacpp-qat-q4-0`): <https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4>
- **llama.cpp Q4_K_M (ggml-org)** (`gemma-4-12b-llamacpp-q4km`): <https://github.com/WumboLabs/eval-gemma-4-12b-q4km>
