+++
title = "Qwen3.5-4B Lab Record"
description = "Full model-card context envelope now COMPLETE with evidence-backed dispositions: native 262,144 FIT_LIMIT (f16 lower bound; q4_0 measured admission failure), YaRN 1,010,000 FIT_LIMIT (all representable KV precisions), 32K/64K revalidated at >=99.4% near-full occupancy with perfect retrieval and a measured auxiliary-instruction retention defect. Practical profile unchanged: 32K default, 64K guarded, READY_WITH_GUARDRAILS."
date = 2026-09-09
template = "lab_record.html"
weight = 7

[extra]
model = "Qwen3.5-4B"
producer = "Alibaba (Qwen team); GGUF conversion by Unsloth"
quant = "BF16 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface)"
repo = "https://github.com/WumboLabs/eval-qwen3.5-4b"
status = "READY_WITH_GUARDRAILS"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Full model-card context envelope now COMPLETE with evidence-backed dispositions: native 262,144 FIT_LIMIT (f16 lower bound; q4_0 measured admission failure), YaRN 1,010,000 FIT_LIMIT (all representable KV precisions), 32K/64K revalidated at >=99.4% near-full occupancy with perfect retrieval and a measured auxiliary-instruction retention defect. Practical profile unchanged: 32K default, 64K guarded, READY_WITH_GUARDRAILS."
evidence = "published"
+++

## Identity

| Field | Value |
|---|---|
| Model | Qwen3.5-4B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` |
| Tested artifact | Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth revision e87f176479d0855a907a41277aca2f8ee7a09523) |
| Precision | BF16 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |
| Artifact SHA-256 | `9e6e2841a75f503ccb330831832fd7861266e187e0dbf149a954219ccb8c197a` |
| Campaign | `qwen35-4b-rtx5070-context-completion-2026-09-11` |
| Record date | 2026-09-09 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Runtime notes | All 33/33 runtime layers GPU-resident; non-thinking text-only greedy surface; identical inherited baseline stack |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

## WELP outcome

- **Outcome:** PASS — QWEN35_4B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** READY_WITH_GUARDRAILS (unchanged; new occupancy-dependent instruction-retention guardrail added)
- **Artifact classification:** Comfortable-fit high-precision BF16 text control

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/eval-qwen3.5-4b

## Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - native maximum 262,144 on the BF16/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.040569 s | — | 67.91 tok/s |
| Moderate (3642-token input) | 0.691319 s | 5268.19 tok/s | 67.29 tok/s |

<p><small>Near-full context fixture medians per seed pair; client/transport proxies with native timings retained in campaign evidence; short/moderate surfaces inherited unchanged from the baseline campaign (67.9 tok/s short decode, 0.69 s moderate TTFT)</small></p>

## Quality and capabilities

- **Constrained result:** inherited: 7/7 constrained checks and 20/20 bounded reliability (baseline campaign, unchanged, not rerun)
- Perfect synthetic retrieval (20/20 values) at 99.4-99.5% occupancy through 64K on the primary surface
- q4_0-KV alternate surface functionally correct at 32K
- Official YaRN mechanism representable in the pinned runtime

### Guardrails and limitations

- Near-full-occupancy instruction retention defect: auxiliary JSON fields (synthesis/absent/checksum) dropped at both rungs, both seeds; do not place binding output instructions at extreme occupancy
- Inherited free-form grounding cautions unchanged
- Exact native maximum and YaRN maximum are unreachable on 12GB at any representable KV precision; not a model-capability claim on other hardware

**Reliability:** inherited bounded 20/20 reliability (profile unchanged); no new reliability run required; context-specific observations: zero CUDA/OOM/Xid events across all arms including the measured admission-failure attempt

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 68.0 |
| TTFT | 76.92 ms |
| Submission reference | cmtwcmm3207eqps01w7fubuuw |
| verifiedRun | NO |

<p><small>origin VERIFIED_EXISTING (duplicate audit): canonical practical profile unchanged; no new benchmark, no duplicate submission</small></p>

## Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/eval-qwen3.5-4b>

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
