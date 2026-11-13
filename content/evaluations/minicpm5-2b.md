+++
title = "MiniCPM5-2B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 17

[extra]
kind = "model"
model_id = "minicpm5-2b"
vendor = "OpenBMB"
findings_first = true
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "minicpm5-2b-vllm-bf16"
recommended_profile_name = "contained vLLM BF16"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-09-10
+++

## Overview

OpenBMB · 1 tested configuration · 1 evidence event · newest evidence 2026-09-10.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS** - attributed to the [2026-09-10 event](#initial-evaluation-2026-09-10-minicpm5), configuration BF16 weights and BF16 KV · vLLM · RTX 5070.
- **Recommended configuration:** contained vLLM BF16 (current): [event result](#initial-evaluation-2026-09-10-minicpm5).
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 131,072 (envelope complete: YES); source: [event result](#initial-evaluation-2026-09-10-minicpm5)
- **Context limit outcome:** Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304; source: [event result](#initial-evaluation-2026-09-10-minicpm5)
- **Latest evidence:** 2026-09-10: [event result](#initial-evaluation-2026-09-10-minicpm5)
- **2026-09-10** · BF16 weights and BF16 KV · vLLM · RTX 5070: classification READY_WITH_GUARDRAILS; 6/7 constrained checks; one deterministic temperature-0 over-refusal of a benign prime-list prompt failed the repeat-check content scorer; repeat consistency itself held; no repair attempted (frozen contract). [Event result](#initial-evaluation-2026-09-10-minicpm5)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="initial-evaluation-2026-09-10-minicpm5"></a>

### 2026-09-10: Initial evaluation (full characterization)

**Initial Evaluation: contained vLLM BF16** · config BF16 weights and BF16 KV · vLLM · RTX 5070 · maturity: FULL_EVALUATION · status: READY_WITH_GUARDRAILS

Configuration: contained vLLM BF16.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md)

#### WELP outcome

- **Outcome:** PASS: MINICPM5_2B_RTX5070_CHARACTERIZED; MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Official BF16 full-precision candidate (characterized; not deployed); architecture-diversity control value HIGH

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.013037 s | Not recorded | 118.622 tok/s |
| Moderate (2663-token input) | 0.203597 s | 13079.8 tok/s | 116.95 tok/s |

<p><small>Medians over five measured repetitions per surface at 8,192 baseline context; near-full ladder medians of two seeds per rung retained in campaign evidence</small></p>

#### Quality and capabilities

- **Constrained result:** 6/7 constrained checks; one deterministic temperature-0 over-refusal of a benign prime-list prompt failed the repeat-check content scorer; repeat consistency itself held; no repair attempted (frozen contract)
- Thinking/reasoning TESTED_PASS; coding TESTED_PASS (4/4 frozen execution cases); native tool selection and tool-result use TESTED_PASS
- English/Chinese text, instruction following, and structured output TESTED_PASS
- Near-full performance inside practical gates through 98,304 (BF16-KV) with zero errors across 55 scientific requests

##### Guardrails and limitations

- Strict long-context output compliance fails at all rungs (format + absent-field), even though content-level retrieval is strong
- Deterministic temperature-0 over-refusal quirk observed on a benign prompt
- fp8-KV scales uncalibrated (kv_scale 1.0); agent benchmarks deferred as out of scope; not autonomous-agent qualification

**Reliability:** 20/20 COMPLETE and passed on a fresh default-context server; zero HTTP/runtime/CUDA/OOM/Xid errors; bounded, not endurance certification

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 118.2
- TTFT: 22.7 ms
- Submission reference: cmtwcna5907f0ps01sfiwd60a
- verifiedRun: NO
<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); benchmarked on the canonical practical stack (BF16, vLLM contained runtime, 32K default, not the 131K fp8 boundary); actual prompt tokens 252 (endpoint usage); verifiedRun false reflects a client capture limitation</small></p>

**Tested condition:** artifact BF16 weights and BF16 KV · vLLM · RTX 5070 · context 32,768 default / 65,536 guarded · native model-card maximum 131,072 tokens · envelope complete: YES.

**Context limit outcome:** Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304

**Context boundaries:** The strict frozen useful-context gate FAILED at every rung (12/12 requests) with exact attribution: markdown-fenced JSON and an omitted absent field cascade the per-field gates. Supplementary content-level analysis (explicitly not a gate) shows 5/5 exact target retrieval at every depth through 65,536 on both seeds and at 131,072 on one of two seeds. A FAILED gate is a completed negative disposition, not VALIDATED; no rung is claimed VALIDATED.

**Runtime conditions:** Qualified contained CUDA 13.0 toolchain (compute_120f/sm_120f); full transformer GPU residency; fresh-cache containment proven; greedy temperature-0 primary surface

**Hardware conditions:** Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `minicpm5-2b-vllm-bf16` |
| Model | MiniCPM5-2B |
| Producer | OpenBMB |
| Official model | openbmb/MiniCPM5-2B @ `cd199ce3ee67549c42ef7372f809f2c63599a3e9` |
| Tested artifact | model-00000-of-00001.safetensors (official BF16; no quantization or conversion) |
| Precision | BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface |
| Artifact SHA-256 | `14fb8e7f0a18d53d1f239773758bf581cee7e456a4523a54622c3a245b64402c` |
| Campaign | `minicpm5-2b-rtx5070-welp-characterization-2026-09-10` |
| Record date | 2026-09-10 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | vLLM 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | Qualified contained CUDA 13.0 toolchain (compute_120f/sm_120f); full transformer GPU residency; fresh-cache containment proven; greedy temperature-0 primary surface |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304 |

<p><small>The strict frozen useful-context gate FAILED at every rung (12/12 requests) with exact attribution: markdown-fenced JSON and an omitted absent field cascade the per-field gates. Supplementary content-level analysis (explicitly not a gate) shows 5/5 exact target retrieval at every depth through 65,536 on both seeds and at 131,072 on one of two seeds. A FAILED gate is a completed negative disposition, not VALIDATED; no rung is claimed VALIDATED.</small></p>

</details>

## Limitations

- Strict long-context output compliance fails at all rungs (format + absent-field), even though content-level retrieval is strong Source events: [2026-09-10](#initial-evaluation-2026-09-10-minicpm5).
- Deterministic temperature-0 over-refusal quirk observed on a benign prompt Source events: [2026-09-10](#initial-evaluation-2026-09-10-minicpm5).
- fp8-KV scales uncalibrated (kv_scale 1.0); agent benchmarks deferred as out of scope; not autonomous-agent qualification Source events: [2026-09-10](#initial-evaluation-2026-09-10-minicpm5).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| BF16 weights and BF16 KV · vLLM · RTX 5070 | BF16 weights and BF16 KV | vLLM | RTX 5070 | 32,768 default / 65,536 guarded | 1 (2026-09-10) |

<details class="lab-findings-configs">
<summary>Configuration details: BF16 weights and BF16 KV · vLLM · RTX 5070</summary>

- Full profile name: contained vLLM BF16.
- Profile identity: `minicpm5-2b-vllm-bf16`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): model-00000-of-00001.safetensors (official BF16; no quantization or conversion)
- Runtime (as recorded): vLLM 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/minicpm5-2b/profiles/minicpm5-2b-vllm-bf16/profile.json)

Events on this configuration:

- [Initial evaluation (full characterization) (2026-09-10)](/evaluations/minicpm5-2b#initial-evaluation-2026-09-10-minicpm5); status: READY_WITH_GUARDRAILS

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-10 | [Initial evaluation (full characterization)](#initial-evaluation-2026-09-10-minicpm5) | BF16 weights and BF16 KV · vLLM · RTX 5070 | READY_WITH_GUARDRAILS |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/minicpm5-2b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-10 Initial Evaluation: contained vLLM BF16</summary>

- Campaign: `minicpm5-2b-rtx5070-welp-characterization-2026-09-10`
- Export disposition: WEBSITE_READY; publication date 2026-09-11
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md`
- Export source pin: repository-cache WumboLabs/evaluations @ `479cb50c197f8ea0dd905a68ffd61f632f49c652` path models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/website-publication.json sha256 `20f817b5c706f0f68319bebe02e1766510c93a6c5249acb8104a57549eb7f7e1`

</details>

### Legacy provenance

- [WumboLabs/eval-minicpm5-2b @ `e0fba74cf21d6cd0bbac0461e9cba8796825429c`](https://github.com/WumboLabs/eval-minicpm5-2b/blob/e0fba74cf21d6cd0bbac0461e9cba8796825429c/EVIDENCE-SUMMARY.md)
