+++
title = "Methodology"
description = "How WumboLabs produces, reviews, validates, and bounds its evidence."
template = "methodology.html"

[extra]
back_label = "Back to Home"
back_url = "/"
+++

WumboLabs treats test results as **bounded evidence**, not universal rankings. Real hardware. Real testing. No hype.

This page explains how WumboLabs evidence is produced, reviewed, validated, and bounded. Model evaluations live under [Evaluations](/evaluations/); long-form benchmarks, fit tests, baselines, and lab notes live in [Reports](/records/).

## 01 — Evaluation philosophy

- **Real hardware, named systems.** Results come from real consumer hardware in daily use — currently the WumboJetsII workstation (Fedora 44, RTX 5070 12GB) — not from idealized or unnamed test farms.
- **Exact configuration matters.** A result without its model identity, artifact, runtime, and settings is not usable evidence. Records carry those details with the numbers.
- **Failures count as evidence.** A blocked admission, a failed gate, or a physical non-fit is a finding. See [Failures count](#07-failures-count).
- **Bounded claims.** Every result is scoped to the hardware, runtime, artifact, settings, and task set used to produce it.
- **Producer claims require reproduction.** A vendor or quantizer claim stays a producer claim until independently reproduced here. Records use language such as *advertised*, *tested*, *reproduced*, *not reproduced*, *blocked*, or *physically untestable* to keep that distinction visible.
- **Manual review is reviewer judgment.** Manual scores are reviewer judgment recorded under a stated rubric. They are useful review metadata, not objective proof of model quality.

## 02 — WELP

**WELP (WumboLabs Evaluation Lifecycle Protocol)** is the reproducible, phase-gated evaluation lifecycle used for WumboLabs model testing. It is published at <https://github.com/WumboLabs/welp> (DRAFT — not yet frozen as v1.0).

**What it is:** a fixed testing protocol that runs a model through ordered phases — provenance, admission, performance, practical viability, reliability, capability modules, context, variance, optimization, and stability. Each phase has a deterministic gate.

**Why phase gates exist:** the protocol is frozen before a model is evaluated. A failed gate is a valid result. This prevents post-hoc threshold tuning and makes early-stop behavior transparent.

**Why early-stop results are still valuable:** a model that stops at Phase 3 still produces bounded evidence about admission, performance, and practical viability. The absence of later-phase data is itself a finding, not a gap to hide.

**Why campaign depth differs:** different models reach different WELP depths. Some campaigns complete a deep end-to-end evaluation; others stop at a protocol-defined gate or fail an early viability gate and are not advanced. These differences are features of the protocol, not inconsistencies in effort.

**Context claims are bounded by occupancy:** configured capacity is not context validation. Full-context claims require the actual final rendered prompt at near-full occupancy of the usable budget (≥99% preferred, ≥97% hard floor, with reserved generation tokens), full-window performance, and useful-context evidence at that occupancy. Every native and officially advertised extension range — including each exact maximum — requires an explicit tested or demonstrated limiting disposition (`VALIDATED`, `FIT_LIMIT`, `INTEGRATION_BLOCKED`, or a measured `FAILED`) before context characterization may be called complete. A measured FAILED gate is a completed negative disposition, not a hidden one.

**Practical default ≠ context completeness:** selecting a comfortable everyday context is a separate decision from characterizing the full model-card envelope. Records report both independently.

**LocalMaxxing disposition is mandatory:** every full model campaign evaluates LocalMaxxing eligibility on the canonical practical stack and records exactly one completion disposition (`SUBMITTED`, `MEASURED_NOT_SUBMITTED`, `NOT_ELIGIBLE`, or `BLOCKED`). It can never be silently omitted. LocalMaxxing results are practical speed evidence, not the scientific source of truth.

**Report hierarchy:** each campaign has exactly one authoritative scientific report (`REPORT.md`), with the standardized `WELP-LAB-RECORD.md` as a companion summary of the same campaign. Website records are derivatives of that evidence; if a record ever conflicts with it, the campaign evidence governs.

**Where the canonical specification lives:** <https://github.com/WumboLabs/welp>.

## 03 — Evidence

Evaluation pages and technical records preserve the evidence needed to reproduce and audit a result:

- **Hardware:** the named machine and GPU, with relevant notes.
- **Runtime / build:** inference engine and version, with runtime notes.
- **Model / quant identity:** producer, tested artifact, precision, and artifact hash where available.
- **Context configuration:** practical default, guarded context, native model-card maximum, and the tested disposition of that maximum.
- **KV configuration:** cache precision and controls where recorded.
- **Sampling:** generation controls and reasoning state where recorded.
- **GPU residency / offload:** placement evidence where the runtime reports it, without overclaiming residency.
- **Raw outputs:** preserved by the underlying tooling so review does not depend on cleaned summaries.
- **Failures:** blocked admissions, failed gates, and non-fits recorded as findings.
- **Telemetry:** speed, timing, and memory observations with their measurement boundaries.
- **Provenance / fingerprints:** campaign identifiers and evidence fingerprints tying a record to its source campaign.
- **Canonical publication evidence:** each record maps to canonical public evidence, or to an explicit evidence-pending state that claims no evidence URL.

A distinction runs through all of it: a *requested* setting is what a run asked for; an *effective* behavior is what the model actually did. Evidence records note the difference instead of assuming one proves the other.

## 04 — Review and scoring

WumboLabs separates what a machine checked from what a human judged:

- **Deterministic checks:** structural validation of artifacts and results, and deterministic prompt-level checks where a suite defines them.
- **Structural checks:** structural comparison of runs or transcripts. Comparison is structural evidence only — no aggregate score, ranking, winner, statistical claim, or semantic judgment.
- **Executable checks — where admitted:** some suites deliberately do not execute generated code. That boundary is explicit, and changing it requires a separate containment decision, not a silent default.
- **Manual / reviewed scoring:** human scores recorded with rationale under a stated rubric. This is reviewer judgment — bounded, debatable, and never presented as objective truth.
- **Bounded judgment:** practical-use verdicts (for example, readiness for a role on one machine) are judgments tied to their context, not measurements of universal quality.

When a claim depends on judgment rather than a deterministic check, the record says so.

## 05 — Claim boundaries

A WumboLabs result establishes what happened:

- on the stated hardware,
- with the stated model and artifact,
- with the stated runtime,
- under the stated settings,
- on the stated tasks or corpus.

It does **not** automatically establish:

- universal model quality,
- a universal hallucination rate,
- broad hardware compatibility,
- API or cloud-hosted behavior,
- future runtime or version behavior,
- the truth of producer marketing claims.

Local evidence is the point: "full-GPU viable on this hardware" is a finding; "easy to run" would be an overreach.

## 06 — External benchmark evidence

Some evidence WumboLabs publishes comes from external benchmarks, imported rather than reinvented:

- LLMGauge imports, validates, and reports EleutherAI `lm-evaluation-harness` result evidence at a pinned qualification baseline. It does not recreate those benchmarks as native prompts and does not replace their authoritative scoring implementations. Imported benchmark evidence remains authoritative to its upstream benchmark and scoring implementation, and is not an LLMGauge-native quality score.
- LocalMaxxing is an external speed/performance protocol. WumboLabs campaigns record a LocalMaxxing disposition where the protocol applies; those results are practical speed evidence on the tested stack, not the scientific source of truth for model quality.

In both cases the upstream implementation owns what the benchmark measures. WumboLabs preserves, validates where supported, and reports that evidence with its boundaries.

## 07 — Failures count

Failures are findings, not embarrassments to hide. Valid recorded outcomes include:

- out-of-memory and physical non-fit results,
- failure to load or admission failure,
- integration blocked by runtime or toolchain,
- strict-output failure,
- hallucination or instability,
- protocol-defined early stop.

Negative results should not disappear because they are inconvenient. WELP freezes gates before evaluation so a failed gate cannot be tuned away after the fact, and early stops still yield bounded evidence about the phases a model did complete. The publication workflow retains negative results through its public-safe export review. Existing records include blocked runtime admissions, a failed full-GPU memory fit, and reliability-gate failures recorded exactly as encountered.

## 08 — Publication workflow

Website records are derivatives of campaign evidence, never a second independent source of model facts:

The [Evaluations website](/evaluations/) is the human discovery and sharing layer.
[WumboLabs/evaluations](https://github.com/WumboLabs/evaluations) holds the canonical
public scientific registry and reports. Local `research/model-evaluations/` holds
working/raw science; the NAS archive holds large model artifacts. Model, profile,
and event IDs describe science, not repository boundaries.

1. A WELP campaign closes, producing canonical local scientific evidence.
2. A public-safe publication export is prepared — no credentials, no private paths, no raw prompt logs; negative results retained.
3. Accepted event evidence is added to the existing **WumboLabs/evaluations** repository; no new `eval-*` repository is created. Publication and closeout run under the WELP execution-state lifecycle: a clean `COMPLETE_PASS` campaign proceeds automatically through terminal closeout under its standing closeout authorization; any failure or incomplete branch stops and waits for human review.
4. The central registry records the event, its model/profile relationships, and an exact repository + full commit SHA + relative artifact path citation.
5. The website pins that central registry commit and SHA-256; deterministic sync renders its derivative registry, pages, and datasets.
6. The site is built and validated, then deployed under the same lifecycle rule: clean-campaign closeout proceeds automatically; otherwise deployment waits for explicit human authorization.

Every closed campaign records an explicit website-publication disposition, and the website is generated from the pinned central publication registry — never from independently hand-maintained tables. Every record carries an explicit publication state. A record whose canonical evidence is not yet public renders with an **evidence publication pending** state and claims no canonical evidence URL — pending evidence fails closed. If a record ever conflicts with its campaign evidence, the campaign evidence governs. See the [publication operating contract](https://github.com/WumboLabs/welp/blob/main/docs/publication.md) for validation, historical compatibility, and exact sharing/citation rules.
