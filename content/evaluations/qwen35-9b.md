+++
title = "Qwen3.5-9B"
description = "Qwen3.5-9B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 13

[extra]
kind = "model"
model_id = "qwen35-9b"
vendor = "Alibaba (Qwen team)"
recommended_profile_id = "qwen35-9b-llamacpp-q8"
recommended_profile_name = "llama.cpp Q8_0 GGUF"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-11
+++

WumboLabs tests **Qwen3.5-9B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q8_0 GGUF (`qwen35-9b-llamacpp-q8`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Context envelope completion (2026-09-11)](/evaluations/qwen35-9b#context-envelope-completion-2026-09-11-qwen35-9b)
- **Latest evidence:** 2026-09-11 — Context envelope completion

## Tested profiles

### llama.cpp Q8_0 GGUF — CURRENT

Profile identity: `qwen35-9b-llamacpp-q8`.

| Field | Value |
|---|---|
| Runtime | llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Artifact | Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) |
| Precision | Q8_0 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/fed51a3ef66af89cfadd130d6990444797efd7ab/models/qwen35-9b/profiles/qwen35-9b-llamacpp-q8/profile.json)

Events on this profile:

- [Context envelope completion (2026-09-11)](/evaluations/qwen35-9b#context-envelope-completion-2026-09-11-qwen35-9b) — READY_WITH_GUARDRAILS

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="context-envelope-completion-2026-09-11-qwen35-9b"></a>

### 2026-09-11 — Context envelope completion

**Context Envelope — llama.cpp Q8_0** · profile: llama.cpp Q8_0 GGUF · maturity: CONTEXT_COMPLETION · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/fed51a3ef66af89cfadd130d6990444797efd7ab/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3.5-9B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-9B @ `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| Tested artifact | Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) |
| Precision | Q8_0 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |
| Artifact SHA-256 | `809626574d0cb43d4becfa56169980da2bb448f2299270f7be443cb89d0a6ae4` |
| Campaign | `qwen35-9b-rtx5070-context-completion-2026-09-11` |
| Record date | 2026-09-09 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Runtime notes | All 33/33 runtime layers GPU-resident (untied input embedding lookup on CPU, disclosed); non-thinking text-only greedy surface; identical inherited baseline stack |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

##### WELP outcome

- **Outcome:** PASS — QWEN35_9B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** READY_WITH_GUARDRAILS (unchanged; new occupancy guardrail: at >=99.4% occupancy the model returns the absent-information value NOT_SPECIFIED under the literal key name 'zeta' instead of the required 'absent' key)
- **Artifact classification:** High-quality quantized medium-fit text control (unchanged)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - native maximum 262,144 on the Q8_0/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.043883 s | — | 66.66 tok/s |
| Moderate (3642-token input) | 0.831738 s | 4378.79 tok/s | 64.84 tok/s |

<p><small>Near-full context fixture per-seed values; client/transport proxies with native timings retained in campaign evidence; short/moderate surfaces inherited unchanged from the baseline campaign (66.7 tok/s short decode, 0.83 s moderate TTFT)</small></p>

##### Quality and capabilities

- **Constrained result:** inherited: 7/7 constrained checks and 20/20 bounded reliability (baseline campaign, unchanged, not rerun)
- Perfect synthetic retrieval (20/20 values) at 99.49-99.56% occupancy through 64K on the primary surface
- Synthesis and checksum instructions retained at near-full occupancy (unlike the 4B same-family control)
- Highest measured/admitted near-full primary context 65,536 (guarded profile confirmed); 98,304 projected below the frozen operational safety floor and intentionally not launched; exact ceiling not bracketed
- q4_0-KV alternate surface functionally correct at 32K
- Official YaRN mechanism representable in the pinned runtime

###### Guardrails and limitations

- At >=99.4% near-full occupancy the absent-information value is returned under the wrong key name (deterministic at both rungs and both seeds); strict useful-context gate FAILED
- Inherited free-form cautions from the baseline: unsupported provenance/checksum attribution in open-ended answers; human verification required
- Not agent-qualified; no coding/tool/autonomous testing

**Reliability:** not recorded

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | cmtwcn79807eups01faxxmyr1 |
| verifiedRun | null (not claimed) |

<p><small>existing canonical submission audited for exact duplication; no new benchmark or submission performed</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen35-9b-llamacpp-q8**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/fed51a3ef66af89cfadd130d6990444797efd7ab/models/qwen35-9b/profiles/qwen35-9b-llamacpp-q8/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.5-9b @ `096afc64dbceb870e7672c7cdc95e44dea5ade49`](https://github.com/WumboLabs/eval-qwen3.5-9b/blob/096afc64dbceb870e7672c7cdc95e44dea5ade49/reports/qwen35-9b-context-envelope-completion-2026-09-11.md)
