+++
title = "NeoHorse-1-9B"
description = "NeoHorse-1-9B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 2

[extra]
kind = "model"
model_id = "neohorse-1-9b"
vendor = "TokenRhythm"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on"
recommended_profile_name = "llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K)"
profile_count = 2
event_count = 3
latest_evidence_date = 2026-09-25
+++

WumboLabs tests **NeoHorse-1-9B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required) (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925), profile llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K)
- **Recommended profile:** llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) (`neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md)
- **Latest evidence:** 2026-09-25 — First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required)

## Tested profiles

### llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) — CURRENT

Profile identity: `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`.

| Field | Value |
|---|---|
| Runtime | not recorded |
| Artifact | not recorded |
| Precision | not recorded |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on/profile.json)

Events on this profile:

- [First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required) (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925) — READY_WITH_GUARDRAILS
- [First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-agentic-20260925) — READY_WITH_GUARDRAILS

### llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) — CURRENT-ALTERNATE

Profile identity: `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`.

| Field | Value |
|---|---|
| Runtime | not recorded |
| Artifact | not recorded |
| Precision | not recorded |

Status: validated alternate tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)

Events on this profile:

- [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-reasoning-off-20260925) — READY_WITH_GUARDRAILS

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="neohorse-1-9b-rtx5070-welp-reasoning-on-20260925"></a>

### 2026-09-25 — First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required)

**WELP Fresh-Model Characterization — NeoHorse-1-9B (Reasoning On, publisher default)** · profile: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b)

##### Identity

| Field | Value |
|---|---|
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-reasoning-on-2026-09-25` |
| Record date | 2026-09-26 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md

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

<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="neohorse-1-9b-rtx5070-welp-reasoning-off-20260925"></a>

### 2026-09-25 — Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model

**WELP Reasoning-Profile Characterization — NeoHorse-1-9B (Reasoning Off, supported alternate)** · profile: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b)

##### Identity

| Field | Value |
|---|---|
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-reasoning-off-2026-09-25` |
| Record date | 2026-09-26 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md

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

<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="neohorse-1-9b-rtx5070-welp-agentic-20260925"></a>

### 2026-09-25 — First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect

**WELP Agentic — NeoHorse-1-9B (publisher-default profile, native tool calls)** · profile: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b)

##### Identity

| Field | Value |
|---|---|
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-agentic-2026-09-25` |
| Record date | 2026-09-26 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | not recorded |
| Runtime version | not recorded |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

##### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md

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

<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on/profile.json)
- **neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/553a68d915b9ea1c9c9b3be6fa65c16f13527c24/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)
