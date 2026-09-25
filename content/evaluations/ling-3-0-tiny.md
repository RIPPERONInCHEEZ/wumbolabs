+++
title = "Ling 3.0 Tiny"
description = "Ling 3.0 Tiny — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 1

[extra]
kind = "model"
model_id = "ling-3.0-tiny"
vendor = "inclusionAI (Ant Group)"
classification = "NOT_READY"
recommended_profile_id = "ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment"
recommended_profile_name = "llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K)"
profile_count = 2
event_count = 3
latest_evidence_date = 2026-09-25
+++

WumboLabs tests **Ling 3.0 Tiny** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** NOT_READY — [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference) (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925), profile llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K)
- **Recommended profile:** llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) (`ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md)
- **Latest evidence:** 2026-09-25 — Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)

## Tested profiles

### llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) — CURRENT

Profile identity: `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`.

| Field | Value |
|---|---|
| Runtime | not recorded |
| Artifact | not recorded |
| Precision | not recorded |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment/profile.json)

Events on this profile:

- [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference) (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925) — NOT_READY
- [Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0) (2026-09-24)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-characterization-20260924) — NOT_READY

### llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) — CURRENT-ALTERNATE

Profile identity: `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`.

| Field | Value |
|---|---|
| Runtime | not recorded |
| Artifact | not recorded |
| Precision | not recorded |

Status: validated alternate tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)

Events on this profile:

- [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925) — NOT_READY

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925"></a>

### 2026-09-25 — Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)

**WELP Reasoning-Profile Re-derivation — Ling 3.0 Tiny (Reasoning On, publisher default)** · profile: llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny)

##### Identity

| Field | Value |
|---|---|
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-reasoning-on-2026-09-25` |
| Record date | 2026-09-25 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

##### Quality and capabilities

- **Constrained result:** not recorded

###### Guardrails and limitations


**Reliability:** not recorded

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>the engine-native llama-bench record does not exercise the reasoning control, so both reasoning profiles share this record</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925"></a>

### 2026-09-25 — Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model

**WELP Reasoning-Profile Characterization — Ling 3.0 Tiny (Reasoning Off, supported alternate)** · profile: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny)

##### Identity

| Field | Value |
|---|---|
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-reasoning-off-2026-09-25` |
| Record date | 2026-09-25 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

##### Quality and capabilities

- **Constrained result:** not recorded

###### Guardrails and limitations


**Reliability:** not recorded

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>this profile's own bench re-measurement; consistent with the existing service record (benchmark does not exercise the reasoning control; no duplicate submitted)</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="ling-3-0-tiny-rtx5070-welp-characterization-20260924"></a>

### 2026-09-24 — Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0)

**WELP Initial Evaluation — inclusionAI Ling 3.0 Tiny (reasoning-on)** · profile: llama.cpp official Q8_0 (reasoning-on, deployment sampler, 32K) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/43f56d8add4b3dfc51183ccd818fc6037e79bd9c/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny)

##### Identity

| Field | Value |
|---|---|
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-characterization-2026-09-24` |
| Record date | 2026-09-24 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/43f56d8add4b3dfc51183ccd818fc6037e79bd9c/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

##### Quality and capabilities

- **Constrained result:** not recorded

###### Guardrails and limitations


**Reliability:** not recorded

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/43f56d8add4b3dfc51183ccd818fc6037e79bd9c/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment/profile.json)
- **ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)
