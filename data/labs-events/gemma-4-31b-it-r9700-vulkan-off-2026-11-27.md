# Gemma 4 31B IT: Model/Core and corrective Advanced Coding

**HUMAN_ACCEPTED scope: the Model/Core baseline (`model-baseline/2`) and the corrective Advanced Coding section (`coding-advanced/2`) of this event.** One tested configuration; not production readiness.

## Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **49 PASS, 12 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed; both Multi-Document checks failed (requested values partly correct, but replies attributed the conflicting replica count to the wrong document). The configured 16,384-token serving capacity is not a validated useful-context default.

Recorded FAIL identities, retained unchanged: `context-multidocument-v2-6144-seed-42`, `context-multidocument-v2-8192-seed-42`, `evidence-xid`, `linux-diagnosis-stale-config-bind-failure`, `linux-diagnosis-startup-invalid-config`, `multi-turn-correction-01`, `strict-extract-09`, `strict-limit-05`, `structured-schema-01`, `structured-semantics-01`, `tool-recovery-01`, `tool-selection-01`.

## Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS (`advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`), with offline replay verification reproducing all three outcomes under sandbox-executed frozen oracles. This is an independent corrective event against the corrected `/2` construct; it publishes no score for the deferred historical `/1` sections of other models.

## Reconciliation and deployment scope

No campaign-specific reconciliation applies to this campaign. The two Batch 04 reconciliations explicitly accepted by the same owner decision concern the Qwen/Nanbeige provenance record (`da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138`) and the Devstral blinded-review record (`4e3715b1b5f508ab13b639923a6e916f7bca2a0760b3a77d12e9410a4d017384`); their limitations are disclosed on those events.

The deployment uses FlashAttention on, tied to this model's separately functionally admitted Vulkan deployment. That is a model-specific result, not a general FlashAttention kernel qualification, and must not be generalized.

## Identity and deployment

- Event: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27` (the `off` in the identifier refers to the native reasoning arm). Profile: `gemma-4-31b-it-r9700-vulkan-off-2026-11-27`, revision `a93702f29e52b6893d74743d337e4f9149eb4126e3f2b27845c760d16acb18b4`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/google_gemma-4-31B-it-GGUF/tree/619aca7589c72be65dd968de8602ad23d68b5c14): Q5_K_M, 22,608,877,920 bytes, SHA-256 `9f6882d4780880c96f2292c7daf5d5f18fa7e3678cecc47fc22649e93ce6f693`. Upstream `google/gemma-4-31B-it` revision `842da3794eaa0b77d5f08bae87a17459d91ff475` (EXTERNAL_REPORTED identity).
- AMD Radeon AI PRO R9700, Vulkan, llama.cpp `b12556-50518b64c6f2191a116d2760042f106c4b3387d7` (FlashAttention on, model-specific deployment), native reasoning arm OFF (thinking disabled), temperature 1.0, top-p 0.95, top-k 64.
- Accepted section manifests: baseline `e419e1d72fb23155885f295b0e57fad8b0f008661b8e24ea8f432f47dd3efc4f` (report `2784cd2fdd595f47bfca63b2867650be6b011050ffdfe89540c5c95fee8a95d9`); coding `e2b759e5d8d8cebc470969cbc44dba63b6c0b3e1ebd1b9db842e39373b46ad00` (report `2279a88bfcf68b8d40ff1e92f25bded18cbed9549509723dff4afd3a81e590cb`). Owner acceptance 2026-11-28 UTC.

The accompanying structured export, `website-publication.json`, retains every original baseline row including all FAILs, workload measurements, exact deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts.
