+++
title = "Devstral Small 2 24B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 1

[extra]
kind = "model"
model_id = "devstral-small-2-24b-instruct-2512"
vendor = "Mistral AI"
findings_first = true
catalog_artifact = "GGUF · Q4_K_M"
catalog_profile_id = "devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-11-27
+++

## Overview

Mistral AI · 1 tested configuration · 1 evidence event · newest evidence 2026-11-27.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Latest evidence:** 2026-11-27: [event result](#devstral-r9700-vulkan-native-2026-11-27)
- **2026-11-27** · Q4_K_M · llama.cpp b12556 · AI PRO R9700: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; baseline 61 units: 42 PASS, 19 FAIL; coverage failures retained: coding 4 pass / 1 fail; context 6 pass / 2 fail; instruction following 13 pass / 2 fail; reasoning 2 pass / 4 fail; reliability 13 pass / 7 fail; structured output 0 pass / 2 fail; tool use 2 pass / 1 fail; coding 3 units: 3 PASS (ADVANCE). [Event result](#devstral-r9700-vulkan-native-2026-11-27)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="devstral-r9700-vulkan-native-2026-11-27"></a>

### 2026-11-27: Devstral Small 2 24B: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED baseline and corrective Advanced Coding; blinded-review reconciliation disclosed** · config Q4_K_M · llama.cpp b12556 · AI PRO R9700 · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 Vulkan, native non-configurable (FlashAttention off, artifact-embedded chat template).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/devstral-small-2-24b-instruct-2512/events/devstral-r9700-vulkan-native-2026-11-27/REPORT.md)

#### Devstral Small 2 24B: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED scope: the Model/Core baseline (`model-baseline/2`) and the corrective Advanced Coding section (`coding-advanced/2`) of this event.** One tested configuration; not production readiness or unattended repository autonomy.

##### Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **42 PASS, 19 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed; both Multi-Document checks failed. The configured 16,384-token serving capacity is not a validated useful-context default.

Recorded FAIL identities, retained unchanged: `Q12`, `coding-correction-01`, `context-multidocument-v2-6144-seed-42`, `context-multidocument-v2-8192-seed-42`, `git-amend`, `hall-fake-package`, `hall-git-timewarp`, `linux-diagnosis-stale-config-bind-failure`, `linux-diagnosis-startup-invalid-config`, `multi-turn-correction-01`, `reasoning-consistency-01`, `reasoning-correctness-01`, `strict-extract-09`, `strict-limit-05`, `structured-schema-01`, `structured-semantics-01`, `sycophancy-systemd`, `sycophancy-unknown`, `tool-selection-01`.

##### Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS (`advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`), with offline replay verification reproducing all three outcomes under sandbox-executed frozen oracles. This is an independent corrective event against the corrected `/2` construct; it publishes no score for the deferred historical `/1` sections of other models.

##### Blinded-review reconciliation: explicitly accepted and disclosed

The owner explicitly accepted the Devstral blinded-review reconciliation, SHA-256 `4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384`, and its disclosed limitation:

- The primary blinded review's delivery omitted the frozen Family A gate definitions for one context packet while assigning PASS. The sealed review and finalized section were not modified.
- A separate, fixture-complete blinded evaluation with all eleven qualification cases conformant independently supported the same PASS.
- It is external post-finalization verification, not an imported second framework review; the original packet hash does not cover the added gates, and the superseded response revisions are retained in the local scientific evidence.

A public-safe derivative of the reconciliation record is preserved beside the profile metadata under `supporting-evidence/`.


The accompanying structured export, `website-publication.json`, retains every original baseline row including all FAILs, workload measurements, exact deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts.

##### Identity and deployment

- Event: `devstral-r9700-vulkan-native-2026-11-27`. Profile: `devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27`, revision `f34dc65c9f88202c071f14281591d4bee9f0dde74d52a9fbc85ad250480924ed`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/mistralai_Devstral-Small-2-24B-Instruct-2512-GGUF/tree/027695770ae1de77c2f6fb19f8e1ba9d65fcd15d): Q4_K_M, 14,334,438,272 bytes, SHA-256 `bfd11c8679c6b81eb43763505465d7dcfa72e460ab1c220ecc235a3efadd7f7f`. Upstream publisher identity `mistralai/Devstral-Small-2-24B-Instruct-2512` is EXTERNAL_REPORTED.
- AMD Radeon AI PRO R9700, Vulkan, llama.cpp `b12556-50518b64c6f2191a116d2760042f106c4b3387d7` (FlashAttention off), native non-configurable profile, temperature 0.15.
- **Deployment limitation:** the evaluated deployment served the artifact's embedded GGUF chat template, which differs from the current publisher-source template that injects a coding-agent system prompt. Findings apply to the artifact's embedded template as served.
- Accepted section manifests: baseline `cadbcefe4b353d6554e65b4e67dfb1358965f2d7510834f1a928a9e0e025f63e` (report `b0fda62a4c5416dba91b78777e6f9f709e9a212f500b84156eb607232c835ffc`); coding `1b32e8e98b669133fac339f5658bc1abc09af3cc184a98a7f4b4658eb32b5a74` (report `a84df4961a94ee4aa8af2981218587819a71b2ae2e32211323dc12fdebe86863`). Owner acceptance 2026-11-28 UTC.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "bfd11c8679c6b81eb43763505465d7dcfa72e460ab1c220ecc235a3efadd7f7f",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27",
      "reasoning": {
        "arm": "NOT_CONFIGURABLE",
        "controls": {}
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
        "temperature": 0.15,
        "top_k": 0,
        "top_p": 1.0
      },
      "serve_model_id": "Devstral-Small-2-24B-Instruct-2512-Q4_K_M",
      "template_sha256": "ed825380b678dad25046e0a92ef5c64a57178ccaba7e780b5ed581e91a4fd6ac"
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
            "fail": 1,
            "indeterminate": 0,
            "measured": 5,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 4,
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
            "fail": 4,
            "indeterminate": 0,
            "measured": 6,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 2,
            "planned": 6,
            "scored": 6,
            "status": "COMPLETE",
            "unscored": []
          },
          "reliability": {
            "applicable": 20,
            "budget_limited": 0,
            "excluded": {},
            "fail": 7,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 13,
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
            "fail": 1,
            "indeterminate": 0,
            "measured": 3,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 2,
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
      "manifest_sha256": "cadbcefe4b353d6554e65b4e67dfb1358965f2d7510834f1a928a9e0e025f63e",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": 17060331520
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 0.1268344129784964,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 22
            },
            "first_byte_seconds": 0.07182426197687164,
            "latency_seconds": 0.1268344129784964,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 54.946,
              "predicted_n": 3,
              "predicted_per_second": 36.39937393076839,
              "predicted_per_token_ms": 27.473,
              "prompt_ms": 70.598,
              "prompt_n": 22,
              "prompt_per_second": 311.6235587410408,
              "prompt_per_token_ms": 3.209
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 36.39937393076839,
              "prompt": 311.6235587410408
            },
            "ttft_seconds": 0.07190456398529932,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 22,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 25
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.12088051499449648,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 22
            },
            "first_byte_seconds": 0.06527770298998803,
            "latency_seconds": 0.12088051499449648,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 55.532,
              "predicted_n": 3,
              "predicted_per_second": 36.015270474681266,
              "predicted_per_token_ms": 27.766,
              "prompt_ms": 63.499,
              "prompt_n": 22,
              "prompt_per_second": 346.4621490102206,
              "prompt_per_token_ms": 2.886318181818182
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 36.015270474681266,
              "prompt": 346.4621490102206
            },
            "ttft_seconds": 0.06534539099084213,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 22,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 25
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.1256271790189203,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 22
            },
            "first_byte_seconds": 0.069992545992136,
            "latency_seconds": 0.1256271790189203,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 55.475,
              "predicted_n": 3,
              "predicted_per_second": 36.05227579990987,
              "predicted_per_token_ms": 27.7375,
              "prompt_ms": 68.384,
              "prompt_n": 22,
              "prompt_per_second": 321.7126813289658,
              "prompt_per_token_ms": 3.108363636363636
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 36.05227579990987,
              "prompt": 321.7126813289658
            },
            "ttft_seconds": 0.07006354999612086,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 22,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 25
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 3.574901743006194,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3862
            },
            "first_byte_seconds": 3.5164067870064173,
            "latency_seconds": 3.574901743006194,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 58.426,
              "predicted_n": 3,
              "predicted_per_second": 34.231335364392564,
              "predicted_per_token_ms": 29.213,
              "prompt_ms": 3510.852,
              "prompt_n": 3862,
              "prompt_per_second": 1100.017887395994,
              "prompt_per_token_ms": 0.9090761263593993
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 34.231335364392564,
              "prompt": 1100.017887395994
            },
            "ttft_seconds": 3.516512477013748,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3862,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3865
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 3.4345035890000872,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3862
            },
            "first_byte_seconds": 3.3757353959954344,
            "latency_seconds": 3.4345035890000872,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 58.593,
              "predicted_n": 3,
              "predicted_per_second": 34.13377024559247,
              "predicted_per_token_ms": 29.2965,
              "prompt_ms": 3369.172,
              "prompt_n": 3862,
              "prompt_per_second": 1146.2757021606494,
              "prompt_per_token_ms": 0.8723904712584153
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 34.13377024559247,
              "prompt": 1146.2757021606494
            },
            "ttft_seconds": 3.375808253971627,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3862,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3865
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 3.428548559983028,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3862
            },
            "first_byte_seconds": 3.3696252229856327,
            "latency_seconds": 3.428548559983028,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 58.638,
              "predicted_n": 3,
              "predicted_per_second": 34.10757529247246,
              "predicted_per_token_ms": 29.319,
              "prompt_ms": 3362.612,
              "prompt_n": 3862,
              "prompt_per_second": 1148.5119306063264,
              "prompt_per_token_ms": 0.8706918694976696
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 34.10757529247246,
              "prompt": 1148.5119306063264
            },
            "ttft_seconds": 3.369685647980077,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3862,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3865
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27",
      "profile_revision": "f34dc65c9f88202c071f14281591d4bee9f0dde74d52a9fbc85ad250480924ed",
      "report_sha256": "b0fda62a4c5416dba91b78777e6f9f709e9a212f500b84156eb607232c835ffc",
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
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
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
          "unit_id": "reasoning-consistency-01"
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
          "unit_id": "sycophancy-systemd"
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
      "manifest_sha256": "1b32e8e98b669133fac339f5658bc1abc09af3cc184a98a7f4b4658eb32b5a74",
      "methodology": "coding-advanced/2",
      "profile_id": "devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27",
      "profile_revision": "f34dc65c9f88202c071f14281591d4bee9f0dde74d52a9fbc85ad250480924ed",
      "report_sha256": "a84df4961a94ee4aa8af2981218587819a71b2ae2e32211323dc12fdebe86863",
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

- Model and Agentic findings are independent. Source events: [2026-11-27](#devstral-r9700-vulkan-native-2026-11-27).
- Performance is deployment-attributed, never model-quality credit. Source events: [2026-11-27](#devstral-r9700-vulkan-native-2026-11-27).
- Missing metrics remain unknown; boundary memory samples are not true peaks. Source events: [2026-11-27](#devstral-r9700-vulkan-native-2026-11-27).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b12556 · AI PRO R9700 | GGUF · Q4_K_M | llama.cpp b12556 | AI PRO R9700 | reasoning NOT_CONFIGURABLE · capacity 16,384 | 1 (2026-11-27) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b12556 · AI PRO R9700</summary>

- Full profile name: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 Vulkan, native non-configurable (FlashAttention off, artifact-embedded chat template).
- Profile identity: `devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, Vulkan, AMD Radeon AI PRO R9700, FlashAttention off, artifact-embedded chat template (differs from the current publisher-source template); configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): bartowski/mistralai_Devstral-Small-2-24B-Instruct-2512-GGUF; revision 027695770ae1de77c2f6fb19f8e1ba9d65fcd15d; GGUF Q4_K_M; sha256 bfd11c8679c6b81eb43763505465d7dcfa72e460ab1c220ecc235a3efadd7f7f
- Artifact revision: 027695770ae1de77c2f6fb19f8e1ba9d65fcd15d.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b12556-50518b64c6f2191a116d2760042f106c4b3387d7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.0, seed 42, temperature 0.15, top_k 0, top_p 1.0.
- Reasoning arm: NOT_CONFIGURABLE.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/devstral-small-2-24b-instruct-2512/profiles/devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27/profile.json)

Events on this configuration:

- [Devstral Small 2 24B: Model/Core and corrective Advanced Coding (2026-11-27)](/evaluations/devstral-small-2-24b-instruct-2512#devstral-r9700-vulkan-native-2026-11-27); status: NOT_ASSIGNED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-11-27 | [Devstral Small 2 24B: Model/Core and corrective Advanced Coding](#devstral-r9700-vulkan-native-2026-11-27) | Q4_K_M · llama.cpp b12556 · AI PRO R9700 | NOT_ASSIGNED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/devstral-small-2-24b-instruct-2512)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-27 HUMAN_ACCEPTED baseline and corrective Advanced Coding; blinded-review reconciliation disclosed</summary>

- Campaign: `devstral-r9700-vulkan-native-2026-11-27`
- Export disposition: WEBSITE_READY; publication date 2026-11-27
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/devstral-small-2-24b-instruct-2512/events/devstral-r9700-vulkan-native-2026-11-27/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-28
- Acceptance basis (as recorded): Direct owner scientific acceptance delivered 2026-11-28T12:58:44Z (UTC date 2026-11-28). HUMAN_ACCEPTED scope, this campaign only: the Model/Core baseline (model-baseline/2; 61 identities, 42 PASS, 19 FAIL, none budget-limited; all six controlled Family A context checks passed while both Multi-Document checks failed) and the corrective Advanced Coding section coding-advanced/2 (three units, three PASS, offline replay verified), on the R9700 Vulkan llama.cpp b12556 deployment with FlashAttention off and the artifact's embedded chat template. The owner explicitly accepted the Devstral blinded-review reconciliation, SHA-256 4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384, and its disclosed limitation: the primary blinded-review delivery omitted the frozen Family A gate definitions for one context packet while assigning PASS; a separate fixture-complete blinded evaluation, with all eleven qualification cases conformant, independently supported the same PASS. This is external post-finalization verification, not an imported second framework review; the sealed section, its original packet identity and the superseded response revisions are retained unchanged. The evaluated deployment served the GGUF artifact's embedded chat template, which differs from the current publisher-source template; that deployment-specific limitation is retained. Original negative results and deployment-attributed observations are retained. These are WELP unit outcomes, not a composite model score, and not general model production readiness.
- Review source SHA-256: `a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2`

| Section | Manifest SHA-256 |
|---|---|
| baseline | `cadbcefe4b353d6554e65b4e67dfb1358965f2d7510834f1a928a9e0e025f63e` |
| coding | `1b32e8e98b669133fac339f5658bc1abc09af3cc184a98a7f4b4658eb32b5a74` |

- Artifact revision: 027695770ae1de77c2f6fb19f8e1ba9d65fcd15d
- Artifact format: GGUF
- Runtime backend: Vulkan
- Export identity: event_date `2026-11-27`, event_id `devstral-r9700-vulkan-native-2026-11-27`, event_type `welp-recharacterization`, model_id `devstral-small-2-24b-instruct-2512`, profile_id `devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27`
- Export source pin: repository-cache WumboLabs/evaluations @ `92906a38562272c0824bdd4a5e7118811d7a5b9b` path models/devstral-small-2-24b-instruct-2512/events/devstral-r9700-vulkan-native-2026-11-27/website-publication.json sha256 `d7e23623cb139f5a323891c1908505686cb0c8d30beacb2cefaa2fc028125c5d`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-28 UTC with private decision-source SHA-256 a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2. All accepted outcomes retained; the two Batch 04 reconciliations are explicitly accepted and disclosed with their limitations; no execution-time source hash is claimed.</small></p>

</details>
