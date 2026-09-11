+++
title = "Qwen3.8-27B (current H1 profile) Lab Record"
description = "Current canonical RTX 5070 profile: ExLlamaV3 1.4.6 serving SC_2.20bpw_H3_V3 at 65,536 context with H1 recurrent history promoted via E18H/E18I (H4 fallback retained). H1 cuts recurrent storage by 434.8 MiB (held as reserve), passes the E18E oracle 3/3 / 15-15 fields, quality 7/7 and a 20/20 flat stability sequence; 75.8 tok/s decode at a 3,514-token prompt."
date = 2026-09-09
template = "lab_record.html"
weight = 11

[extra]
model = "Qwen3.8-27B (current H1 profile)"
producer = "Alibaba (Qwen team); EXL3 quant by turboderp"
quant = "2.20 bpw EXL3; q4 target KV; q4 draft KV"
repo = "https://github.com/WumboLabs/eval-qwen3.8-27b"
status = "COMPLETE / CURRENT_CANONICAL_H1_PROFILE"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Current canonical RTX 5070 profile: ExLlamaV3 1.4.6 serving SC_2.20bpw_H3_V3 at 65,536 context with H1 recurrent history promoted via E18H/E18I (H4 fallback retained). H1 cuts recurrent storage by 434.8 MiB (held as reserve), passes the E18E oracle 3/3 / 15-15 fields, quality 7/7 and a 20/20 flat stability sequence; 75.8 tok/s decode at a 3,514-token prompt."
evidence = "published"
+++

## Identity

| Field | Value |
|---|---|
| Model | Qwen3.8-27B (current H1 profile) |
| Producer | Alibaba (Qwen team); EXL3 quant by turboderp |
| Tested artifact | Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3) |
| Precision | 2.20 bpw EXL3; q4 target KV; q4 draft KV |
| Campaign | `qwen38-27b-h1-canonical-profile (E18H candidate validation 2026-09-08 + E18I canonical promotion 2026-09-09)` |
| Record date | 2026-09-09 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | ExLlamaV3 |
| Runtime version | 1.4.6+cu128.torch2.10.0 |
| Runtime notes | MTP width 1, batch 1, max_chunk 256, recurrent history H1 (max_history 1) with explicit H4 fallback via --max-history 4; CPU embedding lookup (not transformer-layer offload); all 64 transformer blocks GPU-resident; context 65,536 canonical; recovered memory (434.8125 MiB) retained as unspent reserve |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44 |

## WELP outcome

- **Outcome:** PASS — E18I_H1_CANONICAL_PROMOTION_COMPLETE (E18H: PASS — E18H_H1_VALIDATED_EXPERIMENTAL_PROMOTION_CANDIDATE)
- **Classification:** CURRENT_CANONICAL_PROFILE — engine/history promotion validation, not a new model classification; the historical deep-evaluation role findings remain those of their tested stack
- **Artifact classification:** Current canonical Qwen3.8 serving surface (exact artifact/runtime/geometry scope only)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/eval-qwen3.8-27b

## Context profile

| Field | Value |
|---|---|
| Practical default | 65536 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | No full model-card context campaign exists for this profile; inherited validated evidence: E18E corrected combined oracle 3/3 requests / 15/15 target fields exact on H1 at ~58.8K actual input tokens (prompts 58,849/58,902/58,883) |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | not recorded | — | not recorded |
| Moderate (3514-token input) | 4.4487 s | 789.89 tok/s | 75.79 tok/s |

<p><small>E18H arm-B (H1) frozen 3,514-token prompt, five cold repetitions after warmup, medians; MTP width 1 active</small></p>

## Quality and capabilities

- **Constrained result:** E18H seven-check quality matrix 7/7 PASS on the retained E3 fixture (all three arms A/B/A2); E18I H1 smoke repeated the fixture 7/7
- H1 recurrent/GDN storage 292.6875 MiB vs H4 727.5 MiB (measured reduction 434.8125 MiB, retained as reserve, not spent)
- E18G deterministic mechanism fixture F1/F2/F3 exact on H1; 20/20 stability sequence exactly flat (zero allocated/reserved growth, zero slope)
- H1 oracle minimum free 1,888 MiB vs 1,470 MiB for H4 (+418 MiB measured in the same campaign)

### Guardrails and limitations

- H1 is canonical only for this exact artifact/runtime and text-only width1/batch1 surface
- No context growth or recovered-memory spending; explicit H4 fallback remains available in the same launcher
- Historical model-role findings (hallucination rate, strict interfaces, native tools) belong to the historical UD-Q2_K_XL llama.cpp evaluation and are not superseded by this profile work

**Reliability:** E18H H1 stability: 20/20 exact expected results, HTTP 200 throughout, flat allocator blocks (growth 0, slope 0); zero CUDA/OOM/Xid in both campaigns

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 65536 tokens |
| tok/s out | 75.4 |
| TTFT | 71.35 ms |
| Submission reference | cmtwcncwr07f4ps01ef75q6ne |
| verifiedRun | NO |

<p><small>APPROVED, origin NEW (localmaxxing-backfill-2026-09-10) on the CURRENT H1 canonical profile (ExLlamaV3, SC_2.20bpw_H3_V3, q4/q4 KV, MTP width1, batch1, H1, 65,536); actual prompt tokens 266 (endpoint usage); verifiedRun false with an additional disclosed issue: MTP acceptance counters are not exposed by the canonical wrapper and none were fabricated; a transparent loopback path adapter bridged /chat/completions to /v1/chat/completions and is disclosed in the submission payload. Three historical E4-era submissions (llama.cpp-era wrapper with H4 history) remain historical and supersede nothing.</small></p>

## Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/eval-qwen3.8-27b>

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
