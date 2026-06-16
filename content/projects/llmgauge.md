+++
title = "LLMGauge"
description = "Markdown-first local LLM evaluation workflow for prompt suites, repeatable runs, raw outputs, and practical model comparison."
template = "project.html"
weight = 2
aliases = ["/projects/quant-lab/", "/projects/wumbogauge/"]
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
+++

**Local LLM evaluation workflow**  
**Status:** Active local testing workflow

LLMGauge is a Markdown-first local LLM evaluation workflow for testing practical model behavior on real hardware.

It is built around prompt suites, repeatable runs, raw output preservation, speed notes, context behavior, scoring notes, and evidence-based local model comparison.

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Focus</span>
    <strong>Local LLM evals</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Format</span>
    <strong>Markdown-first</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Models</span>
    <strong>GGUF / llama.cpp</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Hardware</span>
    <strong>Real workstation</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Output</span>
    <strong>Reports + raw logs</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Goal</span>
    <strong>Useful signal</strong>
  </div>
</div>

## What It Tests

<div class="feature-grid">
  <div class="feature-card">
    <h3>Honesty</h3>
    <p>Tests how models handle uncertainty, unknown tools, niche facts, and situations where fabrication is likely.</p>
  </div>

  <div class="feature-card">
    <h3>Linux and Ops</h3>
    <p>Evaluates practical troubleshooting for Linux, Docker, networking, ZFS, configuration review, and system administration.</p>
  </div>

  <div class="feature-card">
    <h3>Coding Usefulness</h3>
    <p>Checks whether model output is usable, bounded, testable, and appropriate for real terminal-driven workflows.</p>
  </div>

  <div class="feature-card">
    <h3>Context Behavior</h3>
    <p>Tracks whether models retain constraints, instructions, and task details as prompts grow longer.</p>
  </div>

  <div class="feature-card">
    <h3>Safety and Judgment</h3>
    <p>Looks for unsafe commands, risky assumptions, overconfident claims, and missing verification steps.</p>
  </div>

  <div class="feature-card">
    <h3>Performance Notes</h3>
    <p>Captures speed, prompt processing, generation behavior, and hardware constraints alongside qualitative results.</p>
  </div>
</div>

## Why It Exists

Local LLM testing can easily become ad hoc: one-off prompts, screenshots, vibes, and loose comparisons.

LLMGauge exists to make that process more repeatable. It preserves prompts, outputs, reports, and notes so model behavior can be compared over time instead of judged from memory.

The goal is not to create a universal leaderboard. The goal is to understand which models are actually useful for local technical work.

## Current Role

LLMGauge is closely related to Monolith.

Monolith is the local AI workbench. LLMGauge is the evaluation workflow behind practical model testing: prompt suites, controlled runs, raw outputs, notes, and comparison structure.

Over time, more of this workflow is expected to move into Monolith directly.
