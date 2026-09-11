+++
title = "Qwen3.5-9B Lab Record"
description = "Medium-fit Q8_0 quantized control (BF16 cannot fit), READY_WITH_GUARDRAILS: 32K default / 64K guarded, 66.7 tok/s short decode, 7/7 constrained quality and 20/20 reliability. The full revised context envelope remains deferred and quality superiority over 4B is unproven; this is not a high-precision BF16 result."
date = 2026-09-09
template = "lab_record.html"
weight = 8

[extra]
model = "Qwen3.5-9B"
producer = "Alibaba (Qwen team); GGUF conversion by Unsloth"
quant = "Q8_0 weights (acquired), F16 KV cache, F32 recurrent state"
repo = "https://github.com/WumboLabs/eval-qwen3.5-9b"
status = "READY_WITH_GUARDRAILS"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Medium-fit Q8_0 quantized control (BF16 cannot fit), READY_WITH_GUARDRAILS: 32K default / 64K guarded, 66.7 tok/s short decode, 7/7 constrained quality and 20/20 reliability. The full revised context envelope remains deferred and quality superiority over 4B is unproven; this is not a high-precision BF16 result."
evidence = "published"
+++

## Identity

| Field | Value |
|---|---|
| Model | Qwen3.5-9B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-9B @ `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| Tested artifact | Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) |
| Precision | Q8_0 weights (acquired), F16 KV cache, F32 recurrent state |
| Artifact SHA-256 | `809626574d0cb43d4becfa56169980da2bb448f2299270f7be443cb89d0a6ae4` |
| Campaign | `qwen35-9b-rtx5070-baseline-2026-09-09` |
| Record date | 2026-09-09 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Runtime notes | All 33/33 runtime layers GPU-resident; CPU-mapped input embedding disclosed; pinned official chat template; non-thinking text-only greedy surface |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

## WELP outcome

- **Outcome:** PASS — QWEN35_9B_RTX5070_BASELINE_CHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** HIGH_QUALITY_QUANTIZED_CONTROL — medium-fit Q8_0 control; this is NOT a high-precision BF16 result (BF16 cannot fit this GPU)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/eval-qwen3.5-9b

## Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | Full revised model-card context envelope still deferred; nothing above 65,536 was tested under the first-pass standard |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.043883 s | — | 66.66 tok/s |
| Moderate (3642-token input) | 0.831738 s | 4378.79 tok/s | 64.84 tok/s |

<p><small>Medians over five measured repetitions per surface; client/transport proxies with native timings retained in the campaign evidence</small></p>

## Quality and capabilities

- **Constrained result:** 7/7 constrained checks on the same compact fixture as the 4B control; the fixture is saturated and does not establish stronger broad 9B capability
- Largest admitted precision that keeps full transformer GPU residency with useful context and reserve on this GPU
- Bounded exact synthetic retrieval through 65,536 configured tokens
- 20/20 bounded reliability with no CUDA/OOM/Xid events

### Guardrails and limitations

- Free-form outputs showed unsupported provenance claims (synthetic checksum fields described as cryptographic); quality superiority over the 4B control is unproven
- Coding, tool use, multi-turn autonomous-agent behavior, and vision were not tested
- Context coverage bounded to six combined retrieval requests / 30 target observations

**Reliability:** 20/20 exact requests on a fresh 32K server; no HTTP/runtime errors; bounded, not endurance certification

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 67.3 |
| TTFT | 88.65 ms |
| Submission reference | cmtwcn79807eups01faxxmyr1 |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); verifiedRun false reflects a client capture limitation; actual prompt tokens 266 (endpoint usage)</small></p>

## Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/eval-qwen3.5-9b>

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
