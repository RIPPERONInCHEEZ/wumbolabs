# AGENTS.md

This file is the canonical operating guide for AI coding agents working in the WumboLabs website repository.

It is tool-agnostic. Do not add assistant-specific configuration files, editor-specific agent files, or provider-specific workflow files unless explicitly requested.

## Project purpose

This repository powers the public WumboLabs website.

The site is the public proof layer for WumboLabs projects. It should communicate practical technical work clearly, conservatively, and with evidence tied to real artifacts, releases, tests, hardware, and documented project state.

Core brand line:

    Real Hardware. Real Testing. No Hype.

The site should stay static, reliable, readable, and easy to maintain.

## Brand and tone

Use language that is:

- practical
- technical
- clear
- conservative
- evidence-focused
- specific about hardware, runtime, versions, and artifacts when relevant

Avoid:

- hype language
- vague startup marketing language
- glossy generic AI branding
- unsupported benchmark claims
- universal model-ranking language
- claims that a model is "best" unless the claim is explicitly scoped and documented
- phrases such as "AI magic", "revolutionary", "leaderboard winner", or "production-ready" unless directly supported by project documentation

Prefer wording such as:

- local evidence
- validated artifacts
- manual scoring metadata
- consumer hardware
- reproducible workflow
- practical-output testing
- claim boundaries
- hardware-scoped result

## Content rules

Claims must be bounded and traceable to real artifacts, releases, tests, or documented project state.

When writing about model results, include the relevant boundary conditions:

- hardware
- GPU class
- runtime
- model/quantization
- context size
- suite or prompt set
- scoring status
- known limitations
- whether the result is a practical-output test, fit test, reasoning-mode test, or another specific lane

Do not imply cloud evaluation when the workflow is local.

Do not imply that LLMGauge downloads models, builds llama.cpp, or automatically judges model quality unless that behavior is explicitly documented in the LLMGauge project.

Do not call model results universal rankings.

Do not present manual scores as objective proof of model quality. Use "manual score metadata", "manual review score", or equivalent bounded language.

Do not publish private local paths, personal email addresses, unpublished internal notes, secrets, tokens, or raw private artifacts.

If local test results are used, summarize them with claim boundaries rather than dumping raw internal paths or logs.

## Technical change policy

Keep changes minimal and scoped.

Prefer static, deterministic content.

Do not introduce new frameworks, client-side fetches, analytics, package managers, dependencies, build steps, or dynamic behavior without explicit approval.

Do not restructure the site unless the task specifically asks for restructuring.

Preserve existing style, layout, templates, CSS conventions, and content structure unless the task is design-related.

Avoid speculative abstractions. Add the smallest useful structure that supports the current content.

Do not overbuild future reports, dashboards, feeds, data pipelines, or sync systems before the manual/static version is stable.

## Repository conventions

This is a Zola static site using Markdown content, templates, plain CSS, GitHub, and Cloudflare Pages.

Use repository files to confirm exact commands before inventing new ones. At the time this file was added, the documented local commands were:

    zola serve
    zola build

Generated output goes to:

    public/

Do not commit generated site output unless the repository already tracks it intentionally.

## LLMGauge website positioning

LLMGauge is the current flagship public project on the WumboLabs website.

Position LLMGauge as a local-first CLI/evidence tool for validating local LLM testing workflows on real consumer hardware.

LLMGauge can be described as running practical evaluation suites, preserving raw and cleaned outputs, tracking speed and VRAM, validating artifacts, supporting manual scoring, generating reports, and exporting machine-readable indexes.

Current public release context:

- LLMGauge v0.77 is the latest formal release, published to production PyPI as `llmgauge` 0.77.0.
- v0.74 established the ordinary-user PyPI distribution path; the canonical install is `uv tool install llmgauge`.
- v0.75 added named reasoning / sampling profiles (`--sampling-profile`, `llmgauge profiles list` / `profiles show`), requested `--min-p` capture, a derived peak-VRAM metric, and read-only Bundle 2 benchmark qualification. Vendor-aligned profile alignment is operator-declared, not vendor-endorsed.
- v0.76 added bounded structural comparison of multi-turn transcript runs (`llmgauge compare`) and content-default-deny public transcript derivatives (`llmgauge export-public-comparison`, `llmgauge export-public-transcript`). Comparison is structural evidence only: no aggregate score, ranking, winner, statistical claim, or semantic judgment, and every public derivative requires human review before publication.
- v0.77 is the Area 4 runtime-evidence stabilization release: opt-in vLLM streaming TTFT evidence (`--vllm-streaming-evidence`), vLLM request-wall-time and request-window peak-VRAM evidence, native llama.cpp timing and placement evidence, and cross-artifact evidence consistency and public-export privacy hardening. Streaming TTFT V1 is qualified for exactly vLLM 0.27.1, not a version range. The non-streaming default is unchanged. TTFT is omitted from v1 public exports. Matching metric IDs do not imply cross-runtime equivalence. Area 4 is not universally complete. The existing transcript comparison and public derivative features from v0.76 remain shipped current capabilities.
- Current testing emphasis is product validation.
- The key workflow is setup, dry run, real run, validation, scoring, report generation, and export-index generation.
- Model results are useful evidence, but LLMGauge should not be framed as a hype benchmark, leaderboard, automatic judge, or universal model-ranking system.

When updating LLMGauge content, prefer this workflow framing:

    Setup -> Dry Run -> Run Model -> Validate Artifacts -> Score Outputs -> Generate Report -> Export Index

When relevant, link to:

    https://github.com/WumboLabs/llmgauge

Keep examples short, copy-pasteable, and consistent with documented commands.

Place claim boundaries near model-result summaries, not only at the bottom of a page.

## Benchmark and report content

Benchmarks and reports should be evidence records, not leaderboard pages.

A good model-result writeup should answer:

- What was tested?
- Where was it tested?
- What hardware and runtime were used?
- Which LLMGauge version, suite, context, and settings were used?
- What artifacts were validated?
- What was scored, and how should the score be interpreted?
- What worked?
- What failed or looked weak?
- What claims are not supported by the result?

Avoid broad claims from a narrow test.

Use "full-GPU viable on this hardware" instead of "easy to run" when that is the actual evidence.

Use "practical-output rubric" instead of "full reasoning evaluation" when testing reasoning models in answer-only or practical-output mode.

## Roadmap and content sync policy

If the site consumes roadmap content from another WumboLabs project, prefer conservative source-of-truth workflows.

For the planned Monolith roadmap sync:

- Source of truth: Monolith repo docs/ROADMAP.md
- Website should consume only a clearly marked public block:
  - marker start: <!-- website-roadmap:start -->
  - marker end: <!-- website-roadmap:end -->
- Prefer static, deterministic sync.
- Do not fetch roadmap content from GitHub in the browser.
- Do not give the website write access to the Monolith repo.
- Prefer manual sync first.
- Add automation only after the manual workflow is stable and explicitly approved.

## Local preview and browser validation

Automated browser tools are not part of the default validation gate because the agent host may require repeated interactive approval for each browser action.

Default website validation should use repository-local commands and generated artifacts:

- run `zola build`
- inspect relevant generated files under `public/`
- inspect generated routes, links, headings, metadata, and redirect artifacts
- run repository-wide searches for stale links or paths
- run `git diff --check`
- inspect the complete final tracked diff

Do not repeatedly request approval for browser-tool actions.

Use `zola serve`, automated browser rendering, screenshots, viewport automation, or scripted interaction checks only when:

- the handoff explicitly requires browser validation; and
- the current session permission profile allows those actions without repeated approval.

If browser validation begins producing repeated approval prompts:

- stop using the browser tool for the milestone
- continue with repository-local and generated-output validation
- record browser validation as not performed
- state whether manual visual review is required
- do not treat the missing browser automation as a blocker unless the task depends on behavior that cannot be validated another way

For visual or responsive changes, the normal completion boundary is:

1. The agent implements the scoped change.
2. The agent runs non-browser validation.
3. The agent reports PASS or FAIL and states that manual visual review is required when applicable.
4. The human may run `zola serve` and inspect the result before staging or committing.

When local preview is explicitly authorized, the agent may:

- bind `zola serve` only to `127.0.0.1`
- use a non-production localhost port
- inspect only the site being developed
- write temporary preview output under `tmp/`
- terminate only processes started for the current milestone

The agent must not:

- bind preview services to a public or network-accessible interface
- access unrelated localhost services
- browse external websites without explicit authorization
- modify persistent browser profiles or personal browser data
- install browsers, packages, or system dependencies
- terminate unrelated processes
- leave preview servers or browser processes running after validation

## Testing and validation expectations

Before handing work back, run the appropriate local checks.

Do not invent commands. Inspect README, Makefile, package files, project docs, or existing scripts first.

For ordinary content/template changes, run:

    zola build

For local preview, use:

    zola serve

If the repository later adds formatters, linters, link checkers, or scripted validation commands, use those documented commands.

Report what was checked and what was not checked.

## Agent report expectations

For non-trivial audits, content passes, implementation passes, or review tasks,
write a structured report at `tmp/<milestone-name>/REPORT.md` before handing
work back. Do not use any other scratch directory for reports.

The report must be the agent's final file-writing action.

Include:

- verified starting branch and HEAD
- working branch
- task summary
- complete tracked diff scope
- files inspected
- files changed
- decisions made
- commands run
- actual validation results
- self-review findings and corrections
- assumptions
- intentionally deferred issues
- residual risks
- explicit PASS or FAIL
- exact recommended next action

Do not report PASS while an in-scope Critical, High, or Medium finding remains unresolved.

Reports must be specific enough for the user to compare the report against the complete Git diff and decide whether to keep, revise, or discard the changes.

The `tmp/` directory is untracked scratch space for local review and handoff.
Do not stage or commit files from `tmp/` unless explicitly instructed. The
final response ends with `REPORT: /absolute/path/to/REPORT.md`.

## Agent workflow and responsibility boundaries

Use one agent for each bounded milestone unless multi-agent work is explicitly requested.

At the start of each non-trivial task, provide a concise to-do list before performing the work. Use the environment's native task/todo mechanism when available; otherwise provide the list directly in the response. Keep it updated as work progresses and mark items complete as they are finished.

The agent may:

- verify the repository baseline
- create and switch to the named branch
- inspect the repository
- make scoped changes
- run local, non-destructive validation
- review and correct the complete final diff
- write the final review report

The human retains exclusive control over:

- staging
- commits
- merges
- branch deletion
- pushes
- tags
- releases
- history rewriting

The agent must not perform those human-controlled Git operations.

Before editing, verify the expected branch, HEAD, remote relationship, and working-tree state. Stop and report a material discrepancy instead of guessing.

Keep handoffs lean and milestone-specific. Stable repository policy belongs in this file. Task prompts should define the concrete outcome, essential context, hard constraints, validation, the exact absolute report path, and the exact next action.

Do not use subagents or multi-agent orchestration unless explicitly requested.

Do not use destructive Git commands.

Do not use network access, install dependencies, modify host or system configuration, write outside the repository, invoke external services, or run expensive workloads unless explicitly authorized.

## Git workflow expectations

Work on one bounded branch per milestone unless instructed otherwise.

Keep changes focused and avoid unrelated cleanup or refactoring.

Before handing work back:

- run `zola build`
- run `git diff --check`
- inspect the complete final tracked diff
- correct all in-scope findings
- write the required report under `tmp/<milestone-name>/REPORT.md`

Do not stage, commit, merge, delete branches, push, tag, publish, release, or rewrite history unless explicitly instructed.

## File and privacy rules

Public content must be safe to publish.

Do not expose:

- private local paths
- personal email addresses
- unpublished model results
- internal scratch notes
- secrets
- tokens
- private service URLs
- raw logs containing sensitive data

Local absolute paths may appear in private development notes, but public website content should usually summarize artifacts without publishing private machine-specific paths.

If a local path is necessary for a technical record, confirm that the user intentionally wants it public.

## Default behavior for agents

When unsure, choose the smaller change.

When a claim is not supported, either remove it or add the necessary boundary.

When content sounds like marketing, make it more specific.

When a result sounds like a ranking, scope it to the hardware, runtime, suite, and artifact set.

When a proposed change adds moving parts, prefer a static/manual version first.

When a task asks for one file, change one file.
