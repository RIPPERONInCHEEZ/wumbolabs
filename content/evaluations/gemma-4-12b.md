+++
title = "Gemma 4 12B IT"
description = "Gemma 4 12B IT: tested profiles, validated context, and chronological evaluation history. Findings are attributed to the profile and event that measured them."
template = "lab_model.html"
weight = 3

[extra]
kind = "model"
model_id = "gemma-4-12b"
vendor = "Google"
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "gemma-4-12b-llamacpp-qat-q4-0"
recommended_profile_name = "llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)"
practical_context = "32,768 default / 131,072 guarded tokens"
profile_count = 5
event_count = 7
latest_evidence_date = 2026-11-09
+++

This page collects WumboLabs evidence for **Gemma 4 12B IT**: current findings, tested profiles, and chronological evaluation history. Each value belongs to its measured deployment; later findings do not silently replace historical evidence.

## Current state

- **Classification:** READY_WITH_GUARDRAILS ; source: [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12), profile llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- **Recommended profile:** llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) (`gemma-4-12b-llamacpp-qat-q4-0`, current); [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
- **Practical context:** 32,768 default / 131,072 guarded tokens; native model-card maximum 262,144 (envelope complete: YES); source: [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12)
- **Latest evidence:** 2026-11-09: Gemma 4 12B IT fresh Model/Core baseline + advanced reasoning (RTX 5070 CUDA)

## Tested profiles

### llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) (CURRENT)

Profile identity: `gemma-4-12b-llamacpp-qat-q4-0`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b9672 (74ade5274), CUDA SM120 |
| Artifact | unsloth/gemma-4-12b-it-GGUF gemma-4-12b-it-UD-Q4_K_XL.gguf (re-acquired 2026-09-13T01:29:47Z after archive-gap repair authorization) |
| Precision | UD-Q4_K_XL (Unsloth Dynamic 2.0 over QAT Q4_0 lineage) |

Status: current canonical/recommended tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)

Events on this profile:

- [Current-WELP recharacterization (2026-09-12)](/evaluations/gemma-4-12b#gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12); status: READY_WITH_GUARDRAILS
- [12B practical pool comparison v025 + Grug (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-practical-pool-v025-2026-07-04); status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)
- [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-practical-use-family-2026-06-21); status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)
- [Honesty ladder smoke (QAT Q4) (2026-06-21)](/evaluations/gemma-4-12b#gemma4-12b-honesty-ladder-2026-06-21); status: SPECIALIZED_TEST / UNSCORED_SMOKE
- [Early core-v1 + agent-backend-v1 scored runs (QAT Q4) (2026-06-16)](/evaluations/gemma-4-12b#gemma4-12b-core-agent-v016-2026-06-16); status: BENCHMARK_ONLY

### UD-Q4_K_XL (Unsloth Dynamic 2.0 GGUF): Unsloth UD-Q4_K_XL GGUF, llama.cpp CUDA on RTX 5070, thinking not configurable, fresh NVMe (SSD) canonical deployment (CURRENT)

Profile identity: `gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09`.

| Field | Value |
|---|---|
| Runtime | llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Artifact | gemma-4-12b |
| Precision | UNKNOWN |

Status: current tested surface; not the recommended profile.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/gemma-4-12b/events/gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09/profile.json)

Events on this profile:

- [Gemma 4 12B IT fresh Model/Core baseline + advanced reasoning (RTX 5070 CUDA) (2026-11-09)](/evaluations/gemma-4-12b#gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09); status: NOT_ASSIGNED

### llama.cpp Q4_K_M (ggml-org) (SPECIALIZED)

Profile identity: `gemma-4-12b-llamacpp-q4km`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-q4km/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) (SPECIALIZED)

Profile identity: `gemma-4-12b-llamacpp-ud-q5-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)

### llama.cpp Q4_K_M (ggml-org) (SPECIALIZED)

Profile identity: `gemma-4-12b-llamacpp-ud-q6-k-xl`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

Events on this profile:

- [LMX speed runs across four Gemma 4 12B quants (2026-07-04)](/evaluations/gemma-4-12b#gemma4-12b-lmx-speed-2026-07-04); status: BENCHMARK_ONLY (LMX local speed)

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09"></a>

### 2026-11-09: Gemma 4 12B IT fresh Model/Core baseline + advanced reasoning (RTX 5070 CUDA)

**WELP v1.0 fresh second-family baseline and reasoning arm** · profile: UD-Q4_K_XL (Unsloth Dynamic 2.0 GGUF): Unsloth UD-Q4_K_XL GGUF, llama.cpp CUDA on RTX 5070, thinking not configurable, fresh NVMe (SSD) canonical deployment · maturity: CURRENT_WELP · status: NOT_ASSIGNED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/gemma-4-12b/events/gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

##### Identity

| Field | Value |
|---|---|
| Model | gemma-4-12b |
| Producer | not recorded |
| Tested artifact | gemma-4-12b |
| Precision | UNKNOWN |
| Artifact SHA-256 | `90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e` |
| Campaign | `gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09` |
| Record date | 2026-11-11 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc |
| Hardware | UNKNOWN |

##### WELP outcome

- **Outcome:** Finalized independent section findings
- **Classification:** NOT_ASSIGNED
- **Methodology snapshot:** model-baseline/2

Publication state: **published**; canonical evidence: https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/gemma-4-12b/events/gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 16384 tokens |
| Guarded context | not recorded |
| Native model-card maximum | not recorded |
| Model-card envelope complete | NO |
| Native maximum disposition | NOT_CLAIMED |

##### Quality and capabilities

- **Constrained result:** See configuration-specific section findings; no composite model score.
- advanced-reasoning: 3 recorded identities
- baseline: 61 recorded identity

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
      "artifact_sha256": "90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09",
      "reasoning": {
        "arm": "NOT_CONFIGURABLE",
        "controls": {}
      },
      "runtime": {
        "backend": "CUDA",
        "engine": "llama.cpp",
        "version": "b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 64,
        "top_p": 0.95
      },
      "template_sha256": "aa3185dfc65051046349995de1cfc2fbb275491b9a3832b71595f1ff5b31d61b"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "801c85c3fa4ea9069c55bdf00daf418b8b0e41717077793dc86a555a31ecb4af",
      "methodology": "reasoning-advanced/1",
      "profile_id": "gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09",
      "profile_revision": "7daaea329557700cd01dc92792976360f91c175b9ba22893dd4f9466fb1c7567",
      "report_sha256": "fef41101f71507a58ef295a596714785f3b3f6941179b0bf7ca2859460b46cee",
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
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
    },
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
            "fail": 2,
            "indeterminate": 0,
            "measured": 8,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 5,
            "planned": 8,
            "scored": 7,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "context-family-a-v2-3072-seed-42"
            ]
          },
          "instruction_following": {
            "applicable": 15,
            "budget_limited": 0,
            "excluded": {},
            "fail": 2,
            "indeterminate": 0,
            "measured": 15,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 13,
            "planned": 15,
            "scored": 15,
            "status": "COMPLETE",
            "unscored": []
          },
          "performance": {
            "applicable": 2,
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 0,
            "measurement_gaps": {
              "perf-short": [
                "memory_consumption"
              ],
              "perf-substantial": [
                "memory_consumption"
              ]
            },
            "minimum_measurement_coverage_met": false,
            "minimum_scoring_coverage_met": null,
            "missing": [
              "perf-short",
              "perf-substantial"
            ],
            "pass": 0,
            "planned": 2,
            "scored": 0,
            "status": "PARTIALLY_COMPLETE",
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
            "budget_limited": 0,
            "excluded": {},
            "fail": 3,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 17,
            "planned": 20,
            "scored": 20,
            "status": "COMPLETE",
            "unscored": []
          },
          "structured_output": {
            "applicable": 2,
            "budget_limited": 0,
            "excluded": {},
            "fail": 1,
            "indeterminate": 0,
            "measured": 2,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 1,
            "planned": 2,
            "scored": 2,
            "status": "COMPLETE",
            "unscored": []
          },
          "tool_use": {
            "applicable": 3,
            "budget_limited": 0,
            "excluded": {},
            "fail": 2,
            "indeterminate": 0,
            "measured": 3,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 1,
            "planned": 3,
            "scored": 3,
            "status": "COMPLETE",
            "unscored": []
          }
        },
        "classification": null,
        "rule": "Every fixed applicable task identity; one result per identity, no duplicated credit",
        "status": "PARTIALLY_COMPLETE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "2386196149a088cca723c9e5c04c7d5bfbbd6541e8d109f33352fefc6b99a164",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": "UNKNOWN"
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 2.850185274000978,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 35
            },
            "first_byte_seconds": 1.2426216849999037,
            "latency_seconds": 2.850185274000978,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1607.021,
              "predicted_n": 106,
              "predicted_per_second": 65.33828742748229,
              "predicted_per_token_ms": 15.304961904761905,
              "prompt_ms": 1237.989,
              "prompt_n": 35,
              "prompt_per_second": 28.27165669484947,
              "prompt_per_token_ms": 35.371114285714285
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 65.33828742748229,
              "prompt": 28.27165669484947
            },
            "ttft_seconds": 1.2962998779985355,
            "usage": {
              "completion_tokens": 106,
              "prompt_tokens": 35,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 141
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 2.7234282290010015,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 35
            },
            "first_byte_seconds": 1.1188276479952037,
            "latency_seconds": 2.7234282290010015,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1603.577,
              "predicted_n": 106,
              "predicted_per_second": 65.47861437274294,
              "predicted_per_token_ms": 15.272161904761905,
              "prompt_ms": 1115.058,
              "prompt_n": 35,
              "prompt_per_second": 31.388501764033798,
              "prompt_per_token_ms": 31.8588
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 65.47861437274294,
              "prompt": 31.388501764033798
            },
            "ttft_seconds": 1.1683740000007674,
            "usage": {
              "completion_tokens": 106,
              "prompt_tokens": 35,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 141
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 2.7329273679933976,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 35
            },
            "first_byte_seconds": 1.1271861589921173,
            "latency_seconds": 2.7329273679933976,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1604.564,
              "predicted_n": 106,
              "predicted_per_second": 65.43833714329874,
              "predicted_per_token_ms": 15.281561904761906,
              "prompt_ms": 1122.664,
              "prompt_n": 35,
              "prompt_per_second": 31.175846023387226,
              "prompt_per_token_ms": 32.07611428571428
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 65.43833714329874,
              "prompt": 31.175846023387226
            },
            "ttft_seconds": 1.1784431889973348,
            "usage": {
              "completion_tokens": 106,
              "prompt_tokens": 35,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 141
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 6.49369424401084,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3635
            },
            "first_byte_seconds": 4.162014397006715,
            "latency_seconds": 6.49369424401084,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2330.02,
              "predicted_n": 136,
              "predicted_per_second": 57.93941682904009,
              "predicted_per_token_ms": 17.25940740740741,
              "prompt_ms": 4128.43,
              "prompt_n": 3635,
              "prompt_per_second": 880.4799887608607,
              "prompt_per_token_ms": 1.1357441540577717
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 57.93941682904009,
              "prompt": 880.4799887608607
            },
            "ttft_seconds": 4.220767614999204,
            "usage": {
              "completion_tokens": 136,
              "prompt_tokens": 3635,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3771
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 6.508392004005145,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3635
            },
            "first_byte_seconds": 4.179393672005972,
            "latency_seconds": 6.508392004005145,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2327.693,
              "predicted_n": 136,
              "predicted_per_second": 57.99733899616486,
              "predicted_per_token_ms": 17.24217037037037,
              "prompt_ms": 4141.863,
              "prompt_n": 3635,
              "prompt_per_second": 877.6243926947849,
              "prompt_per_token_ms": 1.139439614855571
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 57.99733899616486,
              "prompt": 877.6243926947849
            },
            "ttft_seconds": 4.235855052000261,
            "usage": {
              "completion_tokens": 136,
              "prompt_tokens": 3635,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3771
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 6.472986538996338,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3635
            },
            "first_byte_seconds": 4.146988735999912,
            "latency_seconds": 6.472986538996338,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2323.957,
              "predicted_n": 136,
              "predicted_per_second": 58.09057568621107,
              "predicted_per_token_ms": 17.214496296296296,
              "prompt_ms": 4130.314,
              "prompt_n": 3635,
              "prompt_per_second": 880.0783669231927,
              "prompt_per_token_ms": 1.136262448418157
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 58.09057568621107,
              "prompt": 880.0783669231927
            },
            "ttft_seconds": 4.203767286991933,
            "usage": {
              "completion_tokens": 136,
              "prompt_tokens": 3635,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3771
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09",
      "profile_revision": "7daaea329557700cd01dc92792976360f91c175b9ba22893dd4f9466fb1c7567",
      "report_sha256": "0cfe7ffdd935668bed1209a9b6ca1a43805e5c205e4de1f6852d4217bbdaac41",
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
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "completion": "INCOMPLETE",
          "execution": "VALID",
          "limits": "BUDGET",
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "scoring": "NOT_SCOREABLE",
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
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "context-multidocument-v2-6144-seed-42"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
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
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
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
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
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
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
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
          "outcome": "PASS",
          "reason": null,
          "scoring": "SCORED_PASS",
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
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "tool-recovery-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
          "unit_id": "tool-selection-01"
        },
        {
          "completion": "COMPLETE",
          "execution": "VALID",
          "limits": "NONE",
          "outcome": "FAIL",
          "reason": null,
          "scoring": "SCORED_FAIL",
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
| Canonical context | not recorded |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>No submission or service-state claim is made by this export.</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/a8e5cc762eb9b0c52c9de870264d943841c2c8be/models/gemma-4-12b/events/gemma-4-12b-rtx5070-cuda-m2-fresh-ssd-2026-11-09/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12"></a>

### 2026-09-12: Current-WELP recharacterization

**WELP Recharacterization: llama.cpp QAT UD-Q4_K_XL** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

##### Identity

| Field | Value |
|---|---|
| Model | Gemma 4 12B IT |
| Producer | Google |
| Official model | google/gemma-4-12b-it-qat-q4_0-gguf @ `unsloth/gemma-4-12b-it-GGUF fc034cfff751157913579611efad8462ac1be606` |
| Tested artifact | unsloth/gemma-4-12b-it-GGUF gemma-4-12b-it-UD-Q4_K_XL.gguf (re-acquired 2026-09-13T01:29:47Z after archive-gap repair authorization) |
| Precision | UD-Q4_K_XL (Unsloth Dynamic 2.0 over QAT Q4_0 lineage) |
| Artifact SHA-256 | `90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e` |
| Campaign | `gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12` |
| Record date | 2026-09-12 |

##### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp |
| Runtime version | b9672 (74ade5274), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | full GPU residency; one heavy CUDA workload at a time |

##### WELP outcome

- **Outcome:** PASS: RECHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published**; canonical evidence: https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md

##### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 131072 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT: measured: one bounded admission attempt failed with CUDA OOM (compute buffer) and KV-slope accounting (17.4 KiB/token) proves the point cannot fit with required reserve on 12GB; nearest measured boundary 131,072 |

##### Quality and capabilities

- **Constrained result:** 12/12 frozen mechanical quality screen (frozen scorer, temp 0)
- reasoning (thinking ON) multi-hop syllogism PASS
- coding: generated function executes correctly (mechanical exec check)
- tool calling: valid call + grounded continuation PASS

###### Guardrails and limitations

- verbosity: 13-14/20 reliability outputs hit frozen token caps; raise max_tokens or disable thinking for terse duty
- git-safety advisory weakness (amending pushed commits framed as technically possible)
- uncertainty/sycophancy categories 1-2/3
- native 262,144 context is FIT_LIMIT on 12GB; guarded ceiling 131,072
- Multimodal lane (image/audio/video via mmproj) is SUPPORTED_NOT_CHARACTERIZED: this event characterizes the canonical text profile only; no model-wide multimodal claim is made

**Reliability:** Proven mechanical 20-task corpus, 2 seeds: 11/20 and 10/20 mechanical pass; evidence discipline (3/3, 2/3) and strict interfaces (3/3, 2/3) strong; hallucination 2/4 both seeds; failures concentrated in uncertainty/sycophancy/git-safety with a strong truncation component

##### LocalMaxxing

| Field | Value |
|---|---|
| Status | MEASURED_NOT_SUBMITTED |
| Canonical context | not recorded |
| tok/s out | not recorded |
| TTFT | not recorded |
| Submission reference | not recorded |
| verifiedRun | null (not claimed) |

<p><small>local canonical-profile benchmark pp512 3201 tok/s / tg128 72.92 tok/s (5 reps); no exact existing service record (historical 2026-07-04 gemma4 LMX record is an unexecuted dry-run); submission requires separate human gate</small></p>

##### Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md>

This event section is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.

<a id="gemma4-12b-practical-pool-v025-2026-07-04"></a>

### 2026-07-04: 12B practical pool comparison v025 + Grug

**Practical Use: shared comparison (canonical)** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0`: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Second shared multi-model practical-use comparison: the incumbent QAT Q4 practical default (259.2/300 from the v024 suite) against five additional tested models on wumbolabs-practical-use-v1 at 8k: Grug-12B 243.6, Mellum2 Instruct 239.9, Mellum2 Thinking 232.8, Qwen3.6-35B-A3B 233.9, Qwen3-14B 228.4 (all /300 manual practical scores). One immutable shared report; each related model page lists this event with its own score.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Shared comparison: `practical-use-comparison-2026-07-04`: one immutable shared report; related model pages list
this event with their own measured entries.

<a id="gemma4-12b-lmx-speed-2026-07-04"></a>

### 2026-07-04: LMX speed runs across four Gemma 4 12B quants

**Benchmark Only: LMX local speed** · profile: llama.cpp Q4_K_M (ggml-org) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY (LMX local speed) · related profiles: `gemma-4-12b-llamacpp-qat-q4-0`, `gemma-4-12b-llamacpp-ud-q5-k-xl`, `gemma-4-12b-llamacpp-ud-q6-k-xl`

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)
[Profile Metadata: gemma-4-12b-llamacpp-qat-q4-0](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)
[Profile Metadata: gemma-4-12b-llamacpp-ud-q5-k-xl](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)
[Profile Metadata: gemma-4-12b-llamacpp-ud-q6-k-xl](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-q4km`: llama.cpp Q4_K_M (ggml-org)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: Q4_K_M 72.11, UD-Q5_K_XL 62.76, UD-Q6_K_XL 51.26 tok/s out (llama.cpp). Archaeology additionally cites Q8_0 test and NVFP4 conversion-attempt records (weights since removed).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="gemma4-12b-practical-use-family-2026-06-21"></a>

### 2026-06-21: 12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)

**Practical Use: LLMGauge wumbolabs-practical-use-v1** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: PRACTICAL_USE · status: PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical)

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/shared-events/practical-use-comparison-2026-06-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

[Long-form report: 12B Gemma-Based Practical Use Test](/records/gemma-12b-practical-use/)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0`: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite; that model carries its own Evaluation page.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Shared comparison: `practical-use-comparison-2026-06-21`: one immutable shared report; related model pages list
this event with their own measured entries.

<a id="gemma4-12b-honesty-ladder-2026-06-21"></a>

### 2026-06-21: Honesty ladder smoke (QAT Q4)

**Specialized Test: honesty ladder** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: SPECIALIZED_TEST · status: SPECIALIZED_TEST / UNSCORED_SMOKE

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-honesty-ladder-2026-06-21/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0`: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, reliability
- Hardware: WumboJetsII (RTX 5070 12GB)

Honesty-ladder smoke runs against the QAT Q4 practical profile.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

<a id="gemma4-12b-core-agent-v016-2026-06-16"></a>

### 2026-06-16: Early core-v1 + agent-backend-v1 scored runs (QAT Q4)

**Benchmark Only: LLMGauge v0.16 era** · profile: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging) · maturity: BENCHMARK_ONLY · status: BENCHMARK_ONLY

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/gemma-4-12b/events/gemma4-12b-core-agent-v016-2026-06-16/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b)

### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0`: llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, capabilities
- Hardware: WumboJetsII (RTX 5070 12GB)

QAT Q4 completed core-v1 (8/8, manual score 308/400) and agent-backend-v1 (2048 ctx) during LLMGauge v0.16 validation.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **gemma-4-12b-llamacpp-qat-q4-0**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-qat-q4-0/profile.json)
- **gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-rtx5070-cuda-ssd-not-configurable-2026-11-09/profile.json)
- **gemma-4-12b-llamacpp-q4km**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-q4km/profile.json)
- **gemma-4-12b-llamacpp-ud-q5-k-xl**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/profile.json)
- **gemma-4-12b-llamacpp-ud-q6-k-xl**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/gemma-4-12b/profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/profile.json)

### Legacy provenance

- [WumboLabs/eval-gemma-4-12b-q4km @ `561be30e6f39eefb19fa36844904fb110c6a66a8`](https://github.com/WumboLabs/eval-gemma-4-12b-q4km/blob/561be30e6f39eefb19fa36844904fb110c6a66a8/events/gemma4-12b-lmx-speed-2026-07-04.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/events/gemma4-12b-core-agent-v016-2026-06-16.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/events/gemma4-12b-honesty-ladder-2026-06.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/reports/gemma4-12b-welp-recharacterization-2026-09-12.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/shared/compare-gemma4-family-wumbolabs-practical-v024-scored.md)
- [WumboLabs/eval-gemma-4-12b-qat-q4 @ `13051c0eb36cd7dc1c1e407b31db451e6c5c806e`](https://github.com/WumboLabs/eval-gemma-4-12b-qat-q4/blob/13051c0eb36cd7dc1c1e407b31db451e6c5c806e/shared/compare-wumbolabs-practical-v025-plus-grug.md)
