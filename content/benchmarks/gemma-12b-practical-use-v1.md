+++
title = "12B Gemma-Based Practical Use Test"
description = "Gemmable 4 12B, Gemma 4 12B QAT Q4, and Gemma 4 12B UD-Q5 tested through LLMGauge on WumboJetsII."
date = 2026-06-21
[extra]
back_label = "Back to Benchmarks"
back_url = "/benchmarks/"
+++

Gemmable 4 12B MTP Q4_K_M, Gemma 4 12B IT QAT UD-Q4_K_XL, and Gemma 4 12B IT UD-Q5_K_XL were tested through LLMGauge on WumboJetsII.

This is a practical local usefulness test, not a leaderboard ranking.

<p class="kicker">2026-06-21 / LLMGAUGE PRACTICAL USE TEST</p>

## Test Context

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Model group</span>
    <strong>12B Gemma-based</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Variants</span>
    <strong>Gemmable / QAT Q4 / UD-Q5</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Suite</span>
    <strong>wumbolabs-practical-use-v1</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Tool</span>
    <strong>LLMGauge v0.24</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Hardware</span>
    <strong>RTX 5070 12GB</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Result</span>
    <strong>QAT Q4 best overall</strong>
  </div>
</div>

## Practical Use Summary

<div class="feature-grid">
  <div class="feature-card">
    <h3>Gemma 4 12B IT QAT UD-Q4_K_XL</h3>
    <ul>
      <li><strong>Score:</strong> 259.2 / 300.0</li>
      <li><strong>Average:</strong> 4.32 / 5.00</li>
      <li><strong>Generation:</strong> 73.45 tok/s avg</li>
      <li><strong>Prompt eval:</strong> 1867.27 tok/s avg</li>
      <li><strong>Peak VRAM:</strong> 7539 MiB</li>
      <li><strong>Headroom:</strong> 4688 MiB</li>
      <li><strong>Verdict:</strong> best practical balance</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Gemma 4 12B IT UD-Q5_K_XL</h3>
    <ul>
      <li><strong>Score:</strong> 254.0 / 300.0</li>
      <li><strong>Average:</strong> 4.23 / 5.00</li>
      <li><strong>Generation:</strong> 59.15 tok/s avg</li>
      <li><strong>Prompt eval:</strong> 1522.53 tok/s avg</li>
      <li><strong>Peak VRAM:</strong> 9341 MiB</li>
      <li><strong>Headroom:</strong> 2886 MiB</li>
      <li><strong>Verdict:</strong> strong, but heavier</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Mia-AiLab Gemmable 4 12B MTP Q4_K_M</h3>
    <ul>
      <li><strong>Score:</strong> 119.8 / 300.0</li>
      <li><strong>Average:</strong> 2.00 / 5.00</li>
      <li><strong>Generation:</strong> 69.10 tok/s avg</li>
      <li><strong>Prompt eval:</strong> 1675.03 tok/s avg</li>
      <li><strong>Peak VRAM:</strong> 8173 MiB</li>
      <li><strong>Headroom:</strong> 4054 MiB</li>
      <li><strong>Verdict:</strong> structurally viable, practically mixed</li>
    </ul>
  </div>
</div>

## What Was Tested

The WumboLabs Practical Use Suite tested normal local-assistant usefulness across Linux, coding, Docker, honesty, summarization, and local LLM advice.

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Linux</span>
    <strong>Arch / NVIDIA update guidance</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Coding</span>
    <strong>Python log parser</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Docker</span>
    <strong>Compose review</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Honesty</span>
    <strong>Unknown package safety</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Summary</span>
    <strong>Technical run summary</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Local LLM</span>
    <strong>12GB GPU advice</strong>
  </div>
</div>

<details class="project-details">
<summary>Scored prompt results</summary>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Linux update guidance</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 1.50</li>
      <li><strong>Gemma QAT Q4:</strong> 4.44</li>
      <li><strong>Gemma UD-Q5:</strong> 4.39</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Python log parser</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 1.50</li>
      <li><strong>Gemma QAT Q4:</strong> 4.35</li>
      <li><strong>Gemma UD-Q5:</strong> 4.39</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Docker Compose review</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 1.50</li>
      <li><strong>Gemma QAT Q4:</strong> 4.19</li>
      <li><strong>Gemma UD-Q5:</strong> 3.40</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Unknown package honesty</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 1.50</li>
      <li><strong>Gemma QAT Q4:</strong> 4.17</li>
      <li><strong>Gemma UD-Q5:</strong> 4.30</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>Technical run summary</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 4.48</li>
      <li><strong>Gemma QAT Q4:</strong> 4.79</li>
      <li><strong>Gemma UD-Q5:</strong> 4.79</li>
    </ul>
  </div>

  <div class="feature-card">
    <h3>12GB local LLM advice</h3>
    <ul>
      <li><strong>Gemmable Q4_K_M:</strong> 1.50</li>
      <li><strong>Gemma QAT Q4:</strong> 3.98</li>
      <li><strong>Gemma UD-Q5:</strong> 4.13</li>
    </ul>
  </div>
</div>

The scores are manual local-context judgments. They are review aids, not universal model rankings.

</details>

<details class="project-details">
<summary>Runtime settings</summary>

| Field | Value |
|---|---|
| Backend | llama.cpp |
| Context | 8192 |
| Max tokens | 1200 |
| Temperature | 0.2 |
| Top-p | 0.95 |
| Batch | 256 |
| UBatch | 64 |
| GPU layers | 999 |

All three models completed the six-prompt suite with zero runtime failures.

</details>

## Initial Read

Gemma 4 12B IT QAT UD-Q4_K_XL was the strongest practical-use result in this comparison. It produced useful answers across the suite while also using the least VRAM and delivering the fastest average generation speed.

Gemma 4 12B IT UD-Q5_K_XL was also strong, but it used substantially more VRAM and ran slower. In this run, the heavier quant did not clearly justify its extra 12GB hardware cost.

Mia-AiLab Gemmable 4 12B MTP Q4_K_M fit well and produced a good summarization answer, but most practical prompts drifted into action-oriented or incomplete responses instead of directly answering from the provided context. It remains interesting for prompt-template or MTP runtime investigation, but it was not the best practical-use model in this comparison.

The no-hype takeaway: for WumboJetsII / RTX 5070 12GB practical local use, Gemma 4 12B IT QAT UD-Q4_K_XL is currently the strongest 12B Gemma-based result from this test.
