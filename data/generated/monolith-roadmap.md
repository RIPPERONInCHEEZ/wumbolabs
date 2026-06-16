## Monolith public roadmap

Monolith is a technical public alpha for local LLM workbench development, model testing, and practical evaluation on real hardware.

Current phase:

- `alpha v0.11.12` — repo-local bootstrap script and guided setup preparation
- clean-clone install validation
- setup diagnostics
- dependency and runtime detection
- safer model onboarding

Next milestone:

- `alpha v0.11.13` — guided setup wizard

Upcoming phases:

- guided first-run setup flow
- clearer llama.cpp/runtime detection
- safer model profile editing
- improved model onboarding
- stronger setup doctor output
- cleaner local evaluation workflow
- better comparison views for model runs and context tests

Future direction:

- eval scoring workflow
- comparison dashboard
- global search or command palette
- run notes and annotations
- agent-backend readiness dashboard
- workstation monitoring improvements
- future CLI/TUI companion

Current caveats:

- Monolith is a technical public alpha.
- Monolith is source-available; no open-source license has been selected yet.
- Setup is still manual, though repo-local bootstrap support is being added.
- llama.cpp is not bundled or installed automatically.
- GPU drivers, CUDA, ROCm, and system runtimes are not installed or modified by Monolith.
- There is no one-command installer yet.
- There is no production multi-user/auth deployment model yet.
