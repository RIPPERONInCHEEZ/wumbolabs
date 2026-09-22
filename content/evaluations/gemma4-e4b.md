+++
title = "Gemma 4 E4B"
description = "Gemma 4 E4B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 11

[extra]
kind = "model"
model_id = "gemma4-e4b"
vendor = "Google"
classification = "READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL"
recommended_profile_id = "gemma4-e4b-llamacpp-qat-q4-0"
recommended_profile_name = "llama.cpp official QAT Q4_0"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-10
+++

WumboLabs tests **Gemma 4 E4B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL — [Initial evaluation (full characterization) (2026-09-10)](/evaluations/gemma4-e4b#initial-evaluation-2026-09-10-gemma4), profile llama.cpp official QAT Q4_0
- **Recommended profile:** llama.cpp official QAT Q4_0 (`gemma4-e4b-llamacpp-qat-q4-0`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md)
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 131,072 (envelope complete: YES) — [Initial evaluation (full characterization) (2026-09-10)](/evaluations/gemma4-e4b#initial-evaluation-2026-09-10-gemma4)
- **Latest evidence:** 2026-09-10 — Initial evaluation (full characterization)

## Tested profiles

### llama.cpp official QAT Q4_0 — CURRENT

Profile identity: `gemma4-e4b-llamacpp-qat-q4-0`.

| Field | Value |
|---|---|
| Runtime | llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120) |
| Artifact | gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release) |
| Precision | QAT Q4_0 weights, F16 KV cache |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/gemma4-e4b/profiles/gemma4-e4b-llamacpp-qat-q4-0/profile.json)

Events on this profile:

- [Initial evaluation (full characterization) (2026-09-10)](/evaluations/gemma4-e4b#initial-evaluation-2026-09-10-gemma4) — READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="initial-evaluation-2026-09-10-gemma4"></a>

### 2026-09-10 — Initial evaluation (full characterization)

**Initial Evaluation — official QAT Q4_0** · profile: llama.cpp official QAT Q4_0 · maturity: FULL_EVALUATION · status: READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/gemma4-e4b)

##### Identity

| Field | Value |
|---|---|
| Model | Gemma 4 E4B |
| Producer | Google |
| Official model | google/gemma-4-E4B-it @ `ee0ef6023621cff504d758262d4e04895a5af4a2` |
| Tested artifact | gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release) |
| Precision | QAT Q4_0 weights, F16 KV cache |
| Artifact hash evidence | 676c3507 (weights; matches pinned upstream LFS) / 7498a37c (mmproj; matches pinned upstream LFS) |
| Campaign | `gemma4-e4b-rtx5070-welp-characterization-2026-09-10` |
| Record date | 2026-09-10 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120) |
| Runtime notes | All 42 layers + PLE tables + vision/audio encoders GPU-resident; official mmproj loaded for multimodal arms; greedy temperature-0 primary surface |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

##### WELP outcome

- **Outcome:** PASS — GEMMA4_E4B_EVIDENCE_COMPLETION_COMPLETE
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Official Google QAT Q4_0 + official mmproj — the only official precision that hosts the full card range with reserve on this GPU; community Q4_K_M pair retained as evidence only (provenance unknown)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | Exact native 131,072: measured FAILED on the strict aggregate useful-context gate while near-full performance itself was valid (both seeds 99.50% occupancy, TTFT ~38 s, decode ~79 tok/s, zero errors) and five-needle target retrieval stayed perfect (10/10 across ALL rungs including the exact maximum) |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.0225 s | — | 150.4 tok/s |
| Moderate (2785-token input) | 0.504 s | 7217 tok/s | 145.7 tok/s |

<p><small>Medians over five measured repetitions per surface; near-full ladder values are medians of two seeds per rung</small></p>

##### Quality and capabilities

- **Constrained result:** 3/7 strict gates (markdown-fenced JSON plus a real absent-field grounding defect); content-level supplement: 3/3 needle facts exact, decoy absent, checksum correct
- Multimodal on 12 GB: vision TESTED_PASS, multi-image TESTED_PASS, audio ASR TESTED_PASS, audio AST TESTED_PASS, bounded three-frame video TESTED_PASS
- Reasoning (thinking mode), coding (4/4 execution cases), function calling, and bounded tool-result use TESTED_PASS
- Perfect five-needle retrieval through the exact 131,072 maximum; 80 valid scientific requests across 9 supervised arms with zero CUDA/OOM/Xid

###### Guardrails and limitations

- Strict-format fragility: fenced JSON when markdown is not explicitly forbidden; schema-tail truncation from 16K upward; absent-field (negative-space) answers unreliable at temperature 0
- OCR/document understanding TESTED_LIMITED (one document ID digit dropped at temperature 0; broader OCR types untested)
- Video evidence bounded to frame-sequence probes (full <=60 s @1fps producer envelope not established); MTP/speculative deferred (distinct serving surface)

**Reliability:** Canonical 32K profile: 20/20 runtime completion with zero errors; behavioral exactness 14/20 — all six failures are the known dossier strict-format/absent defect, bit-stable across arms; bounded, not soak/endurance

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 152.7 |
| TTFT | 59.74 ms |
| Submission reference | cmtwgcs7c097sps01sdq9ihbu |
| verifiedRun | null (not claimed) |

<p><small>SUBMITTED once, origin NEW, service APPROVED (in-campaign, 2026-09-11); verifiedRun null — the service returned no verification state and the client could not transmit verification fields; recorded honestly, not claimed as verified; actual prompt tokens 77 (endpoint usage); tokSPrefill 1,322.5</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **gemma4-e4b-llamacpp-qat-q4-0**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/8badb2c83aa486740f58f2e8f290d4b8d599232d/models/gemma4-e4b/profiles/gemma4-e4b-llamacpp-qat-q4-0/profile.json)

### Legacy provenance

- [WumboLabs/eval-gemma4-e4b @ `980b54ac5a0bb26534929149d6f6f3d041e65e56`](https://github.com/WumboLabs/eval-gemma4-e4b/blob/980b54ac5a0bb26534929149d6f6f3d041e65e56/EVIDENCE-SUMMARY.md)
