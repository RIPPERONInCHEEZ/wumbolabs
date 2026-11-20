+++
title = "Occamy-1.0"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 3

[extra]
kind = "model"
model_id = "occamy-1.0"
vendor = "Accio Lab"
findings_first = true
catalog_artifact = "GGUF · Q4_K_M"
catalog_profile_id = "occamy-1.0-r9700-hip-on-2026-11-17"
profile_count = 1
event_count = 1
latest_evidence_date = 2026-11-17
+++

## Overview

Accio Lab · 1 tested configuration · 1 evidence event · newest evidence 2026-11-17.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Latest evidence:** 2026-11-17: [event result](#occamy10-r9700-hip-on-2026-11-17)
- **2026-11-17** · Q4_K_M · llama.cpp b11311 · AI PRO R9700: classification NOT_ASSIGNED; See configuration-specific section findings; no composite model score; advanced-reasoning 3 units: 3 PASS (ADVANCE); baseline 61 units: 49 PASS, 12 FAIL; coverage failures retained: context 6 pass / 2 fail; instruction following 14 pass / 1 fail; reasoning 4 pass / 2 fail; reliability 14 pass / 6 fail; tool use 2 pass / 1 fail. [Event result](#occamy10-r9700-hip-on-2026-11-17)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="occamy10-r9700-hip-on-2026-11-17"></a>

### 2026-11-17: Occamy-1.0: Model/Core and Advanced Reasoning

**HUMAN_ACCEPTED independent sections; SCI-01 Q02 interpretation attributed separately** · config Q4_K_M · llama.cpp b11311 · AI PRO R9700 · maturity: CURRENT_WELP · status: NOT_ASSIGNED

Configuration: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, reasoning ON.

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/5a8ecd7cafe5ff70c5f718620820d02f03be9ca5/models/occamy-1.0/events/occamy10-r9700-hip-on-2026-11-17/REPORT.md)

#### Occamy-1.0: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Reasoning only. Event `occamy10-r9700-hip-on-2026-11-17`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

##### Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **47 PASS, 12 FAIL, 0 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five baseline coding probes and both structured-output tasks passed. Genuine negatives included a fabricated Git command, unsupported present-health inference, two Multi-Document failures and strict format failure after executed tool feedback. The original retained request strings were already NFC; this does not establish general Unicode tokenizer equivalence.

Six of eight bounded Practical Context checks passed; both Multi-Document checks failed. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `context-multidocument-v2-6144-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `context-multidocument-v2-8192-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-cuda` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-package` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-git-timewarp` | FAIL | Recorded frozen-check or rubric outcome. |
| `linux-diagnosis-stale-config-bind-failure` | FAIL | Recorded frozen-check or rubric outcome. |
| `linux-diagnosis-startup-invalid-config` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-limit-05` | FAIL | Recorded frozen-check or rubric outcome. |
| `tool-recovery-01` | FAIL | Recorded frozen-check or rubric outcome. |
| `uncertainty-file` | FAIL | Recorded frozen-check or rubric outcome. |

##### Advanced Reasoning (reasoning-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-constraints-01`, `advanced-evidence-01`, `advanced-revision-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

##### SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `5fcef1deb62a1f7d3c1b74aec6bdc3884a23312673cbe0f8e14302cba09a12ed`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.


The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.

##### Identity and deployment

- Profile: `occamy-1.0-r9700-hip-on-2026-11-17`, revision `8fe42148c60216898b68983dbd77167e0e2e907572a7d3d54eafbecf9d521198`.
- Tested artifact: [Accio-Lab/occamy-1.0-GGUF](https://huggingface.co/Accio-Lab/occamy-1.0-GGUF/tree/15027de49a5f8bbb5a131ed3fcfc1b54a543089d), GGUF Q4_K_M, 21,166,757,696 bytes; SHA-256 `ffb25f763ff9c27f5f4e2adcdef399c5654f9f840fdac33dffe7035ba8266a87`.
- Runtime: llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (HIP); tested GPU: AMD Radeon AI PRO R9700.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=1, top_k=20, top_p=0.95.
- Original manifest SHA-256: baseline `05ef081eed62e764b5934b64b7b0fc9df11916e32e2bbdd9dfab66341c0ce3f0`; advanced-reasoning `d78b52f56c64a97aa123a5891110b56230e5799fa75a2410f3f2389d2a6b4c48`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

<details class="lab-findings-provenance">
<summary>Raw section findings and provenance (JSON: outcomes, hashes, manifest and sampling conditions)</summary>

```json
{
  "profile_conditions": [
    {
      "artifact_sha256": "ffb25f763ff9c27f5f4e2adcdef399c5654f9f840fdac33dffe7035ba8266a87",
      "context_capacity": 16384,
      "framework": {
        "methodology": "model-baseline/2",
        "version": "welp/1.0.0-alpha-m2"
      },
      "profile_id": "occamy-1.0-r9700-hip-on-2026-11-17",
      "reasoning": {
        "arm": "ON",
        "controls": {
          "chat_template_kwargs": {
            "enable_thinking": true,
            "preserve_thinking": true
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
      "serve_model_id": "occamy-1.0-Q4_K_M",
      "template_sha256": "e84f32a23fdda27689f868aa4a1a5621f41133e51a48d7f3efcbea2839574259"
    }
  ],
  "sections": [
    {
      "advancement": {
        "decision": "ADVANCE"
      },
      "evidence_kind": "REAL_MODEL",
      "manifest_sha256": "d78b52f56c64a97aa123a5891110b56230e5799fa75a2410f3f2389d2a6b4c48",
      "methodology": "reasoning-advanced/1",
      "profile_id": "occamy-1.0-r9700-hip-on-2026-11-17",
      "profile_revision": "8fe42148c60216898b68983dbd77167e0e2e907572a7d3d54eafbecf9d521198",
      "report_sha256": "a73a5d35d24fb2820a34203a06fe2bd3299a2b61bd3c4b4c729091f4f8c56bf6",
      "section": "advanced-reasoning",
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
          "unit_id": "advanced-constraints-01"
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
          "unit_id": "advanced-evidence-01"
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
            "fail": 6,
            "indeterminate": 0,
            "measured": 20,
            "minimum_measurement_coverage_met": true,
            "minimum_scoring_coverage_met": true,
            "missing": [],
            "pass": 14,
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
      "manifest_sha256": "05ef081eed62e764b5934b64b7b0fc9df11916e32e2bbdd9dfab66341c0ce3f0",
      "memory": {
        "sampled_host_available_min_bytes": "UNKNOWN",
        "sampled_vram_used_max_bytes": 22488809472
      },
      "methodology": "model-baseline/2",
      "performance_observations": [
        {
          "elapsed_seconds": 1.8101336680001623,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.0813918429998921,
            "latency_seconds": 1.8101336680001623,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1727.988,
              "predicted_n": 156,
              "predicted_per_second": 89.69969698863649,
              "predicted_per_token_ms": 11.148309677419356,
              "prompt_ms": 79.557,
              "prompt_n": 29,
              "prompt_per_second": 364.5185213117639,
              "prompt_per_token_ms": 2.743344827586207
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 89.69969698863649,
              "prompt": 364.5185213117639
            },
            "ttft_seconds": 0.08145904100001644,
            "usage": {
              "completion_tokens": 156,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 185
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.7653532039998936,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.0701369989997147,
            "latency_seconds": 1.7653532039998936,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1694.467,
              "predicted_n": 156,
              "predicted_per_second": 91.47419217960574,
              "predicted_per_token_ms": 10.932045161290324,
              "prompt_ms": 67.786,
              "prompt_n": 29,
              "prompt_per_second": 427.8169533531998,
              "prompt_per_token_ms": 2.337448275862069
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 91.47419217960574,
              "prompt": 427.8169533531998
            },
            "ttft_seconds": 0.07017025199957061,
            "usage": {
              "completion_tokens": 156,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 185
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 1.7533891269999913,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 29
            },
            "first_byte_seconds": 0.059227497999927436,
            "latency_seconds": 1.7533891269999913,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 1693.362,
              "predicted_n": 156,
              "predicted_per_second": 91.5338834815001,
              "predicted_per_token_ms": 10.924916129032258,
              "prompt_ms": 57.337,
              "prompt_n": 29,
              "prompt_per_second": 505.78160699025057,
              "prompt_per_token_ms": 1.9771379310344828
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 91.5338834815001,
              "prompt": 505.78160699025057
            },
            "ttft_seconds": 0.05927810399998634,
            "usage": {
              "completion_tokens": 156,
              "prompt_tokens": 29,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 185
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-short"
        },
        {
          "elapsed_seconds": 6.170125054999971,
          "sample": 1,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 2.1448137239999596,
            "latency_seconds": 6.170125054999971,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 4023.726,
              "predicted_n": 336,
              "predicted_per_second": 83.25616605106809,
              "predicted_per_token_ms": 12.011122388059702,
              "prompt_ms": 2139.26,
              "prompt_n": 3629,
              "prompt_per_second": 1696.380991557828,
              "prompt_per_token_ms": 0.589490217690824
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 83.25616605106809,
              "prompt": 1696.380991557828
            },
            "ttft_seconds": 2.144880589999957,
            "usage": {
              "completion_tokens": 336,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3965
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 6.1684263300003295,
          "sample": 2,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 2.142784914999993,
            "latency_seconds": 6.1684263300003295,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 4023.826,
              "predicted_n": 336,
              "predicted_per_second": 83.25409697138991,
              "predicted_per_token_ms": 12.011420895522388,
              "prompt_ms": 2137.52,
              "prompt_n": 3629,
              "prompt_per_second": 1697.761892286388,
              "prompt_per_token_ms": 0.5890107467621934
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 83.25409697138991,
              "prompt": 1697.761892286388
            },
            "ttft_seconds": 2.14285068900017,
            "usage": {
              "completion_tokens": 336,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3965
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        },
        {
          "elapsed_seconds": 6.172489488000338,
          "sample": 3,
          "timings": {
            "cache_state": {
              "cache_n": 0,
              "prompt_n": 3629
            },
            "first_byte_seconds": 2.148189501000161,
            "latency_seconds": 6.172489488000338,
            "native_timings": {
              "cache_n": 0,
              "predicted_ms": 4022.676,
              "predicted_n": 336,
              "predicted_per_second": 83.27789759851403,
              "predicted_per_token_ms": 12.007988059701493,
              "prompt_ms": 2142.333,
              "prompt_n": 3629,
              "prompt_per_second": 1693.947672934133,
              "prompt_per_token_ms": 0.5903370074400661
            },
            "streaming": true,
            "tokens_per_second": {
              "generation": 83.27789759851403,
              "prompt": 1693.947672934133
            },
            "ttft_seconds": 2.1482620880001377,
            "usage": {
              "completion_tokens": 336,
              "prompt_tokens": 3629,
              "prompt_tokens_details": {
                "cached_tokens": 0
              },
              "total_tokens": 3965
            },
            "usage_source": "sse_usage_frame"
          },
          "unit_id": "perf-substantial"
        }
      ],
      "profile_id": "occamy-1.0-r9700-hip-on-2026-11-17",
      "profile_revision": "8fe42148c60216898b68983dbd77167e0e2e907572a7d3d54eafbecf9d521198",
      "report_sha256": "4fae58c96d0b29792d27bb182df32cc7beed5c46ecec115b38db3ced4a8c5781",
      "scoring_errata": {
        "Q02": {
          "attempt_id": "0001",
          "erratum_sha256": "5fcef1deb62a1f7d3c1b74aec6bdc3884a23312673cbe0f8e14302cba09a12ed",
          "finding_id": "SCI-01",
          "manifest_sha256": "05ef081eed62e764b5934b64b7b0fc9df11916e32e2bbdd9dfab66341c0ce3f0",
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

- Model and Agentic findings are independent. Source events: [2026-11-17](#occamy10-r9700-hip-on-2026-11-17).
- Performance is deployment-attributed, never model-quality credit. Source events: [2026-11-17](#occamy10-r9700-hip-on-2026-11-17).
- Missing metrics remain unknown; boundary memory samples are not true peaks. Source events: [2026-11-17](#occamy10-r9700-hip-on-2026-11-17).
- SCI-01 (baseline Q02): recorded FAIL used the wrong key order. The unchanged answer replays as PASS under the pinned source check. Section rows and totals remain as recorded. Source events: [2026-11-17](#occamy10-r9700-hip-on-2026-11-17).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| Q4_K_M · llama.cpp b11311 · AI PRO R9700 | GGUF · Q4_K_M | llama.cpp b11311 | AI PRO R9700 | reasoning ON · capacity 16,384 | 1 (2026-11-17) |

<details class="lab-findings-configs">
<summary>Configuration details: Q4_K_M · llama.cpp b11311 · AI PRO R9700</summary>

- Full profile name: Q4_K_M: llama.cpp / AMD Radeon AI PRO R9700 HIP, reasoning ON.
- Profile identity: `occamy-1.0-r9700-hip-on-2026-11-17`.
- Status: current tested surface; not the recommended profile.
- Deployment topology (as recorded): llama.cpp, HIP, AMD Radeon AI PRO R9700, native reasoning ON; configured 16384 tokens, not validation at full capacity. No serving recommendation assigned.
- Artifact (as recorded): Accio-Lab/occamy-1.0-GGUF; revision 15027de49a5f8bbb5a131ed3fcfc1b54a543089d; GGUF Q4_K_M; sha256 ffb25f763ff9c27f5f4e2adcdef399c5654f9f840fdac33dffe7035ba8266a87
- Artifact revision: 15027de49a5f8bbb5a131ed3fcfc1b54a543089d.
- Artifact format: GGUF.
- Runtime (as recorded): llama.cpp b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7.
- Hardware (as recorded): AMD Radeon AI PRO R9700.
- Sampling (as recorded): min_p 0.0, presence_penalty 0.0, repeat_penalty 1.0, seed 42, temperature 1.0, top_k 20, top_p 0.95.
- Reasoning arm: ON.
- Configured capacity: 16,384 tokens.
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/4f93731a9f042b9c1d86718a98a4e0e13d0fbd21/models/occamy-1.0/profiles/occamy-1.0-r9700-hip-on-2026-11-17/profile.json)

Events on this configuration:

- [Occamy-1.0: Model/Core and Advanced Reasoning (2026-11-17)](/evaluations/occamy-1-0#occamy10-r9700-hip-on-2026-11-17); status: NOT_ASSIGNED

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-11-17 | [Occamy-1.0: Model/Core and Advanced Reasoning](#occamy10-r9700-hip-on-2026-11-17) | Q4_K_M · llama.cpp b11311 · AI PRO R9700 | NOT_ASSIGNED |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/4f93731a9f042b9c1d86718a98a4e0e13d0fbd21/models/occamy-1.0)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-11-17 HUMAN_ACCEPTED independent sections; SCI-01 Q02 interpretation attributed separately</summary>

- Campaign: `occamy10-r9700-hip-on-2026-11-17`
- Export disposition: WEBSITE_READY; publication date 2026-11-17
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/5a8ecd7cafe5ff70c5f718620820d02f03be9ca5/models/occamy-1.0/events/occamy10-r9700-hip-on-2026-11-17/REPORT.md`
- Methodology snapshot: model-baseline/2
- Scientific acceptance: schema welp-scientific-acceptance/1, decision HUMAN_ACCEPTED, reviewed 2026-11-18
- Acceptance basis (as recorded): Owner accepted the original Model/Core and Advanced Reasoning findings for this tested profile, including genuine negative outcomes. Advanced Reasoning passed all three bounded tasks. Model/Core retained failures in strict answer formatting, present-health inference, bounded Multi-Document tasks and tool-recovery final formatting. The retained inputs were already NFC; this does not establish arbitrary Unicode tokenizer equivalence. SCI-01 Q02 remains recorded FAIL; only the unchanged answer under the pinned source oracle replays as PASS. Original totals are retained. SCI-02 exact extraction is ambiguous; SCI-03 lexical checks do not establish broad semantic failures. Tested artifact, reasoning mode and bounded context only; no general readiness certification.
- Review source SHA-256: `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`

| Section | Manifest SHA-256 |
|---|---|
| advanced-reasoning | `d78b52f56c64a97aa123a5891110b56230e5799fa75a2410f3f2389d2a6b4c48` |
| baseline | `05ef081eed62e764b5934b64b7b0fc9df11916e32e2bbdd9dfab66341c0ce3f0` |

- Artifact revision: 15027de49a5f8bbb5a131ed3fcfc1b54a543089d
- Artifact format: GGUF
- Runtime backend: HIP
- Export identity: event_date `2026-11-17`, event_id `occamy10-r9700-hip-on-2026-11-17`, event_type `welp-recharacterization`, model_id `occamy-1.0`, profile_id `occamy-1.0-r9700-hip-on-2026-11-17`
- Export source pin: repository-cache WumboLabs/evaluations @ `5a8ecd7cafe5ff70c5f718620820d02f03be9ca5` path models/occamy-1.0/events/occamy10-r9700-hip-on-2026-11-17/website-publication.json sha256 `0e96117c73f217a47299d97feb87804a8bcc96e5f2f297c27eb5f57e8130fad2`

<p><small>Publication provenance note (as recorded): Direct owner scientific acceptance 2026-11-18 UTC with private decision-source SHA-256 bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4. Original sections and outcomes retained; SCI-01 Q02 is an attributed interpretation, not a rescore. Event and registry pins remain distinct.</small></p>

</details>
