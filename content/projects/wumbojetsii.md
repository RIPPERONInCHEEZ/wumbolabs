+++
title = "WumboJetsII"
description = "Headless Fedora 44 AI compute node for local-model evaluation, LLMGauge runs, and WumboLabs evidence."
template = "project.html"
weight = 100
[extra]
back_label = "Back to Home"
back_url = "/"
public_project = false
content_kind = "infrastructure"
+++

WumboJetsII is the WumboLabs AI compute node: a headless Fedora 44 system dedicated to local-model evaluation and compute work rather than daily desktop use.

It runs Fedora 44 without a desktop session and supports LLMGauge testing, deeper local-model evaluation campaigns, and local execution work for the wider lab.

<strong>Headless AI compute / evaluation hardware</strong>

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">OS</span>
    <strong>Fedora 44</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Form Factor</span>
    <strong>Headless, no desktop session</strong>
  </div>

  <div class="info-card">
    <span class="info-label">GPU</span>
    <strong>AMD Radeon AI PRO R9700 32GB</strong>
  </div>

  <div class="info-card">
    <span class="info-label">CPU / Memory</span>
    <strong>Ryzen 7 9800X3D / 32GB DDR5</strong>
  </div>

  <div class="info-card">
    <span class="info-label">AI Stack</span>
    <strong>llama.cpp ROCm/HIP and Vulkan builds</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Local AI</span>
    <strong>R9700 evaluation hardware</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Role</span>
    <strong>Headless AI compute node</strong>
  </div>
</div>

## Role in WumboLabs

WumboJetsII is where WumboLabs local AI compute happens: LLMGauge runs, deeper model-evaluation campaigns, and supporting execution work for the other systems in the lab.

The AMD Radeon AI PRO R9700 provides 32GB of physical GPU VRAM for local AI compute. ROCm/HIP and Vulkan development and testing are hardware-scoped; runtime qualification applies to the tested model, artifact, build, backend, and configuration, not to every workload or to a preferred runtime.

The Qwen3.8-27B deep-evaluation campaign ran on the RTX 5070 with llama.cpp/CUDA; that GPU has since been removed, and the campaign stands as historical evidence for that hardware. [Read the historical campaign report](/records/qwen38-27b-rtx5070-evaluation/) for its runtime-specific findings and limitations. The Qwen3.8 H1 canonical profile from that era is documented on the [canonical Qwen3.8 evaluation page](/evaluations/qwen38-27b/#h1-canonical-promotion-2026-09-09).

<details class="project-details">
<summary>Focus areas</summary>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Headless Fedora</h3>
    <p>Fedora 44 operated without a desktop session, managed remotely, and kept to a stable baseline for compute work.</p>
  </div>

  <div class="feature-card">
    <h3>Local LLM Evaluation</h3>
    <p>LLMGauge workflows and WELP scientific evaluation on the R9700, with model/runtime compatibility, context limits, generation speed, VRAM behavior, and reliability recorded for each tested stack.</p>
  </div>

  <div class="feature-card">
    <h3>Lab Compute Infrastructure</h3>
    <p>Execution node for WumboLabs evaluation campaigns and local runs that support the other systems in the environment.</p>
  </div>

  <div class="feature-card">
    <h3>ROCm and Vulkan Work</h3>
    <p>Hardware-scoped AMD compute testing on RDNA4 (gfx1201), including llama.cpp HIP and Vulkan builds, with claim boundaries kept explicit.</p>
  </div>
</div>

</details>

<details class="project-details">
<summary>Operating goal</summary>

The goal is to keep the system stable, reliable, and useful as dedicated evaluation hardware.

Experiments are welcome, but the baseline should remain dependable for compute work.

</details>
