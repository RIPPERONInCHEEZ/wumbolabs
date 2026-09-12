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

- **Recommended profile:** llama.cpp Q4_K_M (Instruct) (`mellum2-12b-a2.5b-llamacpp-q4km-instruct`, current) — [canonical evidence](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct)
- **Latest evidence:** 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

## Tested profiles

### llama.cpp Q4_K_M (Instruct) — CURRENT

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-thinking`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct>

Events on this profile:

- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

### llama.cpp Q4_K_M (Instruct) — CURRENT

Profile identity: `mellum2-12b-a2.5b-llamacpp-q4km-instruct`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct>

Events on this profile:

- [LocalMaxxing LMX speed runs (Instruct + Thinking) (2026-07-04)](/evaluations/mellum2-12b-a2-5b#mellum2-lmx-speed-2026-07-04) — BENCHMARK_ONLY (LMX local speed)
- [Fake-tool honesty runs (64k) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-fake-tool-2026-06-17) — SPECIALIZED_TEST / UNSCORED_PROBES
- [Agent backend fit test (64k, Instruct + Thinking) (2026-06-17)](/evaluations/mellum2-12b-a2-5b#mellum2-agent-backend-64k-2026-06-17) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="mellum2-lmx-speed-2026-07-04"></a>

### 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

**Benchmark Only — LMX local speed** · profile: llama.cpp Q4_K_M (Instruct) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct)

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

[Canonical evidence for this event](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct)

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

[Canonical evidence for this event](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct)

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

This model appears as a related model in shared multi-model comparisons. The underlying report remains one immutable shared artifact, published in the canonical model's evidence repository; this model's measured entries:

- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04) — Instruct 239.9/300 (4.0); Thinking 232.8/300 (3.88).

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **llama.cpp Q4_K_M (Instruct)** (`mellum2-12b-a2.5b-llamacpp-q4km-thinking`): <https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-instruct>
