+++
title = "Qwen3.8-2B (Empero)"
description = "Qwen3.8-2B (Empero) — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 18

[extra]
kind = "model"
model_id = "qwen3.8-2b-empero"
vendor = "empero-ai (Qwen3.8 derivative)"
recommended_profile_id = "qwen3.8-2b-empero-vllm-bf16"
recommended_profile_name = "vLLM BF16 vendor-alignment battery"
profile_count = 1
event_count = 1
latest_event_date = 2026-08-18
+++

WumboLabs tests **Qwen3.8-2B (Empero)** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** vLLM BF16 vendor-alignment battery (`qwen3.8-2b-empero-vllm-bf16`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-2b-empero/events/qwen38-empero-2b-vendor-battery-2026-08-18/REPORT.md)
- **Latest evidence:** 2026-08-18 — LLMGauge vendor-alignment battery (2B bf16)

## Tested profiles

### vLLM BF16 vendor-alignment battery — CURRENT

Profile identity: `qwen3.8-2b-empero-vllm-bf16`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-2b-empero/events/qwen38-empero-2b-vendor-battery-2026-08-18/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/qwen3.8-2b-empero/profiles/qwen3.8-2b-empero-vllm-bf16/profile.json)

Events on this profile:

- [LLMGauge vendor-alignment battery (2B bf16) (2026-08-18)](/evaluations/qwen3-8-2b-empero#qwen38-empero-2b-vendor-battery-2026-08-18) — SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen38-empero-2b-vendor-battery-2026-08-18"></a>

### 2026-08-18 — LLMGauge vendor-alignment battery (2B bf16)

**Specialized Test — vendor alignment** · profile: vLLM BF16 vendor-alignment battery · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen3.8-2b-empero/events/qwen38-empero-2b-vendor-battery-2026-08-18/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/aa707beabd64a875e74703ff13f638067799422d/models/qwen3.8-2b-empero)

### Identity and scope

- Profile: `qwen3.8-2b-empero-vllm-bf16` — vLLM BF16 vendor-alignment battery
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, performance, context
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge vendor-alignment qualification battery on empero-ai Qwen3.8-2B (BF16/GGUF): full suites at vendor 8192 plus configured-context default probing up to 262144. Primary subject is LLMGauge vendor alignment; model results retained.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen3.8-2b-empero-vllm-bf16**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/aa707beabd64a875e74703ff13f638067799422d/models/qwen3.8-2b-empero/profiles/qwen3.8-2b-empero-vllm-bf16/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.8-2b-empero @ `e09ed632fe835dac69eb05f9e37f7b57485923fd`](https://github.com/WumboLabs/eval-qwen3.8-2b-empero/blob/e09ed632fe835dac69eb05f9e37f7b57485923fd/events/qwen38-empero-2b-vendor-battery-2026-08-18.md)
