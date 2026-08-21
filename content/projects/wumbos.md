+++
title = "wumbOS"
description = "A developing Linux desktop environment centered on Hyprland, Quickshell, and local-first Agent integration."
template = "project.html"
weight = 2
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
portfolio_status = "MAIN FOCUS · ACTIVE DEVELOPMENT"
release_status = "PUBLIC BASELINE · Alpha.2 · current prealpha in development"
wumbos = true
+++

<strong>MAIN FOCUS / ACTIVE DEVELOPMENT</strong>

wumbOS is a developing Linux desktop environment / desktop shell centered on Hyprland, Quickshell, a cohesive WumboLabs desktop experience, local-first Agent integration, and practical workstation use. It integrates proven Linux components rather than replacing them first. It is not a complete operating system, installer, or separately distributable OS today.

The website distinguishes the **public baseline** from **current prealpha development**. Public Alpha.2 is the installable shell release. Current prealpha work is active and has not shipped as a public release.

<div class="wumbos-cta-row">
  <a class="wumbos-cta" href="https://github.com/WumboLabs/wumbo-quickshell">View wumbOS Shell on GitHub</a>
  <a class="wumbos-cta wumbos-cta--secondary" href="https://github.com/WumboLabs/wumbo-quickshell/releases/tag/v0.1.0-alpha.2">Read the Alpha.2 Release</a>
</div>

## Current Status

<div class="info-grid wumbos-status-grid">
  <div class="info-card"><span class="info-label">Public baseline</span><strong>Alpha.2</strong></div>
  <div class="info-card"><span class="info-label">Public tag</span><strong>v0.1.0-alpha.2</strong></div>
  <div class="info-card"><span class="info-label">Current work</span><strong>Prealpha / in development</strong></div>
  <div class="info-card"><span class="info-label">License</span><strong>MPL-2.0</strong></div>
  <div class="info-card"><span class="info-label">Tested OS</span><strong>Fedora 44</strong></div>
  <div class="info-card"><span class="info-label">Required compositor</span><strong>Hyprland</strong></div>
</div>

Alpha.2 is a functional desktop shell, not a mockup. It was tested with **Hyprland 0.56.2**, **Quickshell 0.3.0**, Qt 6, PipeWire/WirePlumber, NetworkManager, and systemd/logind. Hyprland is required. These are tested versions, not minimum-version promises.

Current prealpha work continues on the same Fedora 44 / Hyprland workstation stack. Prealpha Agent, Control Panel, and visual work is not part of the published Alpha.2 baseline unless a later public release says so.

## Shell-First Desktop

wumbOS Shell keeps persistent chrome compact: a top bar is created dynamically for each connected display. It presents workspaces, active-window state, date and weather, Attention and Agent status, audio, networking and DNS information, system status, GPU information, tray, power/session controls, launcher, and clipboard access. Related details live in coordinated contextual popups rather than becoming permanent bar modules.

Multi-monitor behavior is deliberate: bars follow connected displays without hard-coded connector names, and popup ownership follows the target monitor. Multi-monitor operation was live-tested. Single-monitor operation is structurally supported but has not received equivalent live qualification.

## Sandstone Night

The canonical **current** visual direction is **Sandstone Night**. It supersedes the earlier Copper Bench / dual-theme experiment.

Current prealpha visual work includes a unified Sandstone Night shell palette across top bars, popups, Control Panel, Hyprland integration, lock screen, terminal/tooling integration, GTK applications, wallpaper treatment, and broader workstation visual consistency.

Sandstone Night is current prealpha direction. It is not claimed as part of public Alpha.2. The published Alpha.2 shell still used the earlier Copper Bench look.

## Control Panel

The earlier System Monitor popup has evolved into **Control Panel**.

In current prealpha work, Control Panel is becoming the broader native wumbOS status and configuration surface. That evolution is in development. It does not mean every planned Control Panel capability exists today.

## Agent-Aware Workstation

Agent activity is treated as workstation state rather than chatbot branding.

The established public integration remains optional **OMP**, tested with **OMP 17.2.11**. It reads structured Agent state and can represent running, tool activity, waiting, blocked, completed, failed, and idle states when the harness supplies them. OMP does not reliably expose every ordinary human-question waiting transition, so the shell does not invent one from timers, CPU use, unread state, or Attention.

Current prealpha work is developing a shared Agent layer that can represent multiple local coding/AI harnesses through one desktop-native status and Attention system. That foundation is unreleased. It is not part of public Alpha.2.

<div class="wumbos-architecture" aria-label="Planned Agent abstraction">
  <div>Agent UI</div><span>↓</span><div>Shared Agent layer <em>PREALPHA</em></div><span>↓</span><div>OMP Adapter &nbsp;|&nbsp; Research / future adapters</div>
</div>

### OMP

OMP remains the established Agent integration. Truthful missing state is better than heuristic confidence. No additional OMP capabilities are claimed beyond the tested public boundary.

### Codex

Codex integration research is experimental. Bounded app-server lifecycle qualification exists, but ordinary Codex CLI/TUI 0.147.0 does not expose a suitable privacy-safe owner-session interface for normal live wumbOS monitoring. Normal Codex monitoring remains inactive / deferred pending a suitable privacy-safe owner-session interface.

Do not read this as “Codex supported.”

### Grok Build

Grok Build integration is active research against qualified local version **1.0.4**. Current findings support authoritative persistent session identity, qualified identity/lifecycle semantics, and the feasibility of privacy-safe metadata projection. Production owner/session event integration is not complete.

Do not read this as “Grok supported.” Inactive is not the same as disconnected, and heartbeat/freshness behavior is not claimed as proven.

## Attention and Architecture

**Attention asks: “What needs me?”** Today it is a notification-centered foundation. When the optional private/local **wumbosd** service is available, it can provide deeper notification and Attention state. wumbosd is not public and is **not included** in wumbOS Shell Alpha.2; the shell continues without it, hiding or restoring dependent surfaces cleanly as the service disappears or returns.

<div class="wumbos-architecture" aria-label="wumbOS architecture">
  <div><strong>wumbOS Shell</strong><br>Quickshell / QML</div><span>↕</span><div><strong>wumbosd</strong><br>private optional system/session service</div><span>↕</span><div>Notifications · Attention · System State</div><span>↕</span><div>Linux / Fedora · Hyprland / Wayland / systemd</div><span>↕</span><div><strong>Longer-term system layer</strong><br>install, update, recovery, later distribution questions</div>
</div>

## System Integration

<div class="feature-grid">
  <div class="feature-card"><h3>Integrate first. Own later.</h3><p>Hyprland remains the compositor and window manager. PipeWire/WirePlumber remain audio authority. NetworkManager remains network authority. Nemo remains the current proven file manager. Fedora/Linux infrastructure stays where replacing it adds no meaningful product value.</p></div>
  <div class="feature-card"><h3>Control Panel</h3><p>Current prealpha work is expanding Control Panel beyond the earlier System Monitor telemetry popup. GPU identification remains available; NVIDIA has the strongest enhanced path through optional <code>nvidia-smi</code>. Missing telemetry must not break the shell.</p></div>
  <div class="feature-card"><h3>Desktop services</h3><p>Audio integrates with PipeWire and WirePlumber. Networking uses normal Linux infrastructure including NetworkManager, <code>nmcli</code>, resolver information, <code>resolvectl</code>, and <code>ip</code>.</p></div>
  <div class="feature-card"><h3>Defined boundaries</h3><p>Modern StatusNotifierItem and AppIndicator-style tray interfaces are supported. Legacy XEmbed-only tray applications are not. Weather uses Open-Meteo and Zippopotam.us with location state stored locally.</p></div>
</div>

## Status Matrix

<div class="wumbos-status-matrix">
  <div><strong>wumbOS Shell public baseline</strong><span>AVAILABLE / CURRENT · Alpha.2</span></div>
  <div><strong>Current shell development</strong><span>PREALPHA / IN DEVELOPMENT</span></div>
  <div><strong>Sandstone Night</strong><span>CURRENT PREALPHA VISUAL DIRECTION</span></div>
  <div><strong>Control Panel</strong><span>IN DEVELOPMENT</span></div>
  <div><strong>Multi-harness Agent foundation</strong><span>IN DEVELOPMENT · not in Alpha.2</span></div>
  <div><strong>OMP</strong><span>AVAILABLE / CURRENT · bounded</span></div>
  <div><strong>Codex</strong><span>RESEARCH · normal TUI monitoring deferred</span></div>
  <div><strong>Grok Build</strong><span>RESEARCH · owner-session events incomplete</span></div>
  <div><strong>Agent Module v2</strong><span>PLANNED / NEXT</span></div>
  <div><strong>wumbosd</strong><span>PRIVATE / ACTIVE DEVELOPMENT</span></div>
  <div><strong>Housekeeper / File Intelligence</strong><span>PLANNED</span></div>
  <div><strong>Native file manager</strong><span>PLANNED · Nemo remains current</span></div>
  <div><strong>Full wumbOS distribution</strong><span>LONG TERM · decision not made</span></div>
</div>

## Roadmap

<div class="roadmap-list">
  <div class="roadmap-item"><strong>1. Multi-harness Agent foundation</strong><span>IN DEVELOPMENT: shared Agent status and Attention across local harnesses. Unreleased prealpha work, not Alpha.2.</span></div>
  <div class="roadmap-item"><strong>2. Agent Module v2 — session routing and focus</strong><span>PLANNED / NEXT: evolve from passive status monitoring into an Agent task switcher that can focus the exact terminal/window, switch Hyprland workspace when required, route to tmux session/window/pane where applicable, mark the focused Agent, and send Attention/approval alerts to the requesting Agent. Desktop-routing metadata stays separate from harness-neutral lifecycle state.</span></div>
  <div class="roadmap-item"><strong>3. Desktop UX / Control Panel</strong><span>IN DEVELOPMENT: broaden Control Panel as the native status/configuration surface. Later areas may include shell/module configuration, Agent status, Housekeeper permissions, File Intelligence index status, local model selection, Audio Mixer, Night Light via <code>hyprsunset</code> first, module visibility, and diagnostics.</span></div>
  <div class="roadmap-item"><strong>4. Housekeeper Safety Core</strong><span>PLANNED — before LLM autonomy: authorized roots, protected areas, canonical path validation, symlink safety, typed filesystem operations, collision protection, Trash instead of destructive removal, transaction journal, complete Undo, dry-run/planning, and risk classifications. Deterministic safety before Agent autonomy.</span></div>
  <div class="roadmap-item"><strong>5. Shared File Intelligence</strong><span>PLANNED: local/private index and discovery for Housekeeper, a future native file manager, semantic desktop/file search, and later project awareness. Files are not uploaded to cloud infrastructure.</span></div>
  <div class="roadmap-item"><strong>6. Housekeeper Local Intelligence</strong><span>PLANNED after safety and indexing: on-demand local LLM classification, grouping, semantic organization, natural-language planning, and local semantic search. The model should load when needed rather than permanently consume GPU resources.</span></div>
  <div class="roadmap-item"><strong>7. Housekeeper Desktop Integration</strong><span>PLANNED: a native Housekeeper surface for reviewing proposed actions, applying/editing/rejecting/undoing them, and seeing authorized roots and local/privacy state. Exact UI is not promised.</span></div>
  <div class="roadmap-item"><strong>8. Native wumbOS File Manager</strong><span>PLANNED after Safety Core and File Intelligence. Nemo remains the current proven file manager until a replacement is genuinely daily-drivable. The goal is not a prettier Nemo; Housekeeper and the native file manager must share File Intelligence, the capability broker, permissions, the transaction journal, and Undo.</span></div>
  <div class="roadmap-item"><strong>9. Housekeeper Trusted Rules / Automation</strong><span>PLANNED later: repeatable local organization rules only after the local Housekeeper loop is proven.</span></div>
  <div class="roadmap-item"><strong>10. Optional provider-backed Housekeeper</strong><span>LONG TERM, only after local Housekeeper proof. A provider would be reasoning only. Filesystem authority always stays local through the deterministic capability broker. No silent cloud fallback. Local mode remains first-class.</span></div>
  <div class="roadmap-item"><strong>11. Runtime efficiency / Lean Audit</strong><span>PLANNED / LATER: measure a real cold-login/idle baseline, change one bounded item, remeasure, and keep demonstrated wins. Do not strip Hyprland functionality arbitrarily or remove useful behavior only to lower a benchmark number.</span></div>
  <div class="roadmap-item"><strong>12. Reproducible install / update / recovery</strong><span>LONG TERM: installation, configuration/version migration, update/rollback, recovery, first-run/bootstrap, and wumbOS service conventions.</span></div>
  <div class="roadmap-item"><strong>13. Daily-drivable wumbOS system</strong><span>LONG TERM: a workstation that is genuinely daily-drivable as a cohesive system, not merely a shell overlay.</span></div>
  <div class="roadmap-item"><strong>14. Longer-term Agent platform / distributable-system evaluation</strong><span>LONG TERM: only later decide how far wumbOS should evolve toward a separately distributable OS. That decision is not already made.</span></div>
</div>

<details class="project-details">
<summary>Housekeeper product concept</summary>

Housekeeper is intended to become the first major native wumbOS desktop Agent: a local Agent that helps organize and maintain the user's filesystem.

Example intents: clean up Downloads, find project-related reports, find duplicate ISOs, find related files scattered across directories, and identify files that appear misplaced.

The LLM does not receive unrestricted shell or filesystem authority.

Local model → typed Housekeeper capabilities → deterministic filesystem capability broker → filesystem.

Housekeeper begins local / offline first. Interaction concept: request → plan → review → apply → undo available.

The core product gate is whether a fully local Housekeeper can understand messy files, propose sensible organization, execute safely, and undo mistakes. That must be proven before remote-provider complexity is added.

</details>

<details class="project-details">
<summary>Audio Panel v2</summary>

Status: **PLANNED**.

Initial direction: enumerate active PipeWire/WirePlumber playback streams, identify applications currently producing audio, provide per-source volume and mute, let streams appear and disappear live, and retain master output control.

Future expansion may include recording/input clients, grouping, per-stream output-device routing, saved routing preferences, and optional source/application focus.

Use existing PipeWire/WirePlumber state and events. Do not create a duplicate custom audio daemon.

</details>

## Fast, Light, Event-Driven

wumbOS should grow in capability without accumulating unnecessary background work.

- Prefer events before polling.
- Share data and state instead of duplicating collectors.
- Lazy-load expensive UI.
- No always-on local LLM by default.
- Do not create a daemon when an existing Linux service owns the problem.
- Do not periodically spawn subprocesses when native events or APIs exist.
- Every background workload needs a reason to exist.
- Optimization claims require measurement.
- Stability and responsiveness matter more than synthetic minimum-RAM bragging.
- Useful functionality should not be removed only to lower a benchmark number.

Examples: PipeWire events for audio, a shared stats provider, Agent adapters that publish state, Housekeeper models loaded on demand, and File Intelligence that is event-driven and resource-budgeted.

## Known Public-Baseline Boundaries

<details class="project-details">
<summary>Tested support and current limitations</summary>

- Tested Alpha.2 stack: Fedora 44, Wayland, Hyprland 0.56.2, Quickshell 0.3.0, Qt 6, PipeWire/WirePlumber, NetworkManager, and systemd/logind.
- Other Wayland compositors, KDE, and GNOME are unsupported. Older and newer Hyprland and Quickshell versions are unqualified.
- A stationary-pointer popup retarget behavior exists on the tested Hyprland/Quickshell stack; Escape, click-away, switching popups, and slight pointer movement remain practical close paths.
- OMP is the established Agent harness; its ordinary human-question waiting state cannot always be represented.
- Codex is not a supported live monitoring integration. Grok Build is research, not a supported production integration.
- Enhanced AMD and Intel GPU telemetry are not implemented; XEmbed-only tray applications are unsupported; wumbosd is not bundled with Alpha.2.
- Housekeeper, File Intelligence, the native file manager, provider-backed reasoning, installer/ISO media, and a separately distributable OS are not current shipping features.

</details>

## Development Discipline

wumbOS makes narrow support claims, centralizes state where practical, and treats graceful degradation as a core requirement. Real interaction behavior overrides static reasoning; brittle delays, synthetic input, and per-component hacks are not substitutes for correct architecture.

The public alpha line was validated through license and privacy review, clean archive and simulated-install checks, dependency/import checks, live shell and session-integrity validation, release-candidate work, and public-clone review. Public `main` is intended to represent something an outside user can reasonably install. Current prealpha branches are development, not a substitute for that public baseline.

## Open Source Public Alpha

wumbOS Shell is available under **MPL-2.0**. Its public repository has GitHub Issues enabled: <a href="https://github.com/WumboLabs/wumbo-quickshell">WumboLabs/wumbo-quickshell</a>. Alpha.2 is the current public baseline. The full wumbOS distribution, installer, ISO, and broad hardware qualification remain future work.
