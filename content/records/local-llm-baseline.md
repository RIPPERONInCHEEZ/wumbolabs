+++
title = "Local LLM Baseline"
description = "Historical baseline notes for local LLM testing on WumboJetsII."
date = 2026-06-09
[extra]
record_type = "HISTORICAL BASELINE"
back_label = "Back to Reports"
back_url = "/records/"
+++

This historical baseline predates the current WELP evaluation and publication methodology. It preserves the original test context; current model-testing method and claim rules live in [Methodology](/methodology/).

## Test Bench

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Machine</span>
    <strong>WumboJetsII</strong>
  </div>

  <div class="info-card">
    <span class="info-label">OS</span>
    <strong>Arch Linux</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Desktop</span>
    <strong>Hyprland</strong>
  </div>

  <div class="info-card">
    <span class="info-label">GPU</span>
    <strong>RTX 5070 12GB</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Backend</span>
    <strong>llama.cpp CUDA</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Format</span>
    <strong>GGUF</strong>
  </div>
</div>

## Historical Baseline Philosophy

A model is only useful if it can fit the hardware, stay stable, follow instructions, avoid confident fabrication, and produce output that helps with real work.

For WumboLabs, that means testing against practical tasks:

- Linux troubleshooting
- Docker and networking diagnostics
- ZFS/recovery procedures
- configuration review
- local AI workflow support
- long-context behavior
- honesty under uncertainty

<details class="project-details">
<summary>What gets tracked</summary>

Local model testing needs more than raw tokens per second.

Each useful benchmark record should include:

- model name
- quantization
- backend
- hardware
- context size
- prompt processing speed
- generation speed
- VRAM behavior
- fit/headroom notes
- failure modes
- practical usefulness
- whether the result is repeatable enough to trust

</details>

## How to Read These Notes

Numbers are useful, but they are not enough.

A faster model that hallucinates commands, invents tools, or gives unsafe system advice is not a better model for this lab. The baseline is meant to capture both performance and judgment.

Later model-evaluation methodology is governed by WELP and the current evidence and publication rules in [Methodology](/methodology/). This record remains a dated baseline, not the current testing entry point.
