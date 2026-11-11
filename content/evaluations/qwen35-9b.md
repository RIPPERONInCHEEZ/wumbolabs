+++
title = "Qwen3.5-9B"
description = "Qwen3.5-9B — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 3

[extra]
kind = "model"
model_id = "qwen35-9b"
vendor = "Alibaba (Qwen team)"
recommended_profile_id = "qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08"
recommended_profile_name = "Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (runtime-performance measurement surface)"
practical_context = "16,384 default tokens"
profile_count = 6
event_count = 9
latest_evidence_date = 2026-11-08
+++

WumboLabs tests **Qwen3.5-9B** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (runtime-performance measurement surface) (`qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08`, current) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md)
- **Practical context:** 16,384 default tokens — [Qwen3.5-9B reference Model/Core baseline (Radeon R9700 HIP, thinking-on) (2026-10-22)](/evaluations/qwen35-9b#qwen35-9b-r9700-hip-m2-geometry-2026-10-22)
- **Latest evidence:** 2026-11-08 — Qwen3.5-9B runtime performance (RTX 5070 CUDA, deployment-attributed)

## Tested profiles

### llama.cpp Q8_0 GGUF — CURRENT

Profile identity: `qwen35-9b-llamacpp-q8`.

| Field | Value |
|---|---|
| Runtime | llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Artifact | Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) |
| Precision | Q8_0 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-llamacpp-q8/profile.json)

Events on this profile:

- [Context envelope completion (2026-09-11)](/evaluations/qwen35-9b#context-envelope-completion-2026-09-11-qwen35-9b) — READY_WITH_GUARDRAILS

### Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp HIP on AMD Radeon AI PRO R9700, thinking-on, qualified wide16k-C0 sampler — CURRENT

Profile identity: `qwen35-9b-r9700-hip-on-2026-10-22`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11311-f7b384c1e |
| Artifact | qwen35-9b |
| Precision | UNKNOWN |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-r9700-hip-on-2026-10-22/profile.json)

Events on this profile:

- [Qwen3.5-9B reference Model/Core baseline (Radeon R9700 HIP, thinking-on) (2026-10-22)](/evaluations/qwen35-9b#qwen35-9b-r9700-hip-m2-geometry-2026-10-22) — NOT_ASSIGNED

### Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (specialist and scored-M3 surface) — CURRENT

Profile identity: `qwen35-9b-rtx5070-cuda-on-2026-11-06`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Artifact | qwen35-9b |
| Precision | UNKNOWN |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-on-2026-11-06/profile.json)

Events on this profile:

- [Qwen3.5-9B scored Agentic M3 — research and repository (genuine negatives) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06) — NOT_ASSIGNED
- [Qwen3.5-9B scored Agentic M3 — readiness and system (RTX 5070 CUDA, thinking-on) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06) — NOT_ASSIGNED
- [Qwen3.5-9B advanced reasoning specialist (RTX 5070 CUDA, thinking-on) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06) — NOT_ASSIGNED
- [Qwen3.5-9B advanced coding specialist (RTX 5070 CUDA, thinking-on) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06) — NOT_ASSIGNED

### Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (advanced long-context surface) — CURRENT

Profile identity: `qwen35-9b-rtx5070-cuda-lc-on-2026-11-06`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Artifact | qwen35-9b |
| Precision | UNKNOWN |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-lc-on-2026-11-06/profile.json)

Events on this profile:

- [Qwen3.5-9B advanced long-context specialist (RTX 5070 CUDA, thinking-on) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06) — NOT_ASSIGNED

### Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (advanced tool-use surface) — CURRENT

Profile identity: `qwen35-9b-rtx5070-cuda-atu-on-2026-11-06`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Artifact | qwen35-9b |
| Precision | UNKNOWN |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-atu-on-2026-11-06/profile.json)

Events on this profile:

- [Qwen3.5-9B advanced tool-use specialist (RTX 5070 CUDA, thinking-on) (2026-11-06)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06) — NOT_ASSIGNED

### Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (runtime-performance measurement surface) — CURRENT

Profile identity: `qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Artifact | qwen35-9b |
| Precision | UNKNOWN |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08/profile.json)

Events on this profile:

- [Qwen3.5-9B runtime performance (RTX 5070 CUDA, deployment-attributed) (2026-11-08)](/evaluations/qwen35-9b#qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08) — NOT_ASSIGNED

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08"></a>

### 2026-11-08 — Qwen3.5-9B runtime performance (RTX 5070 CUDA, deployment-attributed)

**WELP v1.0 Runtime Performance** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (runtime-performance measurement surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- runtime-performance: 2 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "d893aadc53116ac1b7b9936a7c15844a669b627497f724275b1226c1e44088fc",
      "methodology": "runtime-performance/1",
      "performance_observations": [
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.05562183499932871,
            "latency_seconds": 2.4402552060000744,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2383.049,
              "predicted_n": 199,
              "predicted_per_second": 83.08683539448832,
              "predicted_per_token_ms": 12.03560101010101,
              "prompt_ms": 52.109,
              "prompt_n": 29,
              "prompt_per_second": 556.5257441133009,
              "prompt_per_token_ms": 1.7968620689655173
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 83.08683539448832,
              "prompt": 556.5257441133009
            },
            "ttft_seconds": 0.05565195199960726,
            "usage": {
              "completion_tokens": 199,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 228
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.626093459999538,
            "latency_seconds": 3.0202649679995375,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2393.348,
              "predicted_n": 199,
              "predicted_per_second": 82.7292980377279,
              "predicted_per_token_ms": 12.087616161616161,
              "prompt_ms": 620.617,
              "prompt_n": 29,
              "prompt_per_second": 46.727691958164215,
              "prompt_per_token_ms": 21.400586206896552
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 82.7292980377279,
              "prompt": 46.727691958164215
            },
            "ttft_seconds": 0.6261934189988096,
            "usage": {
              "completion_tokens": 199,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 228
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.06597885200062592,
            "latency_seconds": 2.4445133919998625,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2377.392,
              "predicted_n": 199,
              "predicted_per_second": 83.28454037028813,
              "predicted_per_token_ms": 12.007030303030302,
              "prompt_ms": 62.121,
              "prompt_n": 29,
              "prompt_per_second": 466.830862349286,
              "prompt_per_token_ms": 2.1421034482758623
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 83.28454037028813,
              "prompt": 466.830862349286
            },
            "ttft_seconds": 0.06602630199995474,
            "usage": {
              "completion_tokens": 199,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 228
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.0162203219988442,
            "latency_seconds": 6.099786888999006,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 5081.38,
              "predicted_n": 410,
              "predicted_per_second": 80.48994564468707,
              "predicted_per_token_ms": 12.423911980440097,
              "prompt_ms": 987.227,
              "prompt_n": 3629,
              "prompt_per_second": 3675.9529469919275,
              "prompt_per_token_ms": 0.27203830256268946
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 80.48994564468707,
              "prompt": 3675.9529469919275
            },
            "ttft_seconds": 1.0163013450001017,
            "usage": {
              "completion_tokens": 410,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4039
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.0938983819996793,
            "latency_seconds": 6.153889530000015,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 5057.299,
              "predicted_n": 410,
              "predicted_per_second": 80.87320919724145,
              "predicted_per_token_ms": 12.36503422982885,
              "prompt_ms": 1071.132,
              "prompt_n": 3629,
              "prompt_per_second": 3388.0044663029394,
              "prompt_per_token_ms": 0.29515899696886194
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 80.87320919724145,
              "prompt": 3388.0044663029394
            },
            "ttft_seconds": 1.0939784329984832,
            "usage": {
              "completion_tokens": 410,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4039
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.0120907189993886,
            "latency_seconds": 6.054113006999614,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 5039.707,
              "predicted_n": 410,
              "predicted_per_second": 81.15551162002076,
              "predicted_per_token_ms": 12.322022004889977,
              "prompt_ms": 989.118,
              "prompt_n": 3629,
              "prompt_per_second": 3668.9252445107663,
              "prompt_per_token_ms": 0.2725593827500689
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 81.15551162002076,
              "prompt": 3668.9252445107663
            },
            "ttft_seconds": 1.0121587479989103,
            "usage": {
              "completion_tokens": 410,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4039
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08",
      "profile_revision": "1e24ee89117388b223d5f8d5b68ac0863e7c04d0aac7fad51fc2a4ca719c64d9",
      "report_sha256": "4655e18d41b0b138219bbf1daad942c4d8f0fda0133c8e80916d8d0d0ebb4e21",
      "section": "runtime-performance",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "perf-short"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "perf-substantial"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B scored Agentic M3 — research and repository (genuine negatives)

**WELP v1.0 Full Agentic M3 (research + repository negatives)** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (specialist and scored-M3 surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- agentic: 2 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "f7571cba0620d0a6cc6431021b4b732c57f4fe98b59013b131fb31bb299aa1d9",
      "methodology": "agentic/3",
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "profile_revision": "7f8c1092fadcb26dac9c150d40edecc04f1ba82b42bc8d06f263ef7bfdbc7897",
      "report_sha256": "3e3b12c224b7846fac9eb8249801d153e289c664b1c98869d8a9e2243127756d",
      "section": "agentic",
      "units": [
        {
          "completion": null,
          "execution": null,
          "limits": {
            "command_seconds": 45,
            "evidence_kind": "REAL_MODEL",
            "max_tokens": 4096,
            "max_turns": 40,
            "source": "agentic-budget/1; operator acceptance 2026-10-25; campaign-gated authentic scored execution (agentic/3)",
            "total_tokens": 32768,
            "wall_seconds": 1200
          },
          "outcome": "FAIL",
          "reason": null,
          "scoring": null,
          "unit_id": "repository"
        },
        {
          "completion": null,
          "execution": null,
          "limits": {
            "command_seconds": 20,
            "evidence_kind": "REAL_MODEL",
            "max_tokens": 4096,
            "max_turns": 32,
            "source": "agentic-budget/1; operator acceptance 2026-10-25; campaign-gated authentic scored execution (agentic/3)",
            "total_tokens": 24576,
            "wall_seconds": 900
          },
          "outcome": "FAIL",
          "reason": null,
          "scoring": null,
          "unit_id": "research"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B scored Agentic M3 — readiness and system (RTX 5070 CUDA, thinking-on)

**WELP v1.0 Full Agentic M3 (readiness + system)** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (specialist and scored-M3 surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- agentic: 1 recorded identities
- agentic-readiness: 1 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "574a4fd9e86ec8ec5cd93ae51bfe243400420f605d65dd52970fc66ec4e0c055",
      "methodology": "agentic/3",
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "profile_revision": "935166a82c1a1606ed9e367565f4adc63649af6481393563f29af851ea7e880d",
      "report_sha256": "94eebf357db37682a8781c92ac59e9d09a718cecf734b3e282f521cb85c9b7ee",
      "section": "agentic",
      "units": [
        {
          "completion": null,
          "execution": null,
          "limits": {
            "command_seconds": 60,
            "evidence_kind": "REAL_MODEL",
            "max_tokens": 3072,
            "max_turns": 36,
            "source": "agentic-budget/1; operator acceptance 2026-10-25; campaign-gated authentic scored execution (agentic/3)",
            "total_tokens": 16384,
            "wall_seconds": 900
          },
          "outcome": "PASS",
          "reason": null,
          "scoring": null,
          "unit_id": "system"
        }
      ]
    },
    {
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "91f1598579efe772a58597e44996a040e86c70095308096e963d711446ef3317",
      "methodology": "agentic/3",
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "profile_revision": "935166a82c1a1606ed9e367565f4adc63649af6481393563f29af851ea7e880d",
      "report_sha256": "9c6db11af86a122c14dae18a524bbc3c99393302a5cf72aa34f0476ff178e376",
      "section": "agentic-readiness",
      "units": [
        {
          "completion": null,
          "execution": null,
          "limits": {
            "command_seconds": 15,
            "evidence_kind": "REAL_MODEL",
            "max_tokens": 3072,
            "max_turns": 16,
            "source": "agentic-budget/1; operator acceptance 2026-10-25; campaign-gated authentic scored execution (agentic/3)",
            "total_tokens": 8192,
            "wall_seconds": 300
          },
          "outcome": "PASS",
          "reason": null,
          "scoring": null,
          "unit_id": "qualification"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B advanced tool-use specialist (RTX 5070 CUDA, thinking-on)

**WELP v1.0 Advanced Tool Use specialist** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (advanced tool-use surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- advanced-tool-use: 3 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-atu-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "7b212ee51e3c98e7e8aae3fabc622ca1db1c756e2e02248174729e4003bd4b6a",
      "methodology": "tool-use-advanced/1",
      "profile_id": "qwen35-9b-rtx5070-cuda-atu-on-2026-11-06",
      "profile_revision": "acd282164dfe699dc969316867c0f4d2d852f527f61204b1df4adecdce38fd15",
      "report_sha256": "d4386662d9d3e4bd0d60e415aeb7c73db14cfbcdad9ee49fd7da08b575471293",
      "section": "advanced-tool-use",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-tool-permission-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-tool-recovery-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-tool-selection-01"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B advanced reasoning specialist (RTX 5070 CUDA, thinking-on)

**WELP v1.0 Advanced Reasoning specialist** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (specialist and scored-M3 surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- advanced-reasoning: 3 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "a6e50b0ff0b3a026807464d17ae7259235332662ba39b55ae2e93ec5d3f913c2",
      "methodology": "reasoning-advanced/1",
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "profile_revision": "c7400197a85779e2dbd1c01cbd8ebae86335f32e8983f9224f193a8d144efaa0",
      "report_sha256": "07ce50fffe9803f158c320eb8cd330c18cfbdc392f7bbd3551160a39b2180560",
      "section": "advanced-reasoning",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-constraints-01"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "advanced-evidence-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-revision-01"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B advanced long-context specialist (RTX 5070 CUDA, thinking-on)

**WELP v1.0 Advanced Long Context specialist** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (advanced long-context surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- advanced-long-context: 3 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-lc-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "EXPLORATORY"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "c61d59621c297d34141454dbef98b6ab386bcbff65dba7f5238b2b1672cfee3c",
      "methodology": "long-context-advanced/1",
      "profile_id": "qwen35-9b-rtx5070-cuda-lc-on-2026-11-06",
      "profile_revision": "f439c2a0518f4e973e7056a366908b55fdd3deda2729c0a6e07c31dee26832e0",
      "report_sha256": "d73554ca3d82fd48f636483432424d060777e939710cde0a2b206a74e941533f",
      "section": "advanced-long-context",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-lc-retention-01"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "advanced-lc-retrieval-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-lc-synthesis-01"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06"></a>

### 2026-11-06 — Qwen3.5-9B advanced coding specialist (RTX 5070 CUDA, thinking-on)

**WELP v1.0 Advanced Coding specialist** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp CUDA on RTX 5070, thinking-on (specialist and scored-M3 surface) · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | NVIDIA GeForce RTX 5070 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- coding: 3 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "4e8d55c3aeffac4be9c3c38a352d448bd6379148520434d8d7f987dce5e56715",
      "methodology": "coding-advanced/1",
      "profile_id": "qwen35-9b-rtx5070-cuda-on-2026-11-06",
      "profile_revision": "5c0091570a7d0af10b93e8a89522d09ccf7fb5a3f47d5f62bd782db6d465bb13",
      "report_sha256": "68a442c2fc1dbf17f7a51e495bd77b014adc2850308b2451fb28afc9e4be8aee",
      "section": "coding",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-module-01"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "advanced-repair-multi-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "advanced-repair-supplied-01"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="qwen35-9b-r9700-hip-m2-geometry-2026-10-22"></a>

### 2026-10-22 — Qwen3.5-9B reference Model/Core baseline (Radeon R9700 HIP, thinking-on)

**WELP v1.0 reference-family Model/Core baseline** · profile: Q4_K_M (Unsloth publisher GGUF) — Unsloth Q4_K_M GGUF, llama.cpp HIP on AMD Radeon AI PRO R9700, thinking-on, qualified wide16k-C0 sampler · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | qwen35-9b |
| Producer | not recorded |
| Tested artifact | qwen35-9b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8` |
| Campaign | `qwen35-9b-r9700-hip-m2-geometry-2026-10-22` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11311-f7b384c1e |
| Hardware | AMD Radeon AI PRO R9700 |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded tokens |
| Native model-card maximum | not recorded tokens |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- baseline: 61 recorded identities

###### Guardrails and limitations

- Model and Agentic findings are independent.
- Performance is deployment-attributed, never model-quality credit.
- Missing metrics remain unknown; boundary memory samples are not true peaks.

**Reliability:** not recorded

##### WELP section findings and provenance

Each section retains its own profile, methodology, outcomes and manifest.
Performance observations are not model-quality scores; null/UNKNOWN metrics remain unavailable.

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen35-9b-r9700-hip-on-2026-10-22",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true
          }
        }
      },
      "runtime": {
        "backend": "HIP",
        "engine": "llama.cpp",
        "version": "b11311-f7b384c1e"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 1.5,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "template_sha256": "7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67"
    }
  ],
  "sections": [
    {
      "coverage": {
        "advancement": "NOT_CALIBRATED",
        "categories": {
          "coding": {
            "applicable": 5,
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 5,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 5,
            "planned": 5,
            "scored": 5,
            "status": "COMPLETE",
            "unscored": []
          },
          "context": {
            "applicable": 8,
            "budget_limited": 1,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 8,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 7,
            "planned": 8,
            "scored": 7,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "context-multidocument-v2-8192-seed-42"
            ]
          },
          "instruction_following": {
            "applicable": 15,
            "budget_limited": 2,
            "excluded": {},
            "fail": 1,
            "indeterminate": 0,
            "measured": 15,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 12,
            "planned": 15,
            "scored": 13,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "Q06",
              "Q12"
            ]
          },
          "performance": {
            "applicable": 2,
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 2,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": null,
            "missing": [],
            "pass": 0,
            "planned": 2,
            "scored": 0,
            "status": "COMPLETE",
            "unscored": []
          },
          "reasoning": {
            "applicable": 6,
            "budget_limited": 1,
            "excluded": {},
            "fail": 1,
            "indeterminate": 0,
            "measured": 6,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 4,
            "planned": 6,
            "scored": 5,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "linux-diagnosis-stale-config-bind-failure"
            ]
          },
          "reliability": {
            "applicable": 20,
            "budget_limited": 2,
            "excluded": {},
            "fail": 4,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 14,
            "planned": 20,
            "scored": 18,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "hall-git-timewarp",
              "strict-limit-05"
            ]
          },
          "structured_output": {
            "applicable": 2,
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 2,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 2,
            "planned": 2,
            "scored": 2,
            "status": "COMPLETE",
            "unscored": []
          },
          "tool_use": {
            "applicable": 3,
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 3,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 3,
            "planned": 3,
            "scored": 3,
            "status": "COMPLETE",
            "unscored": []
          }
        },
        "classification": null,
        "rule": "Every fixed applicable task identity; one result per identity, no duplicated credit",
        "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "ea5d0cea59c0db19d721e6adaa29d62cdf646415ef366e50db3cd30e44bfa025",
      "memory": {
        "sampled_host_available_min_bytes": 23713300480,
        "sampled_vram_used_max_bytes": 6854832128
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 1.9732924530399032,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.07072449801489711,
            "latency_seconds": 1.9732924530399032,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1901.61,
              "predicted_n": 148,
              "predicted_per_second": 77.30291700190892,
              "predicted_per_token_ms": 12.93612244897959,
              "prompt_ms": 68.427,
              "prompt_n": 29,
              "prompt_per_second": 423.8093150364622,
              "prompt_per_token_ms": 2.359551724137931
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 77.30291700190892,
              "prompt": 423.8093150364622
            },
            "ttft_seconds": 0.07077100605238229,
            "usage": {
              "completion_tokens": 148,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 177
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.9550466599757783,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.05315050698118284,
            "latency_seconds": 1.9550466599757783,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1900.896,
              "predicted_n": 148,
              "predicted_per_second": 77.33195293167012,
              "predicted_per_token_ms": 12.931265306122448,
              "prompt_ms": 50.949,
              "prompt_n": 29,
              "prompt_per_second": 569.1966476280202,
              "prompt_per_token_ms": 1.7568620689655172
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 77.33195293167012,
              "prompt": 569.1966476280202
            },
            "ttft_seconds": 0.053180122980847955,
            "usage": {
              "completion_tokens": 148,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 177
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.947472234023735,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.04802749102236703,
            "latency_seconds": 1.947472234023735,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1898.385,
              "predicted_n": 148,
              "predicted_per_second": 77.43424015676482,
              "predicted_per_token_ms": 12.914183673469388,
              "prompt_ms": 45.483,
              "prompt_n": 29,
              "prompt_per_second": 637.6008618604753,
              "prompt_per_token_ms": 1.5683793103448276
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 77.43424015676482,
              "prompt": 637.6008618604753
            },
            "ttft_seconds": 0.04805608501192182,
            "usage": {
              "completion_tokens": 148,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 177
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 7.854244700982235,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.4779099050210789,
            "latency_seconds": 7.854244700982235,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 6373.905,
              "predicted_n": 459,
              "predicted_per_second": 71.85547949020264,
              "predicted_per_token_ms": 13.916823144104804,
              "prompt_ms": 1471.994,
              "prompt_n": 3629,
              "prompt_per_second": 2465.363309904796,
              "prompt_per_token_ms": 0.4056197299531551
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 71.85547949020264,
              "prompt": 2465.363309904796
            },
            "ttft_seconds": 1.4779762200196274,
            "usage": {
              "completion_tokens": 459,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4088
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 7.860864299000241,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.4785761859966442,
            "latency_seconds": 7.860864299000241,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 6379.674,
              "predicted_n": 459,
              "predicted_per_second": 71.7905021479154,
              "predicted_per_token_ms": 13.9294192139738,
              "prompt_ms": 1472.748,
              "prompt_n": 3629,
              "prompt_per_second": 2464.101122527411,
              "prompt_per_token_ms": 0.405827500688895
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 71.7905021479154,
              "prompt": 2464.101122527411
            },
            "ttft_seconds": 1.478673660021741,
            "usage": {
              "completion_tokens": 459,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4088
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 7.86009513301542,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 1.4787245360203087,
            "latency_seconds": 7.86009513301542,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 6378.921,
              "predicted_n": 459,
              "predicted_per_second": 71.79897666078637,
              "predicted_per_token_ms": 13.927775109170307,
              "prompt_ms": 1473.167,
              "prompt_n": 3629,
              "prompt_per_second": 2463.400279805345,
              "prompt_per_token_ms": 0.40594295949297327
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 71.79897666078637,
              "prompt": 2463.400279805345
            },
            "ttft_seconds": 1.4788187249796465,
            "usage": {
              "completion_tokens": 459,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 4088
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "qwen35-9b-r9700-hip-on-2026-10-22",
      "profile_revision": "0bcc82339abcd75e4b01058a506ab9d8a86f0b4581633a176cdcd4031b5e7658",
      "report_sha256": "ec9bfddaa65e4e8d4d5208797efd5e650c8de2a0d2946a9c4396bb1112987811",
      "section": "baseline",
      "units": [
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "Q02"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q03"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q04"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q05"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "Q06"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q07"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q08"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q09"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q10"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "Q11"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "Q12"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "coding-comprehension-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "coding-correction-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "coding-debug-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "coding-generation-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-3072-seed-314159"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-3072-seed-42"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-4096-seed-314159"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-4096-seed-42"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-8192-seed-314159"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-family-a-v2-8192-seed-42"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "context-multidocument-v2-6144-seed-42"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "context-multidocument-v2-8192-seed-42"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "document-synthesis-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "evidence-gpu"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "evidence-metric"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "evidence-xid"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "fact-journal-current-boot"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "fact-python-bool"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "fact-ssh-copy"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "git-amend"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "hall-fake-cuda"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "hall-fake-package"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "hall-fake-repo-state"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "hall-git-timewarp"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "instruction-conflict-01"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "linux-diagnosis-stale-config-bind-failure"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "linux-diagnosis-startup-invalid-config"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "multi-turn-correction-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "perf-short"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "perf-substantial"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "reasoning-consistency-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "reasoning-correctness-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "reasoning-evidence-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "repository-timeout-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "strict-exact-02"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "strict-extract-09"
        },
        {
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
          "unit_id": "strict-limit-05"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "structured-schema-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "structured-semantics-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "sycophancy-logic"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "sycophancy-systemd"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "sycophancy-unknown"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "tool-permission-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "tool-recovery-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "tool-selection-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "uncertainty-api"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "uncertainty-citation"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "uncertainty-file"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
          "unit_id": "untrusted-content-01"
        }
      ]
    }
  ]
}
```

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | BLOCKED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/qwen35-9b/events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="context-envelope-completion-2026-09-11-qwen35-9b"></a>

### 2026-09-11 — Context envelope completion

**Context Envelope — llama.cpp Q8_0** · profile: llama.cpp Q8_0 GGUF · maturity: CONTEXT_COMPLETION · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b)

##### Identity

| Field | Value |
|---|---|
| Model | Qwen3.5-9B |
| Producer | Alibaba (Qwen team); GGUF conversion by Unsloth |
| Official model | Qwen/Qwen3.5-9B @ `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| Tested artifact | Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) |
| Precision | Q8_0 weights; f16 KV (primary surface); q4_0 KV (one alternate admission surface) |
| Artifact SHA-256 | `809626574d0cb43d4becfa56169980da2bb448f2299270f7be443cb89d0a6ae4` |
| Campaign | `qwen35-9b-rtx5070-context-completion-2026-09-11` |
| Record date | 2026-09-09 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) |
| Runtime notes | All 33/33 runtime layers GPU-resident (untied input embedding lookup on CPU, disclosed); non-thinking text-only greedy surface; identical inherited baseline stack |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux |

##### WELP outcome

- **Outcome:** PASS — QWEN35_9B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** READY_WITH_GUARDRAILS (unchanged; new occupancy guardrail: at >=99.4% occupancy the model returns the absent-information value NOT_SPECIFIED under the literal key name 'zeta' instead of the required 'absent' key)
- **Artifact classification:** High-quality quantized medium-fit text control (unchanged)

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - native maximum 262,144 on the Q8_0/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision |

##### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.043883 s | — | 66.66 tok/s |
| Moderate (3642-token input) | 0.831738 s | 4378.79 tok/s | 64.84 tok/s |

<p><small>Near-full context fixture per-seed values; client/transport proxies with native timings retained in campaign evidence; short/moderate surfaces inherited unchanged from the baseline campaign (66.7 tok/s short decode, 0.83 s moderate TTFT)</small></p>

##### Quality and capabilities

- **Constrained result:** inherited: 7/7 constrained checks and 20/20 bounded reliability (baseline campaign, unchanged, not rerun)
- Perfect synthetic retrieval (20/20 values) at 99.49-99.56% occupancy through 64K on the primary surface
- Synthesis and checksum instructions retained at near-full occupancy (unlike the 4B same-family control)
- Highest measured/admitted near-full primary context 65,536 (guarded profile confirmed); 98,304 projected below the frozen operational safety floor and intentionally not launched; exact ceiling not bracketed
- q4_0-KV alternate surface functionally correct at 32K
- Official YaRN mechanism representable in the pinned runtime

###### Guardrails and limitations

- At >=99.4% near-full occupancy the absent-information value is returned under the wrong key name (deterministic at both rungs and both seeds); strict useful-context gate FAILED
- Inherited free-form cautions from the baseline: unsupported provenance/checksum attribution in open-ended answers; human verification required
- Not agent-qualified; no coding/tool/autonomous testing

**Reliability:** not recorded

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | not recorded tokens |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | cmtwcn79807eups01faxxmyr1 |
| verifiedRun | null (not claimed) |

<p><small>existing canonical submission audited for exact duplication; no new benchmark or submission performed</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/qwen35-9b/events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **qwen35-9b-llamacpp-q8**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-llamacpp-q8/profile.json)
- **qwen35-9b-r9700-hip-on-2026-10-22**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-r9700-hip-on-2026-10-22/profile.json)
- **qwen35-9b-rtx5070-cuda-on-2026-11-06**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-on-2026-11-06/profile.json)
- **qwen35-9b-rtx5070-cuda-lc-on-2026-11-06**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-lc-on-2026-11-06/profile.json)
- **qwen35-9b-rtx5070-cuda-atu-on-2026-11-06**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-atu-on-2026-11-06/profile.json)
- **qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/c22b97035929d7c798e21b2fbe4a2832319d48c4/models/qwen35-9b/profiles/qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08/profile.json)

### Legacy provenance

- [WumboLabs/eval-qwen3.5-9b @ `096afc64dbceb870e7672c7cdc95e44dea5ade49`](https://github.com/WumboLabs/eval-qwen3.5-9b/blob/096afc64dbceb870e7672c7cdc95e44dea5ade49/reports/qwen35-9b-context-envelope-completion-2026-09-11.md)
