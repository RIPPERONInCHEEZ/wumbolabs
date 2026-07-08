+++
title = "Monolith"
description = "Local-first AI workbench for testing, comparing, and evaluating local LLMs on real hardware."
template = "project.html"
weight = 4
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
+++

## Try Monolith

Monolith is the local AI workbench layer on WumboLabs: a local web UI for model tracking and future LLMGauge import workflows. LLMGauge remains the flagship public evidence tool.

It is a technical public alpha. Setup is still manual, and it is intended for users comfortable with Linux, Python, local model files, GGUF, and llama.cpp-style workflows.

<div class="feature-grid">
  <div class="feature-card">
    <h3>1. Open the repo</h3>
    <p>Start from the GitHub repository and read the current public alpha setup notes.</p>
  </div>

  <div class="feature-card">
    <h3>2. Clone it locally</h3>
    <p>Monolith runs as a local web UI. It is not a hosted service or production deployment target.</p>
  </div>

  <div class="feature-card">
    <h3>3. Run setup checks</h3>
    <p>Use the setup diagnostics to confirm the local environment before adding real model profiles.</p>
  </div>

  <div class="feature-card">
    <h3>4. Start the local UI</h3>
    <p>The current local interface runs at <code>http://127.0.0.1:8765/</code>.</p>
  </div>
</div>

<div class="start-actions page-start-actions">
  <a href="https://github.com/WumboLabs/monolith">GitHub Repository</a>
  <a href="https://github.com/WumboLabs/monolith/blob/main/docs/public_alpha.md">Public Alpha Notes</a>
</div>

## Current Development Note

Recent Monolith development is focused on importing LLMGauge artifacts into the local workbench: import tables, artifact metadata parsing, importer architecture, listing pages, detail pages, and sidebar UI polish.

That work is active development beyond the current public alpha release metadata, so it should be read as current project direction rather than a packaged release claim.

{{ monolith_status() }}

## Current Roadmap

The roadmap below is synced from Monolith's canonical `docs/ROADMAP.md` public website block.

{{ generated_markdown(path="data/generated/monolith-roadmap.md") }}
