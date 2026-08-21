+++
title = "Qwen3.8-27B on 12GB: How Far Can an RTX 5070 Really Push It?"
description = "A complete Qwen3.8-27B campaign on WumboJetsII covering quant selection, context limits, templates, reasoning, speculative decoding, coding, reliability, and final readiness."
date = 2026-08-21
[extra]
record_type = "REPORT"
back_label = "Back to Lab Records"
back_url = "/records/"
+++

This completed local campaign tested Qwen3.8-27B on [WumboJetsII](/projects/wumbojetsii/). It is evidence from one consumer workstation and a frozen WumboLabs corpus—not a universal model ranking or accuracy claim.

<p class="kicker">2026-08-21 / QWEN3.8-27B LOCAL EVALUATION CAMPAIGN</p>

## Executive Summary

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Final model</span>
    <strong>UD-Q2_K_XL</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Template</span>
    <strong>FIXED v22.3</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Daily profile</span>
    <strong>16K / Q8-Q8</strong>
  </div>
  <div class="info-card">
    <span class="info-label">Final verdict</span>
    <strong>NOT READY AS DAILY DRIVER</strong>
  </div>
</div>

**Unsloth Qwen3.8-27B UD-Q2_K_XL** is an unusually capable 27B-class model for this RTX 5070 12GB configuration, especially for reviewed coding and bounded reasoning. The final reliability campaign nevertheless found too many hallucinations and strict-interface failures for unguarded daily use.

| Frozen component | Identity |
|---|---|
| Model | Unsloth Qwen3.8-27B UD-Q2_K_XL; revision `27af057ecb382ddfea5d12837360a8980560e3ed`; SHA-256 `fd4730dd8aad070517978752b63d530aeb1740d2283cab9fa24f1e404032ddb0` |
| Template | froggeric FIXED v22.3; revision `3be7669fac73085a458e20e81ee9dc5c322aefb2`; SHA-256 `6e1439c913ad7df4a966493ad70de7e7fc5a548d41bbe417c1571f766603629b` |
| Runtime | llama.cpp b10449; commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd` |

Headline evidence from this campaign:

- Executable coding: **28/30**; coding recovery: **36/40**.
- Hard reasoning: **9/10** with reasoning on versus **4/10** off.
- Strict interfaces: **197/250 (78.8%)** on the frozen bounded campaign.
- Primary reliability executions: **130/685 (19.0%)** classified as hallucinations.
- Full native-tool sequence: **5/50** satisfied the complete strict end-to-end contract.
- Fresh 64K bounded probes passed retrieval, synthesis, and instruction/code retention.
- Two-hour soak: **225/225** HTTP successes.

Those fractions describe the frozen WumboLabs corpus and its explicit contracts. They do not establish general model accuracy, a universal hallucination rate, or a universal model ranking.

## Test Platform

| Field | Campaign configuration |
|---|---|
| System | WumboJetsII; Fedora 44 / Hyprland daily desktop |
| GPU | NVIDIA GeForce RTX 5070 12GB; observed physical VRAM ~12,227 MiB |
| GPU power | 250 W stock reference limit |
| CPU / memory | AMD Ryzen 7 9800X3D / ~32GB DDR5 |
| Driver / CUDA | NVIDIA 610.57.04 / CUDA 13.3 |
| llama.cpp CUDA | SM120 / CUDA 13.3.73 |

The RTX 5070 also drove the Fedora/Hyprland desktop during testing. Practical free VRAM was therefore lower than raw physical capacity; this is representative workstation evidence, not benchmark isolation.

A historical Xid 109 existed before the final controlled campaigns. It remains unrelated and unattributed; it demonstrated that a reset could affect the display session. No new Xid or reset occurred during the final controlled campaign.

## Evaluation Policy

Primary candidates had to meet strict full-GPU admission: CUDA0, one active request, `parallel 1`, `fit off`, model/KV/recurrent Gated-DeltaNet state on GPU, no CPU model offload, no CPU KV, and Flash Attention where appropriate. Automatic fitting or CPU fallback did not count as successful admission.

The campaign froze 233 task definitions before bulk execution. It evaluated 1,228 task executions and 1,348 local chat-completion turns including recovery and tool follow-ups. Exact-output, JSON, required/forbidden-content, tool-structure, and disposable-sandbox execution checks were deterministic; manual review remained bounded and explicitly scoped.

## Package Showdown

The initial comparison included Unsloth Dynamic, AtomicChat, quimmedes XYZ, original/control variants, and later Empero Ridge work.

| Candidate | CUDA model buffer | Approx. free VRAM | Result |
|---|---:|---:|---|
| Unsloth UD-IQ2_XXS | 7,974 MiB | 2,539 MiB | PASS |
| Unsloth UD-IQ2_M | 9,228 MiB | 1,351 MiB | PASS |
| AtomicChat AD-IQ2_XXS | 7,628 MiB | 3,014 MiB | PASS |
| AtomicChat AD-IQ1_M | 7,171 MiB | 3,241 MiB | PASS |
| XYZ Q2 | 7,544 MiB | 3,035 MiB | PASS |
| XYZ Q3 | 9,721 MiB | 857 MiB | PASS, edge |
| XYZ Q1Q | 5,608 MiB | 5,037 MiB | functional failure |

XYZ Q1Q had substantial headroom but produced immediate EOG. XYZ Q1Z loaded and produced the expected admission phrase, then failed to terminate and was killed after timeout. Lower VRAM use did not imply better usability.

## First Winner

The initial completed package campaign selected **Unsloth UD-IQ2_M**, with a transparent weighted study score of 0.9264 versus XYZ Q3 at 0.7583 and AtomicChat AD-IQ2_XXS at 0.6606. Reviewed coding was 10/11, 8/11, and 7/11 respectively; the strict three-seed contract was 3/3, 2/3, and 0/3.

That was the evidence-backed initial winner. It was superseded after the finalized Dynamic V3 release was tested.

## Dynamic V3.0 Retest

The final V3 revision was pinned at `27af057ecb382ddfea5d12837360a8980560e3ed`; the old-preview control was `f1bfb127c64f7072bdd2cad55f258b9c8b2910fe`.

| Candidate | Campaign score |
|---|---:|
| UD-Q2_K_XL | **83.54** |
| Old preview UD-IQ2_M | 73.20 |
| UD-IQ2_XXS | 63.97 |
| UD-IQ2_S | 60.25 |
| UD-IQ3_XXS | 59.03 |
| UD-IQ1_M | 46.77 |
| UD-IQ1_S | 10.04 |

UD-IQ3_S was excluded after recurrent-state allocation failure under strict 16K full-GPU operation. The Q3_K_XL class was outside the practical 12GB envelope. The new 1-bit variants were useful for memory/context exploration, but the lowest-bit model was not the best practical model.

Q2_K_XL passed 5/6 strict Generic checks and 5/6 isolated coding tasks; the old preview passed 4/6 comparable coding tasks. Natural-text perplexity was 5.9108 for Q2_K_XL versus 6.0061 for preview; code perplexity was 1.8029 versus 1.7974. Perplexity alone did not predict practical coding performance in this campaign.

## KV Cache

The final winner preferred **Q8_0 / Q8_0** at daily 16K. Filled-retrieval headroom was approximately 1,877 MiB. Q4/Q4 saved only approximately another 256 MiB but repeatedly truncated the filled 16K retrieval contract; Q8/Q4 was pathologically slow.

That makes Q8/Q8 the normal daily choice. It does not make Q4/Q4 universally defective: Q4/Q4 remains appropriate for the reasoning, Fast/MTP, and reviewed 64K profiles below.

## Context

Context findings are distinct, not one maximum-context claim:

- **Daily context:** 16K / Q8-Q8.
- **Useful guarded final context:** Q2_K_XL showed bounded work at 65,536.
- **Final large-context profile:** 64K / Q4-Q4 / baseline decoding / reviewed work.
- **Early absolute retrieval edge:** UD-IQ2_XXS passed filled beginning/middle/end retrieval through 96K with Q4/Q4 GPU KV and Flash Attention; 96K measured ~616.6 prompt tok/s and ~27.7 generation tok/s. At 128K, CUDA could not allocate a ~538 MiB compute buffer. This was an early candidate's verified retrieval edge, not the final winner's daily recommendation.
- **Low-bit edge work:** IQ1_M retrieved exactly at ~196,608 and was memory-guarded around 163,840, but did not establish a complete useful retrieval/synthesis/instruction-retention rung. No candidate established native 262K as a useful full-GPU profile; 1M YaRN was physically impractical.

## Reasoning

Reasoning was tested, not enabled by default. On the fresh hard subset, reasoning on passed **9/10**, versus **4/10** for the matched reasoning-off control. Seven bounded reasoning probes were exact at explicit 2K, 4K, 8K, and 16K budgets; this suite showed no benefit beyond 2K.

Use the reasoning profile for difficult math, logic, code diagnosis, evidence synthesis, and constrained planning. Leave it off for ordinary factual questions, strict interfaces, native tools, and routine work.

Preserve-thinking did not improve the tested correction/recovery task. It increased generated tokens by about 22.3% with FIXED and 27.6% with SHARP; the recommendation is **off**.

## Template Showdown

At 16K Q8/Q8 non-thinking across three seeds:

| Template | Pass | Mean final tokens | Mean wall time | Mean generation |
|---|---:|---:|---:|---:|
| STOCK | 55/72 | 121.85 | 3.061 s | 43.51 tok/s |
| FIXED | 55/72 | 121.85 | 3.045 s | 43.87 tok/s |
| SHARP | 52/72 | 91.47 | 2.290 s | 43.41 tok/s |

**FIXED v22.3** matched STOCK on the bounded practical, coding, hallucination, strict-output, and uncertainty checks, improved native mock-tool discipline from 7/9 to 9/9, and retained 64K filled retrieval. It became the final template.

Top-level OpenAI-style `reasoning_effort=xhigh` was ignored. Steering had to pass through `chat_template_kwargs`; rendered steering was verified before reasoning comparisons.

### Sharp

SHARP shortened answers by approximately **24.9%**, but did not improve overall reliability. Practical passes were 7/15 for SHARP versus 9/15 for STOCK/FIXED; hallucination resistance was 7/15 versus 11/15. Reduced filler and answer tokens were reproduced; lower thinking/total cost was only partially reproduced. Improved practical accuracy and better coding were not reproduced; post-cutoff bug fixing was inconclusive. SHARP did not make the model smarter in this campaign.

## Speculative Decoding

Matched 8K Q4/Q4 FIXED evidence:

| Method | Generation | Result |
|---|---:|---|
| Baseline | 45.03 tok/s | reference |
| Native MTP, `nmax=1` | 66.13 tok/s | 1.469x speedup; ~75.1% acceptance |

Earlier optimization work found 22/24 byte-identical outputs. The fresh 50-task matched subset found the same quality classes for baseline and MTP—39 CLEAN_PASS, 7 MATERIAL_DEFECT, 3 HALLUCINATION, 1 STRUCTURAL_FAILURE—and 46/50 byte-identical outputs. Fresh mean generation was 45.10 versus 63.81 tok/s, or **1.41x**; headroom was 1,899 versus 1,353 MiB.

MTP is an optional fast 8K profile, not the daily default. The output mismatches require reviewed use and rule out a blanket equivalence claim. At 32K MTP started with ~141 MiB headroom and CUDA-OOMed during a filled ~31.7K prompt; 64K MTP was not attempted. N-gram speculation did not offer enough useful gain to recommend.

### DFlash2

DFlash2 required experimental llama.cpp support. The Q4_K_M draft loaded metadata through `llama-server --spec-type draft-dflash`, but at the common 8K Q4/Q4 rung CUDA could not allocate its ~1,079.61 MiB draft buffer. It was **physically untestable** under this target's strict 12GB all-GPU rule. No speed or quality comparison with MTP was possible.

## Vision

With a pinned F16 projector, bounded OCR, counting, and spatial-reasoning probes passed **3/3**. Peak VRAM was approximately 11,301 MiB with ~926 MiB headroom. Vision worked for this bounded test, but is an edge configuration on this 12GB card—not a comfortable default.

## Coding

Coding is the strongest supported domain. Fresh executable coding passed **28/30** in disposable sandboxes with no network, minimal devices, resource limits, and no host modification. The two failures were real execution failures.

Coding recovery passed **36/40** changed-constraint revisions. This supports Qwen3.8-27B UD-Q2_K_XL as a strong **reviewed** local coding assistant, not a hallucination-free coding system. Generated code still requires tests and review before host use.

## Reliability Reality Check

After the model, quant, template, and runtime were frozen, primary reliability statistics covered **685 evaluated task executions**. No MINOR_DEFECT responses were assigned.

| Classification | Count | Rate | 95% Wilson CI |
|---|---:|---:|---:|
| CLEAN_PASS | 414 | 60.4% | 56.7–64.0% |
| MATERIAL_DEFECT | 43 | 6.3% | 4.7–8.3% |
| HALLUCINATION | 130 | 19.0% | 16.2–22.1% |
| STRUCTURAL_FAILURE | 98 | 14.3% | 11.9–17.1% |
| UNSAFE_DEFECT | 0 | 0.0% | 0.0–0.6% |
| NONTERMINATING | 0 | 0.0% | 0.0–0.6% |

These are frozen WumboLabs corpus-classification rates under conservative literal contracts, not general Qwen3.8 statistics or a 60.4% accuracy claim.

False-premise resistance was the decisive readiness failure: hallucination-category runs were 67/150 CLEAN_PASS and 83/150 HALLUCINATION; sycophancy/false-premise runs were 28/75 CLEAN_PASS and 47/75 HALLUCINATION. Treat claims about packages, CLI flags, APIs, repository state, citations, hardware, and user-supplied technical assertions as untrusted until independently verified.

Other bounded slices were 15/20 factual CLEAN_PASS, 12/15 evidence discipline, 14/20 Linux, and 10/20 Git safety. The model often produced useful-looking answers while violating exact evidence or contract requirements.

## Strict Interfaces

The frozen strict campaign passed **197/250 (78.8%)** and failed **53/250 (21.2%)** across exact strings, JSON, extraction, enums, CSV, and word limits. Do not rely on one-shot strict responses; parse and mechanically validate structured output.

## Native Tools

Only **5/50** full native-tool sequences satisfied the complete frozen end-to-end contract. This is not generic “tool-call accuracy”: selection and argument structure performed better than the strict execution/recovery sequence. Tool workflows were not reliable enough for unattended use. Native tools require deterministic execution, schema validation, result validation, and external supervision.

## Long Context

Fresh baseline Q4 work passed bounded retrieval, synthesis, and instruction/code-retention probes at 16K, 32K, and 64K. The first filled 64K prompt contained approximately 64,275 tokens; first prefill took 91.24 s at 704.5 prompt tok/s, generation was 30.4 tok/s, and headroom was 663 MiB.

This demonstrates bounded 64K retrieval, contradiction-aware synthesis, instruction retention, and code-boundary reasoning on this configuration. It does not establish that arbitrary 64K workloads are reliable. 64K remains a low-headroom reviewed-work profile.

## Stability and GPU Safety

A two-hour balanced-profile soak completed **225/225** HTTP successes and **46/46** exact sentinels. Mean generation was 44.81 tok/s; first/last ten-request means were 44.89/44.59 tok/s. Mean latency was 2.06 s. VRAM started/ended/peaked at 10,340/10,248/10,342 MiB; peak soak temperature was 65 C.

Persistent `llama-server` use showed substantial host-RAM growth as prompt-cache state accumulated: RSS grew from about 1.4 GiB to 9.9 GiB. This is not a proven memory leak. VRAM remained stable and released normally after shutdown, but long-running deployments should monitor host RAM.

Twenty startup/shutdown cycles achieved **20/20** exact first requests and normally released VRAM to approximately 476 MiB. Shutdown was not perfectly graceful: the harness sometimes required a second interrupt or supervised process-tree termination.

Continuous telemetry captured 12,381 samples: maximum VRAM 11,148 MiB, minimum free 663 MiB, maximum temperature 74 C, and maximum power 234.32 W. No new Xid, reset-required state, GSP failure, channel/context-switch fault, unrecoverable CUDA event, or display-engine collapse appeared during the controlled final campaign.

## Recommended Profiles

| Profile | Configuration | Use boundary |
|---|---|---|
| Balanced assisted-use | UD-Q2_K_XL; FIXED v22.3; 16K Q8/Q8; Flash Attention; batch 256; ubatch 64; parallel 1; fit off; GPU model/KV/recurrent state; reasoning/preserve/speculation off; output cap 1024 | Reviewed coding, drafting, checked technical assistance |
| Maximum reliability | Same as Balanced | No separate safer bounded sampling profile was established |
| Coding | Same as Balanced | Tests and review are the guardrails |
| Reasoning | 32K Q4/Q4; FIXED; medium; explicit 2K budget; preserve off; official thinking sampling | Difficult bounded reasoning only |
| Fast | 8K Q4/Q4; FIXED; native MTP `nmax=1` | Optional, reviewed speed mode |
| Large context | 64K Q4/Q4; FIXED; baseline decoding | Low-headroom reviewed work only |

Balanced, maximum-reliability, and coding profiles used the campaign's official non-thinking Qwen sampling. They are assisted-use profiles, not autonomy profiles.

## Guardrails

1. Verify factual claims, citations, package names, CLI flags, APIs, and repository state.
2. Never infer tool execution, Git commit/push/merge, or a file's existence from model prose.
3. Mechanically validate strict and JSON output.
4. Test generated code before host use.
5. Native tools require deterministic execution plus schema and result validation.
6. Keep 64K for low-headroom reviewed work.
7. Treat MTP as optional speed mode.
8. Avoid concurrent heavy GPU workloads with edge profiles.

## Final Verdict

<div class="feature-card">
  <h3>NOT READY AS DAILY DRIVER</h3>
  <p>Qwen3.8-27B UD-Q2_K_XL is stable in the tested runtime, practically fast, unusually strong at coding, capable of useful bounded 64K context, and substantially improved by bounded reasoning on hard tasks.</p>
  <p>But the frozen primary reliability corpus classified 19.0% of executions as hallucinations; the frozen strict campaign had 21.2% failures; false-premise resistance was weak; and only 5/50 full native-tool sequences met the strict contract.</p>
</div>

**Recommended classification: Strong reviewed local coding/technical assistant.**

The evidence does not support use as an unattended agent, source of unverified technical facts, autonomous system administrator, autonomous Git operator, unsupervised native-tool agent, or fail-closed structured-output engine. It is not an unguarded daily assistant.

## Methodology and Limitations

This report combines the initial package showdown, finalized Dynamic V3 quantification retest, Sharp/DFlash optimization work, and final lock-in reliability campaign. Earlier evidence establishes candidate comparisons and selected configurations; the final lock-in supersedes earlier optimistic readiness language.

Results apply to the pinned artifacts, llama.cpp b10449 runtime, Fedora 44 workstation condition, RTX 5070 12GB configuration, stated contexts, and frozen WumboLabs probes. They do not establish producer accuracy claims, cloud behavior, broad hardware representativeness, or universal model quality. Manual and rule-based outcomes remain evidence metadata with stated boundaries, not objective proof of model quality.
