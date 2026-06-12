+++
title = "Wumbo Core"
description = "Home network and homelab infrastructure for WumboLabs."
weight = 3
+++

# Wumbo Core

**Home network and homelab infrastructure**  
**Status:** Active production environment

Wumbo Core is the home network and homelab infrastructure behind WumboLabs.

It includes the server, workstations, mobile systems, local network, storage, DNS, Docker services, documentation, and recovery planning that support day-to-day use and local experimentation.

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

## Core Areas

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
    <h3>Workstations and Clients</h3>
    <p>WumboJetsII, WumboMini, WumboMobile, and future systems are treated as part of the broader lab environment.</p>
  </div>

  <div class="feature-card">
    <h3>Storage and Backups</h3>
    <p>ZFS storage, datasets, snapshots, backup planning, and clear recovery procedures are core parts of the infrastructure.</p>
  </div>

  <div class="feature-card">
    <h3>Services and Dashboards</h3>
    <p>Docker Compose services, Homepage, AdGuard Home, media services, monitoring, logs, and operational visibility.</p>
  </div>

  <div class="feature-card">
    <h3>Documentation and Recovery</h3>
    <p>MkDocs documentation, rebuild notes, emergency procedures, service checklists, and stability-first change tracking.</p>
  </div>
</div>

## Current Systems

### WumboServer

The main homelab server. It runs the core Docker service stack, storage, DNS, media services, VPN-routed workloads, dashboards, and documentation.

### WumboJetsII

The primary Linux workstation and local AI test machine. It is part of Wumbo Core because it depends on, tests against, and helps operate the broader lab environment.

### WumboMini

A secondary small-form-factor system used as part of the broader infrastructure and redundancy plan.

### WumboMobile

A mobile Linux system used for portable work, testing, and access into the WumboLabs environment.

## Operating Philosophy

Wumbo Core is not just a server. It is the full local infrastructure layer.

The main priorities are:

- stable home networking
- reliable local services
- clear documentation
- recoverable configuration
- conservative changes
- practical monitoring
- room for future expansion

## Future Expansion

Wumbo Core is expected to grow over time.

Future expansion may include additional wired drops, new lab hardware, more structured backups, improved monitoring, better network segmentation, and deeper integration between local systems.

The goal is to keep the infrastructure understandable and recoverable as it grows.
