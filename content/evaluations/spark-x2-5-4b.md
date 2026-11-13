+++
title = "Spark-X2.5-4B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 8

[extra]
kind = "model"
model_id = "spark-x2.5-4b"
vendor = "XHToken (SparkLLM Team, iFlytek)"
findings_first = true
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "spark25-4b-q8-0-llamacpp"
recommended_profile_name = "llama.cpp upstream official Q8_0 (reasoning-on, vendor default)"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-20
+++

## Overview

XHToken (SparkLLM Team, iFlytek) · 1 tested configuration · 1 evidence event · newest evidence 2026-09-20.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS** - attributed to the [2026-09-20 event](#spark25-4b-rtx5070-welp-20260920), configuration Q8_0 · llama.cpp b10999 · RTX 5070.
- **Recommended configuration:** llama.cpp upstream official Q8_0 (reasoning-on, vendor default) (current): [event result](#spark25-4b-rtx5070-welp-20260920).
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 1,048,576 (envelope complete: YES); source: [event result](#spark25-4b-rtx5070-welp-20260920)
- **Context limit outcome:** FIT_LIMIT: f16 KV alone requires 38,654,705,664 bytes at the exact native maximum (36,864 B/token measured) - 3.16x the 12,227 MiB card; bounded admission attempt failed cleanly. Official extension: none advertised (documented absence).; source: [event result](#spark25-4b-rtx5070-welp-20260920)
- **Latest evidence:** 2026-09-20: [event result](#spark25-4b-rtx5070-welp-20260920)
- **2026-09-20** · Q8_0 · llama.cpp b10999 · RTX 5070: classification READY_WITH_GUARDRAILS; 10/12 frozen quality screen (temp 0, thinking-off diagnostic lane); canonical thinking-on lane 1/12 with 11/12 budget-starved to NOT_EVALUABLE. [Event result](#spark25-4b-rtx5070-welp-20260920)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="spark25-4b-rtx5070-welp-20260920"></a>

### 2026-09-20: Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)

**WELP Characterization: iFlytek Spark-X2.5-4B (reasoning-on)** · config Q8_0 · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp upstream official Q8_0 (reasoning-on, vendor default).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md)

#### WELP outcome

- **Outcome:** COMPLETE_PASS - characterization complete (all planned surfaces executed with valid evidence, including negatives)
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.0266 s | Not recorded | 122.1 tok/s |
| Moderate (4114-token input) | 0.4946 s | 8318.3 tok/s | not recorded |

<p><small>llama-bench canonical arm (5 reps), uncached; near-full prefill 8,329 tok/s (8K) to 4,318 tok/s (128K); full-occupancy decode ~59 tok/s at 128K vs 122 tok/s short-prompt; SWA hybrid keeps prefill fast through 128K.</small></p>

#### Quality and capabilities

- **Constrained result:** 10/12 frozen quality screen (temp 0, thinking-off diagnostic lane); canonical thinking-on lane 1/12 with 11/12 budget-starved to NOT_EVALUABLE
- reasoning probe: PASS at frozen 1500 and operational 4096 ceilings (exact 'TOTAL HOURS: 4')
- coding: executable-oracle PASS at 400 (thinking-off canonical) and 1500 (thinking-on diagnostic)
- native tools: exact call + args + grounded continuation PASS
- structured interfaces: PASS (both lanes)

##### Guardrails and limitations

- BUDGET_DISCIPLINE POOR on the canonical thinking-on profile: 0/20 operational-lane completions on BOTH reliability seeds - thinking consumes the frozen 20-256 token ceilings entirely.
- Semantic capability intact (30/33 evaluable clean on the predeclared 2048 lane); one fabricated 'git timewarp --undo' command instance observed in a truncated channel (not replicated across seeds).
- Greedy (temp 0) thinking can degenerate into repetition loops on absent-evidence probes; vendor sampling (1.0/0.95/-1) is the intended regime.
- No effort-level reasoning control exists on the pinned runtime; only enable_thinking=false changes behavior (requested=effective proven in both states).

**Reliability:** Frozen 20-task corpus, canonical vendor profile (thinking-on), seeds 42 and 314159: gate DO_NOT_ADVANCE - 0/20 completions on both seeds (budget exhaustion, 0 UNSAFE; adaptive third seed not triggered). Predeclared semantic lane (2048): 15/15 and 15/18 evaluable clean. Thinking-off diagnostic at the same tiny ceilings: 9/20 COMPLETE, 7/10 evaluable clean.

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 126.14
- TTFT: 55.2 ms
- Submission reference: cmudarhyh0aw9lq018zug8yna
- verifiedRun: NO
<p><small>Terminal closeout 2026-09-22: the canonical llama-bench arm (pp512 9,275.99 / tg128 126.14 tok/s, 5 reps) submitted verbatim; duplicate audit NO_EXACT_MATCH (exhaustive authenticated history of 35 user submissions with a control record verified present; zero Spark entries locally, in history, or in the public listing). verifiedRun=false recorded honestly: llama-bench local mode cannot supply prompt/output/engine-timing capture. Campaign close (2026-09-20) was MEASURED_NOT_SUBMITTED per the Stage-A boundary.</small></p>

**Tested condition:** artifact Q8_0 · llama.cpp b10999 · RTX 5070 · context 32,768 default / 131,072 guarded · native model-card maximum 1,048,576 tokens · envelope complete: YES.

**Context limit outcome:** FIT_LIMIT: f16 KV alone requires 38,654,705,664 bytes at the exact native maximum (36,864 B/token measured) - 3.16x the 12,227 MiB card; bounded admission attempt failed cleanly. Official extension: none advertised (documented absence).

**Context boundaries:** Useful context is PROFILE-SCOPED: USEFUL_CONTEXT_MAX_SEMANTIC = 131,072 on the predeclared thinking-off non-starving lane (2/2 seeds, all gates PASS at >=99% occupancy). The canonical vendor-default thinking-on lane is BUDGET_LIMITED at every tested rung (the standardized 512-token output reserve is consumed by thinking); retrieval capability is intact - the reserve-vs-thinking interaction is the blocker, not retrieval failure. The thinking-off lane is a declared alternative lane, not a separately fully characterized profile.

**Runtime conditions:** Native spark2_5 support (first release b10828, PR #27868); ENHANCED_SEMANTIC admission passed (new-architecture battery)

**Hardware conditions:** full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `spark25-4b-q8-0-llamacpp` |
| Model | Spark-X2.5-4B |
| Producer | XHToken (SparkLLM Team, iFlytek) |
| Official model | XHToken/Spark-X2.5-4B @ `0bcb35678590218655dff3765b9e61c83b35e9c4` |
| Tested artifact | Spark-X2.5-4B-Q8_0.gguf; 4,375,021,152 bytes; SHA-256 verified exact official LFS identity |
| Precision | Q8_0 (official publisher GGUF, 8.50 BPW) |
| Artifact SHA-256 | `5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2` |
| Campaign | `spark-x2.5-4b-rtx5070-welp-characterization-2026-09-20` |
| Record date | 2026-09-22 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (upstream) b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | Native spark2_5 support (first release b10828, PR #27868); ENHANCED_SEMANTIC admission passed (new-architecture battery) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 1048576 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT: f16 KV alone requires 38,654,705,664 bytes at the exact native maximum (36,864 B/token measured) - 3.16x the 12,227 MiB card; bounded admission attempt failed cleanly. Official extension: none advertised (documented absence). |

<p><small>Useful context is PROFILE-SCOPED: USEFUL_CONTEXT_MAX_SEMANTIC = 131,072 on the predeclared thinking-off non-starving lane (2/2 seeds, all gates PASS at >=99% occupancy). The canonical vendor-default thinking-on lane is BUDGET_LIMITED at every tested rung (the standardized 512-token output reserve is consumed by thinking); retrieval capability is intact - the reserve-vs-thinking interaction is the blocker, not retrieval failure. The thinking-off lane is a declared alternative lane, not a separately fully characterized profile.</small></p>

</details>

## Limitations

- BUDGET_DISCIPLINE POOR on the canonical thinking-on profile: 0/20 operational-lane completions on BOTH reliability seeds - thinking consumes the frozen 20-256 token ceilings entirely. Source events: [2026-09-20](#spark25-4b-rtx5070-welp-20260920).
- Semantic capability intact (30/33 evaluable clean on the predeclared 2048 lane); one fabricated 'git timewarp --undo' command instance observed in a truncated channel (not replicated across seeds). Source events: [2026-09-20](#spark25-4b-rtx5070-welp-20260920).
- Greedy (temp 0) thinking can degenerate into repetition loops on absent-evidence probes; vendor sampling (1.0/0.95/-1) is the intended regime. Source events: [2026-09-20](#spark25-4b-rtx5070-welp-20260920).
- No effort-level reasoning control exists on the pinned runtime; only enable_thinking=false changes behavior (requested=effective proven in both states). Source events: [2026-09-20](#spark25-4b-rtx5070-welp-20260920).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q8_0 · llama.cpp b10999 · RTX 5070 | Q8_0 | llama.cpp b10999 | RTX 5070 | 32,768 default / 131,072 guarded | 1 (2026-09-20) |

<details class="lab-findings-configs">
<summary>Configuration details: Q8_0 · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp upstream official Q8_0 (reasoning-on, vendor default).
- Profile identity: `spark25-4b-q8-0-llamacpp`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (36/36 layers), -fa on, f16 KV, -np 1 (verified via /slots), embedded Jinja template, vendor sampler (temp 1.0 / top_p 0.95 / top_k -1); REASONING_ON vendor default with enable_thinking=false as the only effective control (no effort-level control exists). Default context 32,768 / guarded fit ceiling 131,072; standardized 512-token output reserve.
- Artifact (as recorded): XHToken/Spark-X2.5-4B-GGUF@9826e0be :: Spark-X2.5-4B-Q8_0.gguf (sha256 5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2)
- Runtime (as recorded): llama.cpp (upstream) b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/spark-x2.5-4b/profiles/spark25-4b-q8-0-llamacpp/profile.json)

Events on this configuration:

- [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999) (2026-09-20)](/evaluations/spark-x2-5-4b#spark25-4b-rtx5070-welp-20260920); status: READY_WITH_GUARDRAILS

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-20 | [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)](#spark25-4b-rtx5070-welp-20260920) | Q8_0 · llama.cpp b10999 · RTX 5070 | READY_WITH_GUARDRAILS |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/spark-x2.5-4b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-20 WELP Characterization: iFlytek Spark-X2.5-4B (reasoning-on)</summary>

- Campaign: `spark-x2.5-4b-rtx5070-welp-characterization-2026-09-20`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-22
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md`
- Export identity: event_date `2026-09-20`, event_id `spark25-4b-rtx5070-welp-20260920`, event_type `initial-evaluation`, evidence_scope `['performance', 'reliability', 'quality', 'capability-probes', 'context-envelope', 'useful-context', 'localmaxxing', 'model-classification']`, model_id `spark-x2.5-4b`, profile_id `spark25-4b-q8-0-llamacpp`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `3fe25165969c303ad32dd5002943f17e368993e0` path models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/website-publication.json sha256 `a93b2c8c3d9049e9007aa70c7a7bb29b5f0687ad3e566c5ab3559ef92ad01d09`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; no eval-* repository. Campaign measurement snapshot welp-next-snapshot-2026-09-19-methodology-revision (WELP commit 79f9de13de04325e50e05b0eed28b56471a19028); the science closed 2026-09-20/21 under the then-applicable two-stage human-acceptance gate, superseded before terminal closeout by the 2026-09-22 execution-state lifecycle (welp-next-snapshot-2026-09-22-automatic-closeout-lifecycle, methodology_changed: NO) - historical evidence states preserved unchanged. LocalMaxxing terminal disposition recorded 2026-09-22: SUBMITTED origin NEW, id cmudarhyh0aw9lq018zug8yna, APPROVED, verifiedRun false (honest; llama-bench local mode cannot supply prompt/output/engine-timing capture); duplicate audit NO_EXACT_MATCH.</small></p>

</details>
