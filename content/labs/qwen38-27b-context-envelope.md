+++
title = "Qwen3.8-27B Lab Record"
description = "Model-card context envelope COMPLETE on the canonical ExLlamaV3 H1 surface: 65,536 default revalidated and 98,304 guarded boundary VALIDATED at >=99.4% near-full occupancy with strict useful-context 4/4; native 262,144 FIT_LIMIT on this 12 GB H1 surface (nearest measured boundary 98,304); official YaRN 1,000,000 INTEGRATION_BLOCKED on the accepted surface and independently FIT_LIMIT. Default unchanged at 65,536; inherited guarded/limited classification carries; LocalMaxxing VERIFIED_EXISTING, no new submission."
date = 2026-09-12
template = "lab_record.html"
weight = 13

[extra]
model = "Qwen3.8-27B"
producer = "Alibaba (Qwen team); EXL3 quant by turboderp"
quant = "2.20 bpw EXL3; q4 target KV; q4 draft KV; MTP width 1"
repo = "https://github.com/WumboLabs/eval-qwen3.8-27b"
status = "GUARDED / MODEL-CARD CONTEXT ENVELOPE COMPLETE"
hardware = "WumboJetsII (NVIDIA GeForce RTX 5070 12GB)"
headline = "Model-card context envelope COMPLETE on the canonical ExLlamaV3 H1 surface: 65,536 default revalidated and 98,304 guarded boundary VALIDATED at >=99.4% near-full occupancy with strict useful-context 4/4; native 262,144 FIT_LIMIT on this 12 GB H1 surface (nearest measured boundary 98,304); official YaRN 1,000,000 INTEGRATION_BLOCKED on the accepted surface and independently FIT_LIMIT. Default unchanged at 65,536; inherited guarded/limited classification carries; LocalMaxxing VERIFIED_EXISTING, no new submission."
evidence = "published"
+++

## Identity

| Field | Value |
|---|---|
| Model | Qwen3.8-27B |
| Producer | Alibaba (Qwen team); EXL3 quant by turboderp |
| Official model | Qwen/Qwen3.8-27B @ `card lastModified 2026-08-14 (native 262,144; YaRN factor 4.0 advertised to 1,000,000)` |
| Tested artifact | Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3) |
| Precision | 2.20 bpw EXL3; q4 target KV; q4 draft KV; MTP width 1 |
| Campaign | `qwen38-27b-rtx5070-context-completion-2026-09-12` |
| Record date | 2026-09-12 |

## Runtime and hardware

| Field | Value |
|---|---|
| Engine | ExLlamaV3 |
| Runtime version | 1.4.6+cu128.torch2.10.0 (torch 2.10.0+cu128, CUDA 12.8) |
| Runtime notes | Canonical H1 surface unchanged: MTP width 1, batch 1, max_chunk 256, recurrent history H1, CPU embedding lookup, all 64 transformer blocks GPU-resident; only serving context varies per arm |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Hardware notes | Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44; displays on iGPU |

## WELP outcome

- **Outcome:** PASS — QWEN38_27B_CONTEXT_ENVELOPE_COMPLETED
- **Classification:** MODEL-CARD CONTEXT ENVELOPE COMPLETE at the inherited guarded deployment classification; practical default unchanged

Publication state: **published** — canonical evidence: https://github.com/WumboLabs/eval-qwen3.8-27b

## Context profile

| Field | Value |
|---|---|
| Practical default | 65536 tokens |
| Guarded context | 98304 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT - exact native maximum 262,144 on the accepted H1 ExLlamaV3 surface: requires 12,530 MiB at ready (8,178 MiB context-independent + 262,144 x 17,408 B/token KV) versus 12,227 MiB total card VRAM; nearest measured boundary 98,304 VALIDATED. Official YaRN 1,000,000 extension INTEGRATION_BLOCKED on the accepted surface (runtime 1.4.6 has the YaRN implementation but exposes no supported activation without editing the protected artifact config) and independently FIT_LIMIT (cache alone ~16.6 GiB, ~1.36x total card VRAM) |

## Quality and capabilities

- **Constrained result:** useful-context strict aggregate 4/4 requests (2 rungs x 2 seeds) at >=99.4% occupancy: exact retrieval 5/5, synthesis, decoy resistance, absent-information grounding, instruction compliance all 4/4; measured depths 2/25/50/75/95% within +/-0.036 pp
- first near-full context evidence above 65,536 on the ExLlamaV3 2.20bpw Qwen3.8 surface
- frozen fit model validated at both measured rungs (conservative by 28-80 MiB)
- prefill degradation curve characterized: ~790 tok/s at 3.5K -> 606 at 64.7K -> 537 at 97.3K

### Guardrails and limitations

- retrieval-quality evidence is bounded to the tested fixture style and depths; it is not a general long-context quality claim
- reliability and role classification remain the inherited historical model-level findings; practical default unchanged
- the 98,304 operating point is guarded: ~181 s near-full TTFT and a ~300 MiB floor margin

**Reliability:** no CUDA/OOM/Xid events in the campaign; both arms torn down to verified idle; cold-cache enforced per request (verified cached_tokens 0 in all four retained terminal events)

## LocalMaxxing

| Field | Value |
|---|---|
| Status | SUBMITTED |
| Canonical context | 65536 tokens |
| tok/s out | 75.4 |
| TTFT | 71.35 ms |
| Submission reference | cmtwcncwr07f4ps01ef75q6ne |
| verifiedRun | NO |

<p><small>existing authorized submission on the identical canonical practical profile (VERIFIED_EXISTING); no new benchmark or submission in this campaign</small></p>

## Canonical evidence

Canonical public evidence: <https://github.com/WumboLabs/eval-qwen3.8-27b>

This Lab Record is a human-readable derivative of the accepted local WELP
campaign evidence named above; the campaign's REPORT.md is the authoritative
scientific source. Results are bounded by the tested artifact, runtime,
hardware, configuration, and protocol snapshot, and are not universal model
rankings.
