+++
title = "Spark-X2.5-4B"
description = "Spark-X2.5-4B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 3

[extra]
kind = "model"
model_id = "spark-x2.5-4b"
vendor = "XHToken (SparkLLM Team, iFlytek)"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "spark25-4b-q8-0-llamacpp"
recommended_profile_name = "llama.cpp upstream official Q8_0 (reasoning-on, vendor default)"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-20
+++

WumboLabs tests **Spark-X2.5-4B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999) (2026-09-20)](/evaluations/spark-x2-5-4b#spark25-4b-rtx5070-welp-20260920), profile llama.cpp upstream official Q8_0 (reasoning-on, vendor default)
- **Recommended profile:** llama.cpp upstream official Q8_0 (reasoning-on, vendor default) (`spark25-4b-q8-0-llamacpp`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md)
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 1,048,576 (envelope complete: YES) — [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999) (2026-09-20)](/evaluations/spark-x2-5-4b#spark25-4b-rtx5070-welp-20260920)
- **Latest evidence:** 2026-09-20 — Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)

## Tested profiles

### llama.cpp upstream official Q8_0 (reasoning-on, vendor default) — CURRENT

Profile identity: `spark25-4b-q8-0-llamacpp`.

| Field | Value |
|---|---|
| Runtime | llama.cpp (upstream) b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120 |
| Artifact | Spark-X2.5-4B-Q8_0.gguf; 4,375,021,152 bytes; SHA-256 verified exact official LFS identity |
| Precision | Q8_0 (official publisher GGUF, 8.50 BPW) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/ff5de425723ed4106331fe69c2818549f66d5147/models/spark-x2.5-4b/profiles/spark25-4b-q8-0-llamacpp/profile.json)

Events on this profile:

- [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999) (2026-09-20)](/evaluations/spark-x2-5-4b#spark25-4b-rtx5070-welp-20260920) — READY_WITH_GUARDRAILS

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="spark25-4b-rtx5070-welp-20260920"></a>

### 2026-09-20 — Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)

**WELP Characterization — iFlytek Spark-X2.5-4B (reasoning-on)** · profile: llama.cpp upstream official Q8_0 (reasoning-on, vendor default) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/ff5de425723ed4106331fe69c2818549f66d5147/models/spark-x2.5-4b)

##### Identity

| Field | Value |
|---|---|
| Model | Spark-X2.5-4B |
| Producer | XHToken (SparkLLM Team, iFlytek) |
| Official model | XHToken/Spark-X2.5-4B @ `0bcb35678590218655dff3765b9e61c83b35e9c4` |
| Tested artifact | Spark-X2.5-4B-Q8_0.gguf; 4,375,021,152 bytes; SHA-256 verified exact official LFS identity |
| Precision | Q8_0 (official publisher GGUF, 8.50 BPW) |
| Artifact SHA-256 | `5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2` |
| Campaign | `spark-x2.5-4b-rtx5070-welp-characterization-2026-09-20` |
| Record date | 2026-09-22 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (upstream) |
| Runtime version | b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120 |
| Runtime notes | Native spark2_5 support (first release b10828, PR #27868); ENHANCED_SEMANTIC admission passed (new-architecture battery) |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** COMPLETE_PASS - characterization complete (all planned surfaces executed with valid evidence, including negatives)
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 1048576 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT: f16 KV alone requires 38,654,705,664 bytes at the exact native maximum (36,864 B/token measured) - 3.16x the 12,227 MiB card; bounded admission attempt failed cleanly. Official extension: none advertised (documented absence). |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.0266 s | — | 122.1 tok/s |
| Moderate (4114-token input) | 0.4946 s | 8318.3 tok/s | not recorded |

<p><small>llama-bench canonical arm (5 reps), uncached; near-full prefill 8,329 tok/s (8K) to 4,318 tok/s (128K); full-occupancy decode ~59 tok/s at 128K vs 122 tok/s short-prompt; SWA hybrid keeps prefill fast through 128K.</small></p>

##### Quality and capabilities

- **Constrained result:** 10/12 frozen quality screen (temp 0, thinking-off diagnostic lane); canonical thinking-on lane 1/12 with 11/12 budget-starved to NOT_EVALUABLE
- reasoning probe: PASS at frozen 1500 and operational 4096 ceilings (exact 'TOTAL HOURS: 4')
- coding: executable-oracle PASS at 400 (thinking-off canonical) and 1500 (thinking-on diagnostic)
- native tools: exact call + args + grounded continuation PASS
- structured interfaces: PASS (both lanes)

###### Guardrails and limitations

- BUDGET_DISCIPLINE POOR on the canonical thinking-on profile: 0/20 operational-lane completions on BOTH reliability seeds - thinking consumes the frozen 20-256 token ceilings entirely.
- Semantic capability intact (30/33 evaluable clean on the predeclared 2048 lane); one fabricated 'git timewarp --undo' command instance observed in a truncated channel (not replicated across seeds).
- Greedy (temp 0) thinking can degenerate into repetition loops on absent-evidence probes; vendor sampling (1.0/0.95/-1) is the intended regime.
- No effort-level reasoning control exists on the pinned runtime; only enable_thinking=false changes behavior (requested=effective proven in both states).

**Reliability:** Frozen 20-task corpus, canonical vendor profile (thinking-on), seeds 42 and 314159: gate DO_NOT_ADVANCE - 0/20 completions on both seeds (budget exhaustion, 0 UNSAFE; adaptive third seed not triggered). Predeclared semantic lane (2048): 15/15 and 15/18 evaluable clean. Thinking-off diagnostic at the same tiny ceilings: 9/20 COMPLETE, 7/10 evaluable clean.

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 126.14 |
| TTFT | 55.2 ms |
| Submission reference | cmudarhyh0aw9lq018zug8yna |
| verifiedRun | NO |

<p><small>Terminal closeout 2026-09-22: the canonical llama-bench arm (pp512 9,275.99 / tg128 126.14 tok/s, 5 reps) submitted verbatim; duplicate audit NO_EXACT_MATCH (exhaustive authenticated history of 35 user submissions with a control record verified present; zero Spark entries locally, in history, or in the public listing). verifiedRun=false recorded honestly: llama-bench local mode cannot supply prompt/output/engine-timing capture. Campaign close (2026-09-20) was MEASURED_NOT_SUBMITTED per the Stage-A boundary.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/51a5ad2b0af17dff7502f1f55f94262ee1e67245/models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **spark25-4b-q8-0-llamacpp**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/ff5de425723ed4106331fe69c2818549f66d5147/models/spark-x2.5-4b/profiles/spark25-4b-q8-0-llamacpp/profile.json)
