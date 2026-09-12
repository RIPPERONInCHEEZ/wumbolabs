+++
title = "Qwen3.8-4B (Empero)"
description = "Qwen3.8-4B (Empero) — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 19

[extra]
kind = "model"
model_id = "qwen3.8-4b-empero"
vendor = "empero-ai (Qwen3.8 derivative)"
recommended_profile_id = "qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver"
recommended_profile_name = "llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane)"
profile_count = 2
event_count = 2
latest_event_date = 2026-09-01
+++

WumboLabs tests **Qwen3.8-4B (Empero)** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane) (`qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver`, specialized) — [canonical evidence](https://github.com/WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver)
- **Latest evidence:** 2026-09-01 — WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M

## Tested profiles

### LLMGauge vendor-alignment battery (bf16/q4) — CURRENT

Profile identity: `qwen3.8-4b-empero-vendor-battery`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-qwen3.8-4b-empero>

Events on this profile:

- [LLMGauge vendor-alignment battery (4B bf16/q4) (2026-08-18)](/evaluations/qwen3-8-4b-empero#qwen38-empero-4b-vendor-battery-2026-08-18) — SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

### llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane) — SPECIALIZED

Profile identity: `qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

Canonical profile repository: <https://github.com/WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver>

Events on this profile:

- [WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M (2026-09-01)](/evaluations/qwen3-8-4b-empero#qwen38-empero-4b-distill-wumboserver-2026-09-01) — BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen38-empero-4b-distill-wumboserver-2026-09-01"></a>

### 2026-09-01 — WumboServer RTX 2060S LocalMaxxing 4B Q4_K_M

**Benchmark Only — WumboServer hardware lane** · profile: llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result)

[Canonical evidence for this event](https://github.com/WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver)

### Identity and scope

- Profile: `qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver` — llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboServer (RTX 2060 SUPER 8GB)

empero-ai/Qwen3.8-4B-Distill-GGUF Q4_K_M on WumboServer RTX 2060S: 97.14 tok/s out, 2145.66 tok/s prefill, 3.0 GB peak VRAM, 172 W. Hardware-lane benchmark; not a WumboJetsII WELP result.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen38-empero-4b-vendor-battery-2026-08-18"></a>

### 2026-08-18 — LLMGauge vendor-alignment battery (4B bf16/q4)

**Specialized Test — vendor alignment** · profile: LLMGauge vendor-alignment battery (bf16/q4) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

[Canonical evidence for this event](https://github.com/WumboLabs/eval-qwen3.8-4b-empero)

### Identity and scope

- Profile: `qwen3.8-4b-empero-vendor-battery` — LLMGauge vendor-alignment battery (bf16/q4)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge vendor-alignment qualification battery on empero-ai Qwen3.8-4B (BF16 + Q4).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

One canonical evidence repository per tested profile; each event above links its exact evidence. LocalMaxxing dispositions are recorded per event. Where a repository shows an original publication location, the evidence was migrated byte-identically to the canonical profile repository and the original remains a preserved archive.

- **LLMGauge vendor-alignment battery (bf16/q4)** (`qwen3.8-4b-empero-vendor-battery`): <https://github.com/WumboLabs/eval-qwen3.8-4b-empero>
- **llama.cpp Q4_K_M Distill (WumboServer RTX 2060S lane)** (`qwen3.8-4b-empero-distill-llamacpp-q4km-wumboserver`): <https://github.com/WumboLabs/eval-qwen3.8-4b-empero-distill-wumboserver>
