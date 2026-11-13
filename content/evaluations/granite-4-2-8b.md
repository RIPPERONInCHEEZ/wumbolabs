+++
title = "Granite 4.2 8B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 7

[extra]
kind = "model"
model_id = "granite-4.2-8b"
vendor = "IBM (ibm-granite)"
findings_first = true
classification = "NOT_READY"
recommended_profile_id = "granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment"
recommended_profile_name = "llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K)"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-24
+++

## Overview

IBM (ibm-granite) · 1 tested configuration · 1 evidence event · newest evidence 2026-09-24.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: NOT_READY** - attributed to the [2026-09-24 event](#granite-42-8b-rtx5070-welp-context-completion-20260924), configuration llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070.
- **Recommended configuration:** llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) (current): [event result](#granite-42-8b-rtx5070-welp-context-completion-20260924).
- **Latest evidence:** 2026-09-24: [event result](#granite-42-8b-rtx5070-welp-context-completion-20260924)
- **2026-09-24** · llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070: classification NOT_READY. [Event result](#granite-42-8b-rtx5070-welp-context-completion-20260924)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="granite-42-8b-rtx5070-welp-context-completion-20260924"></a>

### 2026-09-24: First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)

**WELP Initial Evaluation: IBM Granite 4.2 8B (reasoning-on)** · config llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 · maturity: CURRENT_WELP · status: NOT_READY

Methodology snapshot: `welp-next-snapshot-2026-09-24-context-outcome-repair` · WELP commit `ead28bde1ea9bce20cec6b3930125016068a8bbc`

Configuration: llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md)

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
<p><small>SUBMITTED/NEW, service record cmug9qe0i0d5wlq01lep45uua (APPROVED, verifiedRun false)</small></p>

**Tested condition:** llama.cpp b10999 · RTX 5070.

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment` |
| Model | Granite 4.2 8B |
| Producer | not recorded |
| Tested artifact | not recorded |
| Precision | not recorded |
| Artifact SHA-256 | `16a9369d0805f80b7377d25d87f937a90c05dc04ad79173a52001e42c9aab311` |
| Campaign | `granite-4.2-8b-rtx5070-welp-context-outcome-completion-2026-09-24` |
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
| llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | Q4_K_M official publisher GGUF; f16 K/V cache | llama.cpp b10999 | RTX 5070 | not recorded | 1 (2026-09-24) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070</summary>

- Full profile name: llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K).
- Profile identity: `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (40/40 layers), -fa on, f16 KV, -np 1, embedded GGUF Jinja template, DEPLOYMENT sampler (temp 0.2 / top_k 80 / top_p 1.0 / repeat_penalty 1.05); effective reasoning ON (built-in thinking; OFF control proven effective but not the campaign profile). Default context 32,768 / native exact 131,072; uncached scientific arms via --cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0 with cache_prompt:false (proven by repeated-prompt probe). Publisher sampler (temp 1.0 / top_p 0.95) measured as a matched comparison, never pooled.
- Artifact (as recorded): ibm-granite/granite-4.2-8b-GGUF@93f3f6a8 :: granite-4.2-8b-Q4_K_M.gguf (sha256 16a9369d0805f80b7377d25d87f937a90c05dc04ad79173a52001e42c9aab311)
- Runtime (as recorded): llama.cpp b10999.
- Hardware (as recorded): NVIDIA GeForce RTX 5070 12 GB.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/granite-4.2-8b/profiles/granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment/profile.json)

Events on this configuration:

- [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999) (2026-09-24)](/evaluations/granite-4-2-8b#granite-42-8b-rtx5070-welp-context-completion-20260924); status: NOT_READY

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-24 | [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)](#granite-42-8b-rtx5070-welp-context-completion-20260924) | llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K) · llama.cpp b10999 · RTX 5070 | NOT_READY |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/granite-4.2-8b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-24 WELP Initial Evaluation: IBM Granite 4.2 8B (reasoning-on)</summary>

- Campaign: `granite-4.2-8b-rtx5070-welp-context-outcome-completion-2026-09-24`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-24
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/adcfa178b6dd9b52eede2c433ffc691dbcd26941/models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md`
- Export identity: event_date `2026-09-24`, event_id `granite-42-8b-rtx5070-welp-context-completion-20260924`, event_type `initial-evaluation`, model_id `granite-4.2-8b`, predecessor_campaign `granite-4.2-8b-rtx5070-welp-characterization-2026-09-24`, profile_id `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`, profile_status `current`
- Export source pin: repository-cache WumboLabs/evaluations @ `250afdf042677d8c6dc19275c357ad0f5a2b870a` path models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/website-publication.json sha256 `978d09e20e166ff7ecec559a1b10a5a7d3de10292aa663ac3e6ce6e018cced1b`

<p><small>Publication provenance note (as recorded): Native current-WELP linked completion event under the consolidated architecture. The retained COMPLETE_WITH_GAPS predecessor campaign is preserved unchanged and unpublished; every raw evidence file is reused byte-identically (size + SHA-256 verified); only the answerless context cell's disposition/outcome is re-derived from original raw bytes under welp-context 0.3.0-draft.</small></p>

</details>
