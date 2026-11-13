+++
title = "Qwen3.5-4B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 15

[extra]
kind = "model"
model_id = "qwen35-4b"
vendor = "Alibaba (Qwen team)"
findings_first = true
recommended_profile_id = "qwen35-4b-llamacpp-bf16"
recommended_profile_name = "llama.cpp BF16 GGUF"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-11
+++

## Overview

Alibaba (Qwen team) · 1 tested configuration · 1 evidence event · newest evidence 2026-09-11.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** llama.cpp BF16 GGUF (current): [event result](#context-envelope-completion-2026-09-11-qwen35-4b).
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 262,144 (envelope complete: YES); source: [event result](#context-envelope-completion-2026-09-11-qwen35-4b)
- **Context limit outcome:** FIT_LIMIT - native maximum 262,144 on the BF16/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision; source: [event result](#context-envelope-completion-2026-09-11-qwen35-4b)
- **Latest evidence:** 2026-09-11: [event result](#context-envelope-completion-2026-09-11-qwen35-4b)
- **2026-09-11** · BF16 weights; f16 KV · llama.cpp · RTX 5070: classification READY_WITH_GUARDRAILS; inherited: 7/7 constrained checks and 20/20 bounded reliability (baseline campaign, unchanged, not rerun). [Event result](#context-envelope-completion-2026-09-11-qwen35-4b)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="context-envelope-completion-2026-09-11-qwen35-4b"></a>

### 2026-09-11: Context envelope completion

**Context Envelope: llama.cpp BF16** · config BF16 weights; f16 KV · llama.cpp · RTX 5070 · maturity: CONTEXT_COMPLETION · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp BF16 GGUF.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-4b/events/context-envelope-completion-2026-09-11-qwen35-4b/REPORT.md)

#### WELP outcome

- **Outcome:** PASS: QWEN35_4B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** READY_WITH_GUARDRAILS (unchanged; new occupancy-dependent instruction-retention guardrail added)
- **Artifact classification:** Comfortable-fit high-precision BF16 text control

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.040569 s | Not recorded | 67.91 tok/s |
| Moderate (3642-token input) | 0.691319 s | 5268.19 tok/s | 67.29 tok/s |

<p><small>Near-full context fixture medians per seed pair; client/transport proxies with native timings retained in campaign evidence; short/moderate surfaces inherited unchanged from the baseline campaign (67.9 tok/s short decode, 0.69 s moderate TTFT)</small></p>

#### Quality and capabilities

- **Constrained result:** inherited: 7/7 constrained checks and 20/20 bounded reliability (baseline campaign, unchanged, not rerun)
- Perfect synthetic retrieval (20/20 values) at 99.4-99.5% occupancy through 64K on the primary surface
- Highest measured/admitted near-full primary context 65,536 (guarded profile confirmed); 98,304 projected below the frozen operational safety floor and intentionally not launched; exact ceiling not bracketed
- q4_0-KV alternate surface functionally correct at 32K
- Official YaRN mechanism representable in the pinned runtime

##### Guardrails and limitations

- Near-full-occupancy instruction retention defect: auxiliary JSON fields (synthesis/absent/checksum) dropped at both rungs, both seeds; do not place binding output instructions at extreme occupancy
- Inherited free-form grounding cautions unchanged
- Exact native maximum and YaRN maximum are unreachable on 12GB at any representable KV precision; not a model-capability claim on other hardware

**Reliability:** inherited bounded 20/20 reliability (profile unchanged); no new reliability run required; context-specific observations: zero CUDA/OOM/Xid events across all arms including the measured admission-failure attempt

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 68.0
- TTFT: 76.92 ms
- Submission reference: cmtwcmm3207eqps01w7fubuuw
- verifiedRun: NO
<p><small>origin VERIFIED_EXISTING (duplicate audit): canonical practical profile unchanged; no new benchmark, no duplicate submission</small></p>

**Tested condition:** artifact BF16 weights; f16 KV · llama.cpp · RTX 5070 · context 32,768 default / 65,536 guarded · native model-card maximum 262,144 tokens · envelope complete: YES.

**Context limit outcome:** FIT_LIMIT - native maximum 262,144 on the BF16/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision

**Context boundaries:** 32K default and 64K guarded profile both reevaluated at the current WELP near-full standard and confirmed; occupied 32K performance 6.6-6.7 s TTFT / 60.3 tok/s decode; 64K 15.2 s TTFT / 54.1-54.4 tok/s decode

**Runtime conditions:** All 33/33 runtime layers GPU-resident; non-thinking text-only greedy surface; identical inherited baseline stack

**Hardware conditions:** Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `qwen35-4b-llamacpp-bf16` |
| Model | Qwen3.5-4B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` |
| Tested artifact | Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth revision e87f176479d0855a907a41277aca2f8ee7a09523) |
| Precision | BF16 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |
| Artifact SHA-256 | `9e6e2841a75f503ccb330831832fd7861266e187e0dbf149a954219ccb8c197a` |
| Campaign | `qwen35-4b-rtx5070-context-completion-2026-09-11` |
| Record date | 2026-09-09 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | All 33/33 runtime layers GPU-resident; non-thinking text-only greedy surface; identical inherited baseline stack |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - native maximum 262,144 on the BF16/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision |

<p><small>32K default and 64K guarded profile both reevaluated at the current WELP near-full standard and confirmed; occupied 32K performance 6.6-6.7 s TTFT / 60.3 tok/s decode; 64K 15.2 s TTFT / 54.1-54.4 tok/s decode</small></p>

</details>

## Limitations

- Near-full-occupancy instruction retention defect: auxiliary JSON fields (synthesis/absent/checksum) dropped at both rungs, both seeds; do not place binding output instructions at extreme occupancy Source events: [2026-09-11](#context-envelope-completion-2026-09-11-qwen35-4b).
- Inherited free-form grounding cautions unchanged Source events: [2026-09-11](#context-envelope-completion-2026-09-11-qwen35-4b).
- Exact native maximum and YaRN maximum are unreachable on 12GB at any representable KV precision; not a model-capability claim on other hardware Source events: [2026-09-11](#context-envelope-completion-2026-09-11-qwen35-4b).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| BF16 weights; f16 KV · llama.cpp · RTX 5070 | BF16 weights; f16 KV | llama.cpp | RTX 5070 | 32,768 default / 65,536 guarded | 1 (2026-09-11) |

<details class="lab-findings-configs">
<summary>Configuration details: BF16 weights; f16 KV · llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp BF16 GGUF.
- Profile identity: `qwen35-4b-llamacpp-bf16`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth rev e87f176479d0855a907a41277aca2f8ee7a09523)
- Runtime (as recorded): llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120).
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen35-4b/profiles/qwen35-4b-llamacpp-bf16/profile.json)

Events on this configuration:

- [Context envelope completion (2026-09-11)](/evaluations/qwen35-4b#context-envelope-completion-2026-09-11-qwen35-4b); status: READY_WITH_GUARDRAILS

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-11 | [Context envelope completion](#context-envelope-completion-2026-09-11-qwen35-4b) | BF16 weights; f16 KV · llama.cpp · RTX 5070 | READY_WITH_GUARDRAILS |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/qwen35-4b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-11 Context Envelope: llama.cpp BF16</summary>

- Campaign: `qwen35-4b-rtx5070-context-completion-2026-09-11`
- Export disposition: WEBSITE_READY; publication date 2026-09-11
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-4b/events/context-envelope-completion-2026-09-11-qwen35-4b/REPORT.md`
- Export source pin: repository-cache WumboLabs/evaluations @ `479cb50c197f8ea0dd905a68ffd61f632f49c652` path models/qwen35-4b/events/context-envelope-completion-2026-09-11-qwen35-4b/website-publication.json sha256 `3c8fab5a1dcea73dd57a5296a00fd8238caf1b3eb8dd28be7fb2d5d56ee4bb04`

</details>

### Legacy provenance

- [WumboLabs/eval-qwen3.5-4b @ `c85ec602269eeb01d3cf3c50b5f9a76506338e66`](https://github.com/WumboLabs/eval-qwen3.5-4b/blob/c85ec602269eeb01d3cf3c50b5f9a76506338e66/reports/qwen35-4b-context-envelope-completion-2026-09-11.md)
