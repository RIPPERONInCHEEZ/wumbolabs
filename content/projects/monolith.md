+++
title = "Monolith"
description = "A local LLM workbench for model testing, evaluation, and comparison."
weight = 1
+++

Monolith is a local LLM web UI and testbench project focused on practical model evaluation.

It is designed to help manage local model profiles, prompt suites, evaluation runs, imported results, benchmark visibility, and future context-scaling workflows.

The goal is not to chase hype.

The goal is to identify what is actually useful on consumer hardware.

## Focus Areas

- local model profile management
- controlled prompt-suite execution
- Quant Lab integration
- SQLite-backed result storage
- raw output preservation
- benchmark visibility
- context-scaling experiments
- model comparison workflows

## Design Principles

Monolith is intended to remain controlled, bounded, visible, and reversible.

It avoids arbitrary shell execution, arbitrary model paths from the UI, arbitrary prompt roots, and unsafe automation.
