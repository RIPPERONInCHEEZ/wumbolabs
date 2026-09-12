+++
title = "Nemotron 3 Nano 4B Lab Record"
description = "Append-only dated recharacterization under the current WELP protocol: the historical PROTOCOL_BLOCKED record is preserved unchanged, and this campaign completes the model-card context envelope (native 262,144 VALIDATED at both seeds; extensions source-backed absent), reproduces the reliability weakness as a measurable guardrail (clean-pass 0.30/0.25; hallucination 0.20/0.15), and confirms the dense hybrid Mamba-2/4-attention-layer architecture. Classification READY_WITH_GUARDRAILS; practical profile 32K default / 131K guarded; LocalMaxxing VERIFIED_EXISTING."
date = 2026-09-11
template = "lab_record.html"
weight = 12

[extra]
model = "Nemotron 3 Nano 4B"
producer = "NVIDIA"
quant = "Q4_K_M weights; f16 KV cache; dense hybrid (no MoE)"
repo = "https://github.com/WumboLabs/eval-nemotron-3-nano-4b"
status = "READY_WITH_GUARDRAILS"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Append-only dated recharacterization under the current WELP protocol: the historical PROTOCOL_BLOCKED record is preserved unchanged, and this campaign completes the model-card context envelope (native 262,144 VALIDATED at both seeds; extensions source-backed absent), reproduces the reliability weakness as a measurable guardrail (clean-pass 0.30/0.25; hallucination 0.20/0.15), and confirms the dense hybrid Mamba-2/4-attention-layer architecture. Classification READY_WITH_GUARDRAILS; practical profile 32K default / 131K guarded; LocalMaxxing VERIFIED_EXISTING."
evidence = "published"
+++

## Identity

| Field | Value |
|---|---|
| Model | Nemotron 3 Nano 4B |
| Producer | NVIDIA |
| Official model | nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF (GGUF) / nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 (BF16 weights) @ `ba223d14e45525f7fae81db77ea8cabeb2fc6c25` |
| Tested artifact | NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf — the only official llama.cpp quant NVIDIA publishes for this model |
| Precision | Q4_K_M weights; f16 KV cache; dense hybrid (no MoE) |
| Artifact SHA-256 | `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2` |
| Campaign | `nemotron3-nano-4b-rtx5070-welp-recharacterization-2026-09-11` |
| Record date | 2026-09-11 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA SM120) |
| Runtime notes | Full GPU residency (-ngl 999), parallel=1, FlashAttention on, f16 KV, reasoning-off baseline via the official enable_thinking template kwarg |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

## WELP outcome

- **Outcome:** PASS — NEMOTRON3_NANO_4B_RTX5070_RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS (reliability is the guardrail)
- **Artifact classification:** Canonical official llama.cpp deployment surface (sole official quant); BF16 fit-limited on this GPU at the tested context targets; Q4_K_M quality confound disclosed

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/eval-nemotron-3-nano-4b

## Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED — capacity admitted, near-full performance measured (uncached prefill ~2,877 tok/s, decode ~79-81 tok/s, 7,268 MiB VRAM), strict useful-context PASS at both required seeds (42, 314159) |

## Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.046 s | — | 186.6 tok/s |
| Moderate (3880-token input) | 0.507 s | 7498 tok/s | 182.9 tok/s |

<p><small>Short/moderate values are campaign-measured streaming surfaces; context-rung values are near-full occupancy measurements with unique prompts (cached tokens 0 at the native-maximum rungs)</small></p>

## Quality and capabilities

- **Constrained result:** frozen 12-task model-neutral screen 12/12 PASS (mechanical scorer frozen before outputs; temp 0, seed 42)
- Reasoning TESTED_PASS in the official thinking mode; coding TESTED_PASS on executable frozen cases; tool calling TESTED_PASS (structural validity + grounded continuation, bounded — not autonomous-agent qualification)
- Strongest near-full strict-compliance context result in the current control set: strict useful-context aggregate PASS at every rung through 99.49% of the native 262,144-token maximum
- First hybrid Mamba-2 model characterized under current WELP on this host; measured allocation confirms fixed recurrent state plus 4-layer context-linear KV
- Zero OOM, zero CUDA errors, zero Xid; peak 247-249 W within the stock 250 W envelope

### Guardrails and limitations

- Behavioral reliability has measurable hallucination/evidence-discipline defects under the adversarial corpus: clean-pass 0.30/0.25 and hallucination 0.20/0.15 across seeds 42/314159 on a 20-request stratified sample of the proven mechanical reliability corpus (transport success 40/40)
- The model confidently fabricated a nonexistent CUDA API and capitulated to a false user assertion; independently verify technical/factual claims in adversarial or evidence-discipline-sensitive contexts
- The 12/12 bounded quality screen is not evidence of universal reliability; the strict near-full context PASS is not proof of universal long-document reasoning
- Q4_K_M quantization confound disclosed, not measured against BF16

**Reliability:** Transport/runtime reliability strong; bounded quality/structured behavior clean; adversarial behavioral reliability materially weaker — the historical Phase-4 weakness is reproduced on the current instrument and remains the mandatory guardrail

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 185.8 |
| TTFT | 125.1 ms |
| Submission reference | cmt86gy1j000eli01ca3cwwn0 |
| verifiedRun | NO |

<p><small>Exact canonical practical profile (Q4_K_M, llama.cpp b10449, 32,768 context, f16 KV, full GPU, RTX 5070) already submitted and approved 2026-08-25; per the never-duplicate rule zero new submissions were created. A fresh 5-rep local benchmark (tg128 191.0 tok/s, pp512 8,275 tok/s) reproduces the submitted result.</small></p>

## Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/eval-nemotron-3-nano-4b>

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
