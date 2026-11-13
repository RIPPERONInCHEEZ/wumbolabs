+++
title = "Apodex 1.1 mini"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 23

[extra]
kind = "model"
model_id = "apodex-1.1-mini"
vendor = "Apodex (Qwen3.5-35B-A3B MoE base)"
findings_first = true
classification = "BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE"
recommended_profile_id = "apodex-1.1-mini-llamacpp-iq1m"
recommended_profile_name = "llama.cpp IQ1_M (community conversion)"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-08-25
+++

## Overview

Apodex (Qwen3.5-35B-A3B MoE base) · 1 tested configuration · 1 evidence event · newest evidence 2026-08-25.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE** - attributed to the [2026-08-25 event](#initial-evaluation-2026-08-25-apodex), configuration IQ1_M · llama.cpp · RTX 5070.
- **Recommended configuration:** llama.cpp IQ1_M (community conversion) (current): [event result](#initial-evaluation-2026-08-25-apodex).
- **Latest evidence:** 2026-08-25: [event result](#initial-evaluation-2026-08-25-apodex)
- **2026-08-25** · IQ1_M · llama.cpp · RTX 5070: classification BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE. [Event result](#initial-evaluation-2026-08-25-apodex)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="initial-evaluation-2026-08-25-apodex"></a>

### 2026-08-25: Initial evaluation (bounded early stop)

**Initial Evaluation: Early Stop** · config IQ1_M · llama.cpp · RTX 5070 · maturity: EARLY_STOP · status: BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE

Configuration: llama.cpp IQ1_M (community conversion).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/apodex-1.1-mini/events/initial-evaluation-2026-08-25-apodex/REPORT.md)


###### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp pinned at `f280b26983ad0fdb705a0d9ebf0503e76f2899b0` (2026-08-24) |

###### Headline Verdict

**DO_NOT_ADVANCE at Phase 3 (early stop, frozen gate).**

The model failed the applicable advancement gate. Per WELP protocol, later phases were not run. This is a bounded result, not a complete capability review.

The early-stop behavior is a feature of WELP transparency: the model failed the gate, so the evaluation stopped. This is not a protocol failure; it is the protocol working as designed.

###### Performance

| Metric | Result |
|---|---|
| Decode throughput | 169.36 tok/s (median 169.46, sigma 1.70) |
| Prefill (~5.6K tok) | 1,798.76 tok/s |
| TTFT (short prompt) | ~125 ms |
| VRAM idle | 9.7 GB |

###### Phase 3 Practical Viability: DO_NOT_ADVANCE

Contract WELP Practical Viability 0.1.2-draft, scorer `score_pv.py` (self-test 35/35), 30 tasks x seeds {42,43,44}, thinking OFF baseline.

| Gate | Threshold | s42 | s43 | s44 | Verdict |
|---|---|---|---|---|---|
| G1 aggregate | >=0.75 | 0.667 | 0.700 | 0.733 | **FAIL (all)** |
| G2 false-premise | >=0.60 | 0.400 | 0.200 | 0.600 | **FAIL (42,43)** |
| G3 factual-uncertainty | >=0.50 | 0.500 | 0.750 | 0.500 | PASS (boundary) |
| G4 structured-output | >=0.70 | 0.714 | 0.714 | 0.714 | PASS |

Decision identical across seeds => stable FAIL. Bounded failure review: ~19 genuine failures (fabricated package description, explained nonexistent git flag, asserted that 25 is prime, invented phone number, echoed un-reversed word); ~8 scorer lexicon artifacts. Verdict robust: correcting every artifact still leaves seed-42 aggregate <0.75.

###### What Was NOT Tested

- Native Tools module
- Coding module
- Reasoning module (dedicated)
- Context / Variance / Optimization / Stability
- Soak
- OMP Stage 2 (agent)

**Do not fabricate missing results.** This evaluation establishes that the strongest representation satisfying the frozen WumboJetsII full-GPU baseline (IQ1_M, 1.75-bpw) does not clear the frozen viability gate. It does NOT establish that BF16/FP8/GPTQ or Agent Team deployments would fail.

###### Role Classification

**Supported roles:** none beyond "runs coherently on 12GB at extreme quantization."

**NOT_REACHED:** Phases 4–10, OMP Stage 2, all capability modules, context/variance/optimization/soak/classification engine.

###### Important Limitations

- **Extreme quantization forced by hardware:** single 12GB consumer GPU required IQ1_M (1.75-bpw). Producer positioning rests on BF16-class deployments plus an agent harness that was not authorized to run.
- **Phase-3 failure at IQ1_M does NOT establish that BF16/FP8/GPTQ or Agent Team deployments would fail.** It establishes that the strongest representation satisfying the frozen full-GPU baseline does not clear the frozen viability gate.
- **Scorer lexicon defect** understates false-premise performance modestly; verdict unaffected.
- **No reliability, coding, tools, context, or soak results exist.**

###### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/apodex-1.1-mini/profiles/apodex-1.1-mini-llamacpp-iq1m
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models
- **LocalMaxxing:** Speed result SUBMITTED/APPROVED (ID `cmt9ijytg00xali017f46xk25`, 182.31 tok/s p512/n128). Benchmark suites NOT_SUBMITTED due to early WELP stop.

###### Reproduction

Direct link to canonical reproduction material: [Central evidence](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/apodex-1.1-mini/profiles/apodex-1.1-mini-llamacpp-iq1m)

This Lab Record is a summary; the canonical repo is the source of truth.

###### Identity

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

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| IQ1_M · llama.cpp · RTX 5070 | IQ1_M | llama.cpp | RTX 5070 | not recorded | 1 (2026-08-25) |

<details class="lab-findings-configs">
<summary>Configuration details: IQ1_M · llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp IQ1_M (community conversion).
- Profile identity: `apodex-1.1-mini-llamacpp-iq1m`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): Apodex-1.1-mini-IQ1_M.gguf (community conversion abenzerps/Apodex-1.1-mini-GGUF @ 59afa57852525f79a9634d5f80dd639cceee572c)
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/apodex-1.1-mini/profiles/apodex-1.1-mini-llamacpp-iq1m/profile.json)

Events on this configuration:

- [Initial evaluation (bounded early stop) (2026-08-25)](/evaluations/apodex-1-1-mini#initial-evaluation-2026-08-25-apodex); status: BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-08-25 | [Initial evaluation (bounded early stop)](#initial-evaluation-2026-08-25-apodex) | IQ1_M · llama.cpp · RTX 5070 | BOUNDED_EARLY_STOP / PHASE_3_DO_NOT_ADVANCE |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/apodex-1.1-mini)

### Legacy provenance

- [WumboLabs/eval-apodex-1.1-mini @ `202d2ee09cec20ec6981c6ed22541e44b9dc3865`](https://github.com/WumboLabs/eval-apodex-1.1-mini/blob/202d2ee09cec20ec6981c6ed22541e44b9dc3865/report.md)
