+++
title = "Bonsai 27B (Q1_0)"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 26

[extra]
kind = "model"
model_id = "bonsai-27b"
vendor = "Upstream identity unresolved (local artifact name)"
findings_first = true
recommended_profile_id = "bonsai-27b-q1-0-llamacpp"
recommended_profile_name = "llama.cpp Q1_0 (unscored smoke payload)"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-07-14
+++

## Overview

Upstream identity unresolved (local artifact name) · 1 tested configuration · 1 evidence event · newest evidence 2026-07-14.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Recommended configuration:** llama.cpp Q1_0 (unscored smoke payload) (specialized): [event result](#bonsai-27b-smoke-v070-2026-07-14).
- **Latest evidence:** 2026-07-14: [event result](#bonsai-27b-smoke-v070-2026-07-14)
- **2026-07-14** · Q1_0 · llama.cpp: classification SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED. [Event result](#bonsai-27b-smoke-v070-2026-07-14)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="bonsai-27b-smoke-v070-2026-07-14"></a>

### 2026-07-14: LLMGauge v0.70 smoke runs (Q1_0 payload, unscored)

**Specialized Test: unscored smoke** · config Q1_0 · llama.cpp · maturity: UNRESOLVED_HISTORICAL · status: SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED

Configuration: llama.cpp Q1_0 (unscored smoke payload).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/bonsai-27b/events/bonsai-27b-smoke-v070-2026-07-14/REPORT.md)


Three completed 1-prompt unscored smoke runs (JSON-discipline, honesty, fake-field) under LLMGauge v0.70 with a Q1_0 27B artifact locally labeled bonsai_27b_q1_0. Upstream artifact identity unresolved (model paths redacted in v0.70+ provenance); archaeology preserves a 3,803,452,480-byte fingerprint. Not a quality verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.
###### Identity caveat

The exact upstream artifact identity cannot be proven from retained evidence: LLMGauge
v0.70+ provenance redacts model paths, and only the local artifact name `bonsai_27b_q1_0`
plus a 3,803,452,480-byte fingerprint survive. No canonical profile repository is claimed
for this event until the upstream identity is established. The runs are unscored smokes;
no quality claim is made.

###### Identity and scope

- Profile: `bonsai-27b-q1-0-llamacpp`: llama.cpp Q1_0 (unscored smoke payload)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q1_0 · llama.cpp | Q1_0 | llama.cpp | not recorded | not recorded | 1 (2026-07-14) |

<details class="lab-findings-configs">
<summary>Configuration details: Q1_0 · llama.cpp</summary>

- Full profile name: llama.cpp Q1_0 (unscored smoke payload).
- Profile identity: `bonsai-27b-q1-0-llamacpp`.
- Status: specialized tested surface.
- Artifact (as recorded): Upstream identity unresolved; retained public evidence describes a 3,803,452,480-byte Q1_0 artifact fingerprint.
- Runtime (as recorded): llama.cpp.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/bonsai-27b/profiles/bonsai-27b-q1-0-llamacpp/profile.json)

Events on this configuration:

- [LLMGauge v0.70 smoke runs (Q1_0 payload, unscored) (2026-07-14)](/evaluations/bonsai-27b#bonsai-27b-smoke-v070-2026-07-14); status: SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-07-14 | [LLMGauge v0.70 smoke runs (Q1_0 payload, unscored)](#bonsai-27b-smoke-v070-2026-07-14) | Q1_0 · llama.cpp | SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/bonsai-27b)

### Legacy provenance

- [RIPPERONInCHEEZ/wumbolabs @ `e27ddcb89b56c27e87d7a3af34003cd8c6d7355b`](https://github.com/RIPPERONInCHEEZ/wumbolabs/blob/e27ddcb89b56c27e87d7a3af34003cd8c6d7355b/data/labs-events/bonsai-27b-smoke-v070-2026-07-14.md)
