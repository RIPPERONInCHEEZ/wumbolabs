+++
title = "Gemmable 4 12B MTP"
description = "Gemmable 4 12B MTP — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 15

[extra]
kind = "model"
model_id = "gemmable-4-12b"
vendor = "Mia-AiLab (Gemma 4 12B MTP derivative)"
recommended_profile_id = "gemmable-4-12b-llamacpp-q4km"
recommended_profile_name = "llama.cpp Q4_K_M"
profile_count = 1
event_count = 2
latest_event_date = 2026-07-04
+++

WumboLabs tests **Gemmable 4 12B MTP** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q4_K_M (`gemmable-4-12b-llamacpp-q4km`, current) — [canonical evidence](https://github.com/WumboLabs/eval-gemmable-4-12b)
- **Latest evidence:** 2026-07-04 — LMX speed run

## Tested profiles

### llama.cpp Q4_K_M — CURRENT

Profile identity: `gemmable-4-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-gemmable-4-12b>

Events on this profile:

- [LMX speed run (2026-07-04)](/evaluations/gemmable-4-12b#gemmable-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Agent-backend + fake-tool runs (2026-06-21)](/evaluations/gemmable-4-12b#gemmable-agent-backend-2026-06-21) — SPECIALIZED_TEST

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="gemmable-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LMX speed run

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemmable-4-12b)

### Identity and scope

- Profile: `gemmable-4-12b-llamacpp-q4km` — llama.cpp Q4_K_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: 71.24 tok/s out (llama.cpp Q4_K_M).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="gemmable-agent-backend-2026-06-21"></a>

### 2026-06-21 — Agent-backend + fake-tool runs

**Specialized Test — agent backend** · profile: llama.cpp Q4_K_M · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST

[Canonical evidence for this event](https://github.com/WumboLabs/eval-gemmable-4-12b)

### Identity and scope

- Profile: `gemmable-4-12b-llamacpp-q4km` — llama.cpp Q4_K_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

Agent-backend-v1 and fake-tool answer-only probes for the Gemmable MTP artifact.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Shared comparison events

This model appears as a related model in shared multi-model comparisons. The underlying report remains one immutable shared artifact, published in the canonical model's evidence repository; this model's measured entries:

- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21) — Gemmable 4 12B MTP Q4_K_M scored 119.8/300 (2.0 avg) on the same suite

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **llama.cpp Q4_K_M** (`gemmable-4-12b-llamacpp-q4km`): <https://github.com/WumboLabs/eval-gemmable-4-12b>
