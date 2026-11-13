+++
title = "Ling 3.0 Tiny"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 5

[extra]
kind = "model"
model_id = "ling-3.0-tiny"
vendor = "inclusionAI (Ant Group)"
findings_first = true
classification = "NOT_READY"
recommended_profile_id = "ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment"
recommended_profile_name = "llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K)"
profile_count = 2
event_count = 4
latest_evidence_date = 2026-09-25
+++

## Overview

inclusionAI (Ant Group) · 2 tested configurations · 4 evidence events · newest evidence 2026-09-25.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: NOT_READY** - attributed to the [2026-09-25 event](#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925), configuration llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070.
- **Recommended configuration:** llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) (current): [event result](#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925).
- **Latest evidence:** 2026-09-25: [event result](#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification NOT_READY. [Event result](#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification NOT_READY. [Event result](#ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925)
- **2026-09-25** · llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification NOT_READY. [Event result](#ling-3-0-tiny-rtx5070-welp-agentic-20260925)
- **2026-09-24** · llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification NOT_READY. [Event result](#ling-3-0-tiny-rtx5070-welp-characterization-20260924)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925"></a>

### 2026-09-25: Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)

**WELP Reasoning-Profile Re-derivation: Ling 3.0 Tiny (Reasoning On, publisher default)** · config llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp official Q8_0 (reasoning-on, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md)

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
<p><small>the engine-native llama-bench record does not exercise the reasoning control, so both reasoning profiles share this record</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment` |
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-reasoning-on-2026-09-25` |
| Record date | 2026-09-25 |

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

<a id="ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925"></a>

### 2026-09-25: Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model

**WELP Reasoning-Profile Characterization: Ling 3.0 Tiny (Reasoning Off, supported alternate)** · config llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md)

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
<p><small>this profile's own bench re-measurement; consistent with the existing service record (benchmark does not exercise the reasoning control; no duplicate submitted)</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off` |
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-reasoning-off-2026-09-25` |
| Record date | 2026-09-25 |

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

<a id="ling-3-0-tiny-rtx5070-welp-agentic-20260925"></a>

### 2026-09-25: First WELP Agentic section execution: three bounded tool tasks through the pinned harness in a disposable offline sandbox; methodology-validation event on a known model

**WELP Agentic: Ling 3.0 Tiny (Reasoning Off; methodology validation)** · config llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/599063be57edd4f3b01f27c33da02d48abc541d8/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-agentic-20260925/REPORT.md)

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
<p><small>this profile's own bench re-measurement; consistent with the existing service record (benchmark does not exercise the reasoning control; no duplicate submitted)</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off` |
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-reasoning-off-2026-09-25` |
| Record date | 2026-09-25 |

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

<a id="ling-3-0-tiny-rtx5070-welp-characterization-20260924"></a>

### 2026-09-24: Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0)

**WELP Initial Evaluation: inclusionAI Ling 3.0 Tiny (reasoning-on)** · config llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp official Q8_0 (reasoning-on, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/43f56d8add4b3dfc51183ccd818fc6037e79bd9c/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md)

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

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment` |
| Model | Ling 3.0 Tiny |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6` |
| Campaign | `ling-3.0-tiny-rtx5070-welp-characterization-2026-09-24` |
| Record date | 2026-09-24 |

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
| llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | Q8_0 official publisher GGUF; f16 K/V cache | llama.cpp b10999 | RTX 5070 | not recorded | 2 (2026-09-24, 2026-09-25) |
| llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | Q8_0 official publisher GGUF; f16 K/V cache | llama.cpp b10999 | RTX 5070 | not recorded | 2 (2026-09-25, 2026-09-25) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K).
- Profile identity: `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (24/24 layers), -fa on, f16 KV, -np 1, embedded GGUF Bailing-V3 Jinja template, DEPLOYMENT sampler (temp 0.2 / top_k 80 / top_p 1.0 / repeat_penalty 1.05); effective reasoning ON (bailing v3 thinking default; enable_thinking=false OFF control proven effective but not the campaign profile). Default context 32,768 / native exact 131,072 / advertised 262,144 (YaRN x2.0, mechanism-qualified on this runtime); uncached scientific arms via --cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0 with cache_prompt:false (proven by repeated-prompt probe). Publisher sampler (temp 1.0 / top_k 20 / top_p 0.95) measured as a matched comparison, never pooled.
- Artifact (as recorded): inclusionAI/Ling-3.0-tiny-GGUF@01b850e2 :: Ling-3.0-tiny-Q8_0.gguf (sha256 9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6)
- Runtime (as recorded): llama.cpp b10999.
- Hardware (as recorded): NVIDIA GeForce RTX 5070 12 GB.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment/profile.json)

Events on this configuration:

- [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference) (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925); status: NOT_READY
- [Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0) (2026-09-24)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-characterization-20260924); status: NOT_READY

</details>

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K).
- Profile identity: `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`.
- Status: validated alternate tested surface.
- Artifact (as recorded): inclusionAI/Ling-3.0-tiny-GGUF@01b850e2 :: Ling-3.0-tiny-Q8_0.gguf (sha256 9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6)
- Runtime (as recorded): llama.cpp b10999.
- Hardware (as recorded): NVIDIA GeForce RTX 5070 12 GB.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/ling-3.0-tiny/profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/profile.json)

Events on this configuration:

- [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925); status: NOT_READY
- [First WELP Agentic section execution: three bounded tool tasks through the pinned harness in a disposable offline sandbox; methodology-validation event on a known model (2026-09-25)](/evaluations/ling-3-0-tiny#ling-3-0-tiny-rtx5070-welp-agentic-20260925); status: NOT_READY

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-25 | [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)](#ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925) | llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | NOT_READY |
| 2026-09-25 | [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model](#ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925) | llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | NOT_READY |
| 2026-09-25 | [First WELP Agentic section execution: three bounded tool tasks through the pinned harness in a disposable offline sandbox; methodology-validation event on a known model](#ling-3-0-tiny-rtx5070-welp-agentic-20260925) | llama.cpp official Q8_0 (Reasoning Off, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | NOT_READY |
| 2026-09-24 | [Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0)](#ling-3-0-tiny-rtx5070-welp-characterization-20260924) | llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | NOT_READY |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/ling-3.0-tiny)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Reasoning-Profile Re-derivation: Ling 3.0 Tiny (Reasoning On, publisher default)</summary>

- Campaign: `ling-3.0-tiny-rtx5070-welp-reasoning-on-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-25
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925`, event_type `follow-up`, evidence_scope `['reliability', 'context', 'capabilities', 'performance', 'localmaxxing', 'model-classification']`, model_id `ling-3.0-tiny`, profile_id `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`, profile_status `current`, related_profile_ids `['ling-3-0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off']`
- Export source pin: repository-cache WumboLabs/evaluations @ `c41e09b5909f633e3d9093747398e162e17a50c4` path models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/website-publication.json sha256 `84a8a7153682ff4d311ffc082b04758ddae1662a73983164c309b14dfb74f2e3`

<p><small>Publication provenance note (as recorded): Reuse/re-derivation event under welp-reasoning-topology-0.1.0-draft: full migration matrix (REUSE/RE-DERIVED/INCOMPARABLE) in the campaign's REUSE-MIGRATION.md; the source event stays immutable. Executed under snapshot welp-next-snapshot-2026-09-25-reasoning-profiles (WELP commit 193cb645c81440cc1232447f3ebc32a8197a7f3e, DRAFT - NOT v1.0).</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Reasoning-Profile Characterization: Ling 3.0 Tiny (Reasoning Off, supported alternate)</summary>

- Campaign: `ling-3.0-tiny-rtx5070-welp-reasoning-off-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-25
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/a5717d2fecc21184da6dfa20d973fb8e4fbca0e4/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925`, event_type `follow-up`, evidence_scope `['reliability', 'context', 'capabilities', 'performance', 'localmaxxing', 'model-classification']`, model_id `ling-3.0-tiny`, profile_id `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`, profile_status `current-alternate`, related_profile_ids `['ling-3-0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment']`
- Export source pin: repository-cache WumboLabs/evaluations @ `c41e09b5909f633e3d9093747398e162e17a50c4` path models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/website-publication.json sha256 `5a5374c9e13a9ca7fcc89e7e8bbf48be18d7d5933f42685988b1f309192959a3`

<p><small>Publication provenance note (as recorded): Full independent WELP profile campaign under welp-next-snapshot-2026-09-25-reasoning-profiles (WELP commit 193cb645c81440cc1232447f3ebc32a8197a7f3e, DRAFT - NOT v1.0); artifact restored from the verified canonical archive with SHA-256 re-verification; LocalMaxxing VERIFIED_EXISTING (the llama-bench record does not exercise the reasoning control).</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-25 WELP Agentic: Ling 3.0 Tiny (Reasoning Off; methodology validation)</summary>

- Campaign: `ling-3.0-tiny-rtx5070-welp-reasoning-off-2026-09-25`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-25
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/599063be57edd4f3b01f27c33da02d48abc541d8/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-agentic-20260925/REPORT.md`
- Export identity: event_date `2026-09-25`, event_id `ling-3-0-tiny-rtx5070-welp-agentic-20260925`, event_type `welp-agentic-methodology-validation`, evidence_scope `['agentic-task-outcomes', 'agentic-methodology-validation']`, model_id `ling-3.0-tiny`, profile_id `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`, profile_status `current-alternate`
- Export source pin: repository-cache WumboLabs/evaluations @ `0382fc7dd89fd403869fa3d81830adc15233da7b` path models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-agentic-20260925/website-publication.json sha256 `5044e15ea13bbfc65819cac929429e7357b2ce43f8bff52dba2ee8f32f049ce6`

<p><small>Publication provenance note (as recorded): METHODOLOGY_VALIDATION event under welp-next-snapshot-2026-09-25-model-agentic (WELP commit 5f611de36e44a2d06fa41acd75aa62dcf66c0edb, DRAFT - NOT v1.0). Agentic verdict reported independently of the Model verdict; never averaged.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-24 WELP Initial Evaluation: inclusionAI Ling 3.0 Tiny (reasoning-on)</summary>

- Campaign: `ling-3.0-tiny-rtx5070-welp-characterization-2026-09-24`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-24
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/43f56d8add4b3dfc51183ccd818fc6037e79bd9c/models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md`
- Export identity: event_date `2026-09-24`, event_id `ling-3-0-tiny-rtx5070-welp-characterization-20260924`, event_type `initial-evaluation`, model_id `ling-3.0-tiny`, profile_id `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `719810861ab6d02136ea68fdd5d5e4e34e3e4ddb` path models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/website-publication.json sha256 `128e900f0a2f3965b0833ad30c7ec5f5654a82b07e3a3cea9571ba2ca0f83871`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; the campaign completed on the success branch with zero methodology defects (WELP stabilization campaign CLEAN, clean-count 2). Executed under snapshot welp-next-snapshot-2026-09-24-context-outcome-repair (WELP commit ead28bde1ea9bce20cec6b3930125016068a8bbc, DRAFT - NOT v1.0); classification contract welp-final-classification-0.4.0-draft; verdict NOT_READY (R-C3) with campaign execution COMPLETE_PASS.</small></p>

</details>
