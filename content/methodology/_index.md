+++
title = "WELP v1.0 - Evaluation Methodology"
description = "Eight modular evaluation sections, original evidence, independent validation, and configuration-specific findings."
template = "methodology.html"

[extra]
back_label = "Back to Home"
back_url = "/"
+++

WELP v1.0 is the completed, released WumboLabs model-evaluation framework. The source, fixtures, tests, CLI instructions and scientific specification live in [WumboLabs/welp](https://github.com/WumboLabs/welp), with the release pinned at [v1.0.0](https://github.com/WumboLabs/welp/tree/v1.0.0).

## Eight independent sections

| Section | What it measures |
|---|---|
| Model / Core | A standardized baseline covering reliability, instruction following, assistant quality, practical context, real work, and capability probes. |
| Coding | Advanced construction and repair, with sandbox-executed checks. |
| Reasoning | Multi-constraint reasoning, grounded evidence, and revised conditions. |
| Long Context | Retrieval, synthesis, and retention/update tasks at fixed context checkpoints. |
| Tool Use | Tool selection, authorization compliance, and recovery using actual tool feedback. |
| Agentic | Independent harness readiness and bounded repository, system, and research tasks. |
| HelicopterBench | One-shot HTML5 helicopter-game construction and independently executed objective gameplay checks. |
| Runtime Performance | Deployment-attributed latency, throughput and available memory observations; comparisons only when their conditions support them. |

## Baseline first; advancement from evidence

Every model begins with the same Model/Core baseline. Capability evidence guides advanced-section selection under fixed methodology and workload budgets. Deferral, unsupported interfaces and explicit exploratory runs remain visible; they are not silently treated as ordinary advancement. Agentic readiness and results are independent of Model findings. Reasoning configurations and materially different deployment profiles are reported separately, never averaged.

## Original evidence and valid negative results

Tasks, scoring and budgets are fixed before measurement. Original requests, responses, attempt accounting and configuration attribution are retained. Finalized sections carry manifests and support offline reconstruction; independent review is used where the method requires it. Public-safe evidence omits private operational material and reviewer identities, not unfavorable findings.

A genuine **FAIL** or low benchmark score is a valid result. Token, turn or time exhaustion is **BUDGET_LIMITED**, not an invented semantic failure. Technical **INVALID** means the affected measurement cannot support scientific credit. Failed evidence verification, unresolved review, unsafe content or technical invalidity compromising required coverage stops publication for correction.

HelicopterBench /2 reports objective raw points and a normalized score, with no subjective visual score. Genuine captured gameplay is supplementary evidence, not a replacement for scoring. Historical /1 scores and footage retain their original methodology and attribution; /1 is never retrospectively scored under /2.

## Attribution and comparison limits

The framework separates model-quality findings from serving performance. Results belong to the measured model artifact and quantization, reasoning profile, runtime/backend, context, sampler, budgets, GPU and supplied host conditions. Hardware metadata is not independent machine attestation. Missing metrics remain unknown; two boundary memory samples are not continuous peaks. Finite task inventories do not establish universal capability or population-wide predictive validity.

There is no universal overall score, no averaged Model/Agentic verdict and no cross-model leaderboard. Runtime comparisons distinguish matched runtime conditions from broader deployment-stack differences.

## Review to publication

**Evaluation → evidence verification → scientific review → HUMAN_ACCEPTED → automatic public-safe publication.** Scientific acceptance authorizes routine publication without another per-campaign approval. Negative findings and budget-limited outcomes remain publishable; integrity, privacy, acceptance and provenance gates remain mandatory.

[WumboLabs/evaluations](https://github.com/WumboLabs/evaluations) is the canonical public results registry. Each published event has immutable repository/commit/path citations. This website pins a registry snapshot and renders it deterministically. [Evaluations](/evaluations/) provides model discovery; [Research](/records/) retains technical reports.

## Historical boundary

Earlier WELP revisions and other testing workflows remain historical evidence under their original methods. Release of v1.0 does not rescore, invalidate, or imply retesting those results. Compare only within the evidence's stated artifact, methodology and deployment limits.
