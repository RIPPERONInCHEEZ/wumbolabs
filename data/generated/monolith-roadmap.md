## Monolith public roadmap

Monolith is a technical public alpha for local LLM workbench development, model testing, and practical evaluation on real hardware.

Current release state:

- `alpha v0.11.10` — clean-clone install validation and release hardening
- `alpha v0.11.11` — setup doctor hardening and clearer dependency/runtime diagnostics
- `alpha v0.11.12` — repo-local bootstrap script and guided setup preparation
- `alpha v0.11.13` — guided setup wizard

Near-term direction:

- improve first-run setup and diagnostics
- make model onboarding clearer
- add safer model profile editing
- continue improving local evaluation workflows
- improve comparison views for model runs and context tests

Longer-term direction:

- eval scoring workflow
- comparison dashboard
- global search or command palette
- run notes and annotations
- agent-backend readiness dashboard
- future CLI/TUI companion

Current caveats:

- Monolith is a technical public alpha.
- Monolith is source-available; no open-source license has been selected yet.
- Setup is still manual, though repo-local bootstrap support is being added.
- llama.cpp is not bundled or installed automatically.
- GPU drivers, CUDA, ROCm, and system runtimes are not installed or modified by Monolith.
- There is no one-command installer yet.
- There is no production multi-user/auth deployment model yet.
