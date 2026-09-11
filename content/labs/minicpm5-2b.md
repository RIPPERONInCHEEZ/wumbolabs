+++
title = "MiniCPM5-2B Lab Record"
description = "Official BF16 full-precision characterization on a contained vLLM runtime, READY_WITH_GUARDRAILS: 32K default / 64K guarded, complete 131K model-card envelope (98K highest BF16-KV rung; exact 131K FIT_LIMIT on BF16-KV and strict-gate FAILED on the authorized fp8-KV surface), 118.6 tok/s decode, thinking/coding/tools PASS, 20/20 reliability."
date = 2026-09-10
template = "lab_record.html"
weight = 9

[extra]
model = "MiniCPM5-2B"
producer = "OpenBMB"
quant = "BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface"
repo = ""
status = "READY_WITH_GUARDRAILS"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Official BF16 full-precision characterization on a contained vLLM runtime, READY_WITH_GUARDRAILS: 32K default / 64K guarded, complete 131K model-card envelope (98K highest BF16-KV rung; exact 131K FIT_LIMIT on BF16-KV and strict-gate FAILED on the authorized fp8-KV surface), 118.6 tok/s decode, thinking/coding/tools PASS, 20/20 reliability."
evidence = "pending"
+++

> **Evidence publication pending.** Canonical public evidence for this
> record has not been published yet (proposed repository: `eval-minicpm5-2b`).
> This page is a local derivative prepared ahead of publication; no
> canonical evidence URL is claimed. The listed measurements come from
> the accepted local WELP campaign named below.

## Identity

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

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | vLLM |
| Runtime version | 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3 |
| Runtime notes | Qualified contained CUDA 13.0 toolchain (compute_120f/sm_120f); full transformer GPU residency; fresh-cache containment proven; greedy temperature-0 primary surface |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

## WELP outcome

- **Outcome:** PASS — MINICPM5_2B_RTX5070_CHARACTERIZED; MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Official BF16 full-precision candidate (characterized; not deployed); architecture-diversity control value HIGH

Publication state: **evidence pending human gate** — canonical public evidence is not yet published; this record shows an explicit pending state

## Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 131072 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304 |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.013037 s | — | 118.622 tok/s |
| Moderate (2663-token input) | 0.203597 s | 13079.8 tok/s | 116.95 tok/s |

<p><small>Medians over five measured repetitions per surface at 8,192 baseline context; near-full ladder medians of two seeds per rung retained in campaign evidence</small></p>

## Quality and capabilities

- **Constrained result:** 6/7 constrained checks — one deterministic temperature-0 over-refusal of a benign prime-list prompt failed the repeat-check content scorer; repeat consistency itself held; no repair attempted (frozen contract)
- Thinking/reasoning TESTED_PASS; coding TESTED_PASS (4/4 frozen execution cases); native tool selection and tool-result use TESTED_PASS
- English/Chinese text, instruction following, and structured output TESTED_PASS
- Near-full performance inside practical gates through 98,304 (BF16-KV) with zero errors across 55 scientific requests

### Guardrails and limitations

- Strict long-context output compliance fails at all rungs (format + absent-field), even though content-level retrieval is strong
- Deterministic temperature-0 over-refusal quirk observed on a benign prompt
- fp8-KV scales uncalibrated (kv_scale 1.0); agent benchmarks deferred as out of scope; not autonomous-agent qualification

**Reliability:** 20/20 COMPLETE and passed on a fresh default-context server; zero HTTP/runtime/CUDA/OOM/Xid errors; bounded, not endurance certification

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 118.2 |
| TTFT | 22.7 ms |
| Submission reference | cmtwcna5907f0ps01sfiwd60a |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); benchmarked on the canonical practical stack (BF16, vLLM contained runtime, 32K default — not the 131K fp8 boundary); actual prompt tokens 252 (endpoint usage); verifiedRun false reflects a client capture limitation</small></p>

## Canonical evidence

State: **PENDING_HUMAN_GATE** — the canonical public evidence repository
has not been published yet. This record intentionally claims no canonical
evidence URL. Once the evidence repository is published and the registry is
updated, this record synchronizes against it and the pending state is removed.

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
