+++
title = "Qwen3-14B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 12

[extra]
kind = "model"
model_id = "qwen3-14b"
vendor = "Alibaba (Qwen team)"
findings_first = true
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "qwen3-14b-llamacpp-q4km-q8kv"
recommended_profile_name = "llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface)"
practical_context = "32,768 default / 32,768 guarded tokens"
profile_count = 3
event_count = 4
latest_evidence_date = 2026-09-14
+++

## Overview

Alibaba (Qwen team) · 3 tested configurations · 4 evidence events · newest evidence 2026-09-14.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS** - attributed to the [2026-09-14 event](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14), configuration Q4_K_M · llama.cpp b9672 · RTX 5070.
- **Recommended configuration:** llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface) (current): [event result](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14).
- **Practical context:** 32,768 default / 32,768 guarded tokens; native model-card maximum 32,768 (envelope complete: YES); source: [event result](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14)
- **Context limit outcome:** VALIDATED - near-full performance (99.2-99.6% occupancy, 2 reps) and useful-context PASS at 2 seeds (99.47% occupancy) on the canonical q8_0-KV surface; 2026-09-15 append-only completion added the contract-required 95% depth placement: all five contract depths (2/25/50/75/95) x 2 seeds within the preferred 0.25pp placement bound (max error 0.160/0.087 pp), all gates PASS (99.49% occupancy).; source: [event result](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14)
- **Latest evidence:** 2026-09-14: [event result](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14)
- **2026-09-14** · Q4_K_M · llama.cpp b9672 · RTX 5070: classification READY_WITH_GUARDRAILS; 11/12 frozen mechanical quality screen (frozen scorer, temp 0); sole miss is the no-letter-e lexical-constraint task. [Event result](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14)
- **2026-07-15** · llama.cpp · RTX 5070: classification SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION. [Event result](#qwen3-14b-fit-ladder-2026-07-15)
- **2026-07-05** · llama.cpp · RTX 5070: classification BENCHMARK_ONLY (LMX local speed). [Event result](#qwen3-14b-lmx-speed-2026-07-05)
- **2026-05-07** · Ollama · RTX 5070: classification PRACTICAL_USE / PRE_WELP_HISTORICAL. [Event result](#qwen3-14b-wumbo-daily-evaluation-2026-05-07)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen3-14b-rtx5070-welp-recharacterization-2026-09-14"></a>

### 2026-09-14: Current-WELP recharacterization

**WELP Recharacterization: llama.cpp Q4_K_M q8_0 KV** · config Q4_K_M · llama.cpp b9672 · RTX 5070 · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md)

#### WELP outcome

- **Outcome:** PASS: RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** 11/12 frozen mechanical quality screen (frozen scorer, temp 0); sole miss is the no-letter-e lexical-constraint task
- reasoning (thinking ON, card sampler) multi-hop syllogism PASS with visible chain
- coding: moving_sum generates and executes correctly on all oracle cases
- tool calling: valid call + correct arguments + grounded continuation PASS

##### Guardrails and limitations

- reliability mechanical pass 7/20 (seed 42) and 8/20 (seed 314159); 19 of 25 failing instances are substantively correct answers failing mechanically via question-phrase echo, keyword morphology, or frozen token-cap truncation (finish=length 7/20 and 6/20) - raise output budgets and prefer strict-interface phrasings that do not echo the question
- one true fabrication pattern observed: invented a description of a nonexistent commit (hall-fake-repo-state, both seeds); sycophancy-unknown asserted a root cause without logs (both seeds)
- thinking mode: use the card sampler (temp 0.6/top_p 0.95/top_k 20); greedy decoding risks repetition loops per official card
- official YaRN 131,072 context is FIT_LIMIT on this 12GB hardware; native 32,768 is the validated ceiling

**Reliability:** Proven mechanical 20-task corpus, 2 seeds (card-recommended non-thinking sampler temp 0.7/top_p 0.8/top_k 20): strict_interfaces 3/3 both seeds; evidence_discipline 2/3 both; substantive failures concentrated in hallucination-under-abstract-pressure (1 task), sycophancy (2 tasks), with strong verbosity/truncation interaction at frozen small token caps

#### LocalMaxxing

- Status: MEASURED_NOT_SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>local canonical-profile benchmark pp512 2719.17 tok/s / tg128 65.95 tok/s (5 reps, KV q8_0, FA); historical 2026-07-05 record was never submitted and is not an exact stack match; submission requires separate human gate</small></p>

**Tested condition:** artifact Q4_K_M · llama.cpp b9672 · RTX 5070 · context 32,768 default / 32,768 guarded · native model-card maximum 32,768 tokens · envelope complete: YES.

**Context limit outcome:** VALIDATED - near-full performance (99.2-99.6% occupancy, 2 reps) and useful-context PASS at 2 seeds (99.47% occupancy) on the canonical q8_0-KV surface; 2026-09-15 append-only completion added the contract-required 95% depth placement: all five contract depths (2/25/50/75/95) x 2 seeds within the preferred 0.25pp placement bound (max error 0.160/0.087 pp), all gates PASS (99.49% occupancy).

**Context boundaries:** Native rungs 8K/16K/32K VALIDATED. Official YaRN extension (factor 4.0, exact max 131,072) is FIT_LIMIT on 12GB: measured cudaMalloc OOM at q8_0 KV (10,880 MiB request) and at the lowest dtype q4_0 (5,760 MiB request); nearest measured boundary 32,768. Attribution: RTX 5070 12GB, not the model.

**Hardware conditions:** full GPU residency; KV q8_0; one heavy CUDA workload at a time

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `qwen3-14b-llamacpp-q4km-q8kv` |
| Model | Qwen3-14B |
| Producer | Alibaba (Qwen team) |
| Official model | Qwen/Qwen3-14B @ `unsloth/Qwen3-14B-GGUF lineage artifact (see artifact)` |
| Tested artifact | Qwen3-14B-Q4_K_M.gguf (local canonical copy, downloaded 2026-05-08T22:13:02Z; byte fingerprint matches the central registry historical profile record) |
| Precision | Q4_K_M |
| Artifact SHA-256 | `712c0791d5124d3dd6d1e4968de1201207afeae49c6e10fbeb9c58fe00c58555` |
| Campaign | `qwen3-14b-rtx5070-welp-recharacterization-2026-09-14` |
| Record date | 2026-09-15 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; KV q8_0; one heavy CUDA workload at a time |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 32768 tokens |
| Native model-card maximum | 32768 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED - near-full performance (99.2-99.6% occupancy, 2 reps) and useful-context PASS at 2 seeds (99.47% occupancy) on the canonical q8_0-KV surface; 2026-09-15 append-only completion added the contract-required 95% depth placement: all five contract depths (2/25/50/75/95) x 2 seeds within the preferred 0.25pp placement bound (max error 0.160/0.087 pp), all gates PASS (99.49% occupancy). |

<p><small>Native rungs 8K/16K/32K VALIDATED. Official YaRN extension (factor 4.0, exact max 131,072) is FIT_LIMIT on 12GB: measured cudaMalloc OOM at q8_0 KV (10,880 MiB request) and at the lowest dtype q4_0 (5,760 MiB request); nearest measured boundary 32,768. Attribution: RTX 5070 12GB, not the model.</small></p>

</details>

<a id="qwen3-14b-fit-ladder-2026-07-15"></a>

### 2026-07-15: Fit-ladder success-fallback E2E (LLMGauge feature validation)

**Specialized Test: fit ladder** · config llama.cpp · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION

Configuration: llama.cpp Q4_K_M (unsloth).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)


LLMGauge fit-ladder feature E2E used Qwen3-14B Q4_K_M as payload (32k -> 8k fallback). Primary subject: LLMGauge feature behavior; retained as model-adjacent evidence.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3-14b-llamacpp-q4km`: llama.cpp Q4_K_M (unsloth)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="qwen3-14b-lmx-speed-2026-07-05"></a>

### 2026-07-05: LMX speed run

**Benchmark Only: LMX local speed** · config llama.cpp · RTX 5070 · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

Configuration: llama.cpp Q4_K_M (unsloth).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-lmx-speed-2026-07-05/REPORT.md)


LMX local speed evidence: 66.57 tok/s out (llama.cpp Q4_K_M). Archaeology retention review separately records 63.74 tok/s full-CUDA-offload in the May-era recorded benchmark.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3-14b-llamacpp-q4km`: llama.cpp Q4_K_M (unsloth)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="qwen3-14b-wumbo-daily-evaluation-2026-05-07"></a>

### 2026-05-07: Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag)

**Practical Use: historical daily driver** · config Ollama · RTX 5070 · maturity: PRACTICAL_USE · status: PRACTICAL_USE / PRE_WELP_HISTORICAL

Configuration: Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3-14b/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)


Historical May 2026 Ollama-era evaluation of the custom qwen3-14b-wumbo tag: 'Good enough for daily local technical assistant use'; strengths in Docker/systemd/Arch tooling with mandatory command review; 4096-context guidance. Pre-WELP practical-use evidence, not a WELP verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `qwen3-14b-ollama-q4km-wumbo`: Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

## Limitations

- reliability mechanical pass 7/20 (seed 42) and 8/20 (seed 314159); 19 of 25 failing instances are substantively correct answers failing mechanically via question-phrase echo, keyword morphology, or frozen token-cap truncation (finish=length 7/20 and 6/20) - raise output budgets and prefer strict-interface phrasings that do not echo the question Source events: [2026-09-14](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14).
- one true fabrication pattern observed: invented a description of a nonexistent commit (hall-fake-repo-state, both seeds); sycophancy-unknown asserted a root cause without logs (both seeds) Source events: [2026-09-14](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14).
- thinking mode: use the card sampler (temp 0.6/top_p 0.95/top_k 20); greedy decoding risks repetition loops per official card Source events: [2026-09-14](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14).
- official YaRN 131,072 context is FIT_LIMIT on this 12GB hardware; native 32,768 is the validated ceiling Source events: [2026-09-14](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b9672 · RTX 5070 | Q4_K_M | llama.cpp b9672 | RTX 5070 | 32,768 default / 32,768 guarded | 1 (2026-09-14) |
| Ollama · RTX 5070 | not recorded | Ollama | RTX 5070 | not recorded | 1 (2026-05-07) |
| llama.cpp · RTX 5070 | not recorded | llama.cpp | RTX 5070 | not recorded | 2 (2026-07-05, 2026-07-15) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b9672 · RTX 5070</summary>

- Full profile name: llama.cpp Q4_K_M q8_0 KV (unsloth artifact, native-max 32K surface).
- Profile identity: `qwen3-14b-llamacpp-q4km-q8kv`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU llama.cpp CUDA serving on RTX 5070 12GB: -ngl 999 full residency (40/40 transformer layers), -c 32768 native maximum, -np 1, flash attention, server-side non-thinking baseline
- Artifact (as recorded): unsloth/Qwen3-14B-GGUF Q4_K_M (9,001,753,376-byte Q4_K_M; sha256 712c0791d5124d3dd6d1e4968de1201207afeae49c6e10fbeb9c58fe00c58555)
- Runtime (as recorded): llama.cpp b9672 (74ade5274), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km-q8kv/profile.json)

Events on this configuration:

- [Current-WELP recharacterization (2026-09-14)](/evaluations/qwen3-14b#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14); status: READY_WITH_GUARDRAILS

</details>

<details class="lab-findings-configs">
<summary>Configuration details: Ollama · RTX 5070</summary>

- Full profile name: Ollama Q4_K_M (qwen3-14b-wumbo custom tag, historical daily driver).
- Profile identity: `qwen3-14b-ollama-q4km-wumbo`.
- Status: historical tested surface; retained evidence, not the recommended profile.
- Artifact (as recorded): unsloth/Qwen3-14B-GGUF Q4_K_M (custom qwen3-14b-wumbo Ollama tag; 9,001,753,376-byte weights fingerprint)
- Runtime (as recorded): Ollama.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3-14b/profiles/qwen3-14b-ollama-q4km-wumbo/profile.json)

Events on this configuration:

- [Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag) (2026-05-07)](/evaluations/qwen3-14b#qwen3-14b-wumbo-daily-evaluation-2026-05-07); status: PRACTICAL_USE / PRE_WELP_HISTORICAL

</details>

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp Q4_K_M (unsloth).
- Profile identity: `qwen3-14b-llamacpp-q4km`.
- Status: historical tested surface; retained evidence, not the recommended profile.
- Artifact (as recorded): unsloth/Qwen3-14B-GGUF Q4_K_M
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3-14b/profiles/qwen3-14b-llamacpp-q4km/profile.json)

Events on this configuration:

- [Fit-ladder success-fallback E2E (LLMGauge feature validation) (2026-07-15)](/evaluations/qwen3-14b#qwen3-14b-fit-ladder-2026-07-15); status: SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION
- [LMX speed run (2026-07-05)](/evaluations/qwen3-14b#qwen3-14b-lmx-speed-2026-07-05); status: BENCHMARK_ONLY (LMX local speed)

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-14 | [Current-WELP recharacterization](#qwen3-14b-rtx5070-welp-recharacterization-2026-09-14) | Q4_K_M · llama.cpp b9672 · RTX 5070 | READY_WITH_GUARDRAILS |
| 2026-07-15 | [Fit-ladder success-fallback E2E (LLMGauge feature validation)](#qwen3-14b-fit-ladder-2026-07-15) | llama.cpp · RTX 5070 | SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION |
| 2026-07-05 | [LMX speed run](#qwen3-14b-lmx-speed-2026-07-05) | llama.cpp · RTX 5070 | BENCHMARK_ONLY (LMX local speed) |
| 2026-05-07 | [Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag)](#qwen3-14b-wumbo-daily-evaluation-2026-05-07) | Ollama · RTX 5070 | PRACTICAL_USE / PRE_WELP_HISTORICAL |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen3-14b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-14 WELP Recharacterization: llama.cpp Q4_K_M q8_0 KV</summary>

- Campaign: `qwen3-14b-rtx5070-welp-recharacterization-2026-09-14`
- Export disposition: WEBSITE_READY; publication date 2026-09-14
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/3330db39e23d8a3a02b3d627a895af4b8ae5e4b1/models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md`
- Export identity: event_date `2026-09-14`, event_id `qwen3-14b-rtx5070-welp-recharacterization-2026-09-14`, event_type `CURRENT_WELP_RECHARACTERIZATION`, evidence_scope `['performance', 'quality', 'capabilities', 'reasoning', 'coding', 'tools', 'reliability', 'context-envelope', 'localmaxxing-measured']`, model_id `qwen3-14b`, profile_decision_note `2026-09-15 closeout boundary decision: NEW current profile qwen3-14b-llamacpp-q4km-q8kv (q8_0 K/V cache at the native 32,768 maximum is material to the profile identity; the historical qwen3-14b-llamacpp-q4km descriptor records no cache/topology and remains unchanged/historical).`, profile_id `qwen3-14b-llamacpp-q4km-q8kv`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `2950a5eacd376c4df28b4bf33b96cae0b3db397a` path models/qwen3-14b/events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/website-publication.json sha256 `bc102550a29106b0755f179fbb40fa71aa9d246b30eb934a0d4fd18b5a4136f1`

<p><small>Publication provenance note (as recorded): First native event publication under the consolidated architecture; no legacy repository exists for this campaign.</small></p>

</details>

### Legacy provenance

- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-fit-ladder-2026-07-15.md)
- [WumboLabs/eval-qwen3-14b @ `ea855b38294d1c4c13664a45a2911a6de809ca94`](https://github.com/WumboLabs/eval-qwen3-14b/blob/ea855b38294d1c4c13664a45a2911a6de809ca94/events/qwen3-14b-lmx-speed-2026-07-05.md)
- [WumboLabs/eval-qwen3-14b-ollama-q4km @ `285d06529dab955e9458c646b72493843c8998f0`](https://github.com/WumboLabs/eval-qwen3-14b-ollama-q4km/blob/285d06529dab955e9458c646b72493843c8998f0/events/qwen3-14b-wumbo-daily-evaluation-2026-05-07.md)

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04): Q4_K_M scored 228.4/300 (3.81 avg). [Canonical evidence / full report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
