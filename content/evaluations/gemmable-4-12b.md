+++
title = "Gemmable 4 12B MTP"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 27

[extra]
kind = "model"
model_id = "gemmable-4-12b"
vendor = "Mia-AiLab (Gemma 4 12B MTP derivative)"
findings_first = true
recommended_profile_id = "gemmable-4-12b-llamacpp-q4km"
recommended_profile_name = "llama.cpp Q4_K_M"
profile_count = 1
event_count = 2
latest_evidence_date = 2026-07-04
+++

## Overview

Mia-AiLab (Gemma 4 12B MTP derivative) · 1 tested configuration · 2 evidence events · newest evidence 2026-07-04.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** llama.cpp Q4_K_M (current): [event result](#gemmable-lmx-speed-2026-07-04).
- **Latest evidence:** 2026-07-04: [event result](#gemmable-lmx-speed-2026-07-04)
- **2026-07-04** · llama.cpp · RTX 5070: classification BENCHMARK_ONLY (LMX local speed). [Event result](#gemmable-lmx-speed-2026-07-04)
- **2026-06-21** · llama.cpp · RTX 5070: classification SPECIALIZED_TEST. [Event result](#gemmable-agent-backend-2026-06-21)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="gemmable-lmx-speed-2026-07-04"></a>

### 2026-07-04: LMX speed run

**Benchmark Only: LMX local speed** · config llama.cpp · RTX 5070 · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

Configuration: llama.cpp Q4_K_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-lmx-speed-2026-07-04/REPORT.md)


LMX local speed evidence: 71.24 tok/s out (llama.cpp Q4_K_M).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `gemmable-4-12b-llamacpp-q4km`: llama.cpp Q4_K_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="gemmable-agent-backend-2026-06-21"></a>

### 2026-06-21: Agent-backend + fake-tool runs

**Specialized Test: agent backend** · config llama.cpp · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST

Configuration: llama.cpp Q4_K_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemmable-4-12b/events/gemmable-agent-backend-2026-06-21/REPORT.md)


Agent-backend-v1 and fake-tool answer-only probes for the Gemmable MTP artifact.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `gemmable-4-12b-llamacpp-q4km`: llama.cpp Q4_K_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| llama.cpp · RTX 5070 | not recorded | llama.cpp | RTX 5070 | not recorded | 2 (2026-06-21, 2026-07-04) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp Q4_K_M.
- Profile identity: `gemmable-4-12b-llamacpp-q4km`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): Mia-AiLab/Gemmable-4-12B-MTP-GGUF Q4_K_M
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemmable-4-12b/profiles/gemmable-4-12b-llamacpp-q4km/profile.json)

Events on this configuration:

- [LMX speed run (2026-07-04)](/evaluations/gemmable-4-12b#gemmable-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)
- [Agent-backend + fake-tool runs (2026-06-21)](/evaluations/gemmable-4-12b#gemmable-agent-backend-2026-06-21); status: SPECIALIZED_TEST

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-07-04 | [LMX speed run](#gemmable-lmx-speed-2026-07-04) | llama.cpp · RTX 5070 | BENCHMARK_ONLY (LMX local speed) |
| 2026-06-21 | [Agent-backend + fake-tool runs](#gemmable-agent-backend-2026-06-21) | llama.cpp · RTX 5070 | SPECIALIZED_TEST |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemmable-4-12b)

### Legacy provenance

- [WumboLabs/eval-gemmable-4-12b @ `f307603ad9e1515ff59261d86f842e1cace43980`](https://github.com/WumboLabs/eval-gemmable-4-12b/blob/f307603ad9e1515ff59261d86f842e1cace43980/events/gemmable-agent-backend-2026-06.md)
- [WumboLabs/eval-gemmable-4-12b @ `f307603ad9e1515ff59261d86f842e1cace43980`](https://github.com/WumboLabs/eval-gemmable-4-12b/blob/f307603ad9e1515ff59261d86f842e1cace43980/events/gemmable-lmx-speed-2026-07-04.md)

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21): Gemmable 4 12B MTP Q4_K_M scored 119.8/300 (2.0 avg) on the same suite [Canonical evidence / full report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-06-21/REPORT.md)
