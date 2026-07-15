+++
title = "Mellum2 Agent Backend Test"
description = "JetBrains Mellum2 Instruct and Thinking Q4_K_M tested through LLMGauge on WumboJetsII."
date = 2026-06-17
[extra]
record_type = "FIT TEST"
back_label = "Back to Lab Records"
back_url = "/records/"
+++

JetBrains Mellum2 12B-A2.5B Instruct Q4_K_M and Thinking Q4_K_M were tested through LLMGauge on WumboJetsII.

This is a practical local agent-backend fit test, not a leaderboard ranking.

<p class="kicker">2026-06-17 / LLMGAUGE MODEL TEST</p>

## Test Context

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Model family</span>
    <strong>JetBrains Mellum2</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Variants</span>
    <strong>Instruct / Thinking</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Quant</span>
    <strong>Q4_K_M</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Suite</span>
    <strong>agent-backend-v1</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Hardware</span>
    <strong>RTX 5070 12GB</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Result</span>
    <strong>64k fit confirmed</strong>
  </div>
</div>

## 64k Summary

<div class="feature-grid">
  <div class="feature-card">
    <h3>Mellum2 Instruct Q4_K_M</h3>
    <ul>
      <li><strong>Run:</strong> 5/5 complete, 0 failed</li>
      <li><strong>Generation:</strong> 251.0-257.2 tok/s</li>
      <li><strong>Prompt eval:</strong> 1603.1-2187.6 tok/s</li>
      <li><strong>Peak VRAM:</strong> 9203 MiB</li>
      <li><strong>Headroom:</strong> 3024 MiB</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Mellum2 Thinking Q4_K_M</h3>
    <ul>
      <li><strong>Run:</strong> 5/5 complete, 0 failed</li>
      <li><strong>Generation:</strong> 254.9-259.2 tok/s</li>
      <li><strong>Prompt eval:</strong> 1681.2-2274.9 tok/s</li>
      <li><strong>Peak VRAM:</strong> 9203 MiB</li>
      <li><strong>Headroom:</strong> 3024 MiB</li>
    </ul>
  </div>
</div>

## Context Ladder

Both variants completed the 8k / 16k / 32k agent-backend context ladder.

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Instruct ladder</span>
    <strong>8192 / 16384 / 32768</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Thinking ladder</span>
    <strong>8192 / 16384 / 32768</strong>
  </div>
</div>

<details class="project-details">
<summary>Additional fit checks</summary>

The Instruct model completed 64k fake-tool and synthetic-agent-preload checks.

The Thinking model completed the same fit/performance path.

These checks confirm that both variants fit and run through the selected LLMGauge paths on WumboJetsII. They do not automatically prove that either model is safe or preferable for daily use.

</details>

## Initial Read

Both Mellum2 variants look like strong fit/performance candidates for 64k local agent-backend testing on WumboJetsII.

The result is still a lab note, not a final quality verdict. Fit, speed, and artifact validity are only part of the decision. Shell safety, tool honesty, long-context retention, and practical output quality still need manual review before treating either model as a preferred daily driver.

Early qualitative read: Mellum2 Instruct is the safer candidate to prefer unless manual scoring shows otherwise. Mellum2 Thinking is also fast and stable, but it needs stricter review around shell safety, tool-use restraint, and whether its extra reasoning behavior actually improves outputs.
