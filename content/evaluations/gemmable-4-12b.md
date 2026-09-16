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

- **Recommended profile:** llama.cpp Q4_K_M (`gemmable-4-12b-llamacpp-q4km`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-lmx-speed-2026-07-04/REPORT.md)
- **Latest evidence:** 2026-07-04 — LMX speed run

## Tested profiles

### llama.cpp Q4_K_M — CURRENT

Profile identity: `gemmable-4-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/36ad3309ddb34da143f6fcf629aa1d1eb83f3e25/models/gemmable-4-12b/profiles/gemmable-4-12b-llamacpp-q4km/profile.json)

Events on this profile:

- [LMX speed run (2026-07-04)](/evaluations/gemmable-4-12b#gemmable-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Agent-backend + fake-tool runs (2026-06-21)](/evaluations/gemmable-4-12b#gemmable-agent-backend-2026-06-21) — SPECIALIZED_TEST

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="gemmable-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LMX speed run

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-lmx-speed-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/36ad3309ddb34da143f6fcf629aa1d1eb83f3e25/models/gemmable-4-12b)

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

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-agent-backend-2026-06-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/36ad3309ddb34da143f6fcf629aa1d1eb83f3e25/models/gemmable-4-12b)

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

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21) — Gemmable 4 12B MTP Q4_K_M scored 119.8/300 (2.0 avg) on the same suite — [Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-06-21/REPORT.md)

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **gemmable-4-12b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/36ad3309ddb34da143f6fcf629aa1d1eb83f3e25/models/gemmable-4-12b/profiles/gemmable-4-12b-llamacpp-q4km/profile.json)

### Legacy provenance

- [WumboLabs/eval-gemmable-4-12b @ `f307603ad9e1515ff59261d86f842e1cace43980`](https://github.com/WumboLabs/eval-gemmable-4-12b/blob/f307603ad9e1515ff59261d86f842e1cace43980/events/gemmable-agent-backend-2026-06.md)
- [WumboLabs/eval-gemmable-4-12b @ `f307603ad9e1515ff59261d86f842e1cace43980`](https://github.com/WumboLabs/eval-gemmable-4-12b/blob/f307603ad9e1515ff59261d86f842e1cace43980/events/gemmable-lmx-speed-2026-07-04.md)
