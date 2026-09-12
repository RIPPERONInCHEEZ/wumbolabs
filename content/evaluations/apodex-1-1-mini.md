+++
title = "Apodex 1.1 mini"
description = "Apodex 1.1 mini — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 3

[extra]
kind = "model"
model_id = "apodex-1.1-mini"
vendor = "Apodex (Qwen3.5-35B-A3B MoE base)"
classification = "BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE"
recommended_profile_id = "apodex-1.1-mini-llamacpp-iq1m"
recommended_profile_name = "llama.cpp IQ1_M (community conversion)"
profile_count = 1
event_count = 1
latest_event_date = 2026-08-25
+++

WumboLabs tests **Apodex 1.1 mini** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Classification:** BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE — [Initial evaluation (bounded early stop) (2026-08-25)](/evaluations/apodex-1-1-mini#initial-evaluation-2026-08-25-apodex), profile llama.cpp IQ1_M (community conversion)
- **Recommended profile:** llama.cpp IQ1_M (community conversion) (`apodex-1.1-mini-llamacpp-iq1m`, current) — [canonical evidence](https://github.com/WumboLabs/eval-apodex-1.1-mini)
- **Latest evidence:** 2026-08-25 — Initial evaluation (bounded early stop)

## Tested profiles

### llama.cpp IQ1_M (community conversion) — CURRENT

Profile identity: `apodex-1.1-mini-llamacpp-iq1m`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-apodex-1.1-mini>

Events on this profile:

- [Initial evaluation (bounded early stop) (2026-08-25)](/evaluations/apodex-1-1-mini#initial-evaluation-2026-08-25-apodex) — BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="initial-evaluation-2026-08-25-apodex"></a>

### 2026-08-25 — Initial evaluation (bounded early stop)

**Initial Evaluation — Early Stop** · profile: llama.cpp IQ1_M (community conversion) · status: BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE

[Canonical evidence for this event](https://github.com/WumboLabs/eval-apodex-1.1-mini)

### Identity

| Field | Value |
|---|---|
| Model | Apodex 1.1 mini |
| Producer | Apodex; base: Qwen/Qwen3.5-35B-A3B; ~36B total / A3B active MoE |
| Evaluated artifact | Community conversion `abenzerps/Apodex-1.1-mini-GGUF` @ `59afa57852525f79a9634d5f80dd639cceee572c` (not official) |
| File | Apodex-1.1-mini-IQ1_M.gguf |
| SHA-256 | `1e84d8adf7837e96fb18712882a8a114becc7e53554372e2f612c5e0c6276cd4` |
| Evaluation date | 2026-08-25 |
| Protocol | WELP end-to-end (frozen snapshot `welp-next-snapshot-2026-08-25-end-to-end`) |
| Highest phase reached | Phase 3 (gate decision) |
| Campaign classification | BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp pinned at `f280b26983ad0fdb705a0d9ebf0503e76f2899b0` (2026-08-24) |

### Headline Verdict

**DO_NOT_ADVANCE at Phase 3 (early stop, frozen gate).**

The model failed the applicable advancement gate. Per WELP protocol, later phases were not run. This is a bounded result, not a complete capability review.

The early-stop behavior is a feature of WELP transparency: the model failed the gate, so the evaluation stopped. This is not a protocol failure — it is the protocol working as designed.

### Performance

| Metric | Result |
|---|---|
| Decode throughput | 169.36 tok/s (median 169.46, sigma 1.70) |
| Prefill (~5.6K tok) | 1,798.76 tok/s |
| TTFT (short prompt) | ~125 ms |
| VRAM idle | 9.7 GB |

### Phase 3 Practical Viability — DO_NOT_ADVANCE

Contract WELP Practical Viability 0.1.2-draft, scorer `score_pv.py` (self-test 35/35), 30 tasks x seeds {42,43,44}, thinking OFF baseline.

| Gate | Threshold | s42 | s43 | s44 | Verdict |
|---|---|---|---|---|---|
| G1 aggregate | >=0.75 | 0.667 | 0.700 | 0.733 | **FAIL (all)** |
| G2 false-premise | >=0.60 | 0.400 | 0.200 | 0.600 | **FAIL (42,43)** |
| G3 factual-uncertainty | >=0.50 | 0.500 | 0.750 | 0.500 | PASS (boundary) |
| G4 structured-output | >=0.70 | 0.714 | 0.714 | 0.714 | PASS |

Decision identical across seeds => stable FAIL. Bounded failure review: ~19 genuine failures (fabricated package description, explained nonexistent git flag, asserted 25 prime, invented phone number, echoed un-reversed word); ~8 scorer lexicon artifacts. Verdict robust: correcting every artifact still leaves seed-42 aggregate <0.75.

### What Was NOT Tested

- Native Tools module
- Coding module
- Reasoning module (dedicated)
- Context / Variance / Optimization / Stability
- Soak
- OMP Stage 2 (agent)

**Do not fabricate missing results.** This evaluation establishes that the strongest representation satisfying the frozen WumboJetsII full-GPU baseline (IQ1_M, 1.75-bpw) does not clear the frozen viability gate. It does NOT establish that BF16/FP8/GPTQ or Agent Team deployments would fail.

### Role Classification

**Supported roles:** none beyond "runs coherently on 12GB at extreme quantization."

**NOT_REACHED:** Phases 4–10, OMP Stage 2, all capability modules, context/variance/optimization/soak/classification engine.

### Important Limitations

- **Extreme quantization forced by hardware:** single 12GB consumer GPU required IQ1_M (1.75-bpw). Producer positioning rests on BF16-class deployments plus an agent harness that was not authorized to run.
- **Phase-3 failure at IQ1_M does NOT establish that BF16/FP8/GPTQ or Agent Team deployments would fail.** It establishes that the strongest representation satisfying the frozen full-GPU baseline does not clear the frozen viability gate.
- **Scorer lexicon defect** understates false-premise performance modestly; verdict unaffected.
- **No reliability, coding, tools, context, or soak results exist.**

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/eval-apodex-1.1-mini
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs
- **LocalMaxxing:** Speed result SUBMITTED/APPROVED (ID `cmt9ijytg00xali017f46xk25`, 182.31 tok/s p512/n128). Benchmark suites NOT_SUBMITTED due to early WELP stop.

### Reproduction

Direct link to canonical reproduction material: [eval-apodex-1.1-mini/](https://github.com/WumboLabs/eval-apodex-1.1-mini)

This Lab Record is a summary; the canonical repo is the source of truth.

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **llama.cpp IQ1_M (community conversion)** (`apodex-1.1-mini-llamacpp-iq1m`): <https://github.com/WumboLabs/eval-apodex-1.1-mini>
