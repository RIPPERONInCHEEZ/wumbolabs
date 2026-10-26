+++
title = "Wumbo Core"
description = "Home network and homelab infrastructure for WumboLabs."
template = "project.html"
in_search = false
weight = 101
[extra]
back_label = "Back to Home"
back_url = "/"
public_project = false
content_kind = "infrastructure"
+++

Wumbo Core is the home network and homelab infrastructure behind WumboLabs.

It includes the server, workstations, mobile systems, local network, storage, DNS, Docker services, documentation, and recovery planning that support day-to-day use and local experimentation.

The workstation transition and headless compute conversion are complete. Standardized backup coverage across all four hosts remains deferred.

<strong>Active production environment</strong>

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Core Server</span>
    <strong>WumboServer</strong>
  </div>

  <div class="info-card">
    <span class="info-label">AI Compute</span>
    <strong>WumboJetsII</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Primary DNS</span>
    <strong>WumboMini</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Interactive Workstation</span>
    <strong>WumboMobile</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Network</span>
    <strong>Gigabit + Wi-Fi 6</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Goal</span>
    <strong>Recoverable systems</strong>
  </div>
</div>

## Operating Goal

Wumbo Core is not just a server. It is the local infrastructure layer.

The priorities are stable home networking, reliable local services, clear documentation, recoverable configuration, conservative changes, practical monitoring, and room for future expansion.

<details class="project-details">
<summary>Core areas</summary>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Home Network</h3>
    <p>Gigabit wired networking, Wi-Fi 6 wireless coverage, local DNS, device coordination, and future expansion planning.</p>
  </div>

  <div class="feature-card">
    <h3>Homelab Server</h3>
    <p>WumboServer provides the main Docker, ZFS storage, media, backup, VPN-routed workload, dashboard, and documentation services.</p>
  </div>

  <div class="feature-card">
    <h3>Storage and Backups</h3>
    <p>ZFS storage, datasets, snapshots, backup planning, and clear recovery procedures are core parts of the infrastructure.</p>
  </div>

  <div class="feature-card">
    <h3>Documentation and Recovery</h3>
    <p>MkDocs documentation, rebuild notes, emergency procedures, service checklists, and stability-first change tracking.</p>
  </div>
</div>

</details>

<details class="project-details">
<summary>Current systems</summary>

### WumboServer

The shared infrastructure and storage server, with Docker services, ZFS storage, and media services. Its RTX 2060 Super is available for limited small-model experiments; it is not the primary WELP evaluation machine.

### WumboJetsII

The headless AI compute node. It runs local-model evaluation campaigns, LLMGauge testing, and compute work for the lab on an AMD Radeon AI PRO R9700, with no desktop session.

### WumboMini

The primary DNS server and lightweight infrastructure system.

### WumboMobile

The primary interactive workstation: a Lenovo ThinkPad T14 Gen 1 with an AMD Ryzen 5 PRO 4650U, running Fedora 44 with Hyprland and the custom wumbOS desktop environment. It is the main human-facing desktop and development interface, including access to remote compute.

</details>

<details class="project-details">
<summary>Future expansion</summary>

Future expansion may include additional wired drops, new lab hardware, more structured backups, improved monitoring, better network segmentation, and deeper integration between local systems.

The goal is to keep the infrastructure understandable and recoverable as it grows.

</details>
