+++
title = "Gemma 4 E4B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 16

[extra]
kind = "model"
model_id = "gemma4-e4b"
vendor = "Google"
findings_first = true
classification = "READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL"
recommended_profile_id = "gemma4-e4b-llamacpp-qat-q4-0"
recommended_profile_name = "llama.cpp official QAT Q4_0"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-10
+++

## Overview

Google · 1 tested configuration · 1 evidence event · newest evidence 2026-09-10.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL** - attributed to the [2026-09-10 event](#initial-evaluation-2026-09-10-gemma4), configuration QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070.
- **Recommended configuration:** llama.cpp official QAT Q4_0 (current): [event result](#initial-evaluation-2026-09-10-gemma4).
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 131,072 (envelope complete: YES); source: [event result](#initial-evaluation-2026-09-10-gemma4)
- **Context limit outcome:** Exact native 131,072: measured FAILED on the strict aggregate useful-context gate while near-full performance itself was valid (both seeds 99.50% occupancy, TTFT ~38 s, decode ~79 tok/s, zero errors) and five-needle target retrieval stayed perfect (10/10 across ALL rungs including the exact maximum); source: [event result](#initial-evaluation-2026-09-10-gemma4)
- **Latest evidence:** 2026-09-10: [event result](#initial-evaluation-2026-09-10-gemma4)
- **2026-09-10** · QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070: classification READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL; 3/7 strict gates (markdown-fenced JSON plus a real absent-field grounding defect); content-level supplement: 3/3 needle facts exact, decoy absent, checksum correct. [Event result](#initial-evaluation-2026-09-10-gemma4)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="initial-evaluation-2026-09-10-gemma4"></a>

### 2026-09-10: Initial evaluation (full characterization)

**Initial Evaluation: official QAT Q4_0** · config QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070 · maturity: FULL_EVALUATION · status: READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL

Configuration: llama.cpp official QAT Q4_0.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md)

#### WELP outcome

- **Outcome:** PASS: GEMMA4_E4B_EVIDENCE_COMPLETION_COMPLETE
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Official Google QAT Q4_0 + official mmproj; the only official precision that hosts the full card range with reserve on this GPU; community Q4_K_M pair retained as evidence only (provenance unknown)

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.0225 s | Not recorded | 150.4 tok/s |
| Moderate (2785-token input) | 0.504 s | 7217 tok/s | 145.7 tok/s |

<p><small>Medians over five measured repetitions per surface; near-full ladder values are medians of two seeds per rung</small></p>

#### Quality and capabilities

- **Constrained result:** 3/7 strict gates (markdown-fenced JSON plus a real absent-field grounding defect); content-level supplement: 3/3 needle facts exact, decoy absent, checksum correct
- Multimodal on 12 GB: vision TESTED_PASS, multi-image TESTED_PASS, audio ASR TESTED_PASS, audio AST TESTED_PASS, bounded three-frame video TESTED_PASS
- Reasoning (thinking mode), coding (4/4 execution cases), function calling, and bounded tool-result use TESTED_PASS
- Perfect five-needle retrieval through the exact 131,072 maximum; 80 valid scientific requests across 9 supervised arms with zero CUDA/OOM/Xid

##### Guardrails and limitations

- Strict-format fragility: fenced JSON when markdown is not explicitly forbidden; schema-tail truncation from 16K upward; absent-field (negative-space) answers unreliable at temperature 0
- OCR/document understanding TESTED_LIMITED (one document ID digit dropped at temperature 0; broader OCR types untested)
- Video evidence bounded to frame-sequence probes (full <=60 s @1fps producer envelope not established); MTP/speculative deferred (distinct serving surface)

**Reliability:** Canonical 32K profile: 20/20 runtime completion with zero errors; behavioral exactness 14/20; all six failures are the known dossier strict-format/absent defect, bit-stable across arms; bounded, not soak/endurance

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 152.7
- TTFT: 59.74 ms
- Submission reference: cmtwgcs7c097sps01sdq9ihbu
- verifiedRun: null (not claimed)
<p><small>SUBMITTED once, origin NEW, service APPROVED (in-campaign, 2026-09-11); verifiedRun null; the service returned no verification state and the client could not transmit verification fields; recorded honestly, not claimed as verified; actual prompt tokens 77 (endpoint usage); tokSPrefill 1,322.5</small></p>

**Tested condition:** artifact QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070 · context 32,768 default / 131,072 guarded · native model-card maximum 131,072 tokens · envelope complete: YES.

**Context limit outcome:** Exact native 131,072: measured FAILED on the strict aggregate useful-context gate while near-full performance itself was valid (both seeds 99.50% occupancy, TTFT ~38 s, decode ~79 tok/s, zero errors) and five-needle target retrieval stayed perfect (10/10 across ALL rungs including the exact maximum)

**Context boundaries:** Strict aggregate gate FAILED at every rung; divergence is explicit: content retrieval is perfect everywhere (decoy resistance 10/10), while strict output/instruction compliance is the failure surface (absent-field fills a present value instead of NOT_SPECIFIED; JSON tail truncation from 16K upward). No official context extensions exist for E4B (source-backed absence).

**Runtime conditions:** All 42 layers + PLE tables + vision/audio encoders GPU-resident; official mmproj loaded for multimodal arms; greedy temperature-0 primary surface

**Hardware conditions:** Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `gemma4-e4b-llamacpp-qat-q4-0` |
| Model | Gemma 4 E4B |
| Producer | Google |
| Official model | google/gemma-4-E4B-it @ `ee0ef6023621cff504d758262d4e04895a5af4a2` |
| Tested artifact | gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release) |
| Precision | QAT Q4_0 weights, F16 KV cache |
| Artifact hash evidence | 676c3507 (weights; matches pinned upstream LFS) / 7498a37c (mmproj; matches pinned upstream LFS) |
| Campaign | `gemma4-e4b-rtx5070-welp-characterization-2026-09-10` |
| Record date | 2026-09-10 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120) |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | All 42 layers + PLE tables + vision/audio encoders GPU-resident; official mmproj loaded for multimodal arms; greedy temperature-0 primary surface |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | Exact native 131,072: measured FAILED on the strict aggregate useful-context gate while near-full performance itself was valid (both seeds 99.50% occupancy, TTFT ~38 s, decode ~79 tok/s, zero errors) and five-needle target retrieval stayed perfect (10/10 across ALL rungs including the exact maximum) |

<p><small>Strict aggregate gate FAILED at every rung; divergence is explicit: content retrieval is perfect everywhere (decoy resistance 10/10), while strict output/instruction compliance is the failure surface (absent-field fills a present value instead of NOT_SPECIFIED; JSON tail truncation from 16K upward). No official context extensions exist for E4B (source-backed absence).</small></p>

</details>

## Limitations

- Strict-format fragility: fenced JSON when markdown is not explicitly forbidden; schema-tail truncation from 16K upward; absent-field (negative-space) answers unreliable at temperature 0 Source events: [2026-09-10](#initial-evaluation-2026-09-10-gemma4).
- OCR/document understanding TESTED_LIMITED (one document ID digit dropped at temperature 0; broader OCR types untested) Source events: [2026-09-10](#initial-evaluation-2026-09-10-gemma4).
- Video evidence bounded to frame-sequence probes (full <=60 s @1fps producer envelope not established); MTP/speculative deferred (distinct serving surface) Source events: [2026-09-10](#initial-evaluation-2026-09-10-gemma4).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070 | QAT Q4_0 weights, F16 KV cache | llama.cpp | RTX 5070 | 32,768 default / 131,072 guarded | 1 (2026-09-10) |

<details class="lab-findings-configs">
<summary>Configuration details: QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp official QAT Q4_0.
- Profile identity: `gemma4-e4b-llamacpp-qat-q4-0`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release)
- Runtime (as recorded): llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120).
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma4-e4b/profiles/gemma4-e4b-llamacpp-qat-q4-0/profile.json)

Events on this configuration:

- [Initial evaluation (full characterization) (2026-09-10)](/evaluations/gemma4-e4b#initial-evaluation-2026-09-10-gemma4); status: READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-10 | [Initial evaluation (full characterization)](#initial-evaluation-2026-09-10-gemma4) | QAT Q4_0 weights, F16 KV cache · llama.cpp · RTX 5070 | READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma4-e4b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-10 Initial Evaluation: official QAT Q4_0</summary>

- Campaign: `gemma4-e4b-rtx5070-welp-characterization-2026-09-10`
- Export disposition: WEBSITE_READY; publication date 2026-09-11
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/REPORT.md`
- Export source pin: repository-cache WumboLabs/evaluations @ `479cb50c197f8ea0dd905a68ffd61f632f49c652` path models/gemma4-e4b/events/initial-evaluation-2026-09-10-gemma4/website-publication.json sha256 `45aca9eb0ff421280e04e6137cdcdc8571e40754a89c5f4e705b410ab7a052bb`

</details>

### Legacy provenance

- [WumboLabs/eval-gemma4-e4b @ `980b54ac5a0bb26534929149d6f6f3d041e65e56`](https://github.com/WumboLabs/eval-gemma4-e4b/blob/980b54ac5a0bb26534929149d6f6f3d041e65e56/EVIDENCE-SUMMARY.md)
