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

Current public release context at the time this file was added:

- LLMGauge v0.65 added guided setup and first-run onboarding.
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

For non-trivial audits, content passes, implementation passes, or review tasks, write a structured report into the repository-local `temp/` directory before handing work back.

Use a clear filename such as:

    temp/agent-report-YYYY-MM-DD-short-topic.md
    temp/repo-audit-YYYY-MM-DD.md
    temp/content-pass-YYYY-MM-DD-short-topic.md

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

The `temp/` directory is scratch space for local review and handoff. Do not stage or commit files from `temp/` unless explicitly instructed.

Reports must be specific enough for the user to compare the report against the complete Git diff and decide whether to keep, revise, or discard the changes.

## Agent workflow and responsibility boundaries

Use one agent for each bounded milestone unless multi-agent work is explicitly requested.

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

Keep handoffs lean and milestone-specific. Stable repository policy belongs in this file. Task prompts should define the concrete outcome, essential context, hard constraints, validation, report path, and exact next action.

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
- write the required report under `temp/`

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
