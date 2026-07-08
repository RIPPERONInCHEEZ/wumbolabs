+++
title = "Wumbo Core"
description = "Home network and homelab infrastructure for WumboLabs."
template = "project.html"
weight = 2
[extra]
back_label = "Back to Projects"
back_url = "/projects/"
+++

Wumbo Core is the home network and homelab infrastructure behind WumboLabs.

It includes the server, workstations, mobile systems, local network, storage, DNS, Docker services, documentation, and recovery planning that support day-to-day use and local experimentation.

<strong>Active production environment</strong>

## At a Glance

<div class="info-grid">
  <div class="info-card">
    <span class="info-label">Core Server</span>
    <strong>WumboServer</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Workstation</span>
    <strong>WumboJetsII</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Mini System</span>
    <strong>WumboMini</strong>
  </div>

  <div class="info-card">
    <span class="info-label">Mobile System</span>
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
    <p>WumboServer provides the main Docker, storage, media, DNS, VPN-routed workload, dashboard, and documentation services.</p>
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

The main homelab server. It runs the core Docker service stack, storage, DNS, media services, VPN-routed workloads, dashboards, and documentation.

### WumboJetsII

The primary Linux workstation and local AI test machine. It depends on, tests against, and helps operate the broader lab environment.

### WumboMini

A secondary small-form-factor system used as part of the broader infrastructure and redundancy plan.

### WumboMobile

A mobile Linux system used for portable work, testing, and access into the WumboLabs environment.

</details>

<details class="project-details">
<summary>Future expansion</summary>

Future expansion may include additional wired drops, new lab hardware, more structured backups, improved monitoring, better network segmentation, and deeper integration between local systems.

The goal is to keep the infrastructure understandable and recoverable as it grows.

</details>
