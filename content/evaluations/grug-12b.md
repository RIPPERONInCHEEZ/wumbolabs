+++
title = "Grug 12B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 28

[extra]
kind = "model"
model_id = "grug-12b"
vendor = "kai-os"
findings_first = true
recommended_profile_id = "grug-12b-llamacpp-q4km"
recommended_profile_name = "llama.cpp Q4_K_M"
profile_count = 1
event_count = 2
latest_evidence_date = 2026-07-04
+++

## Overview

kai-os · 1 tested configuration · 2 evidence events · newest evidence 2026-07-04.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** llama.cpp Q4_K_M (current): [event result](#grug-lmx-speed-2026-07-04).
- **Latest evidence:** 2026-07-04: [event result](#grug-lmx-speed-2026-07-04)
- **2026-07-04** · llama.cpp · RTX 5070: classification BENCHMARK_ONLY (LMX local speed). [Event result](#grug-lmx-speed-2026-07-04)
- **2026-07-04** · llama.cpp · RTX 5070: classification SPECIALIZED_TEST / UNSCORED_SMOKE. [Event result](#grug-honesty-smoke-2026-07-04)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="grug-lmx-speed-2026-07-04"></a>

### 2026-07-04: LMX speed run

**Benchmark Only: LMX local speed** · config llama.cpp · RTX 5070 · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

Configuration: llama.cpp Q4_K_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/grug-12b/events/grug-lmx-speed-2026-07-04/REPORT.md)


LMX local speed evidence: 69.24 tok/s out (llama.cpp Q4_K_M).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `grug-12b-llamacpp-q4km`: llama.cpp Q4_K_M
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="grug-honesty-smoke-2026-07-04"></a>

### 2026-07-04: Honesty smoke + provenance refresh

**Specialized Test: honesty/provenance** · config llama.cpp · RTX 5070 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_SMOKE

Configuration: llama.cpp Q4_K_M.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/grug-12b/events/grug-honesty-smoke-2026-07-04/REPORT.md)


Honesty smoke (2026-07-04) and provenance-refresh re-run (2026-07-24) for the Grug practical record.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

###### Identity and scope

- Profile: `grug-12b-llamacpp-q4km`: llama.cpp Q4_K_M
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| llama.cpp · RTX 5070 | not recorded | llama.cpp | RTX 5070 | not recorded | 2 (2026-07-04, 2026-07-04) |

<details class="lab-findings-configs">
<summary>Configuration details: llama.cpp · RTX 5070</summary>

- Full profile name: llama.cpp Q4_K_M.
- Profile identity: `grug-12b-llamacpp-q4km`.
- Status: current canonical/recommended tested surface.
- Artifact (as recorded): kai-os/Grug-12B-GGUF Q4_K_M
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/grug-12b/profiles/grug-12b-llamacpp-q4km/profile.json)

Events on this configuration:

- [LMX speed run (2026-07-04)](/evaluations/grug-12b#grug-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)
- [Honesty smoke + provenance refresh (2026-07-04)](/evaluations/grug-12b#grug-honesty-smoke-2026-07-04); status: SPECIALIZED_TEST / UNSCORED_SMOKE

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-07-04 | [LMX speed run](#grug-lmx-speed-2026-07-04) | llama.cpp · RTX 5070 | BENCHMARK_ONLY (LMX local speed) |
| 2026-07-04 | [Honesty smoke + provenance refresh](#grug-honesty-smoke-2026-07-04) | llama.cpp · RTX 5070 | SPECIALIZED_TEST / UNSCORED_SMOKE |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/grug-12b)

### Legacy provenance

- [WumboLabs/eval-grug-12b @ `1f10b6b157b79b5077e9d4d540db57de78c697c7`](https://github.com/WumboLabs/eval-grug-12b/blob/1f10b6b157b79b5077e9d4d540db57de78c697c7/events/grug-honesty-smoke-2026-07.md)
- [WumboLabs/eval-grug-12b @ `1f10b6b157b79b5077e9d4d540db57de78c697c7`](https://github.com/WumboLabs/eval-grug-12b/blob/1f10b6b157b79b5077e9d4d540db57de78c697c7/events/grug-lmx-speed-2026-07-04.md)

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04): Grug-12B scored 243.6/300 (4.06 avg); viable, not a practical-default replacement. [Canonical evidence / full report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
