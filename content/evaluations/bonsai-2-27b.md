+++
title = "Ternary Bonsai 2 27B"
description = "Published evaluation evidence and testing history. Results remain attributed to their original configurations and methods."
template = "lab_model.html"
weight = 9

[extra]
kind = "model"
model_id = "bonsai-2-27b"
vendor = "PrismML"
findings_first = true
classification = "READY_WITH_GUARDRAILS"
recommended_profile_id = "bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off"
recommended_profile_name = "llama.cpp PTQ1_0 (thinking-off)"
practical_context = "32,768 default / 65,536 guarded tokens"
profile_count = 2
event_count = 2
latest_evidence_date = 2026-09-20
+++

## Overview

PrismML · 2 tested configurations · 2 evidence events · newest evidence 2026-09-20.

Contents: [Findings](#current-state) · [Event results](#testing-history) · [Limitations](#limitations) · [Tested configurations](#tested-profiles) · [Chronology](#chronology) · [Technical provenance](#canonical-evidence)

<a id="current-state"></a>

## Findings

Each finding is attributed to the event and tested configuration that measured it; exact values, failures and limitations are in the [event results](#testing-history). A historical event's recorded status describes that event's own sections at its date and is not a verdict on newer sections.

- **Model classification: READY_WITH_GUARDRAILS** - attributed to the [2026-09-20 event](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920), configuration PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs.
- **Recommended configuration:** llama.cpp PTQ1_0 (thinking-off) (current): [event result](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920).
- **Practical context:** 32,768 default / 65,536 guarded tokens; native model-card maximum 262,144 (envelope complete: YES); source: [event result](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920)
- **Context limit outcome:** FIT_LIMIT (unchanged); 65,536 serves at ~99.6% occupancy on this profile; 98,304+ exceeds card memory.; source: [event result](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920)
- **Latest evidence:** 2026-09-20: [event result](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920)
- **2026-09-20** · PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs: classification READY_WITH_GUARDRAILS; Semantic lane (ceiling 2048): 18/20 + 18/20 PASS (seeds 42/314159), completion 40/40, 0 truncation, 0 NOT_EVALUABLE, 0 UNSAFE. [Event result](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920)
- **2026-09-18** · PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K: classification NOT_READY; 12/12 frozen mechanical quality screen (temp 0). [Event result](#bonsai2-27b-rtx5070-welp-20260918)

<a id="testing-history"></a>

## Event results

Newest first. Each event is one independent testing/publication event with its full report linked once at the top of its section; scores, failures and limitations stay visible and raw section-provenance JSON stays collapsed.

<a id="bonsai2-27b-rtx5070-welp-methodology-supplement-20260920"></a>

### 2026-09-20: Methodology-revision supplement (thinking-off profile)

**WELP Methodology-Revision Supplement: PrismML PTQ1_0 (thinking-off)** · config PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs · maturity: CURRENT_WELP · status: READY_WITH_GUARDRAILS

Configuration: llama.cpp PTQ1_0 (thinking-off).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md)

#### WELP outcome

- **Outcome:** PASS - COMPLETE_PASS (bounded WELP methodology-revision supplement)
- **Classification:** READY_WITH_GUARDRAILS
- **Artifact classification:** current

Publication state: **published**; canonical evidence linked above

#### Quality and capabilities

- **Constrained result:** Semantic lane (ceiling 2048): 18/20 + 18/20 PASS (seeds 42/314159), completion 40/40, 0 truncation, 0 NOT_EVALUABLE, 0 UNSAFE
- hallucination 4/4 + 4/4; uncertainty 3/3 + 3/3; strict interfaces 2/3 + 2/3 (load-bearing: real exact-format defect caught both seeds); sycophancy 2/3 + 2/3
- profile-pure operational-ceiling audit (DERIVED, 0 new requests): completion 0.55/0.65 at legacy caps, EXHAUSTED_IN_ANSWER only - verbosity vs cap sizing, never reasoning starvation

##### Guardrails and limitations

- Pin enable_thinking=false (the only effective reasoning control on the pinned runtime) and size generation ceilings to the measured verbosity; legacy 20-140-token caps truncate 35-45% of tasks on answer length alone.
- BUDGET_DISCIPLINE POOR from this profile's own audit; READY_WITH_GUARDRAILS derived by the frozen harness (R-C5) via the declared non-starving 2048 lane (40/40 completion at 0.90 semantics).
- The reasoning-on profile keeps its historical NOT_READY and remains operationally budget-hostile (completion 1/20 at legacy caps); neither profile represents Bonsai 2 universally.

**Reliability:** WELP scorer v2 / gate_v2, frozen 20-task fixture v2, seeds 42 and 314159: 18/20 semantic each; four genuine semantic FAILs (strict-extract-09 x2, sycophancy-unknown, sycophancy-systemd); adaptive third seed not triggered.

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 59.22
- Submission reference: cmuajqjjd09y4lq01wrf8ht0j
- verifiedRun: NO
<p><small>Carried terminal disposition (no re-benchmark by design): the thinking-off delta changes declared reasoning state only, which is not a LocalMaxxing benchmark identity field. Owning record: the characterization event's campaign. verifiedRun=false recorded honestly.</small></p>

**Tested condition:** artifact PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · context 32,768 default / 65,536 guarded · native model-card maximum 262,144 tokens · envelope complete: YES.

**Context limit outcome:** FIT_LIMIT (unchanged); 65,536 serves at ~99.6% occupancy on this profile; 98,304+ exceeds card memory.

**Context boundaries:** Thinking-off profile: USEFUL_CONTEXT_MAX_SEMANTIC = USEFUL_CONTEXT_MAX_OPERATIONAL = 65,536 (VALIDATED 2/2 seeds; all six gates; the 512-token reserve is the rung output budget; finished stop at 40/512 tokens). The reasoning-on profile keeps 32,768 operational (its 65K run is 1/2 BUDGET_LIMITED; its 65K semantic lane was never measured). No retroactive improvement across profiles.

**Runtime conditions:** Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery)

**Hardware conditions:** full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off` |
| Model | Ternary Bonsai 2 27B (thinking-off) |
| Producer | PrismML |
| Official model | prism-ml/Ternary-Bonsai-2-27B-gguf @ `6ed5e12bf84b7a63069882c91dd9e9218647d17b` |
| Tested artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |
| Artifact SHA-256 | `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3` |
| Campaign | `bonsai-2-27b-welp-methodology-supplement-2026-09-20` |
| Record date | 2026-09-21 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT (unchanged); 65,536 serves at ~99.6% occupancy on this profile; 98,304+ exceeds card memory. |

<p><small>Thinking-off profile: USEFUL_CONTEXT_MAX_SEMANTIC = USEFUL_CONTEXT_MAX_OPERATIONAL = 65,536 (VALIDATED 2/2 seeds; all six gates; the 512-token reserve is the rung output budget; finished stop at 40/512 tokens). The reasoning-on profile keeps 32,768 operational (its 65K run is 1/2 BUDGET_LIMITED; its 65K semantic lane was never measured). No retroactive improvement across profiles.</small></p>

</details>

<a id="bonsai2-27b-rtx5070-welp-20260918"></a>

### 2026-09-18: Current-WELP characterization + compression-retention + RTX 2060 SUPER portability

**WELP Characterization: PrismML PTQ1_0 ternary (reasoning-on)** · config PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K · maturity: CURRENT_WELP · status: NOT_READY

Configuration: llama.cpp PTQ1_0 (reasoning-on, vendor default).

[Full report (REPORT.md)](https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md)

#### WELP outcome

- **Outcome:** PASS - characterization complete (verdict binds the reasoning-on profile)
- **Classification:** NOT_READY
- **Artifact classification:** historical

Publication state: **published**; canonical evidence linked above

#### Headline performance

| Surface | TTFT | Prefill | Decode |
|---|---|---|---|
| Short | 0.2787 s | Not recorded | not recorded |
| Moderate (3600-token input) | 6.366 s | 568.7 tok/s | not recorded |

<p><small>llama-bench canonical arm (5 reps), uncached; near-full prefill 575 to 520 tok/s (8K to 64K); full-occupancy decode 55 to 42 tok/s; prefill is the practical bottleneck on Blackwell for PTQ1_0.</small></p>

#### Quality and capabilities

- **Constrained result:** 12/12 frozen mechanical quality screen (temp 0)
- reasoning probe: PASS (syllogism, coherent answer)
- coding: budget-bound at canonical cap; thinking-off 400-cap PASS and 1500-cap thinking-on PASS (executable oracle 3/3)
- native tools: exact call + args + grounded continuation PASS
- structured interfaces: JSON object/array exact PASS

##### Guardrails and limitations

- Reliability 4/20 + 3/20 (seeds 42/314159) under default xhigh thinking; finish=length 19/20, 20/20 - budget exhaustion, not fabrication; 0 UNSAFE.
- Per-request reasoning budget/effort kwargs are ignored by the pinned runtime; only enable_thinking=false changes behavior.
- Never trust strict one-shot outputs or nonexistent-API/package/commit claims without verification.

**Reliability:** Frozen 20-task corpus, vendor-default thinking, seeds 42 and 314159: 4/20 and 3/20; failure mode replicated across five bounded re-configurations (budget-vs-reasoning interaction).

#### LocalMaxxing

- Status: SUBMITTED
- Canonical context: 32,768 tokens
- tok/s out: 59.22
- TTFT: 872.92 ms
- Submission reference: cmuajqjjd09y4lq01wrf8ht0j
- verifiedRun: NO
<p><small>Terminal closeout 2026-09-21 (origin NEW, APPROVED): the canonical llama-bench arm (pp512 586.54 / tg128 59.22 tok/s, 5 reps) submitted verbatim; duplicate audit NO_EXACT_MATCH (all pre-existing service entries are PQ2_0 on other hardware). verifiedRun=false recorded honestly: llama-bench local mode cannot supply prompt/output/engine-timing capture. TTFT is estimated from prefill.</small></p>

**Tested condition:** artifact PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · context 32,768 default / 65,536 guarded · native model-card maximum 262,144 tokens · envelope complete: YES.

**Context limit outcome:** FIT_LIMIT: f16 KV + weights exceed 12,227 MiB card memory at the exact native maximum (measured-anchored accounting; no launch). Official extension: none advertised (documented absence).

**Context boundaries:** USEFUL_CONTEXT_MAX = 32,768 on this profile (2/2 seeds). 65K useful-context FAILED 1/2 (frozen 512-token reserve exhausted in reasoning; correct facts visible in the trace; thinking-off diagnostic passed in 40 tokens). Capacity and retrieval were intact; the budget interaction was the blocker - precisely attributed by the follow-up event.

**Runtime conditions:** Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery)

**Hardware conditions:** full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time

<details class="lab-findings-configs">
<summary>Full tested identity, runtime and context details (exact hashes, versions and configuration)</summary>

#### Identity

| Field | Value |
|---|---|
| Profile identity | `bonsai2-27b-ptq1-0-prism-llamacpp` |
| Model | Ternary Bonsai 2 27B (reasoning-on) |
| Producer | PrismML |
| Official model | prism-ml/Ternary-Bonsai-2-27B-gguf @ `6ed5e12bf84b7a63069882c91dd9e9218647d17b` |
| Tested artifact | Ternary-Bonsai-2-27B-PTQ1_0.gguf; 5,946,648,928 bytes; SHA-256 verified exact official LFS identity |
| Precision | PTQ1_0 (1.75 bpw ternary group 128, Hadamard-rotated basis) |
| Artifact SHA-256 | `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3` |
| Campaign | `bonsai-2-27b-rtx5070-welp-characterization-2026-09-18` |
| Record date | 2026-09-21 |

#### Runtime and hardware

| Field | Value |
|---|---|
| Engine | llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120 |
| Hardware | WumboJetsII (NVIDIA GeForce RTX 5070 12GB) |
| Runtime notes | Stock llama.cpp never executed PTQ1_0 science; ENHANCED_SEMANTIC admission passed (fork-quant battery) |
| Hardware notes | full GPU residency (-ngl 99); f16 K/V; FA on; -np 1; one heavy CUDA workload at a time |

#### Context profile

| Field | Value |
|---|---|
| Practical default | 32768 tokens |
| Guarded context | 65536 tokens |
| Native model-card maximum | 262144 tokens |
| Model-card envelope complete | YES |
| Native maximum disposition | FIT_LIMIT: f16 KV + weights exceed 12,227 MiB card memory at the exact native maximum (measured-anchored accounting; no launch). Official extension: none advertised (documented absence). |

<p><small>USEFUL_CONTEXT_MAX = 32,768 on this profile (2/2 seeds). 65K useful-context FAILED 1/2 (frozen 512-token reserve exhausted in reasoning; correct facts visible in the trace; thinking-off diagnostic passed in 40 tokens). Capacity and retrieval were intact; the budget interaction was the blocker - precisely attributed by the follow-up event.</small></p>

</details>

## Limitations

- Pin enable_thinking=false (the only effective reasoning control on the pinned runtime) and size generation ceilings to the measured verbosity; legacy 20-140-token caps truncate 35-45% of tasks on answer length alone. Source events: [2026-09-20](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920).
- BUDGET_DISCIPLINE POOR from this profile's own audit; READY_WITH_GUARDRAILS derived by the frozen harness (R-C5) via the declared non-starving 2048 lane (40/40 completion at 0.90 semantics). Source events: [2026-09-20](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920).
- The reasoning-on profile keeps its historical NOT_READY and remains operationally budget-hostile (completion 1/20 at legacy caps); neither profile represents Bonsai 2 universally. Source events: [2026-09-20](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920).
- Reliability 4/20 + 3/20 (seeds 42/314159) under default xhigh thinking; finish=length 19/20, 20/20 - budget exhaustion, not fabrication; 0 UNSAFE. Source events: [2026-09-18](#bonsai2-27b-rtx5070-welp-20260918).
- Per-request reasoning budget/effort kwargs are ignored by the pinned runtime; only enable_thinking=false changes behavior. Source events: [2026-09-18](#bonsai2-27b-rtx5070-welp-20260918).
- Never trust strict one-shot outputs or nonexistent-API/package/commit claims without verification. Source events: [2026-09-18](#bonsai2-27b-rtx5070-welp-20260918).

<a id="tested-profiles"></a>

## Tested configurations

Exact profile identities, sampling conditions and provenance are in each configuration's details below.

| Configuration | Artifact / precision | Runtime | Hardware | Context / reasoning | Events |
|---|---|---|---|---|---|
| PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs | PTQ1_0 | llama.cpp (PrismML-Eng fork) | RTX 5070 | 32,768 default / 65,536 guarded | 1 (2026-09-20) |
| PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K | PTQ1_0 | llama.cpp (PrismML-Eng fork) | RTX 5070 | 32,768 default / 65,536 guarded | 1 (2026-09-18) |

<details class="lab-findings-configs">
<summary>Configuration details: PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs</summary>

- Full profile name: llama.cpp PTQ1_0 (thinking-off).
- Profile identity: `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`.
- Status: current canonical/recommended tested surface.
- Deployment topology (as recorded): Identical serving geometry to the reasoning-on profile (-ngl 99 full GPU, -fa on, f16 KV, -np 1, vendor instruct sampler) with the single declared delta: reasoning OFF via chat_template_kwargs enable_thinking=false - the only reasoning control proven effective on the pinned runtime. Recommended bounded deployment profile (READY_WITH_GUARDRAILS): pin enable_thinking=false and size generation ceilings to the profile's measured verbosity; verify strict one-shot outputs.
- Artifact (as recorded): prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)
- Runtime (as recorded): llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off/profile.json)

Events on this configuration:

- [Methodology-revision supplement (thinking-off profile) (2026-09-20)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920); status: READY_WITH_GUARDRAILS

</details>

<details class="lab-findings-configs">
<summary>Configuration details: PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K</summary>

- Full profile name: llama.cpp PTQ1_0 (reasoning-on, vendor default).
- Profile identity: `bonsai2-27b-ptq1-0-prism-llamacpp`.
- Status: historical tested surface; retained evidence, not the recommended profile.
- Deployment topology (as recorded): Full-GPU PrismML-Eng/llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99, -fa on, f16 KV, -np 1, vendor instruct sampler; REASONING_ON vendor xhigh default (the pinned runtime ignores per-request reasoning budget/effort kwargs; template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K.
- Artifact (as recorded): prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)
- Runtime (as recorded): llama.cpp (PrismML-Eng fork) 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120.
- Hardware (as recorded): WumboJetsII (NVIDIA GeForce RTX 5070 12GB).
- [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/87ab638502d63eea47a5f8734eed729b39e3042c/models/bonsai-2-27b/profiles/bonsai2-27b-ptq1-0-prism-llamacpp/profile.json)

Events on this configuration:

- [Current-WELP characterization + compression-retention + RTX 2060 SUPER portability (2026-09-18)](/evaluations/bonsai-2-27b#bonsai2-27b-rtx5070-welp-20260918); status: NOT_READY

</details>

## Chronology

Compact index; full results are in [Event results](#testing-history).

| Date | Event | Configuration | Status |
|---|---|---|---|
| 2026-09-20 | [Methodology-revision supplement (thinking-off profile)](#bonsai2-27b-rtx5070-welp-methodology-supplement-20260920) | PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · verify strict one-shot outputs | READY_WITH_GUARDRAILS |
| 2026-09-18 | [Current-WELP characterization + compression-retention + RTX 2060 SUPER portability](#bonsai2-27b-rtx5070-welp-20260918) | PTQ1_0 · llama.cpp (PrismML-Eng fork) · RTX 5070 · template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K | NOT_READY |

<a id="canonical-evidence"></a>

## Technical provenance

Publication, acceptance and source-pin provenance for each event, collapsed; the scientific content above never depends on it.

[Model evidence tree (GitHub)](https://github.com/WumboLabs/evaluations/tree/87ab638502d63eea47a5f8734eed729b39e3042c/models/bonsai-2-27b)

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-20 WELP Methodology-Revision Supplement: PrismML PTQ1_0 (thinking-off)</summary>

- Campaign: `bonsai-2-27b-welp-methodology-supplement-2026-09-20`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-21
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md`
- Export identity: event_id `bonsai2-27b-rtx5070-welp-methodology-supplement-20260920`, event_type `follow-up`, model_id `bonsai-2-27b`, profile_id `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`
- Export source pin: repository-cache WumboLabs/evaluations @ `ea0bfa374bc22787357615d4fc2b8ff6883bccd7` path models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/website-publication.json sha256 `4a5c4013173c00d2ef74378279b187ef3876f6ca3a6550a6d73c981284a8d715`

<p><small>Publication provenance note (as recorded): Native event under WELP snapshot welp-next-snapshot-2026-09-19-methodology-revision, DRAFT - NOT v1.0, public WELP commit 79f9de13de04325e50e05b0eed28b56471a19028. Correction chronology represented: the same-day human-gate pass diagnosed (A) a prose-only aggregate transcription error (raw outcomes were always 36 PASS / 4 FAIL / 0 NOT_EVALUABLE, 40/40 COMPLETE) and (B) CASE 1 campaign/report invocation misuse - the reasoning-on Lane B completion had been fed to this profile's BUDGET_DISCIPLINE; no WELP protocol defect; classification recomputed profile-pure by the frozen harness with 0 additional inference requests. Prior event unchanged. LocalMaxxing: the canonical practical profile's measured arm (unchanged by the reasoning-state delta) is SUBMITTED via the prior event's record.</small></p>

</details>

<details class="lab-findings-provenance">
<summary>Event provenance: 2026-09-18 WELP Characterization: PrismML PTQ1_0 ternary (reasoning-on)</summary>

- Campaign: `bonsai-2-27b-rtx5070-welp-characterization-2026-09-18`
- Export disposition: WEBSITE_PUBLISHED; publication date 2026-09-21
- Canonical citation (immutable commit/path pin): `https://github.com/WumboLabs/evaluations/blob/190498671d69583af3202c7f4860531f24c5960c/models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md`
- Export identity: event_id `bonsai2-27b-rtx5070-welp-20260918`, event_type `initial-evaluation`, model_id `bonsai-2-27b`, profile_id `bonsai2-27b-ptq1-0-prism-llamacpp`
- Export source pin: repository-cache WumboLabs/evaluations @ `ea0bfa374bc22787357615d4fc2b8ff6883bccd7` path models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/website-publication.json sha256 `1de9cc7c066e4b9743cfd0310c5b2c894bb4254ca1b0d786e46809f36037f740`

<p><small>Publication provenance note (as recorded): Native current-WELP event under the consolidated architecture; no eval-* repository. Campaign snapshot welp-next-snapshot-2026-09-18-bonsai-2-27b-rtx5070-welp-characterization (WELP 9e3f0afbdfb767148f1612e307bb0150dbe23302). The methodology-revision supplement (separate event) later re-scoped this profile's 64K useful-context failure to reasoning starvation and added the thinking-off profile; this event's verdict and bytes are unchanged. LocalMaxxing terminal disposition recorded 2026-09-21: SUBMITTED origin NEW, id cmuajqjjd09y4lq01wrf8ht0j, APPROVED, verifiedRun false (honest; llama-bench local mode cannot supply prompt/output/engine-timing capture).</small></p>

</details>
