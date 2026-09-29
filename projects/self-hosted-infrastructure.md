# 🏠 Self-Hosted Infrastructure

*My own private cloud.*

## Overview

I run my own services instead of relying only on big cloud providers.
It covers file storage and sync, secure remote access, monitoring alerts, and document signing.
This page describes the skills and tools involved, not the exact setup.

## The problem

I wanted my files, code, mail and monitoring on infrastructure I control,
and a place to practice the same production habits I use at work.

## What I built

- A small fleet of Debian VPS running containerized services 24/7 with Docker.
- A WireGuard mesh so admin access never goes over the open internet.
- A reverse proxy in front of the web apps, with TLS certificates renewed and synced automatically.
- Unattended security patching, plus fleet-wide kernel CVE remediation when a fix lands.
- Uptime monitoring and dashboards, with push alerts to my phone.

## Tech used

- **Base:** Debian, Docker
- **Networking & security:** WireGuard, CrowdSec, Nginx Proxy Manager
- **Data:** PostgreSQL, PgBouncer
- **Apps:** Nextcloud, Syncthing, ntfy, DocuSeal, Gitea
- **Monitoring:** Grafana, Uptime Kuma

## Results

- Services up 24/7, patched without me logging in.
- One place for my files, code and alerts, owned by me.

## What I learned

- Keep access private first (VPN), then expose only what must be public.
- Automate patching and certificates, or they will be forgotten.
- A backup only counts once you've tested the restore.

## Status

🟢 Active

[← Back to home](../README.md)
