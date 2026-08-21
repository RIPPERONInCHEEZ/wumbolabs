+++
title = "Lab Records"
description = "Dated evidence and working history from WumboLabs."
sort_by = "date"
template = "section.html"
page_template = "page.html"
[extra]
back_label = "Back to Home"
back_url = "/"
+++

Lab Records are the dated evidence archive and working history for WumboLabs.

Projects describe what exists. Lab Records document what was tested, observed, changed, or learned on real hardware. Results stay tied to their hardware, runtime, model, context, suite, scoring status, and known limitations.

- **REPORT** — bounded conclusions from completed tests with measured evidence and review context
- **BASELINE** — reference records for a test bench, evaluation expectations, or comparison starting point
- **FIT TEST** — hardware- and runtime-scoped checks that do not imply a quality verdict
- **LAB NOTE** — dated changes, decisions, repairs, and lessons from the lab

These records are practical evidence, not leaderboard rankings or universal model judgments.

## Current Local Model Testing Snapshot

This is a compact orientation for current WumboLabs local-model work. It is not a leaderboard, schedule, or claim that queued models have been tested.

### Current 12GB Reference

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Current 12GB reference</span>
    <strong>Qwen3.8-27B UD-Q2_K_XL</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Hardware</span>
    <strong>RTX 5070 12GB</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Public status</span>
    <strong>Strong reviewed coding/technical assistant</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Daily-use qualification</span>
    <strong>Not ready for unguarded daily use</strong>
  </div>
</div>

Read the [Qwen3.8-27B Lab Record](/records/qwen38-27b-rtx5070-evaluation/). This is the current 12GB reference on WumboJetsII, not a universal best-model claim.

### Tested / Blocked Snapshot

| Family / experiment | Status | High-level finding |
|---|---|---|
| Empero Qwen3.8 distilled 9B / 4B / 2B | Tested — complete campaign | 9B Q4_K_M strongest broad candidate from the family; 4B Q8 strongest bounded coding/efficiency candidate; 2B extremely fast but materially weaker as a primary coding/reasoning assistant. Huge context fit did not guarantee synthesis quality. Reasoning off preferred for strict interfaces. |
| Bonsai 27B Q1 | Partially tested — reliability concerns | Loaded; compression technically impressive; practical Linux/system reliability failures, hallucinated/unsupported commands, and degeneration/repetition. Not recommended as a systems/coding assistant. |
| Ternary Bonsai 27B | Blocked — runtime support | Loader/runtime failed admission. No quality claim. |
| Gemma 4 12B NVFP4 | Blocked — full-GPU memory fit | Native backend/kernel admission succeeded; complete RTX 5070 12GB full-GPU loading failed. No inference-quality verdict. |
| Gemma 4 12B GGUF | Tested — historical strong baseline | Historical performance/efficiency reference. See the existing Gemma report. |
| Mellum2 12B | Tested — historical practical baseline | Historical practical/speed reference. |
| Grug-12B | Tested — historical baseline | Historical comparison entry. |
| Qwen3 / Qwen3.6 | Tested — historical baselines | Earlier Qwen-family evidence, not the current 12GB reference. |
| SGLang / Qwen runtime research | Runtime research — blocked | Environment/toolchain failure, not a model-quality failure. |

Producer claims are not WumboLabs findings. Use language such as advertised, we tested, reproduced, not reproduced, blocked, physically untestable, or bounded result. Example: Liquid AI's advertised approximately 97% BF16-retention result for QAD remains a producer claim until independently reproduced here.

<details class="project-details">
<summary>Upcoming local-model research queue</summary>

This is a living research queue, not a fixed schedule. These models have not been tested by this snapshot.

**High priority**

- Ornith 1.5 — coding / Agent work
- BTL-4 Compact — extreme-compression coding / Agent behavior
- Maple Preview — reasoning / extreme compression
- Liquid AI LFM2.5 QAD — quantization-aware distillation / tiny sidecars
- LFM2.5-VL-3B — multimodal sidecar

**Medium / high**

- AMD Instella-MoE-16B-A3B-Think — alternative MoE reasoning lineage

**Revisit**

- Bonsai / Ternary Bonsai — new backend/runtime support

**Specialized**

- Fara1.5 — browser/computer-use campaign

**External control**

- Ox Alpha — external frontier control. Not a local model. Do not combine API throughput with local hardware throughput, and do not imply private WumboLabs data should be uploaded.

**Future higher-VRAM hardware**

- Nemotron 3.5 Lightning, Muse Glimmer 30B, and DiffusionGemma 26B-A4B are future 24GB+ / higher-VRAM hardware candidates, not current RTX 5070 12GB candidates.

</details>

<details class="project-details">
<summary>Runtime / decoding snapshot</summary>

Current Qwen3.8 findings include: native MTP works; approximately 1.4–1.5x generation improvement in matched bounded tests; MTP has meaningful VRAM cost; DFlash2 Q4 could not physically coexist with the final Qwen target under strict 12GB full-GPU constraints; n-gram speculation gave little useful benefit.

Future methods to monitor may include DFlash, DFlash2, DSpark, MTP improvements, and EAGLE-like approaches where supported. A runtime exposing a flag is not evidence that the method is worth using.

</details>
