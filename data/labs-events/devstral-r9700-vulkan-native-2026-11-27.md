# Devstral Small 2 24B: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED scope: the Model/Core baseline (`model-baseline/2`) and the corrective Advanced Coding section (`coding-advanced/2`) of this event.** One tested configuration; not production readiness or unattended repository autonomy.

## Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **42 PASS, 19 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed; both Multi-Document checks failed. The configured 16,384-token serving capacity is not a validated useful-context default.

Recorded FAIL identities, retained unchanged: `Q12`, `coding-correction-01`, `context-multidocument-v2-6144-seed-42`, `context-multidocument-v2-8192-seed-42`, `git-amend`, `hall-fake-package`, `hall-git-timewarp`, `linux-diagnosis-stale-config-bind-failure`, `linux-diagnosis-startup-invalid-config`, `multi-turn-correction-01`, `reasoning-consistency-01`, `reasoning-correctness-01`, `strict-extract-09`, `strict-limit-05`, `structured-schema-01`, `structured-semantics-01`, `sycophancy-systemd`, `sycophancy-unknown`, `tool-selection-01`.

## Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS (`advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`), with offline replay verification reproducing all three outcomes under sandbox-executed frozen oracles. This is an independent corrective event against the corrected `/2` construct; it publishes no score for the deferred historical `/1` sections of other models.

## Blinded-review reconciliation: explicitly accepted and disclosed

The owner explicitly accepted the Devstral blinded-review reconciliation, SHA-256 `4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384`, and its disclosed limitation:

- The primary blinded review's delivery omitted the frozen Family A gate definitions for one context packet while assigning PASS. The sealed review and finalized section were not modified.
- A separate, fixture-complete blinded evaluation with all eleven qualification cases conformant independently supported the same PASS.
- It is external post-finalization verification, not an imported second framework review; the original packet hash does not cover the added gates, and the superseded response revisions are retained in the local scientific evidence.

A public-safe derivative of the reconciliation record is preserved beside the profile metadata under `supporting-evidence/`.

## Identity and deployment

- Event: `devstral-r9700-vulkan-native-2026-11-27`. Profile: `devstral-small-2-24b-instruct-2512-r9700-vulkan-not-configurable-2026-11-27`, revision `f34dc65c9f88202c071f14281591d4bee9f0dde74d52a9fbc85ad250480924ed`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/mistralai_Devstral-Small-2-24B-Instruct-2512-GGUF/tree/027695770ae1de77c2f6fb19f8e1ba9d65fcd15d): Q4_K_M, 14,334,438,272 bytes, SHA-256 `bfd11c8679c6b81eb43763505465d7dcfa72e460ab1c220ecc235a3efadd7f7f`. Upstream publisher identity `mistralai/Devstral-Small-2-24B-Instruct-2512` is EXTERNAL_REPORTED.
- AMD Radeon AI PRO R9700, Vulkan, llama.cpp `b12556-50518b64c6f2191a116d2760042f106c4b3387d7` (FlashAttention off), native non-configurable profile, temperature 0.15.
- **Deployment limitation:** the evaluated deployment served the artifact's embedded GGUF chat template, which differs from the current publisher-source template that injects a coding-agent system prompt. Findings apply to the artifact's embedded template as served.
- Accepted section manifests: baseline `cadbcefe4b353d6554e65b4e67dfb1358965f2d7510834f1a928a9e0e025f63e` (report `b0fda62a4c5416dba91b78777e6f9f709e9a212f500b84156eb607232c835ffc`); coding `1b32e8e98b669133fac339f5658bc1abc09af3cc184a98a7f4b4658eb32b5a74` (report `a84df4961a94ee4aa8af2981218587819a71b2ae2e32211323dc12fdebe86863`). Owner acceptance 2026-11-28 UTC.

The accompanying structured export, `website-publication.json`, retains every original baseline row including all FAILs, workload measurements, exact deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts.
