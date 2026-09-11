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

**Publication state:** every record maps to canonical public evidence. Records may appear with an explicit **Evidence publication pending** state while their canonical repository awaits publication; such records claim no canonical evidence URL, and the named local campaign evidence remains the scientific source until publication.

---

## WELP — WumboLabs Evaluation Lifecycle Protocol

WELP (WumboLabs Evaluation Lifecycle Protocol) is the reproducible, phase-gated evaluation lifecycle used for WumboLabs model testing. It is published at https://github.com/WumboLabs/welp.

**What it is:** a fixed testing protocol that runs a model through ordered phases — provenance, admission, performance, practical viability, reliability, capability modules, context, variance, optimization, and stability. Each phase has a deterministic gate.

**Why phase gates exist:** the protocol is frozen before a model is evaluated. A failed gate is a valid result. This prevents post-hoc threshold tuning and makes early-stop behavior transparent.

**Why early-stop results are still valuable:** a model that stops at Phase 3 still produces bounded evidence about admission, performance, and practical viability. The absence of later-phase data is itself a finding, not a gap to hide.

**Why campaign depth differs:** different models reach different WELP depths. Qwen3.8-27B completed a deep end-to-end campaign. Nemotron 3 Nano 4B stopped at a protocol-defined gate. Apodex 1.1 mini failed a viability gate and was not advanced. These differences are features of the protocol, not inconsistencies in effort.

**Context claims are bounded by occupancy:** configured capacity is not context validation. Full-context claims require the actual final rendered prompt at near-full occupancy of the usable budget (≥99% preferred, ≥97% hard floor, with reserved generation tokens), full-window performance, and useful-context evidence at that occupancy. Every native and officially advertised extension range — including each exact maximum — requires an explicit tested or demonstrated limiting disposition (`VALIDATED`, `FIT_LIMIT`, `INTEGRATION_BLOCKED`, or a measured `FAILED`) before context characterization may be called complete. A measured FAILED gate is a completed negative disposition, not a hidden one.

**Practical default ≠ context completeness:** selecting a comfortable everyday context is a separate decision from characterizing the full model-card envelope. Records report both independently.

**Report hierarchy:** each campaign has exactly one authoritative scientific report (`REPORT.md`), with the standardized `WELP-LAB-RECORD.md` as a companion summary of the same campaign. Website records are derivatives of that evidence; if a record ever conflicts with it, the campaign evidence governs.

**LocalMaxxing disposition is mandatory:** every full model campaign evaluates LocalMaxxing eligibility on the canonical practical stack and records exactly one completion disposition (`SUBMITTED`, `MEASURED_NOT_SUBMITTED`, `NOT_ELIGIBLE`, or `BLOCKED`). It can never be silently omitted. LocalMaxxing results are practical speed evidence, not the scientific source of truth.

**Website publication workflow:** every campaign records an explicit website-publication disposition, and this site is generated from a publication registry by a deterministic sync — records and the Labs index derive from the registry, never from hand-maintained tables. Publishing evidence repositories and deploying the site remain separate human gates.

**Where the canonical specification lives:** https://github.com/WumboLabs/welp (DRAFT — not yet frozen as v1.0).

---

## Current Lab Records

The table below summarizes each evaluation. Read individual records for evidence boundaries, hardware, and detailed findings.
