+++
title = "Mellum2 12B-A2.5B"
description = "Mellum2 12B-A2.5B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 12

[extra]
kind = "model"
model_id = "mellum2-12b-a2.5b"
vendor = "JetBrains"
recommended_profile_id = "mellum2-12b-a2.5b-llamacpp-q4km-instruct"
recommended_profile_name = "llama.cpp Q4_K_M (Instruct)"
profile_count = 2
event_count = 3
latest_event_date = 2026-07-04
+++

WumboLabs tests **Mellum2 12B-A2.5B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q4_K_M (Instruct) (`mellum2-12b-a2.5b-llamacpp-q4km-instruct`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-lmx-speed-2026-07-04/REPORT.md)
- **Latest evidence:** 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

## Tested profiles

### llama.cpp Q4_K_M (Instruct) — CURRENT

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-agent-backend-64k-2026-06-17/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

Events on this profile:

- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

### llama.cpp Q4_K_M (Instruct) — CURRENT

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/profile.json)

Events on this profile:

- [LocalMaxxing LMX speed runs (Instruct + Thinking) (2026-07-04)](/evaluations/mellum2-12b-a2-5b#mellum2-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Fake-tool honesty runs (64k) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-fake-tool-2026-06-17) — SPECIALIZED_TEST / UNSCORED_PROBES
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="mellum2-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M (Instruct) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-lmx-speed-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: Instruct 261.41 tok/s out; Thinking 265.47 tok/s out (llama.cpp, Q4_K_M). Measured locally; submission disposition covered by the 2026-09-10 backfill scope for canonical profiles only.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="mellum2-fake-tool-2026-06-17"></a>

### 2026-06-17 — Fake-tool honesty runs (64k)

**Specialized Test — fake-tool honesty** · profile: llama.cpp Q4_K_M (Instruct) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_PROBES

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-fake-tool-2026-06-17/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, reliability
- Hardware: WumboJetsII (RTX 5070 12GB)

Fake-tool honesty probes at 64k for both Mellum2 variants; feeding the agent-backend manual scores.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="mellum2-agent-backend-64k-2026-06-17"></a>

### 2026-06-17 — Agent backend fit test (64k, Instruct + Thinking)

**Specialized Test — LLMGauge agent-backend-v1** · profile: llama.cpp Q4_K_M (Instruct) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict) · related profiles: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/mellum2-12b-a2.5b/events/mellum2-agent-backend-64k-2026-06-17/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b)
[Profile Metadata: mellum2-12b-a2.5b-llamacpp-q4km-thinking](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)

[Long-form report: Mellum2 Agent Backend Test](/records/mellum2-agent-backend-test/)

### Identity and scope

- Profile: `mellum2-12b-a2.5b-llamacpp-q4km-instruct` — llama.cpp Q4_K_M (Instruct)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

Instruct + Thinking Q4_K_M through LLMGauge agent-backend-v1 at 64k on WumboJetsII. 64k fit confirmed (Instruct 5/5 complete, 251.0-257.2 tok/s out, 9203 MiB peak VRAM). Manual scores: Instruct preferred (overall trust 3.7/5) over Thinking; neither safe for unsupervised shell/systemd operations. Not a general model-quality verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Related tested profile: `mellum2-12b-a2.5b-llamacpp-q4km-thinking` — both variants were tested in the same event.

## Shared comparison events

This model appears in shared multi-model comparisons. Each report is stored once in WumboLabs/evaluations/shared-events/; the model's measured entries remain attributed to the same historical event:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — Instruct 239.9/300 (4.0); Thinking 232.8/300 (3.88). — [Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **mellum2-12b-a2.5b-llamacpp-q4km-thinking**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/profile.json)
- **mellum2-12b-a2.5b-llamacpp-q4km-instruct**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/mellum2-12b-a2.5b/profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/profile.json)

### Legacy provenance

Historical source identifiers — the legacy `eval-*` repositories named below were retired (deleted from GitHub) on 2026-09-14 after verified consolidation into [WumboLabs/evaluations](https://github.com/WumboLabs/evaluations); these identifiers are provenance, not live sources.

- WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787` — `events/mellum2-agent-backend-64k-2026-06-17.md`
- WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787` — `events/mellum2-fake-tool-2026-06-17.md`
- WumboLabs/eval-mellum2-12b-a2.5b-instruct @ `87d004ee76b6be247308fe69705d8ceb8d12c787` — `events/mellum2-lmx-speed-2026-07-04.md`
