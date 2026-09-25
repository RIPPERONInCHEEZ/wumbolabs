+++
title = "Granite 4.2 8B"
description = "Granite 4.2 8B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 1

[extra]
kind = "model"
model_id = "granite-4.2-8b"
vendor = "IBM (ibm-granite)"
classification = "NOT_READY"
recommended_profile_id = "granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment"
recommended_profile_name = "llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K)"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-24
+++

WumboLabs tests **Granite 4.2 8B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** NOT_READY — [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999) (2026-09-24)](/evaluations/granite-4-2-8b#granite-42-8b-rtx5070-welp-context-completion-20260924), profile llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K)
- **Recommended profile:** llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) (`granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md)
- **Latest evidence:** 2026-09-24 — First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)

## Tested profiles

### llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) — CURRENT

Profile identity: `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`.

| Field | Value |
|---|---|
| Runtime | not recorded |
| Artifact | not recorded |
| Precision | not recorded |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/granite-4.2-8b/profiles/granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment/profile.json)

Events on this profile:

- [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999) (2026-09-24)](/evaluations/granite-4-2-8b#granite-42-8b-rtx5070-welp-context-completion-20260924) — NOT_READY

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="granite-42-8b-rtx5070-welp-context-completion-20260924"></a>

### 2026-09-24 — First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)

**WELP Initial Evaluation — IBM Granite 4.2 8B (reasoning-on)** · profile: llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · maturity: CURRENT_WELP · status: NOT_READY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/granite-4.2-8b)

##### Identity

| Field | Value |
|---|---|
| Model | Granite 4.2 8B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `16a9369d0805f80b7377d25d87f937a90c05dc04ad79173a52001e42c9aab311` |
| Campaign | `granite-4.2-8b-rtx5070-welp-context-outcome-completion-2026-09-24` |
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

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md

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

<p><small>SUBMITTED/NEW, service record cmug9qe0i0d5wlq01lep45uua (APPROVED, verifiedRun false)</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/granite-4.2-8b/profiles/granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment/profile.json)
