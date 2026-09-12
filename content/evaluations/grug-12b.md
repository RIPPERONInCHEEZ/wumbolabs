+++
title = "Grug 12B"
description = "Grug 12B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 16

[extra]
kind = "model"
model_id = "grug-12b"
vendor = "kai-os"
recommended_profile_id = "grug-12b-llamacpp-q4km"
recommended_profile_name = "llama.cpp Q4_K_M"
profile_count = 1
event_count = 2
latest_event_date = 2026-07-04
+++

WumboLabs tests **Grug 12B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q4_K_M (`grug-12b-llamacpp-q4km`, current) — [canonical evidence](https://github.com/WumboLabs/eval-grug-12b)
- **Latest evidence:** 2026-07-04 — LMX speed run

## Tested profiles

### llama.cpp Q4_K_M — CURRENT

Profile identity: `grug-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-grug-12b>

Events on this profile:

- [LMX speed run (2026-07-04)](/evaluations/grug-12b#grug-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Honesty smoke + provenance refresh (2026-07-04)](/evaluations/grug-12b#grug-honesty-smoke-2026-07-04) — SPECIALIZED_TEST / UNSCORED_SMOKE

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="grug-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LMX speed run

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-grug-12b)

### Identity and scope

- Profile: `grug-12b-llamacpp-q4km` — llama.cpp Q4_K_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: 69.24 tok/s out (llama.cpp Q4_K_M).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="grug-honesty-smoke-2026-07-04"></a>

### 2026-07-04 — Honesty smoke + provenance refresh

**Specialized Test — honesty/provenance** · profile: llama.cpp Q4_K_M · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_SMOKE

[Canonical evidence for this event](https://github.com/WumboLabs/eval-grug-12b)

### Identity and scope

- Profile: `grug-12b-llamacpp-q4km` — llama.cpp Q4_K_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

Honesty smoke (2026-07-04) and provenance-refresh re-run (2026-07-24) for the Grug practical record.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Shared comparison events

This model appears as a related model in shared multi-model comparisons. The underlying report remains one immutable shared artifact, published in the canonical model's evidence repository; this model's measured entries:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — Grug-12B scored 243.6/300 (4.06 avg); viable, not a practical-default replacement.

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **llama.cpp Q4_K_M** (`grug-12b-llamacpp-q4km`): <https://github.com/WumboLabs/eval-grug-12b>
