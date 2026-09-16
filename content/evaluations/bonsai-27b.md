+++
title = "Bonsai 27B (Q1_0)"
description = "Bonsai 27B (Q1_0) — the current WumboLabs evidence state on one page: tested profiles, validated context, and the full chronological testing history. Each value is attributed to the profile and event that measured it."
template = "lab_model.html"
weight = 21

[extra]
kind = "model"
model_id = "bonsai-27b"
vendor = "Upstream identity unresolved (local artifact name)"
recommended_profile_id = "bonsai-27b-q1-0-llamacpp"
recommended_profile_name = "llama.cpp Q1_0 (unscored smoke payload)"
profile_count = 1
event_count = 1
latest_event_date = 2026-07-14
+++

WumboLabs tests **Bonsai 27B (Q1_0)** on real consumer hardware. This is the canonical model page: current state first, then every tested profile and every evidence event. Values are attributed to the profile and event that measured them; historical findings remain the evidence of their tested stack and are never silently replaced.

## Current state

- **Recommended profile:** llama.cpp Q1_0 (unscored smoke payload) (`bonsai-27b-q1-0-llamacpp`, specialized) — [canonical evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/bonsai-27b/events/bonsai-27b-smoke-v070-2026-07-14/REPORT.md)
- **Latest evidence:** 2026-07-14 — LLMGauge v0.70 smoke runs (Q1_0 payload, unscored)

## Tested profiles

### llama.cpp Q1_0 (unscored smoke payload) — SPECIALIZED

Profile identity: `bonsai-27b-q1-0-llamacpp`.

Runtime and artifact identity are described inside the event sections below (hand-authored records; no machine-readable export).

Status: specialized tested surface.

[Canonical Evidence](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/bonsai-27b/events/bonsai-27b-smoke-v070-2026-07-14/REPORT.md)
[Profile Metadata](https://github.com/WumboLabs/evaluations/blob/ce3e10ee38bfc19fdc0b78c5648c6e7add5cff4b/models/bonsai-27b/profiles/bonsai-27b-q1-0-llamacpp/profile.json)

Events on this profile:

- [LLMGauge v0.70 smoke runs (Q1_0 payload, unscored) (2026-07-14)](/evaluations/bonsai-27b#bonsai-27b-smoke-v070-2026-07-14) — SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED

## Testing history

Newest first. Each event is one immutable testing/publication event; the exact scientific report lives in the canonical evidence repository linked at the top of each event.

<a id="bonsai-27b-smoke-v070-2026-07-14"></a>

### 2026-07-14 — LLMGauge v0.70 smoke runs (Q1_0 payload, unscored)

**Specialized Test — unscored smoke** · profile: llama.cpp Q1_0 (unscored smoke payload) · maturity: UNRESOLVED_HISTORICAL · status: SPECIALIZED_TEST / UNSCORED_SMOKE / IDENTITY_UNRESOLVED

[Canonical Evidence / Full Report](https://github.com/WumboLabs/evaluations/blob/479cb50c197f8ea0dd905a68ffd61f632f49c652/models/bonsai-27b/events/bonsai-27b-smoke-v070-2026-07-14/REPORT.md)
[View on GitHub](https://github.com/WumboLabs/evaluations/tree/ce3e10ee38bfc19fdc0b78c5648c6e7add5cff4b/models/bonsai-27b)

### Identity and scope

- Profile: `bonsai-27b-q1-0-llamacpp` — llama.cpp Q1_0 (unscored smoke payload)
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized
- Hardware: WumboJetsII (RTX 5070 12GB)

Three completed 1-prompt unscored smoke runs (JSON-discipline, honesty, fake-field) under LLMGauge v0.70 with a Q1_0 27B artifact locally labeled bonsai_27b_q1_0. Upstream artifact identity unresolved (model paths redacted in v0.70+ provenance); archaeology preserves a 3,803,452,480-byte fingerprint. Not a quality verdict.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.
### Identity caveat

The exact upstream artifact identity cannot be proven from retained evidence: LLMGauge
v0.70+ provenance redacts model paths, and only the local artifact name `bonsai_27b_q1_0`
plus a 3,803,452,480-byte fingerprint survive. No canonical profile repository is claimed
for this event until the upstream identity is established. The runs are unscored smokes;
no quality claim is made.

## Canonical evidence

All canonical public evidence lives in WumboLabs/evaluations. Each event links an immutable full-commit/path citation; each profile remains a distinct scientific identity, not a separate repository.

- **bonsai-27b-q1-0-llamacpp**: [Profile Metadata](https://github.com/WumboLabs/evaluations/blob/ce3e10ee38bfc19fdc0b78c5648c6e7add5cff4b/models/bonsai-27b/profiles/bonsai-27b-q1-0-llamacpp/profile.json)

### Legacy provenance

- [RIPPERONInCHEEZ/wumbolabs @ `e27ddcb89b56c27e87d7a3af34003cd8c6d7355b`](https://github.com/RIPPERONInCHEEZ/wumbolabs/blob/e27ddcb89b56c27e87d7a3af34003cd8c6d7355b/data/labs-events/bonsai-27b-smoke-v070-2026-07-14.md)
