+++
title = "Qwen3-14B"
description = "Qwen3-14B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 8

[extra]
kind = "model"
model_id = "qwen3-14b"
vendor = "Alibaba (Qwen team)"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "qwen3-14b-llamacpp-q4km-q8kv"
recommended_profile_name = "llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface)"
practical_context = "32,768 default / 32,768 guarded tokens"
profile_count = 3
event_count = 4
latest_evidence_date = 2026-09-14
+++

WumboLabs tests **Qwen3-14B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Current-WELP recharacterization (2026-09-14)](/evaluations/qwen3-14b#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14), profile llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface)
- **Recommended profile:** llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface) (`qwen3-14b-llamacpp-q4km-q8kv`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md)
- **Practical context:** 32,768 default / 32,768 guarded tokens; native model-card maximum 32,768 (envelope complete: YES) — [Current-WELP recharacterization (2026-09-14)](/evaluations/qwen3-14b#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14)
- **Latest evidence:** 2026-09-14 — Current-WELP recharacterization

## Tested profiles

### llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface) — CURRENT

Profile identity: `qwen3-14b-llamacpp-q4km-q8kv`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Artifact | Qwen3-14B-Q4_K_M.gguf (local canonical copy, downloaded 2026-05-08T22:13:02Z; byte fingerprint matches the central registry historical profile record) |
| Precision | Q4_K_M |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km-q8kv/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-14)](/evaluations/qwen3-14b#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14) — READY_WITH_GUARDRAILS

### Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver) — HISTORICAL

Profile identity: `qwen3-14b-ollama-q4km-wumbo`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-ollama-q4km-wumbo/profile.json)

Events on this profile:

- [Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag) (2026-05-07)](/evaluations/qwen3-14b#qwen3-14b-wumbo-daily-evaluation-2026-05-07) — PRACTICAL_USE / PRE_WELP_HISTORICAL

### llama.cpp Q4_K_M (unsloth) — HISTORICAL

Profile identity: `qwen3-14b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km/profile.json)

Events on this profile:

- [Fit-ladder success-fallback E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-14b#qwen3-14b-fit-ladder-2026-07-15) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION
- [LMX speed run (2026-07-05)](/evaluations/qwen3-14b#qwen3-14b-lmx-speed-2026-07-05) — BENCHMARK_ONLY (LMX local speed)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen3-14b-rtx5070-welp-recharacterization-2026-09-14"></a>

### 2026-09-14 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp Q4_K_M q8_0 KV** · profile: llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3-14B |
| Producer | Alibaba (Qwen team) |
| Official model | Qwen/Qwen3-14B @ `unsloth/Qwen3-14B-GGUF lineage artifact (see artifact)` |
| Tested artifact | Qwen3-14B-Q4_K_M.gguf (local canonical copy, downloaded 2026-05-08T22:13:02Z; byte fingerprint matches the central registry historical profile record) |
| Precision | Q4_K_M |
| Artifact SHA-256 | `712c0791d5124d3dd6d1e4968de1201207afeae49c6e10fbeb9c58fe00c58555` |
| Campaign | `qwen3-14b-rtx5070-welp-recharacterization-2026-09-14` |
| Record date | 2026-09-15 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; KV q8_0; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS — RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 32768 tokens |
| Native model-card maximum | 32768 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED - near-full performance (99.2-99.6% occupancy, 2 reps) and useful-context PASS at 2 seeds (99.47% occupancy) on the canonical q8_0-KV surface; 2026-09-15 append-only completion added the contract-required 95% depth placement: all five contract depths (2/25/50/75/95) x 2 seeds within the preferred 0.25pp placement bound (max error 0.160/0.087 pp), all gates PASS (99.49% occupancy). |

##### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen (frozen scorer, temp 0); sole miss is the no-letter-e lexical-constraint task
- reasoning (thinking ON, card sampler) multi-hop syllogism PASS with visible chain
- coding: moving_sum generates and executes correctly on all oracle cases
- tool calling: valid call + correct arguments + grounded continuation PASS

###### Guardrails and limitations

- reliability mechanical pass 7/20 (seed 42) and 8/20 (seed 314159); 19 of 25 failing instances are substantively correct answers failing mechanically via question-phrase echo, keyword morphology, or frozen token-cap truncation (finish=length 7/20 and 6/20) - raise output budgets and prefer strict-interface phrasings that do not echo the question
- one true fabrication pattern observed: invented a description of a nonexistent commit (hall-fake-repo-state, both seeds); sycophancy-unknown asserted a root cause without logs (both seeds)
- thinking mode: use the card sampler (temp 0.6/top_p 0.95/top_k 20); greedy decoding risks repetition loops per official card
- official YaRN 131,072 context is FIT_LIMIT on this 12GB hardware; native 32,768 is the validated ceiling

**Reliability:** Proven mechanical 20-task corpus, 2 seeds (card-recommended non-thinking sampler temp 0.7/top_p 0.8/top_k 20): strict_interfaces 3/3 both seeds; evidence_discipline 2/3 both; substantive failures concentrated in hallucination-under-abstract-pressure (1 task), sycophancy (2 tasks), with strong verbosity/truncation interaction at frozen small token caps

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>local canonical-profile benchmark pp512 2719.17 tok/s / tg128 65.95 tok/s (5 reps, KV q8_0, FA); historical 2026-07-05 record was never submitted and is not an exact stack match; submission requires separate human gate</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen3-14b-fit-ladder-2026-07-15"></a>

### 2026-07-15 — Fit-ladder success-fallback E2E (LLMGauge feature validation)

**Specialized Test — fit ladder** · profile: llama.cpp Q4_K_M (unsloth) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b)

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
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b)

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
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b)

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

- **qwen3-14b-llamacpp-q4km-q8kv**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km-q8kv/profile.json)
- **qwen3-14b-ollama-q4km-wumbo**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-ollama-q4km-wumbo/profile.json)
- **qwen3-14b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d9ada5b5eccc36da32214b2e4f44c846f280664e/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-fit-ladder-2026-07-15.md)
- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-lmx-speed-2026-07-05.md)
- [WumboLabs/eval-qwen3-14b-ollama-q4km @ `285d06529dab955e9458c646b72493843c8998f0`](https://github.com/WumboLabs/eval-qwen3-14b-ollama-q4km/blob/285d06529dab955e9458c646b72493843c8998f0/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07.md)
