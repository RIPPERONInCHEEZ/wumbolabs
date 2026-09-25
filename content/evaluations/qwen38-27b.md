+++
title = "Qwen3.8-27B"
description = "Qwen3.8-27B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 10

[extra]
kind = "model"
model_id = "qwen38-27b"
vendor = "Alibaba (Qwen team)"
classification = "COMPLETED_DEEP_EVALUATION"
recommended_profile_id = "qwen38-27b-exl3-h1"
recommended_profile_name = "ExLlamaV3 H1 (SC_2.20bpw_H3_V3)"
practical_context = "65,536 default / 98,304 guarded tokens"
profile_count = 2
event_count = 4
latest_evidence_date = 2026-09-12
+++

WumboLabs tests **Qwen3.8-27B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** COMPLETED_DEEP_EVALUATION — [Initial evaluation (deep evaluation, historical llama.cpp) (2026-08-21)](/evaluations/qwen38-27b#initial-evaluation-2026-08-21), profile Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF)
- **Recommended profile:** ExLlamaV3 H1 (SC_2.20bpw_H3_V3) (`qwen38-27b-exl3-h1`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/h1-canonical-promotion-2026-09-09/REPORT.md)
- **Practical context:** 65,536 default / 98,304 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Context envelope completion (2026-09-12)](/evaluations/qwen38-27b#context-envelope-completion-2026-09-12)
- **Latest evidence:** 2026-09-12 — Context envelope completion

## Tested profiles

### ExLlamaV3 H1 (SC_2.20bpw_H3_V3) — CURRENT

Profile identity: `qwen38-27b-exl3-h1`.

| Field | Value |
|---|---|
| Runtime | ExLlamaV3 1.4.6+cu128.torch2.10.0 (torch 2.10.0+cu128, CUDA 12.8) |
| Artifact | Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3) |
| Precision | 2.20 bpw EXL3; q4 target KV; q4 draft KV; MTP width 1 |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/context-envelope-completion-2026-09-12/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-exl3-h1/profile.json)

Events on this profile:

- [Context envelope completion (2026-09-12)](/evaluations/qwen38-27b#context-envelope-completion-2026-09-12) — GUARDED / MODEL-CARD CONTEXT ENVELOPE COMPLETE
- [H1 deployment / canonical promotion (2026-09-09)](/evaluations/qwen38-27b#h1-canonical-promotion-2026-09-09) — COMPLETE / CURRENT_CANONICAL_H1_PROFILE

### Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF) — HISTORICAL

Profile identity: `qwen38-27b-llamacpp-ud-q2-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/initial-evaluation-2026-08-21/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-llamacpp-ud-q2-k-xl/profile.json)

Events on this profile:

- [Initial evaluation (deep evaluation, historical llama.cpp) (2026-08-21)](/evaluations/qwen38-27b#initial-evaluation-2026-08-21) — COMPLETED_DEEP_EVALUATION
- [llama.cpp quant/variant showdown runs (LLMGauge era) (2026-08-20)](/evaluations/qwen38-27b#qwen38-27b-quant-showdowns-2026-08-20) — PROFILE_OPTIMIZATION (historical llama.cpp lane; superseded by ExLlamaV3 H1)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="context-envelope-completion-2026-09-12"></a>

### 2026-09-12 — Context envelope completion

**Context Envelope — ExLlamaV3 H1** · profile: ExLlamaV3 H1 (SC_2.20bpw_H3_V3) · maturity: CONTEXT_COMPLETION · status: GUARDED / MODEL-CARD CONTEXT ENVELOPE COMPLETE

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/context-envelope-completion-2026-09-12/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3.8-27B |
| Producer | Alibaba (Qwen team); EXL3 quant by turboderp |
| Official model | Qwen/Qwen3.8-27B @ `card lastModified 2026-08-14 (native 262,144; YaRN factor 4.0 advertised to 1,000,000)` |
| Tested artifact | Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3) |
| Precision | 2.20 bpw EXL3; q4 target KV; q4 draft KV; MTP width 1 |
| Campaign | `qwen38-27b-rtx5070-context-completion-2026-09-12` |
| Record date | 2026-09-12 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | ExLlamaV3 |
| Runtime version | 1.4.6+cu128.torch2.10.0 (torch 2.10.0+cu128, CUDA 12.8) |
| Runtime notes | Canonical H1 surface unchanged: MTP width 1, batch 1, max_chunk 256, recurrent history H1, CPU embedding lookup, all 64 transformer blocks GPU-resident; only serving context varies per arm |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44; displays on iGPU |

##### WELP outcome

- **Outcome:** PASS — QWEN38_27B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** MODEL-CARD CONTEXT ENVELOPE COMPLETE at the inherited guarded deployment classification; practical default unchanged

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/context-envelope-completion-2026-09-12/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 65536 tokens |
| Guarded context | 98304 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - exact native maximum 262,144 on the accepted H1 ExLlamaV3 surface: requires 12,530 MiB at ready (8,178 MiB context-independent + 262,144 x 17,408 B/token KV) versus 12,227 MiB total card VRAM; nearest measured boundary 98,304 VALIDATED. Official YaRN 1,000,000 extension INTEGRATION_BLOCKED on the accepted surface (runtime 1.4.6 has the YaRN implementation but exposes no supported activation without editing the protected artifact config) and independently FIT_LIMIT (cache alone ~16.6 GiB, ~1.36x total card VRAM) |

##### Quality and capabilities

- **Constrained result:** useful-context strict aggregate 4/4 requests (2 rungs x 2 seeds) at >=99.4% occupancy: exact retrieval 5/5, synthesis, decoy resistance, absent-information grounding, instruction compliance all 4/4; measured depths 2/25/50/75/95% within +/-0.036 pp
- first near-full context evidence above 65,536 on the ExLlamaV3 2.20bpw Qwen3.8 surface
- frozen fit model validated at both measured rungs (conservative by 28-80 MiB)
- prefill degradation curve characterized: ~790 tok/s at 3.5K -> 606 at 64.7K -> 537 at 97.3K

###### Guardrails and limitations

- retrieval-quality evidence is bounded to the tested fixture style and depths; it is not a general long-context quality claim
- reliability and role classification remain the inherited historical model-level findings; practical default unchanged
- the 98,304 operating point is guarded: ~181 s near-full TTFT and a ~300 MiB floor margin

**Reliability:** no CUDA/OOM/Xid events in the campaign; both arms torn down to verified idle; cold-cache enforced per request (verified cached_tokens 0 in all four retained terminal events)

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 65536 tokens |
| tok/s out | 75.4 |
| TTFT | 71.35 ms |
| Submission reference | cmtwcncwr07f4ps01ef75q6ne |
| verifiedRun | NO |

<p><small>existing authorized submission on the identical canonical practical profile (VERIFIED_EXISTING); no new benchmark or submission in this campaign</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/context-envelope-completion-2026-09-12/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="h1-canonical-promotion-2026-09-09"></a>

### 2026-09-09 — H1 deployment / canonical promotion

**H1 Canonical Promotion — ExLlamaV3** · profile: ExLlamaV3 H1 (SC_2.20bpw_H3_V3) · maturity: CURRENT_WELP · status: COMPLETE / CURRENT_CANONICAL_H1_PROFILE

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/h1-canonical-promotion-2026-09-09/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3.8-27B (current H1 profile) |
| Producer | Alibaba (Qwen team); EXL3 quant by turboderp |
| Tested artifact | Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3) |
| Precision | 2.20 bpw EXL3; q4 target KV; q4 draft KV |
| Campaign | `qwen38-27b-h1-canonical-profile (E18H candidate validation 2026-09-08 + E18I canonical promotion 2026-09-09)` |
| Record date | 2026-09-09 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | ExLlamaV3 |
| Runtime version | 1.4.6+cu128.torch2.10.0 |
| Runtime notes | MTP width 1, batch 1, max_chunk 256, recurrent history H1 (max_history 1) with explicit H4 fallback via --max-history 4; CPU embedding lookup (not transformer-layer offload); all 64 transformer blocks GPU-resident; context 65,536 canonical; recovered memory (434.8125 MiB) retained as unspent reserve |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

##### WELP outcome

- **Outcome:** PASS — E18I_H1_CANONICAL_PROMOTION_COMPLETE (E18H: PASS — E18H_H1_VALIDATED_EXPERIMENTAL_PROMOTION_CANDIDATE)
- **Classification:** CURRENT_CANONICAL_PROFILE — engine/history promotion validation, not a new model classification; the historical deep-evaluation role findings remain those of their tested stack
- **Artifact classification:** Current canonical Qwen3.8 serving surface (exact artifact/runtime/geometry scope only)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/h1-canonical-promotion-2026-09-09/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 65536 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | No full model-card context campaign exists for this profile; inherited validated evidence: E18E corrected combined oracle 3/3 requests / 15/15 target fields exact on H1 at ~58.8K actual input tokens (prompts 58,849/58,902/58,883) |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | not recorded | — | not recorded |
| Moderate (3514-token input) | 4.4487 s | 789.89 tok/s | 75.79 tok/s |

<p><small>E18H arm-B (H1) frozen 3,514-token prompt, five cold repetitions after warmup, medians; MTP width 1 active</small></p>

##### Quality and capabilities

- **Constrained result:** E18H seven-check quality matrix 7/7 PASS on the retained E3 fixture (all three arms A/B/A2); E18I H1 smoke repeated the fixture 7/7
- H1 recurrent/GDN storage 292.6875 MiB vs H4 727.5 MiB (measured reduction 434.8125 MiB, retained as reserve, not spent)
- E18G deterministic mechanism fixture F1/F2/F3 exact on H1; 20/20 stability sequence exactly flat (zero allocated/reserved growth, zero slope)
- H1 oracle minimum free 1,888 MiB vs 1,470 MiB for H4 (+418 MiB measured in the same campaign)

###### Guardrails and limitations

- H1 is canonical only for this exact artifact/runtime and text-only width1/batch1 surface
- No context growth or recovered-memory spending; explicit H4 fallback remains available in the same launcher
- Historical model-role findings (hallucination rate, strict interfaces, native tools) belong to the historical UD-Q2_K_XL llama.cpp evaluation and are not superseded by this profile work

**Reliability:** E18H H1 stability: 20/20 exact expected results, HTTP 200 throughout, flat allocator blocks (growth 0, slope 0); zero CUDA/OOM/Xid in both campaigns

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 65536 tokens |
| tok/s out | 75.4 |
| TTFT | 71.35 ms |
| Submission reference | cmtwcncwr07f4ps01ef75q6ne |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10) on the CURRENT H1 canonical profile (ExLlamaV3, SC_2.20bpw_H3_V3, q4/q4 KV, MTP width1, batch1, H1, 65,536); actual prompt tokens 266 (endpoint usage); verifiedRun false with an additional disclosed issue: MTP acceptance counters are not exposed by the canonical wrapper and none were fabricated; a transparent loopback path adapter bridged /chat/completions to /v1/chat/completions and is disclosed in the submission payload. Three historical E4-era submissions (llama.cpp-era wrapper with H4 history) remain historical and supersede nothing.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/h1-canonical-promotion-2026-09-09/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="initial-evaluation-2026-08-21"></a>

### 2026-08-21 — Initial evaluation (deep evaluation, historical llama.cpp)

**Initial Evaluation — Historical llama.cpp** · profile: Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF) · maturity: HISTORICAL_EVALUATION · status: COMPLETED_DEEP_EVALUATION

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/initial-evaluation-2026-08-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b)

[Long-form report: Qwen3.8-27B on 12GB: How Far Can an RTX 5070 Really Push It?](/records/qwen38-27b-rtx5070-evaluation/)

### Identity

| Field | Value |
|---|---|
| Model | Qwen 3.8 27B |
| Producer | Alibaba (Qwen team); quantized by Unsloth |
| Evaluated artifact | Unsloth Qwen3.8-27B UD-Q2_K_XL |
| Source revision | `27af057ecb382ddfea5d12837360a8980560e3ed` |
| SHA-256 | `fd4730dd8aad070517978752b63d530aeb1740d2283cab9fa24f1e404032ddb0` |
| Evaluation date | 2026-08-14 through 2026-08-21 |
| Protocol | WELP end-to-end (frozen snapshot `welp-next-snapshot-2026-08-25-end-to-end`) |
| Highest phase reached | Full campaign (Phase 10+) |
| Campaign classification | COMPLETED_DEEP_EVALUATION |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| GPU power | 250 W stock reference limit |
| CPU | AMD Ryzen 7 9800X3D, 8 cores / 16 threads |
| RAM | ~32 GiB DDR5 (~30 GiB usable) |
| OS | Fedora Linux 44, kernel 7.1.8-200.fc44.x86_64 |
| Driver / CUDA | NVIDIA 610.57.04 / CUDA 13.3 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

The RTX 5070 also drove the Fedora/Hyprland desktop during testing. Practical free VRAM was therefore lower than raw physical capacity; this is representative workstation evidence, not benchmark isolation.

### Headline Verdict

**NOT READY AS DAILY DRIVER**

Qwen3.8-27B UD-Q2_K_XL is stable in the tested runtime, practically fast, unusually strong at coding, capable of useful bounded 64K context, and substantially improved by bounded reasoning on hard tasks.

But the frozen primary reliability corpus classified 19.0% of executions as hallucinations; the frozen strict campaign had 21.2% failures; false-premise resistance was weak; and only 5/50 full native-tool sequences met the strict contract.

**Recommended classification: Strong reviewed local coding/technical assistant.**

The evidence does not support use as an unattended agent, source of unverified technical facts, autonomous system administrator, autonomous Git operator, unsupervised native-tool agent, or fail-closed structured-output engine.

### Performance

| Configuration | Decode tok/s | Prefill tok/s | Context | Notes |
|---|---|---|---|---|
| Quality/balance (Q4_K_M, 38 GPU layers, 8K) | 6.4–6.8 | ~880 | 8K | 4.85–5.0/5 coding score; 467 MiB min headroom |
| Speed (UD-IQ2_M, full GPU, 4K) | 42.0–42.9 | — | 4K | 362/5 manual avg; task-dependent quality |
| Agent-safe (UD-IQ2_XXS, full GPU, 12K) | — | — | 12K | Bounded one-file OMP pass |
| Large context (Q2_K_XL, 64K Q4/Q4) | ~30 | ~704 | 64K | Low-headroom reviewed work |

Native MTP at 8K: ~66 tok/s (1.47x speedup over baseline ~45 tok/s, ~75% acceptance).

### Capabilities

#### Coding
**Strongest supported domain.** Fresh executable coding passed 28/30 in disposable sandboxes with no network, minimal devices, resource limits, and no host modification. Coding recovery passed 36/40 changed-constraint revisions. This supports Qwen3.8-27B as a strong **reviewed** local coding assistant, not a hallucination-free coding system.

#### Reasoning
Tested, not enabled by default. On the fresh hard subset, reasoning on passed 9/10 versus 4/10 for the matched reasoning-off control. Use the reasoning profile for difficult math, logic, code diagnosis, evidence synthesis, and constrained planning. Leave it off for ordinary factual questions, strict interfaces, native tools, and routine work.

#### Strict Interfaces
The frozen strict campaign passed 197/250 (78.8%) and failed 53/250 (21.2%) across exact strings, JSON, extraction, enums, CSV, and word limits. Do not rely on one-shot strict responses; parse and mechanically validate structured output.

#### Native Tools
Only 5/50 full native-tool sequences satisfied the complete frozen end-to-end contract. Tool selection and argument structure performed better than the strict execution/recovery sequence. Native tools require deterministic execution, schema validation, result validation, and external supervision.

#### Long Context
Fresh baseline Q4 work passed bounded retrieval, synthesis, and instruction/code-retention probes at 16K, 32K, and 64K. The first filled 64K prompt contained approximately 64,275 tokens; first prefill took 91.24 s at 704.5 prompt tok/s. This demonstrates bounded 64K retrieval on this configuration. It does not establish that arbitrary 64K workloads are reliable.

#### Reliability
Primary reliability statistics covered 685 evaluated task executions:

| Classification | Count | Rate |
|---|---|---|
| CLEAN_PASS | 414 | 60.4% |
| MATERIAL_DEFECT | 43 | 6.3% |
| HALLUCINATION | 130 | 19.0% |
| STRUCTURAL_FAILURE | 98 | 14.3% |

False-premise resistance was the decisive readiness failure: hallucination-category runs were 67/150 CLEAN_PASS and 83/150 HALLUCINATION; sycophancy/false-premise runs were 28/75 CLEAN_PASS and 47/75 HALLUCINATION.

#### Stability
A two-hour balanced-profile soak completed 225/225 HTTP successes and 46/46 exact sentinels. Mean generation was 44.81 tok/s. VRAM started/ended/peaked at 10,340/10,248/10,342 MiB; peak soak temperature was 65 C. No new Xid, reset-required state, GSP failure, or display-engine collapse appeared during the controlled final campaign.

### Role Classification

**Supported roles:**
- Reviewed local coding assistant
- Technical assistant (with verification)
- Bounded reasoning assistant (reasoning on, difficult tasks only)

**Guarded roles:**
- Drafting and editing (review required)
- 64K context retrieval (low headroom, reviewed only)

**Unsupported / not ready:**
- Unguarded daily driver
- Unattended autonomous agent
- Source of unverified technical facts
- Autonomous system administrator
- Autonomous Git operator
- Unsupervised native-tool agent
- Fail-closed structured-output engine

### Important Limitations

- **No LLMGauge Agent Harness result exists.** This is a coverage limit, not a replacement classification.
- **Autonomy evidence is bounded:** the OMP follow-up completed a deliberately limited one-file inspect/edit/test/report loop. It does not establish broad autonomous-agent suitability.
- **Runtime safety boundary:** the evaluated vLLM configuration exhausted host memory during an earlier admission attempt. This is an operational deployment boundary, not a model-quality result.
- **Useful context not established beyond 8K for the fast quants.**
- Results apply to the pinned artifacts, llama.cpp b10449 runtime, Fedora 44 workstation condition, RTX 5070 12GB configuration, stated contexts, and frozen WumboLabs probes. They do not establish producer accuracy claims, cloud behavior, broad hardware representativeness, or universal model quality.

### Evidence Links

- **Canonical evaluation repo (historical llama.cpp profile):** https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-llamacpp-ud-q2-k-xl
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models
- **LocalMaxxing:** APPROVED speed-test submissions (`cmt3jngze0njfmv0133xpneeu` BALANCED 16K; `cmt3jp2cn0njpmv01t5u8m6wd` FAST 8K MTP) + benchmark suite APPROVED/PUBLIC; ref-quant `cmsv68xl3085ims01w8aeacig`

### Reproduction

Direct link to canonical reproduction material: [Central evidence](https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-llamacpp-ud-q2-k-xl)

Full reproduction instructions, manifests, and checksums are published in the canonical repository. This Lab Record is a summary; the canonical repo is the source of truth.

> **Provenance note (2026-09-12):** this evidence was originally published at
> [WumboLabs/eval-qwen3.8-27b](https://github.com/WumboLabs/eval-qwen3.8-27b)
> (evidence commit `54b14b30e3779f15486c3785222647324459dcf5`). It moved
> byte-identical to the canonical historical-profile repository
> ([eval-qwen3.8-27b-llamacpp](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp))
> by the model/profile/event publication-identity milestone; the original
> repository is preserved unchanged as a historical archive.

<a id="qwen38-27b-quant-showdowns-2026-08-20"></a>

### 2026-08-20 — llama.cpp quant/variant showdown runs (LLMGauge era)

**Profile Optimization — llama.cpp quant selection** · profile: Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF) · maturity: PROFILE_OPTIMIZATION · status: PROFILE_OPTIMIZATION (historical llama.cpp lane; superseded by ExLlamaV3 H1)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen38-27b/events/qwen38-27b-quant-showdowns-2026-08-20/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b)

### Identity and scope

- Profile: `qwen38-27b-llamacpp-ud-q2-k-xl` — Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF)
- Evidence maturity: **PROFILE_OPTIMIZATION**
- Evidence scope: performance, serving-profile
- Hardware: WumboJetsII (RTX 5070 12GB)

llama.cpp-era quant/variant showdown evidence (unsloth v3-final UD-IQ1_S/IQ2_XXS/IQ2_M ladder, community variants AtomicChat/XYZ Q3 smokes, 16k practical-use selection, 196k context-retrieval probe) that informed the historical llama.cpp profile before the ExLlamaV3 H1 promotion. Long-form context completion is separately represented (context-envelope-completion-2026-09-12).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.
### Historical lane note

These showdown runs belong to the historical llama.cpp lane. The current canonical serving
profile for this model is the ExLlamaV3 H1 surface, represented by its own events above.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen38-27b-exl3-h1**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-exl3-h1/profile.json)
- **qwen38-27b-llamacpp-ud-q2-k-xl**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/d3a235eb5a74263f1e980826a7915dd5330ffb53/models/qwen38-27b/profiles/qwen38-27b-llamacpp-ud-q2-k-xl/profile.json)

### Legacy provenance

- [RIPPERONInCHEEZ/wumbolabs @ `e27ddcb89b56c27e87d7a3af34003cd8c6d7355b`](https://github.com/RIPPERONInCHEEZ/wumbolabs/blob/e27ddcb89b56c27e87d7a3af34003cd8c6d7355b/data/labs-events/qwen38-27b-quant-showdowns-2026-08-20.md)
- [WumboLabs/eval-qwen3.8-27b-exl3-h1 @ `484c9184ae459c79754b77b7dc95da09e64d37a5`](https://github.com/WumboLabs/eval-qwen3.8-27b-exl3-h1/blob/484c9184ae459c79754b77b7dc95da09e64d37a5/reports/h1-canonical-profile-update.md)
- [WumboLabs/eval-qwen3.8-27b-exl3-h1 @ `484c9184ae459c79754b77b7dc95da09e64d37a5`](https://github.com/WumboLabs/eval-qwen3.8-27b-exl3-h1/blob/484c9184ae459c79754b77b7dc95da09e64d37a5/reports/qwen38-27b-context-envelope-completion-2026-09-12.md)
- [WumboLabs/eval-qwen3.8-27b-llamacpp @ `2f8d9fa9f9433cb64fcd416492e3a73c3a5773c7`](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp/blob/2f8d9fa9f9433cb64fcd416492e3a73c3a5773c7/reports/comparison.md)
