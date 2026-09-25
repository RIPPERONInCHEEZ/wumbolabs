+++
title = "Nemotron 3 Nano 4B"
description = "Nemotron 3 Nano 4B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 11

[extra]
kind = "model"
model_id = "nemotron-3-nano-4b"
vendor = "NVIDIA"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "nemotron-3-nano-4b-llamacpp-q4km"
recommended_profile_name = "llama.cpp Q4_K_M"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 1
event_count = 2
latest_evidence_date = 2026-09-11
+++

WumboLabs tests **Nemotron 3 Nano 4B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** READY_WITH_GUARDRAILS — [Current-WELP recharacterization (2026-09-11)](/evaluations/nemotron-3-nano-4b#welp-recharacterization-2026-09-11), profile llama.cpp Q4_K_M
- **Recommended profile:** llama.cpp Q4_K_M (`nemotron-3-nano-4b-llamacpp-q4km`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/welp-recharacterization-2026-09-11/REPORT.md)
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 262,144 (envelope complete: YES) — [Current-WELP recharacterization (2026-09-11)](/evaluations/nemotron-3-nano-4b#welp-recharacterization-2026-09-11)
- **Latest evidence:** 2026-09-11 — Current-WELP recharacterization

## Tested profiles

### llama.cpp Q4_K_M — CURRENT

Profile identity: `nemotron-3-nano-4b-llamacpp-q4km`.

| Field | Value |
|---|---|
| Runtime | llama.cpp build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA SM120) |
| Artifact | NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf — the only official llama.cpp quant NVIDIA publishes for this model |
| Precision | Q4_K_M weights; f16 KV cache; dense hybrid (no MoE) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/welp-recharacterization-2026-09-11/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b/profiles/nemotron-3-nano-4b-llamacpp-q4km/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-11)](/evaluations/nemotron-3-nano-4b#welp-recharacterization-2026-09-11) — READY_WITH_GUARDRAILS
- [Initial evaluation (protocol development, PROTOCOL_BLOCKED) (2026-08-25)](/evaluations/nemotron-3-nano-4b#initial-evaluation-2026-08-25) — PARTIAL_PROTOCOL_DEVELOPMENT

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="welp-recharacterization-2026-09-11"></a>

### 2026-09-11 — Current-WELP recharacterization

**WELP Recharacterization — llama.cpp Q4_K_M** · profile: llama.cpp Q4_K_M · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/welp-recharacterization-2026-09-11/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b)

##### Identity

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

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA SM120) |
| Runtime notes | Full GPU residency (-ngl 999), parallel=1, FlashAttention on, f16 KV, reasoning-off baseline via the official enable_thinking template kwarg |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

##### WELP outcome

- **Outcome:** PASS — NEMOTRON3_NANO_4B_RTX5070_RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS (reliability is the guardrail)
- **Artifact classification:** Canonical official llama.cpp deployment surface (sole official quant); BF16 fit-limited on this GPU at the tested context targets; Q4_K_M quality confound disclosed

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/welp-recharacterization-2026-09-11/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | VALIDATED — capacity admitted, near-full performance measured (uncached prefill ~2,877 tok/s, decode ~79-81 tok/s, 7,268 MiB VRAM), strict useful-context PASS at both required seeds (42, 314159) |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.046 s | — | 186.6 tok/s |
| Moderate (3880-token input) | 0.507 s | 7498 tok/s | 182.9 tok/s |

<p><small>Short/moderate values are campaign-measured streaming surfaces; context-rung values are near-full occupancy measurements with unique prompts (cached tokens 0 at the native-maximum rungs)</small></p>

##### Quality and capabilities

- **Constrained result:** frozen 12-task model-neutral screen 12/12 PASS (mechanical scorer frozen before outputs; temp 0, seed 42)
- Reasoning TESTED_PASS in the official thinking mode; coding TESTED_PASS on executable frozen cases; tool calling TESTED_PASS (structural validity + grounded continuation, bounded — not autonomous-agent qualification)
- Strongest near-full strict-compliance context result in the current control set: strict useful-context aggregate PASS at every rung through 99.49% of the native 262,144-token maximum
- First hybrid Mamba-2 model characterized under current WELP on this host; measured allocation confirms fixed recurrent state plus 4-layer context-linear KV
- Zero OOM, zero CUDA errors, zero Xid; peak 247-249 W within the stock 250 W envelope

###### Guardrails and limitations

- Behavioral reliability has measurable hallucination/evidence-discipline defects under the adversarial corpus: clean-pass 0.30/0.25 and hallucination 0.20/0.15 across seeds 42/314159 on a 20-request stratified sample of the proven mechanical reliability corpus (transport success 40/40)
- The model confidently fabricated a nonexistent CUDA API and capitulated to a false user assertion; independently verify technical/factual claims in adversarial or evidence-discipline-sensitive contexts
- The 12/12 bounded quality screen is not evidence of universal reliability; the strict near-full context PASS is not proof of universal long-document reasoning
- Q4_K_M quantization confound disclosed, not measured against BF16

**Reliability:** Transport/runtime reliability strong; bounded quality/structured behavior clean; adversarial behavioral reliability materially weaker — the historical Phase-4 weakness is reproduced on the current instrument and remains the mandatory guardrail

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 32768 tokens |
| tok/s out | 185.8 |
| TTFT | 125.1 ms |
| Submission reference | cmt86gy1j000eli01ca3cwwn0 |
| verifiedRun | NO |

<p><small>Exact canonical practical profile (Q4_K_M, llama.cpp b10449, 32,768 context, f16 KV, full GPU, RTX 5070) already submitted and approved 2026-08-25; per the never-duplicate rule zero new submissions were created. A fresh 5-rep local benchmark (tg128 191.0 tok/s, pp512 8,275 tok/s) reproduces the submitted result.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/welp-recharacterization-2026-09-11/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="initial-evaluation-2026-08-25"></a>

### 2026-08-25 — Initial evaluation (protocol development, PROTOCOL_BLOCKED)

**Initial Evaluation — PROTOCOL_BLOCKED (historical, preserved)** · profile: llama.cpp Q4_K_M · maturity: PROTOCOL_BLOCKED · status: PARTIAL_PROTOCOL_DEVELOPMENT

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/nemotron-3-nano-4b/events/initial-evaluation-2026-08-25/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b)

### Identity

| Field | Value |
|---|---|
| Model | Nemotron 3 Nano 4B |
| Producer | NVIDIA |
| Evaluated artifact | NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf |
| Source revision | `ba223d14e45525f7fae81db77ea8cabeb2fc6c25` |
| SHA-256 | `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2` |
| Evaluation date | 2026-08-25 |
| Protocol | WELP, first deliberate WELP validation campaign |
| Highest phase reached | Phase 3 (gate decision) |
| Campaign classification | PARTIAL_PROTOCOL_DEVELOPMENT |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44, kernel 7.1.9 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

### Headline Verdict

**PROTOCOL_BLOCKED at Phase 3 gate decision.**

The model showed no failing behavior. WELP's documented material contains no Phase 3 advancement threshold, so no deterministic PASS/FAIL could be produced without inventing a rule, which the campaign forbids.

This campaign contributed to protocol development. It is **not a complete WELP capability review**. Do not present it as equivalent in evaluation depth to Qwen3.8-27B.

### Performance

| Metric | Result |
|---|---|
| Decode | ~178 tok/s mean (512-token generations) |
| Prefill | ~6,500 tok/s at ~2,600-token prompts |
| TTFT (short prompt) | ~30 ms |
| llama-bench (p512/n128) | ~180 tok/s out, 65 ms TTFT |

### Phases Reached

| Phase | Gate | Outcome |
|---|---|---|
| 0 Provenance | — | PASS |
| 1 Admission (hard) | PASS | Loads; full GPU residency verified; clean inference/termination |
| 2 Performance | PASS* | Criterion interpreted (F-02) |
| 3 Practical Viability | **PROTOCOL_BLOCKED** | 12/12 screen but protocol defines no advancement threshold (F-01) |
| 4–10, OMP-21B | NOT RUN | Stopped per campaign rule |

### Practical Viability Evidence

12 tasks across instruction following, strict output, extraction, structured JSON, technical knowledge, false-premise rejection, uncertainty behavior, simple reasoning: **12/12**, mechanical scoring. This is screening evidence, not a gate pass.

### Reasoning Findings

Bounded observations only (dedicated module not reached): default mode emits `<think>` traces then answers; `enable_thinking=false` yields direct correct answers. Producer's reasoning-off benchmark framing is operationally reproducible on this runtime.

### Role Classification

**No deployment recommendation is supported by this evidence.**

What the reached phases establish:
- The model loaded cleanly and served stably across the tested phases
- Performance was measured
- The Phase-3 screening result was measured: 12/12
- OMP connectivity was demonstrated
- The reasoning-control mechanism was boundedly observed

**Explicitly NOT TESTED:** reliability, capability modules, context quality, variance, soak, and agent capability.

### Important Limitations

- **Single-seed practical screen.** Reliability, context quality, coding, tools, agent behavior, and soak were NOT TESTED.
- **Context wording:** the server was configured with a 32K context window and inference ran within it. Useful 32K context behavior was **not evaluated**.
- **No LLMGauge Agent Harness result.** LLMGauge was never invoked.
- **Protocol findings:** this campaign identified 9 protocol ambiguities (F-01 through F-09) and 4 undocumented decisions required. These are documented in the canonical repo.
- Results must not be generalized to a model review.

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b/profiles/nemotron-3-nano-4b-llamacpp-q4km
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models
- **LocalMaxxing:** Speed run measured locally (~180 tok/s); submission blocked on missing credentials. No benchmark suite submissions.

### Reproduction

Direct link to canonical reproduction material: [Central evidence](https://github.com/WumboLabs/evaluations/tree/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b/profiles/nemotron-3-nano-4b-llamacpp-q4km)

This Lab Record is a summary; the canonical repo is the source of truth.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **nemotron-3-nano-4b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/e0a8e71ebd2c966a9cd145257025c7bf78fbf094/models/nemotron-3-nano-4b/profiles/nemotron-3-nano-4b-llamacpp-q4km/profile.json)

### Legacy provenance

- [WumboLabs/eval-nemotron-3-nano-4b @ `3e357b5e4fb6b45bddd8a15847e96476dca035ca`](https://github.com/WumboLabs/eval-nemotron-3-nano-4b/blob/3e357b5e4fb6b45bddd8a15847e96476dca035ca/report.md)
- [WumboLabs/eval-nemotron-3-nano-4b @ `3e357b5e4fb6b45bddd8a15847e96476dca035ca`](https://github.com/WumboLabs/eval-nemotron-3-nano-4b/blob/3e357b5e4fb6b45bddd8a15847e96476dca035ca/reports/nemotron3-nano-4b-welp-recharacterization-2026-09-11.md)
