# ⚙️ DevOps at Devora

*DevOps Engineer at Devora, a Canadian firm. Remote, since December 2025.*

> This page stays at the architecture level. No hostnames, addresses or internal details.

## The problem

Devora needed its application deployed to production and kept running, secure and available,
with a small team and no room for downtime.

## What I built

- Deployed the company's application to production, and I maintain it day to day.
- **Four production Debian servers**, operated around the clock.
- **WireGuard VPN** for private access between servers and for administrators.
- **PostgreSQL** for application data and **MinIO** for object storage.
- **CrowdSec** and **fail2ban** for intrusion prevention across the fleet.

## Stack

![Debian](https://img.shields.io/badge/Debian-A81D33?style=flat&logo=debian&logoColor=white)
![WireGuard](https://img.shields.io/badge/WireGuard-88171A?style=flat&logo=wireguard&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white)
![CrowdSec](https://img.shields.io/badge/CrowdSec-2C3E50?style=flat)
![fail2ban](https://img.shields.io/badge/fail2ban-B22222?style=flat)

## Results

- **4** production servers.
- **99.98%** uptime.

## What I learned

- Private networking first: if a service doesn't need to be public, it isn't.
- Layered defense (VPN, intrusion prevention, least access) beats any single tool.
- Uptime comes from boring routines: patching, monitoring, tested backups.

[← Back to home](../README.md)
