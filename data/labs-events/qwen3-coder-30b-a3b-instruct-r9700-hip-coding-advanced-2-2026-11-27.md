# Qwen3-Coder-30B-A3B-Instruct: corrective Advanced Coding

**HUMAN_ACCEPTED scope: the corrective Advanced Coding section (`coding-advanced/2`) only.** This is an independent corrective event, not a regrade. The historical `coding-advanced/1` section stays DEFERRED_BY_OWNER with its original outcomes and manifest provenance unchanged.

## Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS, with offline replay verification reproducing all three outcomes: `advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`. Sandbox-executed frozen oracles decide outcomes. The methodology-versioned `/2` construct corrects the defective `/1` multi-file repair task, whose published deferral reason (frozen task supplied an already-correct target) remains the record of the separate 2026-11-17 baseline event. This corrective section does not supersede that deferral and publishes no score for `/1`.

## Provenance reconciliation: explicitly accepted and disclosed

The owner explicitly accepted the Batch 04 provenance reconciliation, SHA-256 `da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138`, and its disclosed limitations:

- The sealed corrective profile inherited the historical Batch 03 source-inventory hash `8c916381dd5e1505023a00689698ed8a893fd4222ed6f2c802006718f59ff372` and the historical Batch 03 authorization wording. They are not the corrected `coding-advanced/2` source inventory and not the current assignment authorization.
- The corrected post-correction 189-entry source-and-fixtures inventory has SHA-256 `095a5138e667960fa472db4fb7a0317f6c5327ba80d97de5b93b3b26853f45eb`; a later check verified every listed file against it. That later check is not an execution-time hash measurement at each scored dispatch.
- No independently established execution-time source hash is claimed.

A public-safe derivative of the reconciliation record is preserved beside the profile metadata under `supporting-evidence/`; the original record remains in the local scientific evidence.

## Identity and deployment

- Event: `qwen3-coder-30b-a3b-instruct-r9700-hip-coding-advanced-2-2026-11-27`. Profile: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-27`, revision `ae81e97569c656645872679bcd29e923aeb3d4a55166b397c067efe38b157201`.
- Tested [GGUF artifact](https://huggingface.co/ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF/tree/ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3): Q4_K_M, 17,988,419,552 bytes, SHA-256 `f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335`.
- AMD Radeon AI PRO R9700, HIP, llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (FlashAttention off), native non-thinking profile with publisher-recommended non-thinking sampling (temperature 0.7, top-p 0.8, top-k 20). Context and performance findings apply only to the bounded workloads tested; the 16,384-token configured capacity is not a validated useful-context default.
- Accepted section manifest SHA-256 `2e15882ad9117d1b66cb29ae29eb51b9fdcdc38f0118f878516a7550e6773c98`; section report SHA-256 `9dc15c72d4bb682e7c6ecd5a7fc59e3c1c71e76388bfd69105a09d9dae0356fe`; owner acceptance 2026-11-28 UTC.

The accompanying structured export, `website-publication.json`, retains the exact unit outcomes, deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts. This result is bounded to the tested deployment; it is not a composite model score or a production-readiness claim.
