+++
title = "Qwen3-Coder-30B-A3B-Instruct"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 5

[extra]
kind = "model"
model_id = "qwen3-coder-30b-a3b-instruct"
vendor = "Qwen"
findings_first = true
catalog_artifact = "GGUF · Q4_K_M"
catalog_profile_id = "qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-11-27
+++

## Overview

Qwen · 2 tested configurations · 2 evidence events · newest evidence 2026-11-27.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Latest evidence:** 2026-11-27: [event result](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27)
- **2026-11-27** · Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; coding 3 units: 3 PASS (ADVANCE). [Event result](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27)
- **2026-11-17** · Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; baseline 61 units: 51 PASS, 10 FAIL; coverage failures retained: coding 4 pass / 1 fail; context 6 pass / 2 fail; instruction following 14 pass / 1 fail; reasoning 4 pass / 2 fail; reliability 16 pass / 4 fail. [Event result](#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27"></a>

### 2026-11-27: Qwen3-Coder-30B-A3B-Instruct: corrective Advanced Coding

**HUMAN_ACCEPTED corrective coding-advanced/2; historical /1 deferral unchanged** · config Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, native non-thinking.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27/REPORT.md)

#### Qwen3-Coder-30B-A3B-Instruct: corrective Advanced Coding

**HUMAN_ACCEPTED scope: the corrective Advanced Coding section (`coding-advanced/2`) only.** This is an independent corrective event, not a regrade. The historical `coding-advanced/1` section stays DEFERRED_BY_OWNER with its original outcomes and manifest provenance unchanged.

##### Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS, with offline replay verification reproducing all three outcomes: `advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`. Sandbox-executed frozen oracles decide outcomes. The methodology-versioned `/2` construct corrects the defective `/1` multi-file repair task, whose published deferral reason (frozen task supplied an already-correct target) remains the record of the separate 2026-11-17 baseline event. This corrective section does not supersede that deferral and publishes no score for `/1`.

##### Provenance reconciliation: explicitly accepted and disclosed

The owner explicitly accepted the Batch 04 provenance reconciliation, SHA-256 `da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138`, and its disclosed limitations:

- The sealed corrective profile inherited the historical Batch 03 source-inventory hash `8c916381dd5e1505023a00689698ed8a893fd4222ed6f2c802006718f59ff372` and the historical Batch 03 authorization wording. They are not the corrected `coding-advanced/2` source inventory and not the current assignment authorization.
- The corrected post-correction 189-entry source-and-fixtures inventory has SHA-256 `095a5138e667960fa472db4fb7a0317f6c5327ba80d97de5b93b3b26853f45eb`; a later check verified every listed file against it. That later check is not an execution-time hash measurement at each scored dispatch.
- No independently established execution-time source hash is claimed.

A public-safe derivative of the reconciliation record is preserved beside the profile metadata under `supporting-evidence/`; the original record remains in the local scientific evidence.


The accompanying structured export, `website-publication.json`, retains the exact unit outcomes, deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts. This result is bounded to the tested deployment; it is not a composite model score or a production-readiness claim.

##### Identity and deployment

- Event: `qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27`. Profile: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27`, revision `ae81e97569c656645872679bcd29e923aeb3d4a55166b397c067efe38b157201`.
- Tested [GGUF artifact](https://huggingface.co/ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF/tree/ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3): Q4_K_M, 17,988,419,552 bytes, SHA-256 `f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335`.
- AMD Radeon AI PRO R9700, HIP, llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (FlashAttention off), native non-thinking profile with publisher-recommended non-thinking sampling (temperature 0.7, top-p 0.8, top-k 20). Context and performance findings apply only to the bounded workloads tested; the 16,384-token configured capacity is not a validated useful-context default.
- Accepted section manifest SHA-256 `2e15882ad9117d1b66cb29ae29eb51b9fdcdc38f0118f878516a7550e6773c98`; section report SHA-256 `9dc15c72d4bb682e7c6ecd5a7fc59e3c1c71e76388bfd69105a09d9dae0356fe`; owner acceptance 2026-11-28 UTC.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27",
      "reasoning": {
        "arm": "NOT_CONFIGURABLE",
        "controls": {}
      },
      "runtime": {
        "backend": "HIP",
        "engine": "llama.cpp",
        "version": "b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.05,
        "seed": 42,
        "temperature": 0.7,
        "top_k": 20,
        "top_p": 0.8
      },
      "serve_model_id": "Qwen3-Coder-30B-A3B-Instruct-Q4_K_M",
      "template_sha256": "32bf2564d2245b98298677d3ac2332ab50bc3279740c13c3974689464b38aa3c"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "2e15882ad9117d1b66cb29ae29eb51b9fdcdc38f0118f878516a7550e6773c98",
      "methodology": "coding-advanced/2",
      "profile_id": "qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27",
      "profile_revision": "ae81e97569c656645872679bcd29e923aeb3d4a55166b397c067efe38b157201",
      "report_sha256": "9dc15c72d4bb682e7c6ecd5a7fc59e3c1c71e76388bfd69105a09d9dae0356fe",
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

<a id="qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17"></a>

### 2026-11-17: Qwen3-Coder-30B-A3B-Instruct: Model/Core baseline

**HUMAN_ACCEPTED Model/Core only; Advanced Coding deferred by owner** · config Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, native non-thinking.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/844dcc6e47c6092b492af372985cf45f4923a0a9/models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17/REPORT.md)

#### Qwen3-Coder-30B-A3B-Instruct: accepted WELP Model/Core findings

**HUMAN_ACCEPTED scope: Model/Core baseline only.** Advanced Coding is **DEFERRED_BY_OWNER**, not an accepted result. This event describes one tested configuration, not production readiness or unattended repository autonomy.

##### Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **49 PASS, 10 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed. Both Multi-Document checks failed: several requested values were correct, but both replies attributed the conflicting replica count to the wrong document. The configured 16,384-token serving capacity is not a validated useful-context default.

The short coding-correction probe returned the wrong clamped value. Document synthesis promoted two timestamps into an unsupported measured startup interval. In one Linux diagnosis, the model identified the wrong port for a failed bind. The frozen record also retains failures for the forbidden-letter check, invented Git extension behavior, an unavailable-tool instruction, strict extraction, and systemd diagnosis. All three baseline tool probes passed; a separate technical qualification obtained a grounded tool result but made an unnecessary extra call rather than ending cleanly.

**SCI-01:** Q02 originally passed under the corrected frozen key order. No historical erratum or replacement score applies. **SCI-02:** the strict-extraction wording permits more than one plausible reading; the recorded exact-check FAIL does not establish broad instruction-following failure. **SCI-03:** the systemd reply rejected the premise that active means serving, but missed the frozen lexical check and overstated what `active` establishes about listening. Keep the original FAIL without interpreting it as agreement with the premise.

##### Advanced Coding: DEFERRED_BY_OWNER

The frozen multi-file repair task supplied an already-correct target, so the Advanced Coding section is excluded from this scientific acceptance pending a separately governed methodological correction. The original record remains intact; no specialist scores are published here.

- Deferred section: `coding` (`coding-advanced/1`), original manifest SHA-256 `1205222e2e70cce736294026e48892bbc17cb1d8715d71f215cf06b7b8a0659e`.
- Original specialist report SHA-256 `efe469271ffcb193ba147c6a5a9dfac6221aded95561f2ba8281920fe6e7b471`.


The accompanying structured export, `website-publication.json`, retains all identity-level baseline outcomes, workload measurements, exact deployment conditions, acceptance bindings, and deferred-section provenance. Original local evidence governs scientific conflicts.

##### Identity and deployment

- Event: `qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17`. Profile: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17`, revision `cf92da45dbe0ca725b58a0f46457906b3df5ca32702308237afdffd1403ed71e`.
- Tested [GGUF artifact](https://huggingface.co/ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF/tree/ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3): Q4_K_M, 17,988,419,552 bytes, SHA-256 `f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335`.
- AMD Radeon AI PRO R9700, HIP, llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (flash attention off), native non-thinking profile. Context and performance findings apply only to the bounded workloads tested.
- Accepted baseline manifest SHA-256 `6a50a7e8311ada876046ec97e3122f3740a63add953b4b83ee449c5435c688aa`, owner acceptance 2026-11-18 UTC.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17",
      "reasoning": {
        "arm": "NOT_CONFIGURABLE",
        "controls": {}
      },
      "runtime": {
        "backend": "HIP",
        "engine": "llama.cpp",
        "version": "b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.05,
        "seed": 42,
        "temperature": 0.7,
        "top_k": 20,
        "top_p": 0.8
      },
      "serve_model_id": "Qwen3-Coder-30B-A3B-Instruct-Q4_K_M",
      "template_sha256": "32bf2564d2245b98298677d3ac2332ab50bc3279740c13c3974689464b38aa3c"
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
            "fail": 4,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 16,
            "planned": 20,
            "scored": 20,
            "status": "COMPLETE",
            "unscored": []
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
        "status": "COMPLETE"
      },
      "coverage_requirement": "full",
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "6a50a7e8311ada876046ec97e3122f3740a63add953b4b83ee449c5435c688aa",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": 21020803072
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 0.06665843499649782,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 27
            },
            "first_byte_seconds": 0.04094644200085895,
            "latency_seconds": 0.06665843499649782,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 25.62,
              "predicted_n": 3,
              "predicted_per_second": 78.06401249024199,
              "predicted_per_token_ms": 12.81,
              "prompt_ms": 39.531,
              "prompt_n": 27,
              "prompt_per_second": 683.0082719890719,
              "prompt_per_token_ms": 1.4641111111111111
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 78.06401249024199,
              "prompt": 683.0082719890719
            },
            "ttft_seconds": 0.04098917199735297,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 27,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 30
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.06522229799884371,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 27
            },
            "first_byte_seconds": 0.040092816001561005,
            "latency_seconds": 0.06522229799884371,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 25.055,
              "predicted_n": 3,
              "predicted_per_second": 79.82438635002994,
              "predicted_per_token_ms": 12.5275,
              "prompt_ms": 38.341,
              "prompt_n": 27,
              "prompt_per_second": 704.2069846900185,
              "prompt_per_token_ms": 1.420037037037037
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 79.82438635002994,
              "prompt": 704.2069846900185
            },
            "ttft_seconds": 0.040121621001162566,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 27,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 30
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 0.06520854100381257,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 27
            },
            "first_byte_seconds": 0.0407153640044271,
            "latency_seconds": 0.06520854100381257,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 24.413,
              "predicted_n": 3,
              "predicted_per_second": 81.92356531356245,
              "predicted_per_token_ms": 12.2065,
              "prompt_ms": 38.945,
              "prompt_n": 27,
              "prompt_per_second": 693.285402490692,
              "prompt_per_token_ms": 1.4424074074074074
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 81.92356531356245,
              "prompt": 693.285402490692
            },
            "ttft_seconds": 0.04073905800032662,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 27,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 30
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 2.3532647359970724,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3567
            },
            "first_byte_seconds": 2.3176580389990704,
            "latency_seconds": 2.3532647359970724,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 35.515,
              "predicted_n": 3,
              "predicted_per_second": 56.31423342249754,
              "predicted_per_token_ms": 17.7575,
              "prompt_ms": 2312.429,
              "prompt_n": 3567,
              "prompt_per_second": 1542.5338464445827,
              "prompt_per_token_ms": 0.6482839921502663
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 56.31423342249754,
              "prompt": 1542.5338464445827
            },
            "ttft_seconds": 2.317717701997026,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3567,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3570
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 2.3508108320020256,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3567
            },
            "first_byte_seconds": 2.314704990996688,
            "latency_seconds": 2.3508108320020256,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 35.942,
              "predicted_n": 3,
              "predicted_per_second": 55.645206165488844,
              "predicted_per_token_ms": 17.971,
              "prompt_ms": 2309.888,
              "prompt_n": 3567,
              "prompt_per_second": 1544.2307159481327,
              "prompt_per_token_ms": 0.6475716288197364
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 55.645206165488844,
              "prompt": 1544.2307159481327
            },
            "ttft_seconds": 2.314764352995553,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3567,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3570
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 2.3518926489996375,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3567
            },
            "first_byte_seconds": 2.316359401003865,
            "latency_seconds": 2.3518926489996375,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 35.415,
              "predicted_n": 3,
              "predicted_per_second": 56.47324579980234,
              "predicted_per_token_ms": 17.7075,
              "prompt_ms": 2311.502,
              "prompt_n": 3567,
              "prompt_per_second": 1543.1524610404836,
              "prompt_per_token_ms": 0.6480241098962713
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 56.47324579980234,
              "prompt": 1543.1524610404836
            },
            "ttft_seconds": 2.316426869001589,
            "usage": {
              "completion_tokens": 3,
              "prompt_tokens": 3567,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3570
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17",
      "profile_revision": "cf92da45dbe0ca725b58a0f46457906b3df5ca32702308237afdffd1403ed71e",
      "report_sha256": "3776afe86f909e9fbe9a09e0f1a85341abf6c9e32656da58b04db8ccdbfd824d",
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
          "outcome": "FAIL",
          "reason": null,
          "recorded_attempts": 1,
          "scoring": "SCORED_FAIL",
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
          "unit_id": "linux-diagnosis-stale-config-bind-failure"
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
          "unit_id": "linux-diagnosis-startup-invalid-config"
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
          "unit_id": "structured-schema-01"
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
    }
  ]
}
```

</details>

## Limitations

- Model and Agentic findings are independent. Source events: [2026-11-27](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27), [2026-11-17](#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17).
- Performance is deployment-attributed, never model-quality credit. Source events: [2026-11-27](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27), [2026-11-17](#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17).
- Missing metrics remain unknown; boundary memory samples are not true peaks. Source events: [2026-11-27](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27), [2026-11-17](#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned | GGUF · Q4_K_M | llama.cpp b11311 | AI PRO R9700 | reasoning NOT_CONFIGURABLE · capacity 16,384 | 1 (2026-11-17) |
| Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking | GGUF · Q4_K_M | llama.cpp b11311 | AI PRO R9700 | reasoning NOT_CONFIGURABLE · capacity 16,384 | 1 (2026-11-27) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned</summary>

- Full profile name: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, native non-thinking.
- Profile identity: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking; configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF; revision ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3; GGUF Q4_K_M; sha256 f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335
- Artifact revision: ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.05, seed 42, temperature 0.7, top_k 20, top_p 0.8.
- Reasoning arm: NOT_CONFIGURABLE.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/qwen3-coder-30b-a3b-instruct/profiles/qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17/profile.json)

Events on this configuration:

- [Qwen3-Coder-30B-A3B-Instruct: Model/Core baseline (2026-11-17)](/evaluations/qwen3-coder-30b-a3b-instruct#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17); status: NOT_ASSIGNED

</details>

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking</summary>

- Full profile name: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, native non-thinking.
- Profile identity: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking; configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF; revision ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3; GGUF Q4_K_M; sha256 f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335
- Artifact revision: ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.05, seed 42, temperature 0.7, top_k 20, top_p 0.8.
- Reasoning arm: NOT_CONFIGURABLE.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/qwen3-coder-30b-a3b-instruct/profiles/qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27/profile.json)

Events on this configuration:

- [Qwen3-Coder-30B-A3B-Instruct: corrective Advanced Coding (2026-11-27)](/evaluations/qwen3-coder-30b-a3b-instruct#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27); status: NOT_ASSIGNED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-11-27 | [Qwen3-Coder-30B-A3B-Instruct: corrective Advanced Coding](#qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27) | Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned · llama.cpp, HIP, AMD Radeon AI PRO R9700, native non-thinking | NOT_ASSIGNED |
| 2026-11-17 | [Qwen3-Coder-30B-A3B-Instruct: Model/Core baseline](#qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17) | Q4_K_M · llama.cpp b11311 · AI PRO R9700 · configured 16384 tokens, not validation at full capacity. No serving recommendation assigned | NOT_ASSIGNED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/qwen3-coder-30b-a3b-instruct)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-27 HUMAN_ACCEPTED corrective coding-advanced/2; historical /1 deferral unchanged</summary>

- Campaign: `qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27`
- Export disposition: WEBSITE_READY; publication date 2026-11-27
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/d6aa6cecea86ed619d04927bc8017ae0ebded296/models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-28
- Acceptance basis (as recorded): Direct owner scientific acceptance delivered 2026-11-28T12:58:44Z (UTC date 2026-11-28). HUMAN_ACCEPTED scope: the corrective Advanced Coding section coding-advanced/2 of this campaign only (three units, three PASS, offline replay verified); an independent corrective event, not a regrade. The historical coding-advanced/1 section stays DEFERRED_BY_OWNER with its original outcomes and manifest provenance unchanged. The owner explicitly accepted the Batch 04 provenance reconciliation, SHA-256 da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138, and its disclosed limitations: the sealed corrective profile inherited the historical Batch 03 source-inventory hash and authorization wording, which are neither the corrected coding-advanced/2 source inventory nor the current assignment authorization. The corrected post-correction source-and-fixtures inventory (SHA-256 095a5138e667960fa472db4fb7a0317f6c5327ba80d97de5b93b3b26853f45eb) was verified afterward against the current files; that later verification is not an execution-time hash measurement, and no independently established execution-time source hash is claimed. Original negative results, historical deferrals and budget observations are retained. This acceptance covers the bounded scientific findings of the tested deployment, not general model production readiness.
- Review source SHA-256: `a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2`

| Section | Manifest SHA-256 |
|---|---|
| coding | `2e15882ad9117d1b66cb29ae29eb51b9fdcdc38f0118f878516a7550e6773c98` |

- Artifact revision: ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3
- Artifact format: GGUF
- Runtime backend: HIP
- Export identity: event_date `2026-11-27`, event_id `qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27`, event_type `welp-recharacterization`, model_id `qwen3-coder-30b-a3b-instruct`, profile_id `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27`
- Export source pin: repository-cache WumboLabs/evaluations @ `92906a38562272c0824bdd4a5e7118811d7a5b9b` path models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27/website-publication.json sha256 `985952d7b85ee08620d55e4c73d7cdf32cc75c84412cc4b4a25f03e749a1cda1`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-28 UTC with private decision-source SHA-256 a76ccf29e6db88c0f415676f121d0438002bdb6511ebd37b5f6af9c5324105a2. All accepted outcomes retained; the two Batch 04 reconciliations are explicitly accepted and disclosed with their limitations; no execution-time source hash is claimed.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-17 HUMAN_ACCEPTED Model/Core only; Advanced Coding deferred by owner</summary>

- Campaign: `qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17`
- Export disposition: WEBSITE_READY; publication date 2026-11-17
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/844dcc6e47c6092b492af372985cf45f4923a0a9/models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-18
- Acceptance basis (as recorded): The owner reviewed and accepted the verified Model/Core baseline for this tested deployment, including original negative and budget-limited findings and the SCI-02 strict-extraction and SCI-03 lexical-check reporting limitations. Q02 originally passed with the prospective SCI-01 ordering correction. No general production readiness is certified.
- Review source SHA-256: `891b97683f05246b5c8321af0cb0b1e02ebe1218549229cda04f5abf835dbd3c`

| Section | Manifest SHA-256 |
|---|---|
| baseline | `6a50a7e8311ada876046ec97e3122f3740a63add953b4b83ee449c5435c688aa` |

- Artifact revision: ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3
- Artifact format: GGUF
- Runtime backend: HIP
- Export identity: event_date `2026-11-17`, event_id `qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17`, event_type `welp-recharacterization`, model_id `qwen3-coder-30b-a3b-instruct`, profile_id `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17`
- Export source pin: repository-cache WumboLabs/evaluations @ `844dcc6e47c6092b492af372985cf45f4923a0a9` path models/qwen3-coder-30b-a3b-instruct/events/qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17/website-publication.json sha256 `59dad2a877205933116f1c2bcfc2913732a9c9d0267fecbd037ed6e08525129b`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-18 UTC with private decision-source SHA-256 891b97683f05246b5c8321af0cb0b1e02ebe1218549229cda04f5abf835dbd3c. All accepted outcomes retained; Advanced Coding retains original manifest provenance only.</small></p>

</details>
