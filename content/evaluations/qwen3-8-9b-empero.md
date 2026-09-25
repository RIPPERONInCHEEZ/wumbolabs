+++
title = "Qwen3.8-9B (Empero)"
description = "Qwen3.8-9B (Empero) — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 18

[extra]
kind = "model"
model_id = "qwen3.8-9b-empero"
vendor = "empero-ai (Qwen3.8 derivative)"
recommended_profile_id = "qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver"
recommended_profile_name = "llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane)"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-09-01
+++

WumboLabs tests **Qwen3.8-9B (Empero)** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane) (`qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver`, specialized) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-9b-empero/events/qwen38-empero-9b-distill-wumboserver-2026-09-01/REPORT.md)
- **Latest evidence:** 2026-09-01 — WumboServer RTX 2060S admission/boundary + LocalMaxxing (Q4/Q5/Q6)

## Tested profiles

### LLMGauge vendor-alignment battery Q8_0 — CURRENT

Profile identity: `qwen3.8-9b-empero-vendor-battery`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-9b-empero/events/qwen38-empero-9b-vendor-battery-2026-08-18/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero/profiles/qwen3.8-9b-empero-vendor-battery/profile.json)

Events on this profile:

- [LLMGauge vendor-alignment battery (9B Q8_0) (2026-08-18)](/evaluations/qwen3-8-9b-empero#qwen38-empero-9b-vendor-battery-2026-08-18) — SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

### llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane) — SPECIALIZED

Profile identity: `qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-9b-empero/events/qwen38-empero-9b-distill-wumboserver-2026-09-01/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero/profiles/qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver/profile.json)

Events on this profile:

- [WumboServer RTX 2060S admission/boundary + LocalMaxxing (Q4/Q5/Q6) (2026-09-01)](/evaluations/qwen3-8-9b-empero#qwen38-empero-9b-distill-wumboserver-2026-09-01) — BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen38-empero-9b-distill-wumboserver-2026-09-01"></a>

### 2026-09-01 — WumboServer RTX 2060S admission/boundary + LocalMaxxing (Q4/Q5/Q6)

**Benchmark Only — WumboServer hardware lane** · profile: llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-9b-empero/events/qwen38-empero-9b-distill-wumboserver-2026-09-01/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero)

### Identity and scope

- Profile: `qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver` — llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboServer (RTX 2060 SUPER 8GB)

empero-ai/Qwen3.8-9B-Distill-GGUF Q4_K_M/Q5_K_M/Q6_K on WumboServer RTX 2060S: admission benchmark, Q6 fit boundary, Q5 WELP-style serving campaign, and LocalMaxxing reconciliation (9b-q4 60.4 tok/s out, 5.37 GB peak VRAM). Hardware-lane evidence; Ornith-9B admission on the same GPU is recorded under its own model.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen38-empero-9b-vendor-battery-2026-08-18"></a>

### 2026-08-18 — LLMGauge vendor-alignment battery (9B Q8_0)

**Specialized Test — vendor alignment** · profile: LLMGauge vendor-alignment battery Q8_0 · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-9b-empero/events/qwen38-empero-9b-vendor-battery-2026-08-18/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero)

### Identity and scope

- Profile: `qwen3.8-9b-empero-vendor-battery` — LLMGauge vendor-alignment battery Q8_0
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge vendor-alignment battery on empero-ai Qwen3.8-9B (Q8_0 + base Q4).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen3.8-9b-empero-vendor-battery**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero/profiles/qwen3.8-9b-empero-vendor-battery/profile.json)
- **qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/afa0473404135fea513a7cb4ba4d9f568aa8306e/models/qwen3.8-9b-empero/profiles/qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.8-9b-empero @ `ca2784b96332038bce2e7b521fe788e86aac6966`](https://github.com/WumboLabs/eval-qwen3.8-9b-empero/blob/ca2784b96332038bce2e7b521fe788e86aac6966/events/qwen38-empero-9b-vendor-battery-2026-08-18.md)
- [WumboLabs/eval-qwen3.8-9b-empero-distill-wumboserver @ `c8fac91ab8d249b3fcba3512851cda61240868db`](https://github.com/WumboLabs/eval-qwen3.8-9b-empero-distill-wumboserver/blob/c8fac91ab8d249b3fcba3512851cda61240868db/events/qwen38-empero-9b-distill-wumboserver-2026-09-01.md)
