+++
title = "NeoHorse-1-9B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 6

[extra]
kind = "model"
model_id = "neohorse-1-9b"
vendor = "TokenRhythm"
findings_first = true
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off"
recommended_profile_name = "llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K)"
profile_count = 2
event_count = 3
latest_evidence_date = 2026-09-25
+++

## Overview

TokenRhythm · 2 tested configurations · 3 evidence events · newest evidence 2026-09-25.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS** - attributed to the [2026-09-25 event](#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925), configuration llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070.
- **Recommended configuration:** llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) (current-alternate): [event result](#neohorse-1-9b-rtx5070-welp-reasoning-off-20260925).
- **Latest evidence:** 2026-09-25: [event result](#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification READY_WITH_GUARDRAILS. [Event result](#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification READY_WITH_GUARDRAILS. [Event result](#neohorse-1-9b-rtx5070-welp-reasoning-off-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification READY_WITH_GUARDRAILS. [Event result](#neohorse-1-9b-rtx5070-welp-agentic-20260925)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="neohorse-1-9b-rtx5070-welp-reasoning-on-20260925"></a>

### 2026-09-25: First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required)

**WELP Fresh-Model Characterization: NeoHorse-1-9B (Reasoning On, publisher default)** · config llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md)

#### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** not recorded

##### Guardrails and limitations


**Reliability:** not recorded

#### LocalMaxxing

- Status: SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on` |
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-reasoning-on-2026-09-25` |
| Record date | 2026-09-26 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b10999 |
| Runtime tag | `b10999` |
| Runtime commit | `b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063` |
| Runtime build | `build-cuda-sm120` |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

#### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded |
| Guarded context | not recorded |
| Native model-card maximum | not recorded |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

</details>

<a id="neohorse-1-9b-rtx5070-welp-reasoning-off-20260925"></a>

### 2026-09-25: Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model

**WELP Reasoning-Profile Characterization: NeoHorse-1-9B (Reasoning Off, supported alternate)** · config llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md)

#### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** not recorded

##### Guardrails and limitations


**Reliability:** not recorded

#### LocalMaxxing

- Status: SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off` |
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-reasoning-off-2026-09-25` |
| Record date | 2026-09-26 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b10999 |
| Runtime tag | `b10999` |
| Runtime commit | `b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063` |
| Runtime build | `build-cuda-sm120` |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

#### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded |
| Guarded context | not recorded |
| Native model-card maximum | not recorded |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

</details>

<a id="neohorse-1-9b-rtx5070-welp-agentic-20260925"></a>

### 2026-09-25: First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect

**WELP Agentic: NeoHorse-1-9B (publisher-default profile, native tool calls)** · config llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md)

#### WELP outcome

- **Outcome:** COMPLETE_PASS
- **Classification:** not recorded

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** not recorded

##### Guardrails and limitations


**Reliability:** not recorded

#### LocalMaxxing

- Status: SUBMITTED
- Submission reference: not recorded
- verifiedRun: null (not claimed)
<p><small>canonical practical profile Q8_0 llama.cpp; the benchmark workload is reasoning-state invariant</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on` |
| Model | NeoHorse-1-9B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Campaign | `neohorse-1-9b-rtx5070-welp-agentic-2026-09-25` |
| Record date | 2026-09-26 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp b10999 |
| Runtime tag | `b10999` |
| Runtime commit | `b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063` |
| Runtime build | `build-cuda-sm120` |
| Hardware | NVIDIA GeForce RTX 5070 12 GB |

#### Context profile

| Field | Value |
|---|---|
| Practical default | not recorded |
| Guarded context | not recorded |
| Native model-card maximum | not recorded |
| Model-card envelope complete | not recorded |
| Native maximum disposition | not recorded |

</details>

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | Q8_0 official publisher GGUF; f16 K/V cache | llama.cpp b10999 | RTX 5070 | not recorded | 2 (2026-09-25, 2026-09-25) |
| llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | Q8_0 official publisher GGUF; f16 K/V cache | llama.cpp b10999 | RTX 5070 | not recorded | 1 (2026-09-25) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K).
- Profile identity: `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`.
- Status: current tested surface; not the recommended profile.
- Artifact (as recorded): TokenRhythm/NeoHorse-1-9B-GGUF@ddcb4c93 :: NeoHorse-1-9B-Q8_0.gguf (sha256 519869730bda973ec50bb3ac42cd874569e5f3a57c3e0d5d23a2b5040e93310f)
- Runtime (as recorded): llama.cpp b10999.
- Hardware (as recorded): NVIDIA GeForce RTX 5070 12 GB.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on/profile.json)

Events on this configuration:

- [First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required) (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925); status: READY_WITH_GUARDRAILS
- [First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-agentic-20260925); status: READY_WITH_GUARDRAILS

</details>

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K).
- Profile identity: `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`.
- Status: validated alternate tested surface.
- Artifact (as recorded): TokenRhythm/NeoHorse-1-9B-GGUF@ddcb4c93 :: NeoHorse-1-9B-Q8_0.gguf (sha256 519869730bda973ec50bb3ac42cd874569e5f3a57c3e0d5d23a2b5040e93310f)
- Runtime (as recorded): llama.cpp b10999.
- Hardware (as recorded): NVIDIA GeForce RTX 5070 12 GB.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/neohorse-1-9b/profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)

Events on this configuration:

- [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model (2026-09-25)](/evaluations/neohorse-1-9b#neohorse-1-9b-rtx5070-welp-reasoning-off-20260925); status: READY_WITH_GUARDRAILS

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-25 | [First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required)](#neohorse-1-9b-rtx5070-welp-reasoning-on-20260925) | llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | READY_WITH_GUARDRAILS |
| 2026-09-25 | [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model](#neohorse-1-9b-rtx5070-welp-reasoning-off-20260925) | llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | READY_WITH_GUARDRAILS |
| 2026-09-25 | [First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect](#neohorse-1-9b-rtx5070-welp-agentic-20260925) | llama.cpp official Q8_0 (Reasoning On = publisher default, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | READY_WITH_GUARDRAILS |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/neohorse-1-9b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Fresh-Model Characterization: NeoHorse-1-9B (Reasoning On, publisher default)</summary>

- Campaign: `neohorse-1-9b-rtx5070-welp-reasoning-on-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-26
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `neohorse-1-9b-rtx5070-welp-reasoning-on-20260925`, event_type `follow-up`, evidence_maturity `CURRENT_WELP`, model_id `neohorse-1-9b`, profile_id `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`
- Export source pin: repository-cache WumboLabs/evaluations @ `f551e9cc0b00afd5eb8a3bde81ed6f52a12e4e0b` path models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/website-publication.json sha256 `bf4c0f6ad8cb6cef9ea8305576be59f339a466316e15a63a3a18dc61adb6b990`

<p><small>Publication provenance note (as recorded): Native publication of a first fresh-model WELP campaign group under snapshot welp-next-snapshot-2026-09-25-model-agentic; campaign REPORT.md is the primary scientific report; working/raw science retained in local research/model-evaluations/.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Reasoning-Profile Characterization: NeoHorse-1-9B (Reasoning Off, supported alternate)</summary>

- Campaign: `neohorse-1-9b-rtx5070-welp-reasoning-off-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-26
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `neohorse-1-9b-rtx5070-welp-reasoning-off-20260925`, event_type `follow-up`, evidence_maturity `CURRENT_WELP`, model_id `neohorse-1-9b`, profile_id `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`
- Export source pin: repository-cache WumboLabs/evaluations @ `9ecf4f8bd1eed70df5047c64cbe6b1a1b779d1bc` path models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/website-publication.json sha256 `d165d684caa696d516a2b506a0e9c9a8b26ae8ca0a8348918754f6244b5372a3`

<p><small>Publication provenance note (as recorded): Native publication of a first fresh-model WELP campaign group under snapshot welp-next-snapshot-2026-09-25-model-agentic; campaign REPORT.md is the primary scientific report; working/raw science retained in local research/model-evaluations/.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Agentic: NeoHorse-1-9B (publisher-default profile, native tool calls)</summary>

- Campaign: `neohorse-1-9b-rtx5070-welp-agentic-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-26
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/bf5e29e1afee4f391c4b8f83e77636b887453f53/models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `neohorse-1-9b-rtx5070-welp-agentic-20260925`, event_type `follow-up`, evidence_maturity `CURRENT_WELP`, model_id `neohorse-1-9b`, profile_id `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`
- Export source pin: repository-cache WumboLabs/evaluations @ `f551e9cc0b00afd5eb8a3bde81ed6f52a12e4e0b` path models/neohorse-1-9b/events/neohorse-1-9b-rtx5070-welp-agentic-20260925/website-publication.json sha256 `624e4a0197a587ea3c1766901e630d8bb0da337407addc5e798fdf99e0b8e796`

<p><small>Publication provenance note (as recorded): Native publication of a first fresh-model WELP campaign group under snapshot welp-next-snapshot-2026-09-25-model-agentic; campaign REPORT.md is the primary scientific report; working/raw science retained in local research/model-evaluations/.</small></p>

</details>
