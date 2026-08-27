+++
title = "Labs"
description = "WumboLabs model evaluation lab records. Human-readable summaries of canonical GitHub evidence from real-hardware testing."
template = "labs_index.html"
sort_by = "weight"

[extra]
back_label = "Back to Home"
back_url = "/"
+++

## WumboLabs Evaluation Lab Records

WumboCore Lab Records are **human-readable summaries** of canonical evidence published in the `WumboLabs/eval-*` GitHub repositories. They are not independent evaluation artifacts.

**Canonical evidence:** GitHub eval repositories
**Human-readable summary:** this page
**Standardized benchmarks:** LocalMaxxing (where recorded)

Each record stays bounded by the tested artifact, runtime, hardware, configuration, and protocol snapshot. Results are not universal model rankings.

---

## WELP — WumboLabs Evaluation Lifecycle Protocol

WELP (WumboLabs Evaluation Lifecycle Protocol) is the reproducible, phase-gated evaluation lifecycle used for WumboLabs model testing. It is published at https://github.com/WumboLabs/welp.

**What it is:** a fixed testing protocol that runs a model through ordered phases — provenance, admission, performance, practical viability, reliability, capability modules, context, variance, optimization, and stability. Each phase has a deterministic gate.

**Why phase gates exist:** the protocol is frozen before a model is evaluated. A failed gate is a valid result. This prevents post-hoc threshold tuning and makes early-stop behavior transparent.

**Why early-stop results are still valuable:** a model that stops at Phase 3 still produces bounded evidence about admission, performance, and practical viability. The absence of later-phase data is itself a finding, not a gap to hide.

**Why campaign depth differs:** different models reach different WELP depths. Qwen3.8-27B completed a deep end-to-end campaign. Nemotron 3 Nano 4B stopped at a protocol-defined gate. Apodex 1.1 mini failed a viability gate and was not advanced. These differences are features of the protocol, not inconsistencies in effort.

**Where the canonical specification lives:** https://github.com/WumboLabs/welp (DRAFT — not yet frozen as v1.0).

---

## Current Lab Records

The table below summarizes each evaluation. Read individual records for evidence boundaries, hardware, and detailed findings.
