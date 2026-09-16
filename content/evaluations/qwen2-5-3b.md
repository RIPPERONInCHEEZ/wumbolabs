+++
title = "Qwen2.5-3B Instruct"
description = "Qwen2.5-3B Instruct — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 17

[extra]
kind = "model"
model_id = "qwen2.5-3b"
vendor = "Alibaba (Qwen team)"
recommended_profile_id = "qwen2.5-3b-vllm-bf16"
recommended_profile_name = "vLLM BF16 (cross-runtime lane)"
profile_count = 2
event_count = 2
latest_event_date = 2026-07-15
+++

WumboLabs tests **Qwen2.5-3B Instruct** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** vLLM BF16 (cross-runtime lane) (`qwen2.5-3b-vllm-bf16`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-vllm-fingerprint-smoke-2026-07-15/REPORT.md)
- **Latest evidence:** 2026-07-15 — vLLM fingerprint live smoke

## Tested profiles

### llama.cpp F16 (comparison reference) — CURRENT

Profile identity: `qwen2.5-3b-llamacpp-f16`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-cross-runtime-2026-07-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b/profiles/qwen2.5-3b-llamacpp-f16/profile.json)

Events on this profile:

- [Cross-runtime comparison: llama.cpp F16 vs vLLM BF16 (2026-07-15)](/evaluations/qwen2-5-3b#qwen25-3b-cross-runtime-2026-07-15) — BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE

### vLLM BF16 (cross-runtime lane) — CURRENT

Profile identity: `qwen2.5-3b-vllm-bf16`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-vllm-fingerprint-smoke-2026-07-15/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b/profiles/qwen2.5-3b-vllm-bf16/profile.json)

Events on this profile:

- [vLLM fingerprint live smoke (2026-07-15)](/evaluations/qwen2-5-3b#qwen25-3b-vllm-fingerprint-smoke-2026-07-15) — SPECIALIZED_TEST / RUNTIME_FINGERPRINT

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen25-3b-vllm-fingerprint-smoke-2026-07-15"></a>

### 2026-07-15 — vLLM fingerprint live smoke

**Specialized Test — runtime fingerprint** · profile: vLLM BF16 (cross-runtime lane) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / RUNTIME_FINGERPRINT

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-vllm-fingerprint-smoke-2026-07-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b)

### Identity and scope

- Profile: `qwen2.5-3b-vllm-bf16` — vLLM BF16 (cross-runtime lane)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

vLLM runtime-fingerprint smoke using Qwen2.5-3B as payload.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="qwen25-3b-cross-runtime-2026-07-15"></a>

### 2026-07-15 — Cross-runtime comparison: llama.cpp F16 vs vLLM BF16

**Benchmark Only — cross-runtime methodology lane** · profile: llama.cpp F16 (comparison reference) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY / CROSS_RUNTIME_METHODOLOGY_LANE

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen2.5-3b/events/qwen25-3b-cross-runtime-2026-07-15/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b)

### Identity and scope

- Profile: `qwen2.5-3b-llamacpp-f16` — llama.cpp F16 (comparison reference)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge cross-runtime methodology study with model-specific results: Qwen2.5-3B Instruct as F16 llama.cpp vs BF16 vLLM agent-backend comparison incl. failed-command-recovery probes. Primary subject is cross-runtime methodology; the Qwen2.5-3B results are retained as its benchmark-only evidence. Archaeology separately cites a full Qwen2.5-3B quant-lab record set (F16/Q8_0/Q6_K/Q5_K_M/Q4_K_M/IQ4_XS) from the Arch era.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen2.5-3b-llamacpp-f16**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b/profiles/qwen2.5-3b-llamacpp-f16/profile.json)
- **qwen2.5-3b-vllm-bf16**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/901b6733c33939f7a69c4f09a5fa25b9e1080894/models/qwen2.5-3b/profiles/qwen2.5-3b-vllm-bf16/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen2.5-3b-llamacpp-f16 @ `651bbea8c5d1e9c1c5dfa21a538a6922f2bf60a8`](https://github.com/WumboLabs/eval-qwen2.5-3b-llamacpp-f16/blob/651bbea8c5d1e9c1c5dfa21a538a6922f2bf60a8/shared/compare-qwen25-3b-f16-vs-vllm-bf16-8k.md)
- [WumboLabs/eval-qwen2.5-3b-vllm-bf16 @ `92e975e31a46b1e84e21b838f7a79e5c91cd7e86`](https://github.com/WumboLabs/eval-qwen2.5-3b-vllm-bf16/blob/92e975e31a46b1e84e21b838f7a79e5c91cd7e86/events/qwen25-3b-vllm-fingerprint-smoke-2026-07.md)
