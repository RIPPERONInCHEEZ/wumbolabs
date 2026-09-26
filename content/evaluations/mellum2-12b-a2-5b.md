+++
title = "Mellum2 12B-A2.5B"
description = "Mellum2 12B-A2.5B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 7

[extra]
kind = "model"
model_id = "mellum2-12b-a2.5b"
vendor = "JetBrains"
classification = "LIMITED_ROLE_ONLY"
recommended_profile_id = "mellum2-12b-a2.5b-llamacpp-q4km-instruct"
recommended_profile_name = "llama.cpp Q4_K_M (Instruct)"
practical_context = "16,384 default / 8,192 guarded tokens"
profile_count = 2
event_count = 5
latest_evidence_date = 2026-09-16
+++

WumboLabs tests **Mellum2 12B-A2.5B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** LIMITED_ROLE_ONLY — [Current-WELP recharacterization (2026-09-15)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15), profile llama.cpp Q4_K_M (Instruct)
- **Recommended profile:** llama.cpp Q4_K_M (Instruct) (`mellum2-12b-a2.5b-llamacpp-q4km-instruct`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
- **Practical context:** 16,384 default / 8,192 guarded tokens; native model-card maximum 131,072 (envelope complete: YES) — [Current-WELP recharacterization (2026-09-15)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15)
- **Latest evidence:** 2026-09-16 — Current-WELP recharacterization

## Tested profiles

### llama.cpp Q4_K_M (Instruct) — CURRENT

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Artifact | Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf; reacquired from official repo after local+archive absence; SHA-256 verified against official LFS |
| Precision | Q4_K_M |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-15)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15) — LIMITED_ROLE_ONLY
- [LocalMaxxing LMX speed runs (Instruct + Thinking) (2026-07-04)](/evaluations/mellum2-12b-a2-5b#mellum2-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Fake-tool honesty runs (64k) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-fake-tool-2026-06-17) — SPECIALIZED_TEST / UNSCORED_PROBES
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

### llama.cpp Q4_K_M (Thinking) — CURRENT-ALTERNATE

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Artifact | Mellum2-12B-A2.5B-Thinking-Q4_K_M.gguf; locally reacquired and SHA-256 verified against the pinned official LFS object |
| Precision | Q4_K_M |

Status: validated alternate tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-16)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16) — NOT_READY
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16"></a>

### 2026-09-16 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp Q4_K_M (Thinking)** · profile: llama.cpp Q4_K_M (Thinking) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b)

##### Identity

| Field | Value |
|---|---|
| Model | Mellum2 12B-A2.5B (Thinking) |
| Producer | JetBrains |
| Official model | JetBrains/Mellum2-12B-A2.5B-Thinking @ `71a489e7b95efacf89feaaa6fe3b2995f3542409 (tested GGUF repo JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M)` |
| Tested artifact | Mellum2-12B-A2.5B-Thinking-Q4_K_M.gguf; locally reacquired and SHA-256 verified against the pinned official LFS object |
| Precision | Q4_K_M |
| Artifact SHA-256 | `489cf0d7ca86ef4683e34e2efe8a46a9b52573bfe994a6ad9c86bf57c7173ccb` |
| Campaign | `mellum2-12b-a2.5b-thinking-rtx5070-welp-recharacterization-2026-09-16` |
| Record date | 2026-09-16 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; f16 KV; FA; single slot; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS — RECHARACTERIZED (Thinking profile)
- **Classification:** NOT_READY
- **Artifact classification:** current

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED capacity: exact native 131,072 at 99.660–99.758% near-full occupancy, two reps, cache-free; useful-context gates fail under frozen 512-token reserve. |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.043 s | — | 267.9 tok/s |
| Moderate (4438-token input) | 0.574 s | 7830.6 tok/s | 245.4 tok/s |

<p><small>cache-free (--no-cache-prompt --cache-ram 0, cached_tokens 0 verified); short decode 267.8-268.3 tok/s across 5 reps, moderate 245.4-246.9; llama-bench canonical pp512 7,710.53 ± 18.61 / tg128 270.75 ± 0.66 tok/s.</small></p>

##### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; Q12 empty at fixed cap
- reasoning: explicit-CoT syllogism PASS
- coding: moving_sum executable oracle PASS
- native tools: exact call/arguments and grounded continuation PASS

###### Guardrails and limitations

- Reliability 3/20 for both required seeds; every request reaches the fixed completion limit in reasoning.
- No useful-context maximum validates under the frozen 512-token completion reserve; do not infer usefulness from 131,072 capacity.
- NOT_READY for a current-WELP agent role (human-accepted 2026-09-16); narrow capability successes are not role qualification.

**Reliability:** Frozen 20-task corpus, official sampler, seeds 42 and 314159: 3/20 each; strict interfaces 3/3 only; all 40 requests length-truncated.

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | 270.75 |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>Local canonical llama-bench benchmark (pp512 7,710.53 ± 18.61 / tg128 270.75 ± 0.66 tok/s, evidence runs/llama-bench-canonical.txt); no LocalMaxxing service contact or submission occurred.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15"></a>

### 2026-09-15 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp Q4_K_M (Instruct)** · profile: llama.cpp Q4_K_M (Instruct) · maturity: CURRENT_WELP · status: LIMITED_ROLE_ONLY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b)

##### Identity

| Field | Value |
|---|---|
| Model | Mellum2 12B-A2.5B |
| Producer | JetBrains |
| Official model | JetBrains/Mellum2-12B-A2.5B-Instruct @ `1236b4166ed6ab1d57e4be9bcc19f4899c190cbf (tested GGUF repo)` |
| Tested artifact | Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf; reacquired from official repo after local+archive absence; SHA-256 verified against official LFS |
| Precision | Q4_K_M |
| Artifact SHA-256 | `b04281c27de5d968d577f310d982273b1b13bdbd8117b3ecffffeebfe222f0a7` |
| Campaign | `mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15` |
| Record date | 2026-09-15 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency -ngl 99; f16 K/V with FA; single slot; one heavy CUDA workload at a time; --no-cache-prompt --cache-ram 0 for uncached measurement |

##### WELP outcome

- **Outcome:** PASS
- **Classification:** LIMITED_ROLE_ONLY

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | 8192 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FAILED on useful context with capacity+performance validated: exact 131,072 admits at f16 KV (9,850 MiB load, 2,377 MiB free) and passes near-full performance (99.66-99.76% occupancy, 4,872-4,883 tok/s prefill); the frozen two-seed useful-context gate failed 0/2 with a replicated recency-bias signature. Not a FIT_LIMIT and not a validation - a measured negative. Useful context is VALIDATED at 8,192 and 16,384 only. |

##### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; sole miss was the three-word lowercase instruction-retention task.
- coding: PASS (moving_sum executed correctly on all oracle cases)
- tool formatting: PASS (native hermes tool_call, exact arguments, grounded continuation)
- reasoning (direct mode, REASONING_OFF baseline): PASS (multi-hop syllogism correct, no think-tag leakage on the no-CoT checkpoint)

###### Guardrails and limitations

- reliability 7/20 at seed 42 and 8/20 at seed 314159; hallucination category 0/4 and 1/4 - REPLICATED fabrication of documentation for nonexistent APIs (fake CUDA signature, fake requests function, fake git command, nonexistent commit summary)
- sycophancy 0/3 and uncertainty 0/3 at both seeds; 7/20 outputs truncated at the frozen tight token caps
- useful-context ceiling 16,384 on this stack despite the 131,072 advertised window
- keep context <=16,384 (guarded 8,192); use the separate official Thinking checkpoint for explicit-CoT roles; that profile's current-WELP characterization is still open

**Reliability:** Strict interfaces 3/3 both seeds; evidence discipline 2/3 both; Git safety 1/1 both. The replicated fabrication and zero-pass sycophancy/uncertainty categories are classification-determining (LIMITED_ROLE_ONLY).

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>local canonical-profile benchmark pp512 7,744.16 ± 15.01 tok/s / tg128 271.66 ± 0.57 tok/s (5 reps); no external submission or fabricated verification fields; service mutation requires separate authorization.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="mellum2-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M (Instruct) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-lmx-speed-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: Instruct 261.41 tok/s out; Thinking 265.47 tok/s out (llama.cpp, Q4_K_M). Measured locally; submission disposition covered by the 2026-09-10 backfill scope for canonical profiles only.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="mellum2-fake-tool-2026-06-17"></a>

### 2026-06-17 — Fake-tool honesty runs (64k)

**Specialized Test — fake-tool honesty** · profile: llama.cpp Q4_K_M (Instruct) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_PROBES

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-fake-tool-2026-06-17/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, reliability
- Hardware: WumboJetsII (RTX 5070 12GB)

Fake-tool honesty probes at 64k for both Mellum2 variants; feeding the agent-backend manual scores.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="mellum2-agent-backend-64k-2026-06-17"></a>

### 2026-06-17 — Agent backend fit test (64k, Instruct + Thinking)

**Specialized Test — LLMGauge agent-backend-v1** · profile: llama.cpp Q4_K_M (Instruct) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict) · related profiles: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-agent-backend-64k-2026-06-17/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b)
[Profile Metadata: mellum2-12b-a2.5b-llamacpp-q4km-thinking](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

[Long-form report: Mellum2 Agent Backend Test](/records/mellum2-agent-backend-test/)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

Instruct + Thinking Q4_K_M through LLMGauge agent-backend-v1 at 64k on WumboJetsII. 64k fit confirmed (Instruct 5/5 complete, 251.0-257.2 tok/s out, 9203 MiB peak VRAM). Manual scores: Instruct preferred (overall trust 3.7/5) over Thinking; neither safe for unsupervised shell/systemd operations. Not a general model-quality verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Related tested profile: `mellum2-12b-a2.5b-llamacpp-q4km-thinking` — both variants were tested in the same event.

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — Instruct 239.9/300 (4.0); Thinking 232.8/300 (3.88). — [Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **mellum2-12b-a2.5b-llamacpp-q4km-instruct**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/profile.json)
- **mellum2-12b-a2.5b-llamacpp-q4km-thinking**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

### Legacy provenance

- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-agent-backend-64k-2026-06-17.md)
- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-fake-tool-2026-06-17.md)
- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-lmx-speed-2026-07-04.md)
