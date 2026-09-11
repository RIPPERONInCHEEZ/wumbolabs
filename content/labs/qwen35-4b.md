+++
title = "Qwen3.5-4B Lab Record"
description = "Comfortable-fit BF16 text control, READY_WITH_GUARDRAILS on the RTX 5070: 32K default / 64K guarded, 67.9 tok/s short decode, 7/7 constrained quality and 20/20 reliability. Full model-card context completion was NOT completed under the later corrected-WELP standard and remains deferred; free-form grounding cautions apply."
date = 2026-09-09
template = "lab_record.html"
weight = 7

[extra]
model = "Qwen3.5-4B"
producer = "Alibaba (Qwen team); GGUF conversion by Unsloth"
quant = "BF16 weights, F16 KV cache, F32 recurrent state"
repo = ""
status = "READY_WITH_GUARDRAILS"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Comfortable-fit BF16 text control, READY_WITH_GUARDRAILS on the RTX 5070: 32K default / 64K guarded, 67.9 tok/s short decode, 7/7 constrained quality and 20/20 reliability. Full model-card context completion was NOT completed under the later corrected-WELP standard and remains deferred; free-form grounding cautions apply."
evidence = "pending"
+++

> **Evidence publication pending.** Canonical public evidence for this
> record has not been published yet (proposed repository: `eval-qwen3.5-4b`).
> This page is a local derivative prepared ahead of publication; no
> canonical evidence URL is claimed. The listed measurements come from
> the accepted local WELP campaign named below.

## Identity

| Field | Value |
|---|---|
| Model | Qwen3.5-4B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` |
| Tested artifact | Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth revision e87f176479d0855a907a41277aca2f8ee7a09523) |
| Precision | BF16 weights, F16 KV cache, F32 recurrent state |
| Artifact SHA-256 | `9e6e2841a75f503ccb330831832fd7861266e187e0dbf149a954219ccb8c197a` |
| Campaign | `qwen35-4b-rtx5070-baseline-2026-09-09` |
| Record date | 2026-09-09 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Runtime notes | All 33/33 runtime layers GPU-resident; CPU-mapped input embedding disclosed; non-thinking text-only greedy surface |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

## WELP outcome

- **Outcome:** PASS — QWEN35_4B_RTX5070_BASELINE_CHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** Comfortable-fit high-precision BF16 text control

Publication state: **evidence pending human gate** — canonical public evidence is not yet published; this record shows an explicit pending state

## Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT COMPLETED under the later corrected-WELP full model-card envelope standard; nothing above 65,536 was tested and the full-card context completion remains deferred |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.040569 s | — | 67.91 tok/s |
| Moderate (3642-token input) | 0.691319 s | 5268.19 tok/s | 67.29 tok/s |

<p><small>Medians over five measured repetitions per surface; client/transport proxies with native timings retained in the campaign evidence</small></p>

## Quality and capabilities

- **Constrained result:** 7/7 constrained checks (factual, structured, retrieval, conflict resistance, absent-field grounding, instruction retention, repeat consistency)
- Bounded exact synthetic retrieval through 65,536 configured tokens
- 20/20 bounded reliability with no CUDA/OOM/Xid events
- Full transformer GPU residency with meaningful operating reserve at 32K

### Guardrails and limitations

- Free-form outputs showed concrete unsupported claims (unfounded checksum/corruption attributions); passing constrained checks does not establish robust free-form grounding
- Coding, tool use, multi-turn autonomous-agent behavior, and vision were not tested
- Context coverage is bounded (two seeds at 32K/64K; 30 target-depth observations); not general long-document understanding

**Reliability:** 20/20 exact-correct bounded requests on a continuous 32K server; no runtime errors; deliberately bounded, not endurance certification

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 68.0 |
| TTFT | 76.92 ms |
| Submission reference | cmtwcmm3207eqps01w7fubuuw |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); verifiedRun false reflects a client capture limitation, recorded honestly; actual prompt tokens 266 (endpoint usage)</small></p>

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
