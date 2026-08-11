+++
title = "wumbOS"
description = "An agent-aware Linux workstation project, built from the shell outward."
template = "project.html"
weight = 2
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
portfolio_status = "MAIN FOCUS · ACTIVE DEVELOPMENT"
release_status = "PUBLIC SHELL ALPHA · v0.1.0-alpha.1"
wumbos = true
+++

<strong>MAIN FOCUS / ACTIVE DEVELOPMENT</strong>

wumbOS is an actively developed Linux desktop and operating-system project focused on building a cohesive, agent-aware workstation. The first public component, <a href="https://github.com/WumboLabs/wumbo-quickshell">wumbOS Shell</a>, is a Quickshell-based desktop shell built around Hyprland and Wayland. The wider system is being built in layers: a public shell today, a private optional system/session service under development, and a future distribution/integration layer. It is not a finished Linux distribution.

<div class="wumbos-cta-row">
  <a class="wumbos-cta" href="https://github.com/WumboLabs/wumbo-quickshell">View wumbOS Shell on GitHub</a>
  <a class="wumbos-cta wumbos-cta--secondary" href="https://github.com/WumboLabs/wumbo-quickshell/releases/tag/v0.1.0-alpha.1">Read the Alpha Release</a>
</div>

## Current Release

<div class="info-grid wumbos-status-grid">
  <div class="info-card"><span class="info-label">Public component</span><strong>wumbOS Shell</strong></div>
  <div class="info-card"><span class="info-label">Release</span><strong>v0.1.0-alpha.1</strong></div>
  <div class="info-card"><span class="info-label">Status</span><strong>Public Alpha</strong></div>
  <div class="info-card"><span class="info-label">License</span><strong>MPL-2.0</strong></div>
  <div class="info-card"><span class="info-label">Tested OS</span><strong>Fedora 44</strong></div>
  <div class="info-card"><span class="info-label">Required compositor</span><strong>Hyprland</strong></div>
</div>

The alpha is a functional desktop shell, not a mockup or theme concept. It was tested with **Hyprland 0.56.2**, **Quickshell 0.3.0**, Qt 6, PipeWire/WirePlumber, NetworkManager, and systemd/logind. Hyprland is required: the shell directly uses Hyprland functionality and Quickshell’s Hyprland integration. These are tested versions, not minimum-version promises.

## Shell-First Desktop

wumbOS Shell keeps persistent chrome compact: a 34-pixel top bar is created dynamically for each connected display. It presents workspaces, active-window state, date and weather, Attention and Agent status, audio, networking and DNS information, system monitoring, GPU information, tray, power/session controls, launcher, and clipboard access. Related details live in coordinated contextual popups rather than becoming permanent bar modules.

Multi-monitor behavior is deliberate: bars follow connected displays without hard-coded connector names, and popup ownership follows the target monitor. Multi-monitor operation was live-tested. Single-monitor operation is structurally supported but has not received equivalent live qualification.

## Agent-Aware Workstation

Agent activity is treated as workstation state rather than chatbot branding. The current public integration is optional and supports **OMP 17.2.11**; it reads structured Agent state and can represent running, tool activity, waiting, blocked, completed, failed, and idle states when the harness supplies them.

OMP is the only supported Agent harness today. It does not reliably expose every ordinary human-question waiting transition, so the shell does not invent one from timers, CPU use, unread state, or Attention. Truthful missing state is better than heuristic confidence.

<div class="wumbos-architecture" aria-label="Planned Agent abstraction">
  <div>Agent UI</div><span>↓</span><div>Normalized AgentStore <em>NEXT</em></div><span>↓</span><div>OMP Adapter &nbsp;|&nbsp; Future Harness Adapters</div>
</div>

The normalized multi-harness architecture is the next major architecture milestone, not a shipping alpha feature.

## Attention and Architecture

**Attention asks: “What needs me?”** Today it is a notification-centered foundation. When the optional private/local **wumbosd** service is available, it can provide deeper notification and Attention state. wumbosd is not public and is **not included** in wumbOS Shell v0.1.0-alpha.1; the shell continues without it, hiding or restoring dependent surfaces cleanly as the service disappears or returns.

<div class="wumbos-architecture" aria-label="wumbOS architecture">
  <div><strong>wumbOS Shell</strong><br>Quickshell / QML</div><span>↕</span><div><strong>wumbosd</strong><br>private optional system/session service</div><span>↕</span><div>Notifications · Attention · System State</div><span>↕</span><div>Linux / Fedora · Hyprland / Wayland / systemd</div><span>↕</span><div><strong>Future wumbOS distribution layer</strong><br>composition, packages, installer, media, policy</div>
</div>

Future approvals, jobs, broader Agent events, Control Center surfaces, and full distribution work are direction—not alpha functionality.

## System Integration

<div class="feature-grid">
  <div class="feature-card"><h3>One owner for state</h3><p>System Monitor centralizes bounded polling and state ownership for CPU, memory, storage, temperatures where supported, network state, and GPU information.</p></div>
  <div class="feature-card"><h3>GPU telemetry</h3><p>NVIDIA has the strongest enhanced path through optional <code>nvidia-smi</code>. AMD and Intel identification is supported; equivalent enhanced telemetry is not implemented. Missing telemetry must not break the shell.</p></div>
  <div class="feature-card"><h3>Desktop services</h3><p>Audio integrates with PipeWire and WirePlumber. Networking uses normal Linux infrastructure including NetworkManager, <code>nmcli</code>, resolver information, <code>resolvectl</code>, and <code>ip</code>.</p></div>
  <div class="feature-card"><h3>Defined boundaries</h3><p>Modern StatusNotifierItem and AppIndicator-style tray interfaces are supported. Legacy XEmbed-only tray applications are not. Weather uses Open-Meteo and Zippopotam.us with location state stored locally.</p></div>
</div>

## Current Status

<div class="wumbos-status-matrix">
  <div><strong>wumbOS Shell</strong><span>PUBLIC ALPHA · v0.1.0-alpha.1</span></div>
  <div><strong>wumbosd</strong><span>PRIVATE / ACTIVE DEVELOPMENT</span></div>
  <div><strong>Agent Harness Abstraction</strong><span>NEXT MAJOR ARCHITECTURE MILESTONE</span></div>
  <div><strong>Peripheral Device Status</strong><span>PLANNED · System Monitor → Devices</span></div>
  <div><strong>Control Center / System Details</strong><span>PLANNED</span></div>
  <div><strong>Full wumbOS Distribution</strong><span>LONG-TERM</span></div>
</div>

## Roadmap

<div class="roadmap-list">
  <div class="roadmap-item"><strong>Phase 1 — Shell Foundation</strong><span>PUBLIC ALPHA: multi-monitor shell, workspaces, monitoring, audio, networking, notifications, Attention, Agent state, tray, controls, weather.</span></div>
  <div class="roadmap-item"><strong>Phase 2 — Agent and Device Integration</strong><span>NEXT: Agent Harness Abstraction, additional adapters, Peripheral Device Status, Attention quick access.</span></div>
  <div class="roadmap-item"><strong>Phase 3 — System Experience</strong><span>PLANNED: lightweight Control Center, deeper system details, device management, expanded wumbosd integration.</span></div>
  <div class="roadmap-item"><strong>Phase 4 — Agent-Native Workstation</strong><span>FUTURE: jobs, approvals, Command Center, Agent Relay, Builder workflows, and model-routing concepts.</span></div>
  <div class="roadmap-item"><strong>Phase 5 — Full wumbOS Distribution</strong><span>LONG-TERM: composition, packages, installer, ISO/build system, defaults, qualification, and whole-system releases.</span></div>
</div>

## Known Alpha Boundaries

<details class="project-details"><summary>Tested support and current limitations</summary>

- Tested stack: Fedora 44, Wayland, Hyprland 0.56.2, Quickshell 0.3.0, Qt 6, PipeWire/WirePlumber, NetworkManager, and systemd/logind.
- Other Wayland compositors, KDE, and GNOME are unsupported. Older and newer Hyprland and Quickshell versions are unqualified.
- A stationary-pointer popup retarget behavior exists on the tested Hyprland/Quickshell stack; Escape, click-away, switching popups, and slight pointer movement remain practical close paths.
- OMP is the sole supported Agent harness; its ordinary human-question waiting state cannot always be represented.
- Enhanced AMD and Intel GPU telemetry are not implemented; XEmbed-only tray applications are unsupported; wumbosd is not bundled with the alpha.

</details>

## Development and Release Discipline

wumbOS makes narrow support claims, centralizes state where practical, and treats graceful degradation as a core requirement. Real interaction behavior overrides static reasoning; brittle delays, synthetic input, and per-component hacks are not substitutes for correct architecture.

The public alpha was validated through license and privacy review, clean archive and simulated-install checks, dependency/import checks, live shell and session-integrity validation, release-candidate work, and public-clone review. A real Quickshell restart lifecycle race was found and corrected before publication. Public `main` is intended to represent something an outside user can reasonably install.

## Open Source Public Alpha

wumbOS Shell is available under **MPL-2.0**. Its public repository has GitHub Issues enabled for the alpha: <a href="https://github.com/WumboLabs/wumbo-quickshell">WumboLabs/wumbo-quickshell</a>. The shell alpha is the first released layer; the full wumbOS distribution, installer, ISO, and broad hardware qualification remain future work.
