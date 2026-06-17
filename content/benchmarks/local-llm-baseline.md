+++
title = "Local LLM Baseline"
description = "Baseline notes for local LLM testing on WumboJetsII."
date = 2026-06-09
[extra]
back_label = "Back to Benchmarks"
back_url = "/benchmarks/"
+++

This is the starting benchmark record for local LLM testing on WumboJetsII.

It is not a leaderboard. It is a baseline for tracking what actually runs well on the hardware used for WumboLabs work.

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

## Current Baseline Philosophy

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

Future benchmark notes will use this page as the reference point for what needs to be measured.
