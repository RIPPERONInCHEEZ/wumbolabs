+++
title = "MiniCPM5-2B"
description = "MiniCPM5-2B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 9

[extra]
kind = "model"
model_id = "minicpm5-2b"
vendor = "OpenBMB"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "minicpm5-2b-vllm-bf16"
recommended_profile_name = "contained vLLM BF16"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 1
event_count = 1
latest_event_date = 2026-09-10
+++

WumboLabs tests **MiniCPM5-2B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Initial evaluation (full characterization) (2026-09-10)](/evaluations/minicpm5-2b#initial-evaluation-2026-09-10-minicpm5), profile contained vLLM BF16
- **Recommended profile:** contained vLLM BF16 (`minicpm5-2b-vllm-bf16`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md)
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 131,072 (envelope complete: YES) — [Initial evaluation (full characterization) (2026-09-10)](/evaluations/minicpm5-2b#initial-evaluation-2026-09-10-minicpm5)
- **Latest evidence:** 2026-09-10 — Initial evaluation (full characterization)

## Tested profiles

### contained vLLM BF16 — CURRENT

Profile identity: `minicpm5-2b-vllm-bf16`.

| Field | Value |
|---|---|
| Runtime | vLLM 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3 |
| Artifact | model-00000-of-00001.safetensors (official BF16; no quantization or conversion) |
| Precision | BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/minicpm5-2b/profiles/minicpm5-2b-vllm-bf16/profile.json)

Events on this profile:

- [Initial evaluation (full characterization) (2026-09-10)](/evaluations/minicpm5-2b#initial-evaluation-2026-09-10-minicpm5) — READY_WITH_GUARDRAILS

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="initial-evaluation-2026-09-10-minicpm5"></a>

### 2026-09-10 — Initial evaluation (full characterization)

**Initial Evaluation — contained vLLM BF16** · profile: contained vLLM BF16 · maturity: FULL_EVALUATION · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/minicpm5-2b)

##### Identity

| Field | Value |
|---|---|
| Model | MiniCPM5-2B |
| Producer | OpenBMB |
| Official model | openbmb/MiniCPM5-2B @ `cd199ce3ee67549c42ef7372f809f2c63599a3e9` |
| Tested artifact | model-00000-of-00001.safetensors (official BF16; no quantization or conversion) |
| Precision | BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface |
| Artifact SHA-256 | `14fb8e7f0a18d53d1f239773758bf581cee7e456a4523a54622c3a245b64402c` |
| Campaign | `minicpm5-2b-rtx5070-welp-characterization-2026-09-10` |
| Record date | 2026-09-10 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | vLLM |
| Runtime version | 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3 |
| Runtime notes | Qualified contained CUDA 13.0 toolchain (compute_120f/sm_120f); full transformer GPU residency; fresh-cache containment proven; greedy temperature-0 primary surface |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

##### WELP outcome

- **Outcome:** PASS — MINICPM5_2B_RTX5070_CHARACTERIZED; MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Official BF16 full-precision candidate (characterized; not deployed); architecture-diversity control value HIGH

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304 |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.013037 s | — | 118.622 tok/s |
| Moderate (2663-token input) | 0.203597 s | 13079.8 tok/s | 116.95 tok/s |

<p><small>Medians over five measured repetitions per surface at 8,192 baseline context; near-full ladder medians of two seeds per rung retained in campaign evidence</small></p>

##### Quality and capabilities

- **Constrained result:** 6/7 constrained checks — one deterministic temperature-0 over-refusal of a benign prime-list prompt failed the repeat-check content scorer; repeat consistency itself held; no repair attempted (frozen contract)
- Thinking/reasoning TESTED_PASS; coding TESTED_PASS (4/4 frozen execution cases); native tool selection and tool-result use TESTED_PASS
- English/Chinese text, instruction following, and structured output TESTED_PASS
- Near-full performance inside practical gates through 98,304 (BF16-KV) with zero errors across 55 scientific requests

###### Guardrails and limitations

- Strict long-context output compliance fails at all rungs (format + absent-field), even though content-level retrieval is strong
- Deterministic temperature-0 over-refusal quirk observed on a benign prompt
- fp8-KV scales uncalibrated (kv_scale 1.0); agent benchmarks deferred as out of scope; not autonomous-agent qualification

**Reliability:** 20/20 COMPLETE and passed on a fresh default-context server; zero HTTP/runtime/CUDA/OOM/Xid errors; bounded, not endurance certification

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 118.2 |
| TTFT | 22.7 ms |
| Submission reference | cmtwcna5907f0ps01sfiwd60a |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); benchmarked on the canonical practical stack (BF16, vLLM contained runtime, 32K default — not the 131K fp8 boundary); actual prompt tokens 252 (endpoint usage); verifiedRun false reflects a client capture limitation</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/minicpm5-2b/events/initial-evaluation-2026-09-10-minicpm5/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **minicpm5-2b-vllm-bf16**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/db63d6f89b2aeb75279eb4292bda6d0a4d9213c7/models/minicpm5-2b/profiles/minicpm5-2b-vllm-bf16/profile.json)

### Legacy provenance

- [WumboLabs/eval-minicpm5-2b @ `e0fba74cf21d6cd0bbac0461e9cba8796825429c`](https://github.com/WumboLabs/eval-minicpm5-2b/blob/e0fba74cf21d6cd0bbac0461e9cba8796825429c/EVIDENCE-SUMMARY.md)
