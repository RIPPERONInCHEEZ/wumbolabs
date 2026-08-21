+++
title = "WumboJetsII"
description = "Fedora 44 workstation for daily development, local AI evaluation, wumbOS work, and WumboLabs evidence."
template = "project.html"
weight = 3
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
+++

WumboJetsII is the primary WumboLabs desktop workstation: a real daily-use Fedora 44 system, not a dedicated headless benchmark appliance.

It runs Fedora 44 with Hyprland and supports development, wumbOS Shell work, LLMGauge testing, and deeper local-model evaluation on consumer hardware.

<strong>Active daily workstation / evidence source</strong>

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">OS</span>
    <strong>Fedora 44</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Desktop</span>
    <strong>Hyprland</strong>
  </div>

  <div class="info-card">
    <span class="info-label">GPU</span>
    <strong>NVIDIA GeForce RTX 5070 12GB</strong>
  </div>

  <div class="info-card">
    <span class="info-label">CPU / Memory</span>
    <strong>Ryzen 7 9800X3D / ~32GB DDR5</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Storage</span>
    <strong>Samsung 9100 Pro 2TB NVMe</strong>
  </div>

  <div class="info-card">
    <span class="info-label">AI Stack</span>
    <strong>llama.cpp CUDA</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Local AI</span>
    <strong>RTX 5070 evaluation</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Daily desktop workstation</strong>
  </div>
</div>

## Role in WumboLabs

WumboJetsII is where WumboLabs development, wumbOS Shell development/testing, and local AI testing happen.

It is a constrained consumer-workstation environment for LLMGauge runs and deeper model-evaluation campaigns. The RTX 5070 also drives the Fedora/Hyprland session during testing, so practical free VRAM is lower than its physical 12GB capacity. That constraint is intentional evidence context, not controlled-lab isolation.

The current Qwen3.8 campaign used the RTX 5070 with llama.cpp/CUDA; [read the Lab Record](/records/qwen38-27b-rtx5070-evaluation/) for its runtime-specific findings and limitations.

<details class="project-details">
<summary>Focus areas</summary>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Linux Desktop</h3>
    <p>Fedora 44, Hyprland, Wayland workflows, keyboard-driven interaction, theming, and practical daily use.</p>
  </div>

  <div class="feature-card">
    <h3>Local LLM Evaluation</h3>
    <p>LLMGauge workflows and deeper GGUF evaluation across llama.cpp builds, context limits, generation speed, VRAM behavior, and bounded reliability.</p>
  </div>

  <div class="feature-card">
    <h3>Development Workstation</h3>
    <p>Primary system for wumbOS Shell, LLMGauge, website work, scripting, documentation, and local experiments.</p>
  </div>

  <div class="feature-card">
    <h3>CUDA Work</h3>
    <p>Local llama.cpp/CUDA testing on SM120. Current Qwen campaign runtime: driver 610.57.04, CUDA 13.3, and llama.cpp b10449.</p>
  </div>
</div>

</details>

<details class="project-details">
<summary>Operating goal</summary>

The goal is to keep the system clean, stable, fast, keyboard-friendly, and useful for real work.

Experiments are welcome, but the baseline should remain reliable.

</details>
