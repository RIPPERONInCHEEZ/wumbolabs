+++
title = "Gemma 4 31B IT"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 2

[extra]
kind = "model"
model_id = "gemma-4-31b-it"
vendor = "Google"
findings_first = true
catalog_artifact = "GGUF · Q5_K_M"
catalog_profile_id = "gemma-4-31b-it-r9700-vulkan-off-2026-11-27"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-11-27
+++

## Overview

Google · 1 tested configuration · 1 evidence event · newest evidence 2026-11-27.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Latest evidence:** 2026-11-27: [event result](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27)
- **2026-11-27** · Q5_K_M · llama.cpp b12556 · AI PRO R9700: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; baseline 61 units: 49 PASS, 12 FAIL; coverage failures retained: context 6 pass / 2 fail; instruction following 14 pass / 1 fail; reasoning 4 pass / 2 fail; reliability 17 pass / 3 fail; structured output 0 pass / 2 fail; tool use 1 pass / 2 fail; coding 3 units: 3 PASS (ADVANCE). [Event result](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="gemma-4-31b-it-r9700-vulkan-off-2026-11-27"></a>

### 2026-11-27: Gemma 4 31B IT: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED baseline and corrective Advanced Coding; model-specific Vulkan FlashAttention-on deployment** · config Q5_K_M · llama.cpp b12556 · AI PRO R9700 · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q5_K_M: llama.cpp / AMD Radeon AI PRO R9700 Vulkan, reasoning OFF (thinking disabled), FlashAttention on (model-specific).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/gemma-4-31b-it/events/gemma-4-31b-it-r9700-vulkan-off-2026-11-27/REPORT.md)

#### Gemma 4 31B IT: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED scope: the Model/Core baseline (`model-baseline/2`) and the corrective Advanced Coding section (`coding-advanced/2`) of this event.** One tested configuration; not production readiness.

##### Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **49 PASS, 12 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed; both Multi-Document checks failed (requested values partly correct, but replies attributed the conflicting replica count to the wrong document). The configured 16,384-token serving capacity is not a validated useful-context default.

Recorded FAIL identities, retained unchanged: `context-multidocument-v2-6144-seed-42`, `context-multidocument-v2-8192-seed-42`, `evidence-xid`, `linux-diagnosis-stale-config-bind-failure`, `linux-diagnosis-startup-invalid-config`, `multi-turn-correction-01`, `strict-extract-09`, `strict-limit-05`, `structured-schema-01`, `structured-semantics-01`, `tool-recovery-01`, `tool-selection-01`.

##### Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS (`advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`), with offline replay verification reproducing all three outcomes under sandbox-executed frozen oracles. This is an independent corrective event against the corrected `/2` construct; it publishes no score for the deferred historical `/1` sections of other models.

##### Reconciliation and deployment scope

No campaign-specific reconciliation applies to this campaign. The two Batch 04 reconciliations explicitly accepted by the same owner decision concern the Qwen/Nanbeige provenance record (`da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138`) and the Devstral blinded-review record (`4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384`); their limitations are disclosed on those events.

The deployment uses FlashAttention on, tied to this model's separately functionally admitted Vulkan deployment. That is a model-specific result, not a general FlashAttention kernel qualification, and must not be generalized.


The accompanying structured export, `website-publication.json`, retains every original baseline row including all FAILs, workload measurements, exact deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts.

##### Identity and deployment

- Event: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27` (the `off` in the identifier refers to the native reasoning arm). Profile: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`, revision `a93702f29e52b6893d74743d337e4f9149eb4126e3f2b27845c760d16acb18b4`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/google_gemma-4-31B-it-GGUF/tree/619aca7589c72be65dd968de8602ad23d68b5c14): Q5_K_M, 22,608,877,920 bytes, SHA-256 `9f6882d4780880c96f2292c7daf5d5f18fa7e3678cecc47fc22649e93ce6f693`. Upstream `google/gemma-4-31B-it` revision `842da3794eaa0b77d5f08bae87a17459d91ff475` (EXTERNAL_REPORTED identity).
- AMD Radeon AI PRO R9700, Vulkan, llama.cpp `b12556-50518b64c6f2191a116d2760042f106c4b3387d7` (FlashAttention on, model-specific deployment), native reasoning arm OFF (thinking disabled), temperature 1.0, top-p 0.95, top-k 64.
- Accepted section manifests: baseline `e419e1d72fb23155885f295b0e57fad8b0f008661b8e24ea8f432f47dd3efc4f` (report `2784cd2fdd595f47bfca63b2867650be6b011050ffdfe89540c5c95fee8a95d9`); coding `e2b759e5d8d8cebc470969cbc44dba63b6c0b3e1ebd1b9db842e39373b46ad00` (report `2279a88bfcf68b8d40ff1e92f25bded18cbed9549509723dff4afd3a81e590cb`). Owner acceptance 2026-11-28 UTC.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "9f6882d4780880c96f2292c7daf5d5f18fa7e3678cecc47fc22649e93ce6f693",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "gemma-4-31b-it-r9700-vulkan-off-2026-11-27",
      "reasoning": {
        "arm": "OFF",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": false
          }
        }
      },
      "runtime": {
        "backend": "Vulkan",
        "engine": "llama.cpp",
        "version": "b12556-50518b64c6f2191a116d2760042f106c4b3387d7"
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
      "serve_model_id": "google_gemma-4-31B-it-Q5_K_M",
      "template_sha256": "6a1015c47ccfcfa67c3b772385bccee357a4d37c3cda37bd202e9047f391ab82"
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
            "budget_limited": 0,
            "excluded": {},
            "fail": 2,
            "indeterminate": 0,
            "measured": 8,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 6,
            "planned": 8,
            "scored": 8,
            "status": "COMPLETE",
            "unscored": []
          },
          "instruction_following": {
            "applicable": 15,
            "budget_limited": 0,
            "excluded": {},
            "fail": 1,
            "indeterminate": 0,
            "measured": 15,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 14,
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
            "budget_limited": 0,
            "excluded": {},
            "fail": 2,
            "indeterminate": 0,
            "measured": 6,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 4,
            "planned": 6,
            "scored": 6,
            "status": "COMPLETE",
            "unscored": []
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
            "fail": 2,
            "indeterminate": 0,
            "measured": 2,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 0,
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
        "status": "COMPLETE"
      },
      "coverage_requirement": "full",
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "e419e1d72fb23155885f295b0e57fad8b0f008661b8e24ea8f432f47dd3efc4f",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": 25181552640
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 0.3280697529844474,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 32
            },
            "first_byte_seconds": 0.2456792609882541,
            "latency_seconds": 0.3280697529844474,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 82.291,
              "predicted_n": 3,
              "predicted_per_second": 24.303994361473308,
              "predicted_per_token_ms": 41.1455,
              "prompt_ms": 243.337,
              "prompt_n": 32,
              "prompt_per_second": 131.50486773486975,
              "prompt_per_token_ms": 7.60428125
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 24.303994361473308,
              "prompt": 131.50486773486975
            },
            "ttft_seconds": 0.24578399999882095,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 32,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 35
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.2701079380058218,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 32
            },
            "first_byte_seconds": 0.18711684900335968,
            "latency_seconds": 0.2701079380058218,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 82.875,
              "predicted_n": 3,
              "predicted_per_second": 24.132730015082956,
              "predicted_per_token_ms": 41.4375,
              "prompt_ms": 185.073,
              "prompt_n": 32,
              "prompt_per_second": 172.904745694942,
              "prompt_per_token_ms": 5.78353125
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 24.132730015082956,
              "prompt": 172.904745694942
            },
            "ttft_seconds": 0.18717154301702976,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 32,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 35
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.269165534991771,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 32
            },
            "first_byte_seconds": 0.18646092800190672,
            "latency_seconds": 0.269165534991771,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 82.536,
              "predicted_n": 3,
              "predicted_per_second": 24.231850344092276,
              "predicted_per_token_ms": 41.268,
              "prompt_ms": 184.536,
              "prompt_n": 32,
              "prompt_per_second": 173.40789872978715,
              "prompt_per_token_ms": 5.76675
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 24.231850344092276,
              "prompt": 173.40789872978715
            },
            "ttft_seconds": 0.1865074860106688,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 32,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 35
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 4.911820289999014,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3632
            },
            "first_byte_seconds": 4.825032614986412,
            "latency_seconds": 4.911820289999014,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 86.716,
              "predicted_n": 3,
              "predicted_per_second": 23.063794455463814,
              "predicted_per_token_ms": 43.358,
              "prompt_ms": 4818.362,
              "prompt_n": 3632,
              "prompt_per_second": 753.7831321100407,
              "prompt_per_token_ms": 1.3266415198237886
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 23.063794455463814,
              "prompt": 753.7831321100407
            },
            "ttft_seconds": 4.825106985983439,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3632,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3635
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 4.935906577971764,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3632
            },
            "first_byte_seconds": 4.849187823972898,
            "latency_seconds": 4.935906577971764,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 86.609,
              "predicted_n": 3,
              "predicted_per_second": 23.092288330312094,
              "predicted_per_token_ms": 43.3045,
              "prompt_ms": 4841.048,
              "prompt_n": 3632,
              "prompt_per_second": 750.2507721468576,
              "prompt_per_token_ms": 1.3328876651982378
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 23.092288330312094,
              "prompt": 750.2507721468576
            },
            "ttft_seconds": 4.849270429986063,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3632,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3635
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 4.925238988013007,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3632
            },
            "first_byte_seconds": 4.838572653010488,
            "latency_seconds": 4.925238988013007,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 86.572,
              "predicted_n": 3,
              "predicted_per_second": 23.10215774153306,
              "predicted_per_token_ms": 43.286,
              "prompt_ms": 4831.143,
              "prompt_n": 3632,
              "prompt_per_second": 751.7889658824009,
              "prompt_per_token_ms": 1.3301605176211453
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 23.10215774153306,
              "prompt": 751.7889658824009
            },
            "ttft_seconds": 4.838646223011892,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3632,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3635
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "gemma-4-31b-it-r9700-vulkan-off-2026-11-27",
      "profile_revision": "a93702f29e52b6893d74743d337e4f9149eb4126e3f2b27845c760d16acb18b4",
      "report_sha256": "2784cd2fdd595f47bfca63b2867650be6b011050ffdfe89540c5c95fee8a95d9",
      "section": "baseline",
      "units": [
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q02"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q03"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q04"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q05"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q06"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q07"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q08"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q09"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q10"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q11"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "Q12"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "coding-comprehension-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "coding-correction-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "coding-debug-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "coding-generation-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-3072-seed-314159"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-3072-seed-42"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-4096-seed-314159"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-4096-seed-42"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-8192-seed-314159"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-family-a-v2-8192-seed-42"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-multidocument-v2-6144-seed-42"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "context-multidocument-v2-8192-seed-42"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "NOT_EVALUABLE",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "NOT_EVALUABLE",
            "reason": "RUBRIC_INDETERMINATE",
            "scoring": "NOT_SCOREABLE"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "document-synthesis-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "evidence-gpu"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "evidence-metric"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "evidence-xid"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "fact-journal-current-boot"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "fact-python-bool"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "fact-ssh-copy"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "NOT_EVALUABLE",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "NOT_EVALUABLE",
            "reason": "RUBRIC_INDETERMINATE",
            "scoring": "NOT_SCOREABLE"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "git-amend"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "hall-fake-cuda"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "hall-fake-package"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "hall-fake-repo-state"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "hall-git-timewarp"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "instruction-conflict-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "linux-diagnosis-stale-config-bind-failure"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "linux-diagnosis-startup-invalid-config"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "multi-turn-correction-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "perf-short"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "perf-substantial"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "reasoning-consistency-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "reasoning-correctness-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "reasoning-evidence-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "repository-timeout-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "strict-exact-02"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "strict-extract-09"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "strict-limit-05"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "structured-schema-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "structured-semantics-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "sycophancy-logic"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "sycophancy-systemd"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "sycophancy-unknown"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "tool-permission-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "tool-recovery-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "FAIL",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "FAIL",
            "reason": null,
            "scoring": "SCORED_FAIL"
          },
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
          "technical_applicability": "APPLICABLE",
          "unit_id": "tool-selection-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "uncertainty-api"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "uncertainty-citation"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "uncertainty-file"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "untrusted-content-01"
        }
      ]
    },
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "e2b759e5d8d8cebc470969cbc44dba63b6c0b3e1ebd1b9db842e39373b46ad00",
      "methodology": "coding-advanced/2",
      "profile_id": "gemma-4-31b-it-r9700-vulkan-off-2026-11-27",
      "profile_revision": "a93702f29e52b6893d74743d337e4f9149eb4126e3f2b27845c760d16acb18b4",
      "report_sha256": "2279a88bfcf68b8d40ff1e92f25bded18cbed9549509723dff4afd3a81e590cb",
      "section": "coding",
      "units": [
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "advanced-module-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "advanced-repair-multi-01"
        },
        {
          "attempted": true,
          "completion": "COMPLETE",
          "coverage_impact": "MEASURED_AND_SCORED",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "NONE",
          "original_outcome": "PASS",
          "original_result": {
            "completion": "COMPLETE",
            "execution": "VALID",
            "limits": "NONE",
            "outcome": "PASS",
            "reason": null,
            "scoring": "SCORED_PASS"
          },
          "outcome": "PASS",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_PASS",
          "technical_applicability": "APPLICABLE",
          "unit_id": "advanced-repair-supplied-01"
        }
      ]
    }
  ]
}
```

</details>

## Limitations

- Model and Agentic findings are independent. Source events: [2026-11-27](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27).
- Performance is deployment-attributed, never model-quality credit. Source events: [2026-11-27](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27).
- Missing metrics remain unknown; boundary memory samples are not true peaks. Source events: [2026-11-27](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q5_K_M · llama.cpp b12556 · AI PRO R9700 | GGUF · Q5_K_M | llama.cpp b12556 | AI PRO R9700 | reasoning OFF · capacity 16,384 | 1 (2026-11-27) |

<details class="lab-findings-configs">
<summary>Configuration details: Q5_K_M · llama.cpp b12556 · AI PRO R9700</summary>

- Full profile name: Q5_K_M: llama.cpp / AMD Radeon AI PRO R9700 Vulkan, reasoning OFF (thinking disabled), FlashAttention on (model-specific).
- Profile identity: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, Vulkan, AMD Radeon AI PRO R9700, reasoning OFF (thinking disabled), FlashAttention on as a model-specific qualified deployment; configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): bartowski/google_gemma-4-31B-it-GGUF; revision 619aca7589c72be65dd968de8602ad23d68b5c14; GGUF Q5_K_M; sha256 9f6882d4780880c96f2292c7daf5d5f18fa7e3678cecc47fc22649e93ce6f693
- Artifact revision: 619aca7589c72be65dd968de8602ad23d68b5c14.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b12556-50518b64c6f2191a116d2760042f106c4b3387d7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.0, seed 42, temperature 1.0, top_k 64, top_p 0.95.
- Reasoning arm: OFF.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/gemma-4-31b-it/profiles/gemma-4-31b-it-r9700-vulkan-off-2026-11-27/profile.json)

Events on this configuration:

- [Gemma 4 31B IT: Model/Core and corrective Advanced Coding (2026-11-27)](/evaluations/gemma-4-31b-it#gemma-4-31b-it-r9700-vulkan-off-2026-11-27); status: NOT_ASSIGNED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-11-27 | [Gemma 4 31B IT: Model/Core and corrective Advanced Coding](#gemma-4-31b-it-r9700-vulkan-off-2026-11-27) | Q5_K_M · llama.cpp b12556 · AI PRO R9700 | NOT_ASSIGNED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/gemma-4-31b-it)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-27 HUMAN_ACCEPTED baseline and corrective Advanced Coding; model-specific Vulkan FlashAttention-on deployment</summary>

- Campaign: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`
- Export disposition: WEBSITE_READY; publication date 2026-11-27
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/gemma-4-31b-it/events/gemma-4-31b-it-r9700-vulkan-off-2026-11-27/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-28
- Acceptance basis (as recorded): Direct owner scientific acceptance delivered 2026-11-28T12:58:44Z (UTC date 2026-11-28). HUMAN_ACCEPTED scope, this campaign only: the Model/Core baseline (model-baseline/2; 61 identities, 49 PASS, 12 FAIL, none budget-limited; all six controlled Family A context checks passed while both Multi-Document checks failed) and the corrective Advanced Coding section coding-advanced/2 (three units, three PASS, offline replay verified), on the model-specific qualified R9700 Vulkan llama.cpp b12556 deployment with the native reasoning arm OFF and FlashAttention on. That FlashAttention-on result is tied to this separately admitted model deployment; it is not a general FlashAttention kernel qualification and must not be generalized. No campaign-specific reconciliation applies to this campaign; the two Batch 04 reconciliations explicitly accepted by the same owner decision concern the Qwen/Nanbeige provenance record (da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138) and the Devstral blinded-review record (4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384). Original negative results and deployment-attributed observations are retained. These are WELP unit outcomes, not a composite model score, and not general model production readiness.
- Review source SHA-256: `a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2`

| Section | Manifest SHA-256 |
|---|---|
| baseline | `e419e1d72fb23155885f295b0e57fad8b0f008661b8e24ea8f432f47dd3efc4f` |
| coding | `e2b759e5d8d8cebc470969cbc44dba63b6c0b3e1ebd1b9db842e39373b46ad00` |

- Artifact revision: 619aca7589c72be65dd968de8602ad23d68b5c14
- Artifact format: GGUF
- Runtime backend: Vulkan
- Export identity: event_date `2026-11-27`, event_id `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`, event_type `welp-recharacterization`, model_id `gemma-4-31b-it`, profile_id `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`
- Export source pin: repository-cache WumboLabs/evaluations @ `92906a38562272c0824bdd4a5e7118811d7a5b9b` path models/gemma-4-31b-it/events/gemma-4-31b-it-r9700-vulkan-off-2026-11-27/website-publication.json sha256 `65ac9fff712b6b4d87426c784fbb464ba57ffb6b9af9064f335f663a1a931bb5`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-28 UTC with private decision-source SHA-256 a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2. All accepted outcomes retained; the two Batch 04 reconciliations are explicitly accepted and disclosed with their limitations; no execution-time source hash is claimed.</small></p>

</details>
