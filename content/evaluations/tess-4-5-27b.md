+++
title = "Tess-4.5-27B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 8

[extra]
kind = "model"
model_id = "tess-4.5-27b"
vendor = "Migtissera"
findings_first = true
catalog_artifact = "GGUF · Q4_K_M"
catalog_profile_id = "tess-4.5-27b-r9700-hip-on-2026-11-17"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-11-17
+++

## Overview

Migtissera · 1 tested configuration · 1 evidence event · newest evidence 2026-11-17.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Latest evidence:** 2026-11-17: [event result](#tess45-27b-r9700-hip-on-2026-11-17)
- **2026-11-17** · Q4_K_M · llama.cpp b11311 · AI PRO R9700: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; advanced-tool-use 3 units: 3 PASS (ADVANCE); baseline 61 units: 56 PASS, 4 FAIL, 1 NOT_EVALUABLE; coverage failures retained: instruction following 14 pass / 1 fail; reasoning 5 pass / 1 fail; reliability 17 pass / 2 fail. [Event result](#tess45-27b-r9700-hip-on-2026-11-17)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="tess45-27b-r9700-hip-on-2026-11-17"></a>

### 2026-11-17: Tess-4.5-27B: Model/Core and Advanced Tool Use

**HUMAN_ACCEPTED independent sections; SCI-01 Q02 interpretation attributed separately** · config Q4_K_M · llama.cpp b11311 · AI PRO R9700 · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, reasoning ON.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/5a8ecd7cafe5ff70c5f718620820d02f03be9ca5/models/tess-4.5-27b/events/tess45-27b-r9700-hip-on-2026-11-17/REPORT.md)

#### Tess-4.5-27B: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Tool Use only. Event `tess45-27b-r9700-hip-on-2026-11-17`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

##### Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **54 PASS, 4 FAIL, 1 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five baseline coding probes, both structured-output tasks and three basic-tool probes passed. Genuine negatives included unsupported claims about a helper and about a later event absent from the evidence. One task was budget-limited, not a semantic failure. Advanced Tool Use passed executed native-tool selection, read-only permission compliance and feedback recovery on a deterministic simulator; this was not production tool access or an Agentic evaluation.

All eight bounded Practical Context checks passed. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `hall-fake-package` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-git-timewarp` | NOT_EVALUABLE | BUDGET_LIMITED |
| `linux-diagnosis-stale-config-bind-failure` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |

##### Advanced Tool Use (tool-use-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-tool-permission-01`, `advanced-tool-recovery-01`, `advanced-tool-selection-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

##### SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `8a2399e05835a605fd13d89c5236e9a14c75c366a1fdaa20f5a145c68a061b99`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.


The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.

##### Identity and deployment

- Profile: `tess-4.5-27b-r9700-hip-on-2026-11-17`, revision `e0be742026915f58b45c969480b2054b7bdbd5c032dddb66fdf6b9b2a52057c5`.
- Tested artifact: [migtissera/Tess-4.5-27B-GGUF](https://huggingface.co/migtissera/Tess-4.5-27B-GGUF/tree/e632461c0b8b835db69c7efc6aaac539f55b84de), GGUF Q4_K_M, 16,547,399,904 bytes; SHA-256 `7a3157e2d4ab96a2abcee99a986bea11cfe282b58815ec676c5abe7e6a92d8dc`.
- Runtime: llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (HIP); tested GPU: AMD Radeon AI PRO R9700.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=1, top_k=20, top_p=0.95.
- Original manifest SHA-256: baseline `ff99acf02512a66e884929573727f46dc4c9869411aaee7d529cd222fea1b778`; advanced-tool-use `ed19e38f8bb711261bdcdbf43ba0590e5fea2bd3b89c5747e8baa1c977ad7af6`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "7a3157e2d4ab96a2abcee99a986bea11cfe282b58815ec676c5abe7e6a92d8dc",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "tess-4.5-27b-r9700-hip-on-2026-11-17",
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
        "version": "b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7"
      },
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.0,
        "seed": 42,
        "temperature": 1.0,
        "top_k": 20,
        "top_p": 0.95
      },
      "serve_model_id": "Tess-4.5-27B-Q4_K_M",
      "template_sha256": "c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "ed19e38f8bb711261bdcdbf43ba0590e5fea2bd3b89c5747e8baa1c977ad7af6",
      "methodology": "tool-use-advanced/1",
      "profile_id": "tess-4.5-27b-r9700-hip-on-2026-11-17",
      "profile_revision": "e0be742026915f58b45c969480b2054b7bdbd5c032dddb66fdf6b9b2a52057c5",
      "report_sha256": "15af7ece95be8d7256a939c4ff2c383774be36f6dffbe32feb8c6f6dc71418f4",
      "section": "advanced-tool-use",
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
          "unit_id": "advanced-tool-permission-01"
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
          "unit_id": "advanced-tool-recovery-01"
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
          "unit_id": "advanced-tool-selection-01"
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
            "budget_limited": 0,
            "excluded": {},
            "fail": 0,
            "indeterminate": 0,
            "measured": 8,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 8,
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
            "fail": 1,
            "indeterminate": 0,
            "measured": 6,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 5,
            "planned": 6,
            "scored": 6,
            "status": "COMPLETE",
            "unscored": []
          },
          "reliability": {
            "applicable": 20,
            "budget_limited": 1,
            "excluded": {},
            "fail": 2,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": false,
            "missing": [],
            "pass": 17,
            "planned": 20,
            "scored": 19,
            "status": "COMPLETE_WITH_DOCUMENTED_LIMITATIONS",
            "unscored": [
              "hall-git-timewarp"
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
      "coverage_requirement": "full",
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "ff99acf02512a66e884929573727f46dc4c9869411aaee7d529cd222fea1b778",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": 18397265920
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 1.2044663550000223,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 71
            },
            "first_byte_seconds": 0.25648956800000633,
            "latency_seconds": 1.2044663550000223,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 947.602,
              "predicted_n": 29,
              "predicted_per_second": 29.548270265364575,
              "predicted_per_token_ms": 33.84292857142857,
              "prompt_ms": 254.197,
              "prompt_n": 71,
              "prompt_per_second": 279.31092813841235,
              "prompt_per_token_ms": 3.5802394366197183
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 29.548270265364575,
              "prompt": 279.31092813841235
            },
            "ttft_seconds": 0.2565987650000352,
            "usage": {
              "completion_tokens": 29,
              "prompt_tokens": 71,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 100
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.1559121209998011,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 71
            },
            "first_byte_seconds": 0.20871872799989433,
            "latency_seconds": 1.1559121209998011,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 946.945,
              "predicted_n": 29,
              "predicted_per_second": 29.568771153551687,
              "predicted_per_token_ms": 33.81946428571429,
              "prompt_ms": 206.091,
              "prompt_n": 71,
              "prompt_per_second": 344.5080085981435,
              "prompt_per_token_ms": 2.9026901408450705
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 29.568771153551687,
              "prompt": 344.5080085981435
            },
            "ttft_seconds": 0.20877707799991185,
            "usage": {
              "completion_tokens": 29,
              "prompt_tokens": 71,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 100
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.1588181050001367,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 71
            },
            "first_byte_seconds": 0.21134322800003247,
            "latency_seconds": 1.1588181050001367,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 947.25,
              "predicted_n": 29,
              "predicted_per_second": 29.559250461863286,
              "predicted_per_token_ms": 33.830357142857146,
              "prompt_ms": 208.806,
              "prompt_n": 71,
              "prompt_per_second": 340.0285432410946,
              "prompt_per_token_ms": 2.940929577464789
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 29.559250461863286,
              "prompt": 340.0285432410946
            },
            "ttft_seconds": 0.2113922310002181,
            "usage": {
              "completion_tokens": 29,
              "prompt_tokens": 71,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 100
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 7.729629907000117,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3671
            },
            "first_byte_seconds": 4.993605241000068,
            "latency_seconds": 7.729629907000117,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2735.632,
              "predicted_n": 76,
              "predicted_per_second": 27.41596822964492,
              "predicted_per_token_ms": 36.475093333333334,
              "prompt_ms": 4987.704,
              "prompt_n": 3671,
              "prompt_per_second": 736.0099957816262,
              "prompt_per_token_ms": 1.3586771996731135
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 27.41596822964492,
              "prompt": 736.0099957816262
            },
            "ttft_seconds": 4.993677337000008,
            "usage": {
              "completion_tokens": 76,
              "prompt_tokens": 3671,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3747
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 7.739683375999903,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3671
            },
            "first_byte_seconds": 5.002668594999932,
            "latency_seconds": 7.739683375999903,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2736.605,
              "predicted_n": 76,
              "predicted_per_second": 27.40622048121669,
              "predicted_per_token_ms": 36.48806666666667,
              "prompt_ms": 4996.681,
              "prompt_n": 3671,
              "prompt_per_second": 734.6876856857583,
              "prompt_per_token_ms": 1.361122582402615
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 27.40622048121669,
              "prompt": 734.6876856857583
            },
            "ttft_seconds": 5.002735160999919,
            "usage": {
              "completion_tokens": 76,
              "prompt_tokens": 3671,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3747
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 7.737338406000163,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3671
            },
            "first_byte_seconds": 4.999593211000047,
            "latency_seconds": 7.737338406000163,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 2736.98,
              "predicted_n": 76,
              "predicted_per_second": 27.40246549116179,
              "predicted_per_token_ms": 36.493066666666664,
              "prompt_ms": 4993.76,
              "prompt_n": 3671,
              "prompt_per_second": 735.1174265483323,
              "prompt_per_token_ms": 1.3603268864069737
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 27.40246549116179,
              "prompt": 735.1174265483323
            },
            "ttft_seconds": 4.999687389000201,
            "usage": {
              "completion_tokens": 76,
              "prompt_tokens": 3671,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3747
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "tess-4.5-27b-r9700-hip-on-2026-11-17",
      "profile_revision": "e0be742026915f58b45c969480b2054b7bdbd5c032dddb66fdf6b9b2a52057c5",
      "report_sha256": "c8c00f9d8f00d8bc08ebcfd013016e6c2e5701362153c9d9ecde46ad5e23d794",
      "scoring_errata": {
        "Q02": {
          "attempt_id": "0001",
          "erratum_sha256": "8a2399e05835a605fd13d89c5236e9a14c75c366a1fdaa20f5a145c68a061b99",
          "finding_id": "SCI-01",
          "manifest_sha256": "ff99acf02512a66e884929573727f46dc4c9869411aaee7d529cd222fea1b778",
          "original_outcome": "FAIL",
          "saved_key_order": [
            "count",
            "name"
          ],
          "source_fixture_sha256": "4ea5cead9db04ef3d882468bab995b5f4cf0fe5dde6f2a405584ea07fc6094b8",
          "source_key_order": [
            "name",
            "count"
          ],
          "source_oracle_outcome": "PASS"
        }
      },
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
          "unit_id": "context-multidocument-v2-6144-seed-42"
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
          "completion": "INCOMPLETE",
          "coverage_impact": "VALID_UNSCORED_MEASUREMENT",
          "exclusion_reason": null,
          "execution": "VALID",
          "limits": "BUDGET",
          "original_outcome": "NOT_EVALUABLE",
          "original_result": {
            "completion": "INCOMPLETE",
            "execution": "VALID",
            "limits": "BUDGET",
            "outcome": "NOT_EVALUABLE",
            "reason": "BUDGET_LIMITED",
            "scoring": "NOT_SCOREABLE"
          },
          "outcome": "NOT_EVALUABLE",
          "reason": "BUDGET_LIMITED",
          "recorded_attempts": 1,
          "scoring": "NOT_SCOREABLE",
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

- Model and Agentic findings are independent. Source events: [2026-11-17](#tess45-27b-r9700-hip-on-2026-11-17).
- Performance is deployment-attributed, never model-quality credit. Source events: [2026-11-17](#tess45-27b-r9700-hip-on-2026-11-17).
- Missing metrics remain unknown; boundary memory samples are not true peaks. Source events: [2026-11-17](#tess45-27b-r9700-hip-on-2026-11-17).
- SCI-01 (baseline Q02): recorded FAIL used the wrong key order. The unchanged answer replays as PASS under the pinned source check. Section rows and totals remain as recorded. Source events: [2026-11-17](#tess45-27b-r9700-hip-on-2026-11-17).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b11311 · AI PRO R9700 | GGUF · Q4_K_M | llama.cpp b11311 | AI PRO R9700 | reasoning ON · capacity 16,384 | 1 (2026-11-17) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b11311 · AI PRO R9700</summary>

- Full profile name: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, reasoning ON.
- Profile identity: `tess-4.5-27b-r9700-hip-on-2026-11-17`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, HIP, AMD Radeon AI PRO R9700, native reasoning ON; configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): migtissera/Tess-4.5-27B-GGUF; revision e632461c0b8b835db69c7efc6aaac539f55b84de; GGUF Q4_K_M; sha256 7a3157e2d4ab96a2abcee99a986bea11cfe282b58815ec676c5abe7e6a92d8dc
- Artifact revision: e632461c0b8b835db69c7efc6aaac539f55b84de.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.0, seed 42, temperature 1.0, top_k 20, top_p 0.95.
- Reasoning arm: ON.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/tess-4.5-27b/profiles/tess-4.5-27b-r9700-hip-on-2026-11-17/profile.json)

Events on this configuration:

- [Tess-4.5-27B: Model/Core and Advanced Tool Use (2026-11-17)](/evaluations/tess-4-5-27b#tess45-27b-r9700-hip-on-2026-11-17); status: NOT_ASSIGNED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-11-17 | [Tess-4.5-27B: Model/Core and Advanced Tool Use](#tess45-27b-r9700-hip-on-2026-11-17) | Q4_K_M · llama.cpp b11311 · AI PRO R9700 | NOT_ASSIGNED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/48d5e75b7a6e60e26900f2984fc15c54de109e49/models/tess-4.5-27b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-17 HUMAN_ACCEPTED independent sections; SCI-01 Q02 interpretation attributed separately</summary>

- Campaign: `tess45-27b-r9700-hip-on-2026-11-17`
- Export disposition: WEBSITE_READY; publication date 2026-11-17
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/5a8ecd7cafe5ff70c5f718620820d02f03be9ca5/models/tess-4.5-27b/events/tess45-27b-r9700-hip-on-2026-11-17/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-18
- Acceptance basis (as recorded): Owner accepted the original Model/Core and Advanced Tool Use findings for this tested profile, including negative and budget-limited outcomes. Advanced Tool Use passed all three native-tool simulator tasks. The baseline retained unsupported assertions about a helper and a startup record, and a budget-limited task. These findings do not establish autonomy. SCI-01 Q02 remains recorded FAIL; only the unchanged answer under the pinned source oracle replays as PASS. Original totals are retained. SCI-02 exact extraction is ambiguous; SCI-03 lexical checks do not establish broad semantic failures. Tested artifact, reasoning mode and bounded context only; no general readiness certification.
- Review source SHA-256: `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`

| Section | Manifest SHA-256 |
|---|---|
| advanced-tool-use | `ed19e38f8bb711261bdcdbf43ba0590e5fea2bd3b89c5747e8baa1c977ad7af6` |
| baseline | `ff99acf02512a66e884929573727f46dc4c9869411aaee7d529cd222fea1b778` |

- Artifact revision: e632461c0b8b835db69c7efc6aaac539f55b84de
- Artifact format: GGUF
- Runtime backend: HIP
- Export identity: event_date `2026-11-17`, event_id `tess45-27b-r9700-hip-on-2026-11-17`, event_type `welp-recharacterization`, model_id `tess-4.5-27b`, profile_id `tess-4.5-27b-r9700-hip-on-2026-11-17`
- Export source pin: repository-cache WumboLabs/evaluations @ `5a8ecd7cafe5ff70c5f718620820d02f03be9ca5` path models/tess-4.5-27b/events/tess45-27b-r9700-hip-on-2026-11-17/website-publication.json sha256 `dd7e6f2e422a6822aea13632880bd2304efe0de59a42b21a33fdee823f1f2eb6`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-18 UTC with private decision-source SHA-256 bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4. Original sections and outcomes retained; SCI-01 Q02 is an attributed interpretation, not a rescore. Event and registry pins remain distinct.</small></p>

</details>
