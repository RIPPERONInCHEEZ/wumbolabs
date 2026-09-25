+++
title = "Ternary Bonsai 2 27B"
description = "Ternary Bonsai 2 27B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 5

[extra]
kind = "model"
model_id = "bonsai-2-27b"
vendor = "PrismML"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off"
recommended_profile_name = "llama.cpp PTQ1_0 (thinking-off)"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-09-20
+++

WumboLabs tests **Ternary Bonsai 2 27B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Methodology-revision supplement (thinking-off profile) (2026-09-20)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920), profile llama.cpp PTQ1_0 (thinking-off)
- **Recommended profile:** llama.cpp PTQ1_0 (thinking-off) (`bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md)
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Methodology-revision supplement (thinking-off profile) (2026-09-20)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920)
- **Latest evidence:** 2026-09-20 — Methodology-revision supplement (thinking-off profile)

## Tested profiles

### llama.cpp PTQ1_0 (thinking-off) — CURRENT

Profile identity: `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`.

| Field | Value |
|---|---|
| Runtime | llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off/profile.json)

Events on this profile:

- [Methodology-revision supplement (thinking-off profile) (2026-09-20)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920) — READY_WITH_GUARDRAILS

### llama.cpp PTQ1_0 (reasoning-on, vendor default) — HISTORICAL

Profile identity: `bonsai2-27b-ptq1-0-prism-llamacpp`.

| Field | Value |
|---|---|
| Runtime | llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |

Status: historical tested surface; retained evidence, not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp/profile.json)

Events on this profile:

- [Current-WELP characterization + compression-retention + RTX 2060 SUPER portability (2026-09-18)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-20260918) — NOT_READY

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="bonsai2-27b-rtx5070-welp-methodology-supplement-20260920"></a>

### 2026-09-20 — Methodology-revision supplement (thinking-off profile)

**WELP Methodology-Revision Supplement — PrismML PTQ1_0 (thinking-off)** · profile: llama.cpp PTQ1_0 (thinking-off) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b)

##### Identity

| Field | Value |
|---|---|
| Model | Ternary Bonsai 2 27B (thinking-off) |
| Producer | PrismML |
| Official model | prism-ml/Ternary-Bonsai-2-27B-gguf @ `6ed5e12bf84b7a63069882c91dd9e9218647d17b` |
| Tested artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |
| Artifact SHA-256 | `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3` |
| Campaign | `bonsai-2-27b-welp-methodology-supplement-2026-09-20` |
| Record date | 2026-09-21 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (PrismML-Eng fork) |
| Runtime version | 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Runtime notes | Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery) |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS - COMPLETE_PASS (bounded WELP methodology-revision supplement)
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT (unchanged); 65,536 serves at ~99.6% occupancy on this profile; 98,304+ exceeds card memory. |

##### Quality and capabilities

- **Constrained result:** Semantic lane (ceiling 2048): 18/20 + 18/20 PASS (seeds 42/314159), completion 40/40, 0 truncation, 0 NOT_EVALUABLE, 0 UNSAFE
- hallucination 4/4 + 4/4; uncertainty 3/3 + 3/3; strict interfaces 2/3 + 2/3 (load-bearing: real exact-format defect caught both seeds); sycophancy 2/3 + 2/3
- profile-pure operational-ceiling audit (DERIVED, 0 new requests): completion 0.55/0.65 at legacy caps, EXHAUSTED_IN_ANSWER only - verbosity vs cap sizing, never reasoning starvation

###### Guardrails and limitations

- Pin enable_thinking=false (the only effective reasoning control on the pinned runtime) and size generation ceilings to the measured verbosity; legacy 20-140-token caps truncate 35-45% of tasks on answer length alone.
- BUDGET_DISCIPLINE POOR from this profile's own audit; READY_WITH_GUARDRAILS derived by the frozen harness (R-C5) via the declared non-starving 2048 lane (40/40 completion at 0.90 semantics).
- The reasoning-on profile keeps its historical NOT_READY and remains operationally budget-hostile (completion 1/20 at legacy caps); neither profile represents Bonsai 2 universally.

**Reliability:** WELP scorer v2 / gate_v2, frozen 20-task fixture v2, seeds 42 and 314159: 18/20 semantic each; four genuine semantic FAILs (strict-extract-09 x2, sycophancy-unknown, sycophancy-systemd); adaptive third seed not triggered.

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 59.22 |
| TTFT | not recorded |
| Submission reference | cmuajqjjd09y4lq01wrf8ht0j |
| verifiedRun | NO |

<p><small>Carried terminal disposition (no re-benchmark by design): the thinking-off delta changes declared reasoning state only, which is not a LocalMaxxing benchmark identity field. Owning record: the characterization event's campaign. verifiedRun=false recorded honestly.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="bonsai2-27b-rtx5070-welp-20260918"></a>

### 2026-09-18 — Current-WELP characterization + compression-retention + RTX 2060 SUPER portability

**WELP Characterization — PrismML PTQ1_0 ternary (reasoning-on)** · profile: llama.cpp PTQ1_0 (reasoning-on, vendor default) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b)

##### Identity

| Field | Value |
|---|---|
| Model | Ternary Bonsai 2 27B (reasoning-on) |
| Producer | PrismML |
| Official model | prism-ml/Ternary-Bonsai-2-27B-gguf @ `6ed5e12bf84b7a63069882c91dd9e9218647d17b` |
| Tested artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |
| Artifact SHA-256 | `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3` |
| Campaign | `bonsai-2-27b-rtx5070-welp-characterization-2026-09-18` |
| Record date | 2026-09-21 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (PrismML-Eng fork) |
| Runtime version | 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Runtime notes | Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery) |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS - characterization complete (verdict binds the reasoning-on profile)
- **Classification:** NOT_READY
- **Artifact classification:** historical

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT: f16 KV + weights exceed 12,227 MiB card memory at the exact native maximum (measured-anchored accounting; no launch). Official extension: none advertised (documented absence). |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.2787 s | — | not recorded |
| Moderate (3600-token input) | 6.366 s | 568.7 tok/s | not recorded |

<p><small>llama-bench canonical arm (5 reps), uncached; near-full prefill 575 to 520 tok/s (8K to 64K); full-occupancy decode 55 to 42 tok/s; prefill is the practical bottleneck on Blackwell for PTQ1_0.</small></p>

##### Quality and capabilities

- **Constrained result:** 12/12 frozen mechanical quality screen (temp 0)
- reasoning probe: PASS (syllogism, coherent answer)
- coding: budget-bound at canonical cap; thinking-off 400-cap PASS and 1500-cap thinking-on PASS (executable oracle 3/3)
- native tools: exact call + args + grounded continuation PASS
- structured interfaces: JSON object/array exact PASS

###### Guardrails and limitations

- Reliability 4/20 + 3/20 (seeds 42/314159) under default xhigh thinking; finish=length 19/20, 20/20 - budget exhaustion, not fabrication; 0 UNSAFE.
- Per-request reasoning budget/effort kwargs are ignored by the pinned runtime; only enable_thinking=false changes behavior.
- Never trust strict one-shot outputs or nonexistent-API/package/commit claims without verification.

**Reliability:** Frozen 20-task corpus, vendor-default thinking, seeds 42 and 314159: 4/20 and 3/20; failure mode replicated across five bounded re-configurations (budget-vs-reasoning interaction).

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 59.22 |
| TTFT | 872.92 ms |
| Submission reference | cmuajqjjd09y4lq01wrf8ht0j |
| verifiedRun | NO |

<p><small>Terminal closeout 2026-09-21 (origin NEW, APPROVED): the canonical llama-bench arm (pp512 586.54 / tg128 59.22 tok/s, 5 reps) submitted verbatim; duplicate audit NO_EXACT_MATCH (all pre-existing service entries are PQ2_0 on other hardware). verifiedRun=false recorded honestly: llama-bench local mode cannot supply prompt/output/engine-timing capture. TTFT is estimated from prefill.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off/profile.json)
- **bonsai2-27b-ptq1-0-prism-llamacpp**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp/profile.json)
