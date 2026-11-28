# Nanbeige4.2-3B: corrective Advanced Coding

**HUMAN_ACCEPTED scope: the corrective Advanced Coding section (`coding-advanced/2`) only.** This is an independent corrective event, not a regrade. The historical `coding-advanced/1` section stays DEFERRED_BY_OWNER; its original timeout remains a valid resource-limit observation, not a semantic failure.

## Corrective Advanced Coding (coding-advanced/2)

Three units, all PASS, with offline replay verification reproducing all three outcomes: `advanced-module-01`, `advanced-repair-supplied-01`, `advanced-repair-multi-01`. Sandbox-executed frozen oracles decide outcomes. The methodology-versioned `/2` construct corrects the defective `/1` multi-file repair task, whose published deferral reason (frozen task supplied an already-correct target) remains the record of the separate 2026-11-17 baseline event. This corrective section does not supersede that deferral and publishes no score for `/1`.

## Provenance reconciliation: explicitly accepted and disclosed

The owner explicitly accepted the Batch 04 provenance reconciliation, SHA-256 `da7e6ab7b983a0b02e9857d3ef3d293bed3ede92eb64e30c62450c1db158a138`, and its disclosed limitations:

- The sealed corrective profile inherited the historical Batch 03 source-inventory hash `8c916381dd5e1505023a00689698ed8a893fd4222ed6f2c802006718f59ff372` and the historical Batch 03 authorization wording. They are not the corrected `coding-advanced/2` source inventory and not the current assignment authorization.
- The corrected post-correction 189-entry source-and-fixtures inventory has SHA-256 `095a5138e667960fa472db4fb7a0317f6c5327ba80d97de5b93b3b26853f45eb`; a later check verified every listed file against it. That later check is not an execution-time hash measurement at each scored dispatch.
- No independently established execution-time source hash is claimed.

A public-safe derivative of the reconciliation record is preserved beside the profile metadata under `supporting-evidence/`; the original record remains in the local scientific evidence.

## Identity and deployment

- Event: `nanbeige42-3b-rtx5070-cuda-coding-advanced-2-2026-11-27`. Profile: `nanbeige4.2-3b-rtx5070-cuda-on-2026-11-27`, revision `bb68134687d9d49b2e31f3e89f107b36a95a987d3639f950dbbfb33da2f558d9`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/Nanbeige_Nanbeige4.2-3B-GGUF/tree/17562eefe9752007209148d5f7a6e275fc8d8077): Q8_0, 4,434,787,488 bytes, SHA-256 `837ba713ef3a3b5c9aee82e5dcba07600ea7db36ae392419f982b3bfaec04ef2`.
- NVIDIA GeForce RTX 5070, CUDA, llama.cpp `b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc`, native reasoning ON with preserved thinking and XML tool call format (temperature 0.6, top-p 0.95, top-k 20). Context and performance findings apply only to the bounded workloads tested; the 16,384-token configured capacity is not a validated useful-context default.
- Accepted section manifest SHA-256 `f708f688f5999d9e9cb79e79fdcf4fb7c882b19bfe99381efb7d2620e02af6b5`; section report SHA-256 `f6cd7563eaec628bc4e4d6ff13f9d37290a4f6ef9e9b80671b1f4f384ed995d1`; owner acceptance 2026-11-28 UTC.

The accompanying structured export, `website-publication.json`, retains the exact unit outcomes, deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts. This result is bounded to the tested deployment; it is not a composite model score or a production-readiness claim.
