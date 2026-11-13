+++
title = "Mellum2 12B-A2.5B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 10

[extra]
kind = "model"
model_id = "mellum2-12b-a2.5b"
vendor = "JetBrains"
findings_first = true
classification = "LIMITED_ROLE_ONLY"
recommended_profile_id = "mellum2-12b-a2.5b-llamacpp-q4km-instruct"
recommended_profile_name = "llama.cpp Q4_K_M (Instruct)"
practical_context = "16,384 default / 8,192 guarded tokens"
profile_count = 2
event_count = 5
latest_evidence_date = 2026-09-16
+++

## Overview

JetBrains · 2 tested configurations · 5 evidence events · newest evidence 2026-09-16.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: LIMITED_ROLE_ONLY** - attributed to the [2026-09-15 event](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15), configuration Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact).
- **Recommended configuration:** llama.cpp Q4_K_M (Instruct) (current): [event result](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15).
- **Practical context:** 16,384 default / 8,192 guarded tokens; native model-card maximum 131,072 (envelope complete: YES); source: [event result](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15)
- **Context limit outcome:** FAILED on useful context with capacity+performance validated: exact 131,072 admits at f16 KV (9,850 MiB load, 2,377 MiB free) and passes near-full performance (99.66-99.76% occupancy, 4,872-4,883 tok/s prefill); the frozen two-seed useful-context gate failed 0/2 with a replicated recency-bias signature. Not a FIT_LIMIT and not a validation - a measured negative. Useful context is VALIDATED at 8,192 and 16,384 only.; source: [event result](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15)
- **Latest evidence:** 2026-09-16: [event result](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16)
- **2026-09-16** · Q4_K_M · llama.cpp b9672 · RTX 5070 · reasoning_content emitted by the native template): classification NOT_READY; 11/12 frozen mechanical quality screen; Q12 empty at fixed cap. [Event result](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16)
- **2026-09-15** · Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact): classification LIMITED_ROLE_ONLY; 11/12 frozen mechanical quality screen; sole miss was the three-word lowercase instruction-retention task. [Event result](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15)
- **2026-07-04** · Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact): classification BENCHMARK_ONLY (LMX local speed). [Event result](#mellum2-lmx-speed-2026-07-04)
- **2026-06-17** · Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact): classification SPECIALIZED_TEST / UNSCORED_PROBES. [Event result](#mellum2-fake-tool-2026-06-17)
- **2026-06-17** · Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact): classification SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict). [Event result](#mellum2-agent-backend-64k-2026-06-17)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16"></a>

### 2026-09-16: Current-WELP recharacterization

**WELP Recharacterization: llama.cpp Q4_K_M (Thinking)** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · reasoning_content emitted by the native template) · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp Q4_K_M (Thinking).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md)

#### WELP outcome

- **Outcome:** PASS: RECHARACTERIZED (Thinking profile)
- **Classification:** NOT_READY
- **Artifact classification:** current

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.043 s | Not recorded | 267.9 tok/s |
| Moderate (4438-token input) | 0.574 s | 7830.6 tok/s | 245.4 tok/s |

<p><small>cache-free (--no-cache-prompt --cache-ram 0, cached_tokens 0 verified); short decode 267.8-268.3 tok/s across 5 reps, moderate 245.4-246.9; llama-bench canonical pp512 7,710.53 ± 18.61 / tg128 270.75 ± 0.66 tok/s.</small></p>

#### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; Q12 empty at fixed cap
- reasoning: explicit-CoT syllogism PASS
- coding: moving_sum executable oracle PASS
- native tools: exact call/arguments and grounded continuation PASS

##### Guardrails and limitations

- Reliability 3/20 for both required seeds; every request reaches the fixed completion limit in reasoning.
- No useful-context maximum validates under the frozen 512-token completion reserve; do not infer usefulness from 131,072 capacity.
- NOT_READY for a current-WELP agent role (human-accepted 2026-09-16); narrow capability successes are not role qualification.

**Reliability:** Frozen 20-task corpus, official sampler, seeds 42 and 314159: 3/20 each; strict interfaces 3/3 only; all 40 requests length-truncated.

#### LocalMaxxing

- Status: MEASURED_NOT_SUBMITTED
- tok/s out: 270.75
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>Local canonical llama-bench benchmark (pp512 7,710.53 ± 18.61 / tg128 270.75 ± 0.66 tok/s, evidence runs/llama-bench-canonical.txt); no LocalMaxxing service contact or submission occurred.</small></p>

**Tested condition:** artifact Q4_K_M · llama.cpp b9672 · RTX 5070 · native model-card maximum 131,072 tokens · envelope complete: YES.

**Context limit outcome:** VALIDATED capacity: exact native 131,072 at 99.660–99.758% near-full occupancy, two reps, cache-free; useful-context gates fail under frozen 512-token reserve.

**Context boundaries:** Capacity ladder 8,192/16,384/32,768/65,536/131,072 all PASS. USEFUL_CONTEXT_MAX NONE_VALIDATED: both seeds fail at 8,192 and 131,072 because reasoning exhausts the 512-token reserve before final content. No extension mechanism advertised.

**Hardware conditions:** full GPU residency; f16 KV; FA; single slot; one heavy CUDA workload at a time

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `mellum2-12b-a2.5b-llamacpp-q4km-thinking` |
| Model | Mellum2 12B-A2.5B (Thinking) |
| Producer | JetBrains |
| Official model | JetBrains/Mellum2-12B-A2.5B-Thinking @ `71a489e7b95efacf89feaaa6fe3b2995f3542409 (tested GGUF repo JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M)` |
| Tested artifact | Mellum2-12B-A2.5B-Thinking-Q4_K_M.gguf; locally reacquired and SHA-256 verified against the pinned official LFS object |
| Precision | Q4_K_M |
| Artifact SHA-256 | `489cf0d7ca86ef4683e34e2efe8a46a9b52573bfe994a6ad9c86bf57c7173ccb` |
| Campaign | `mellum2-12b-a2.5b-thinking-rtx5070-welp-recharacterization-2026-09-16` |
| Record date | 2026-09-16 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; f16 KV; FA; single slot; one heavy CUDA workload at a time |

#### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded |
| Guarded context | not recorded |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED capacity: exact native 131,072 at 99.660–99.758% near-full occupancy, two reps, cache-free; useful-context gates fail under frozen 512-token reserve. |

<p><small>Capacity ladder 8,192/16,384/32,768/65,536/131,072 all PASS. USEFUL_CONTEXT_MAX NONE_VALIDATED: both seeds fail at 8,192 and 131,072 because reasoning exhausts the 512-token reserve before final content. No extension mechanism advertised.</small></p>

</details>

<a id="mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15"></a>

### 2026-09-15: Current-WELP recharacterization

**WELP Recharacterization: llama.cpp Q4_K_M (Instruct)** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) · maturity: CURRENT_WELP · status: LIMITED_ROLE_ONLY

Configuration: llama.cpp Q4_K_M (Instruct).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)

#### WELP outcome

- **Outcome:** PASS
- **Classification:** LIMITED_ROLE_ONLY

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen; sole miss was the three-word lowercase instruction-retention task.
- coding: PASS (moving_sum executed correctly on all oracle cases)
- tool formatting: PASS (native hermes tool_call, exact arguments, grounded continuation)
- reasoning (direct mode, REASONING_OFF baseline): PASS (multi-hop syllogism correct, no think-tag leakage on the no-CoT checkpoint)

##### Guardrails and limitations

- reliability 7/20 at seed 42 and 8/20 at seed 314159; hallucination category 0/4 and 1/4 - REPLICATED fabrication of documentation for nonexistent APIs (fake CUDA signature, fake requests function, fake git command, nonexistent commit summary)
- sycophancy 0/3 and uncertainty 0/3 at both seeds; 7/20 outputs truncated at the frozen tight token caps
- useful-context ceiling 16,384 on this stack despite the 131,072 advertised window
- keep context <=16,384 (guarded 8,192); use the separate official Thinking checkpoint for explicit-CoT roles; that profile's current-WELP characterization is still open

**Reliability:** Strict interfaces 3/3 both seeds; evidence discipline 2/3 both; Git safety 1/1 both. The replicated fabrication and zero-pass sycophancy/uncertainty categories are classification-determining (LIMITED_ROLE_ONLY).

#### LocalMaxxing

- Status: MEASURED_NOT_SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>local canonical-profile benchmark pp512 7,744.16 ± 15.01 tok/s / tg128 271.66 ± 0.57 tok/s (5 reps); no external submission or fabricated verification fields; service mutation requires separate authorization.</small></p>

**Tested condition:** artifact Q4_K_M · llama.cpp b9672 · RTX 5070 · context 16,384 default / 8,192 guarded · native model-card maximum 131,072 tokens · envelope complete: YES.

**Context limit outcome:** FAILED on useful context with capacity+performance validated: exact 131,072 admits at f16 KV (9,850 MiB load, 2,377 MiB free) and passes near-full performance (99.66-99.76% occupancy, 4,872-4,883 tok/s prefill); the frozen two-seed useful-context gate failed 0/2 with a replicated recency-bias signature. Not a FIT_LIMIT and not a validation - a measured negative. Useful context is VALIDATED at 8,192 and 16,384 only.

**Context boundaries:** Ladder: 8,192/16,384 VALIDATED (two-seed useful-context PASS, placement error <=0.024 pp on the final rendered token stream); 32,768 FAILED 1/2 seeds; 65,536 and 131,072 FAILED 0/2 seeds (identical signature: 75%-depth decoy captured, early/mid-window facts lost, 95%-depth recency intact). USEFUL_CONTEXT_MAX 16,384. CAPACITY 131K is not USEFUL CONTEXT 131K. No official extension mechanism is advertised (the 131,072 native maximum itself is delivered by train-time YaRN factor 16 baked into the checkpoint); documented absence, no extension rungs.

**Hardware conditions:** full GPU residency -ngl 99; f16 K/V with FA; single slot; one heavy CUDA workload at a time; --no-cache-prompt --cache-ram 0 for uncached measurement

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `mellum2-12b-a2.5b-llamacpp-q4km-instruct` |
| Model | Mellum2 12B-A2.5B |
| Producer | JetBrains |
| Official model | JetBrains/Mellum2-12B-A2.5B-Instruct @ `1236b4166ed6ab1d57e4be9bcc19f4899c190cbf (tested GGUF repo)` |
| Tested artifact | Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf; reacquired from official repo after local+archive absence; SHA-256 verified against official LFS |
| Precision | Q4_K_M |
| Artifact SHA-256 | `b04281c27de5d968d577f310d982273b1b13bdbd8117b3ecffffeebfe222f0a7` |
| Campaign | `mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15` |
| Record date | 2026-09-15 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency -ngl 99; f16 K/V with FA; single slot; one heavy CUDA workload at a time; --no-cache-prompt --cache-ram 0 for uncached measurement |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | 8192 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FAILED on useful context with capacity+performance validated: exact 131,072 admits at f16 KV (9,850 MiB load, 2,377 MiB free) and passes near-full performance (99.66-99.76% occupancy, 4,872-4,883 tok/s prefill); the frozen two-seed useful-context gate failed 0/2 with a replicated recency-bias signature. Not a FIT_LIMIT and not a validation - a measured negative. Useful context is VALIDATED at 8,192 and 16,384 only. |

<p><small>Ladder: 8,192/16,384 VALIDATED (two-seed useful-context PASS, placement error <=0.024 pp on the final rendered token stream); 32,768 FAILED 1/2 seeds; 65,536 and 131,072 FAILED 0/2 seeds (identical signature: 75%-depth decoy captured, early/mid-window facts lost, 95%-depth recency intact). USEFUL_CONTEXT_MAX 16,384. CAPACITY 131K is not USEFUL CONTEXT 131K. No official extension mechanism is advertised (the 131,072 native maximum itself is delivered by train-time YaRN factor 16 baked into the checkpoint); documented absence, no extension rungs.</small></p>

</details>

<a id="mellum2-lmx-speed-2026-07-04"></a>

### 2026-07-04: LocalMaxxing LMX speed runs (Instruct + Thinking)

**Benchmark Only: LMX local speed** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

Configuration: llama.cpp Q4_K_M (Instruct).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-lmx-speed-2026-07-04/REPORT.md)


LMX local speed evidence: Instruct 261.41 tok/s out; Thinking 265.47 tok/s out (llama.cpp, Q4_K_M). Measured locally; submission disposition covered by the 2026-09-10 backfill scope for canonical profiles only.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`: llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="mellum2-fake-tool-2026-06-17"></a>

### 2026-06-17: Fake-tool honesty runs (64k)

**Specialized Test: fake-tool honesty** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_PROBES

Configuration: llama.cpp Q4_K_M (Instruct).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-fake-tool-2026-06-17/REPORT.md)


Fake-tool honesty probes at 64k for both Mellum2 variants; feeding the agent-backend manual scores.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`: llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, reliability
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="mellum2-agent-backend-64k-2026-06-17"></a>

### 2026-06-17: Agent backend fit test (64k, Instruct + Thinking)

**Specialized Test: LLMGauge agent-backend-v1** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

Configuration: llama.cpp Q4_K_M (Instruct).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-agent-backend-64k-2026-06-17/REPORT.md)

[Long-form report: Mellum2 Agent Backend Test](/records/mellum2-agent-backend-test/)

Related tested profiles: [mellum2-12b-a2.5b-llamacpp-q4km-thinking](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)


Instruct + Thinking Q4_K_M through LLMGauge agent-backend-v1 at 64k on WumboJetsII. 64k fit confirmed (Instruct 5/5 complete, 251.0-257.2 tok/s out, 9203 MiB peak VRAM). Manual scores: Instruct preferred (overall trust 3.7/5) over Thinking; neither safe for unsupervised shell/systemd operations. Not a general model-quality verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Related tested profile: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`: both variants were tested in the same event.

###### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`: llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

## Limitations

- Reliability 3/20 for both required seeds; every request reaches the fixed completion limit in reasoning. Source events: [2026-09-16](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16).
- No useful-context maximum validates under the frozen 512-token completion reserve; do not infer usefulness from 131,072 capacity. Source events: [2026-09-16](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16).
- NOT_READY for a current-WELP agent role (human-accepted 2026-09-16); narrow capability successes are not role qualification. Source events: [2026-09-16](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16).
- reliability 7/20 at seed 42 and 8/20 at seed 314159; hallucination category 0/4 and 1/4 - REPLICATED fabrication of documentation for nonexistent APIs (fake CUDA signature, fake requests function, fake git command, nonexistent commit summary) Source events: [2026-09-15](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15).
- sycophancy 0/3 and uncertainty 0/3 at both seeds; 7/20 outputs truncated at the frozen tight token caps Source events: [2026-09-15](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15).
- useful-context ceiling 16,384 on this stack despite the 131,072 advertised window Source events: [2026-09-15](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15).
- keep context <=16,384 (guarded 8,192); use the separate official Thinking checkpoint for explicit-CoT roles; that profile's current-WELP characterization is still open Source events: [2026-09-15](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) | Q4_K_M | llama.cpp b9672 | RTX 5070 | 16,384 default / 8,192 guarded | 4 (2026-06-17, 2026-06-17, 2026-07-04, 2026-09-15) |
| Q4_K_M · llama.cpp b9672 · RTX 5070 · reasoning_content emitted by the native template) | Q4_K_M | llama.cpp b9672 | RTX 5070 | not recorded | 2 (2026-06-17, 2026-09-16) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact)</summary>

- Full profile name: llama.cpp Q4_K_M (Instruct).
- Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (28/28 layers GPU-resident, no offload), -np 1, context default 16384 / guarded 8192, --no-cache-prompt --cache-ram 0 for uncached measurement; REASONING_OFF (Instruct is the no-CoT checkpoint; explicit CoT is the separate Thinking artifact)
- Artifact (as recorded): Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf (8,071,293,600-byte Q4_K_M; sha256 b04281c27de5d968d577f310d982273b1b13bdbd8117b3ecffffeebfe222f0a7; official JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M @ 1236b4166ed6ab1d57e4be9bcc19f4899c190cbf, reacquired 2026-09-15 after local+archive absence, byte-verified against official LFS SHA-256)
- Runtime (as recorded): llama.cpp b9672 (74ade5274), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/profile.json)

Events on this configuration:

- [Current-WELP recharacterization (2026-09-15)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15); status: LIMITED_ROLE_ONLY
- [LocalMaxxing LMX speed runs (Instruct + Thinking) (2026-07-04)](/evaluations/mellum2-12b-a2-5b#mellum2-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)
- [Fake-tool honesty runs (64k) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-fake-tool-2026-06-17); status: SPECIALIZED_TEST / UNSCORED_PROBES
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17); status: SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

</details>

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b9672 · RTX 5070 · reasoning_content emitted by the native template)</summary>

- Full profile name: llama.cpp Q4_K_M (Thinking).
- Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`.
- Status: validated alternate tested surface.
- Deployment topology (as recorded): Full-GPU llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (28/28 layers GPU-resident, no offload), -np 1, --no-cache-prompt --cache-ram 0 for uncached measurement; reasoning ON (Thinking is the official explicit-CoT checkpoint; reasoning_content emitted by the native template)
- Artifact (as recorded): JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M
- Runtime (as recorded): llama.cpp b9672 (74ade5274), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

Events on this configuration:

- [Current-WELP recharacterization (2026-09-16)](/evaluations/mellum2-12b-a2-5b#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16); status: NOT_READY
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17); status: SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-16 | [Current-WELP recharacterization](#mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16) | Q4_K_M · llama.cpp b9672 · RTX 5070 · reasoning_content emitted by the native template) | NOT_READY |
| 2026-09-15 | [Current-WELP recharacterization](#mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15) | Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) | LIMITED_ROLE_ONLY |
| 2026-07-04 | [LocalMaxxing LMX speed runs (Instruct + Thinking)](#mellum2-lmx-speed-2026-07-04) | Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) | BENCHMARK_ONLY (LMX local speed) |
| 2026-06-17 | [Fake-tool honesty runs (64k)](#mellum2-fake-tool-2026-06-17) | Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) | SPECIALIZED_TEST / UNSCORED_PROBES |
| 2026-06-17 | [Agent backend fit test (64k, Instruct + Thinking)](#mellum2-agent-backend-64k-2026-06-17) | Q4_K_M · llama.cpp b9672 · RTX 5070 · explicit CoT is the separate Thinking artifact) | SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict) |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/mellum2-12b-a2.5b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-16 WELP Recharacterization: llama.cpp Q4_K_M (Thinking)</summary>

- Campaign: `mellum2-12b-a2.5b-thinking-rtx5070-welp-recharacterization-2026-09-16`
- Export disposition: WEBSITE_READY; publication date 2026-09-16
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/a0ed8d8218d000c40fb2be157f4377d73c67af45/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/REPORT.md`
- Export identity: event_date `2026-09-16`, event_id `mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16`, event_type `CURRENT_WELP_RECHARACTERIZATION`, evidence_scope `['performance', 'quality', 'capabilities', 'reliability', 'context-envelope', 'localmaxxing', 'artifact-provenance']`, model_id `mellum2-12b-a2.5b`, profile_id `mellum2-12b-a2.5b-llamacpp-q4km-thinking`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `5e3bc1d441a90047d5c0cad324469758e96104a6` path models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/website-publication.json sha256 `afce840b738dd8e8aa48642f1d77a263fe57cbe4e332cc7bafc73e1f51df8f92`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; the existing Thinking profile ID was reused (same official Thinking artifact lineage/quant/runtime family/f16 KV). evidence_scope is scoped to the specialized registry lane: this is the second current-WELP profile on one model, and the event must not supersede the model-level canonical lanes (classification/reliability/context/serving-profile) attributed to the separately published Instruct event; per-profile Thinking facts render on the profile section and event section. Historical events retained unchanged; no eval-* repository created.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-15 WELP Recharacterization: llama.cpp Q4_K_M (Instruct)</summary>

- Campaign: `mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15`
- Export disposition: WEBSITE_READY; publication date 2026-09-15
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/adad9217547bf22cea9f2bd27e79a929374a20a9/models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md`
- Export identity: event_date `2026-09-15`, event_id `mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15`, event_type `current-welp-recharacterization`, evidence_scope `['host-preflight', 'identity', 'artifact-provenance', 'performance', 'quality', 'capabilities', 'reliability', 'context', 'useful-context', 'localmaxxing']`, model_id `mellum2-12b-a2.5b`, profile_id `mellum2-12b-a2.5b-llamacpp-q4km-instruct`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `adad9217547bf22cea9f2bd27e79a929374a20a9` path models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-rtx5070-welp-recharacterization-2026-09-15/website-publication.json sha256 `9164e6b671b3de817f699b7e3f944516e11fe85825428dcfb9ec84a5cd408a6a`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; the existing Instruct profile ID was reused (same artifact lineage/quant/runtime family/f16 KV); historical events and the separate Thinking profile retained unchanged; no eval-* repository created.</small></p>

</details>

### Legacy provenance

- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-agent-backend-64k-2026-06-17.md)
- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-fake-tool-2026-06-17.md)
- [WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct/blob/87d004ee76b6be247308fe69705d8ceb8d12c787/events/mellum2-lmx-speed-2026-07-04.md)

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04): Instruct 239.9/300 (4.0); Thinking 232.8/300 (3.88). [Canonical evidence / full report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
