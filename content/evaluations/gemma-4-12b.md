+++
title = "Gemma 4 12B IT"
description = "Gemma 4 12B IT — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 11

[extra]
kind = "model"
model_id = "gemma-4-12b"
vendor = "Google"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "gemma-4-12b-llamacpp-qat-q4-0"
recommended_profile_name = "llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 4
event_count = 6
latest_event_date = 2026-09-12
+++

WumboLabs tests **Gemma 4 12B IT** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12), profile llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- **Recommended profile:** llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) (`gemma-4-12b-llamacpp-qat-q4-0`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12)
- **Latest evidence:** 2026-09-12 — Current-WELP recharacterization

## Tested profiles

### llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) — CURRENT

Profile identity: `gemma-4-12b-llamacpp-qat-q4-0`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Artifact | unsloth/gemma-4-12b-it-GGUF gemma-4-12b-it-UD-Q4_K_XL.gguf (re-acquired 2026-09-13T01:29:47Z after archive-gap repair authorization) |
| Precision | UD-Q4_K_XL (Unsloth Dynamic 2.0 over QAT Q4_0 lineage) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12) — READY_WITH_GUARDRAILS
- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [Honesty ladder smoke (QAT Q4) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-honesty-ladder-2026-06-21) — SPECIALIZED_TEST / UNSCORED_SMOKE
- [Early core-v1 + agent-backend-v1 scored runs (QAT Q4) (2026-06-16)](/evaluations/gemma-4-12b#gemma4-12b-core-agent-v016-2026-06-16) — BENCHMARK_ONLY

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-q4km/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-ud-q5-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) — SPECIALIZED

Profile identity: `gemma-4-12b-llamacpp-ud-q6-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12"></a>

### 2026-09-12 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp QAT UD-Q4_K_XL** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)

##### Identity

| Field | Value |
|---|---|
| Model | Gemma 4 12B IT |
| Producer | Google |
| Official model | google/gemma-4-12b-it-qat-q4_0-gguf @ `unsloth/gemma-4-12b-it-GGUF fc034cfff751157913579611efad8462ac1be606` |
| Tested artifact | unsloth/gemma-4-12b-it-GGUF gemma-4-12b-it-UD-Q4_K_XL.gguf (re-acquired 2026-09-13T01:29:47Z after archive-gap repair authorization) |
| Precision | UD-Q4_K_XL (Unsloth Dynamic 2.0 over QAT Q4_0 lineage) |
| Artifact SHA-256 | `90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e` |
| Campaign | `gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12` |
| Record date | 2026-09-12 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS — RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT — measured: one bounded admission attempt failed with CUDA OOM (compute buffer) and KV-slope accounting (17.4 KiB/token) proves the point cannot fit with required reserve on 12GB; nearest measured boundary 131,072 |

##### Quality and capabilities

- **Constrained result:** 12/12 frozen mechanical quality screen (frozen scorer, temp 0)
- reasoning (thinking ON) multi-hop syllogism PASS
- coding: generated function executes correctly (mechanical exec check)
- tool calling: valid call + grounded continuation PASS

###### Guardrails and limitations

- verbosity: 13-14/20 reliability outputs hit frozen token caps; raise max_tokens or disable thinking for terse duty
- git-safety advisory weakness (amending pushed commits framed as technically possible)
- uncertainty/sycophancy categories 1-2/3
- native 262,144 context is FIT_LIMIT on 12GB; guarded ceiling 131,072
- Multimodal lane (image/audio/video via mmproj) is SUPPORTED_NOT_CHARACTERIZED: this event characterizes the canonical text profile only; no model-wide multimodal claim is made

**Reliability:** Proven mechanical 20-task corpus, 2 seeds: 11/20 and 10/20 mechanical pass; evidence discipline (3/3, 2/3) and strict interfaces (3/3, 2/3) strong; hallucination 2/4 both seeds; failures concentrated in uncertainty/sycophancy/git-safety with a strong truncation component

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>local canonical-profile benchmark pp512 3201 tok/s / tg128 72.92 tok/s (5 reps); no exact existing service record (historical 2026-07-04 gemma4 LMX record is an unexecuted dry-run); submission requires separate human gate</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="gemma4-12b-practical-pool-v025-2026-07-04"></a>

### 2026-07-04 — 12B practical pool comparison v025 + Grug

**Practical Use — shared comparison (canonical)** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)

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

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)
[Profile Metadata: gemma-4-12b-llamacpp-qat-q4-0](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)
[Profile Metadata: gemma-4-12b-llamacpp-ud-q5-k-xl](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)
[Profile Metadata: gemma-4-12b-llamacpp-ud-q6-k-xl](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

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

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-06-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)

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

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-honesty-ladder-2026-06-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)

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

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-core-agent-v016-2026-06-16/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b)

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

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **gemma-4-12b-llamacpp-qat-q4-0**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)
- **gemma-4-12b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-q4km/profile.json)
- **gemma-4-12b-llamacpp-ud-q5-k-xl**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)
- **gemma-4-12b-llamacpp-ud-q6-k-xl**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/3b775bff3f9ccdb7dc9a1a2310ac1910c43e94aa/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

### Legacy provenance

- [WumboLabs/eval-gemma-4-12b-q4km @ `561be30e6f39eefb19fa36844904fb110c6a66a8`](https://github.com/WumboLabs/eval-gemma-4-12b-q4km/blob/561be30e6f39eefb19fa36844904fb110c6a66a8/events/gemma4-12b-lmx-speed-2026-07-04.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/events/gemma4-12b-core-agent-v016-2026-06-16.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/events/gemma4-12b-honesty-ladder-2026-06.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/reports/gemma4-12b-welp-recharacterization-2026-09-12.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/shared/compare-gemma4-family-wumbolabs-practical-v024-scored.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/shared/compare-wumbolabs-practical-v025-plus-grug.md)
