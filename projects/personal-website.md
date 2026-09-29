# 🌐 Personal Website

*[josuejunior.fleuridor.com](https://josuejunior.fleuridor.com): my portfolio, CV and blog, built and run by me.*

## The problem

I needed one place that shows my real work, in English and French, that I can update without
redeploying, and that I host myself with the same standards I apply at work.

## What I built

- **API:** Laravel 13 on PHP 8.4, served by FrankenPHP. MariaDB for data.
- **Front end:** Next.js 16 (React 19), bilingual EN/FR.
- **Everything in Docker:** API, queue worker, scheduler, web and database backups run as containers.
- **CI/CD:** GitHub Actions builds and tests, pushes images to GitHub Container Registry (GHCR),
  then deploys to the server over SSH.
- **CV page** with PDF export through signed links that expire.
- **Hourly GitHub sync** so new public projects show up on their own.
- **Daily database backups**, with old dumps rotated out automatically.
- **Admin panel** to edit profile, projects, certifications and roadmap without touching code.

## Stack

![Laravel](https://img.shields.io/badge/Laravel_13-FF2D20?style=flat&logo=laravel&logoColor=white)
![PHP](https://img.shields.io/badge/PHP_8.4-777BB4?style=flat&logo=php&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=flat&logo=nextdotjs&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat&logo=mariadb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

## Results

- Live at [josuejunior.fleuridor.com](https://josuejunior.fleuridor.com) (EN) and
  [/fr](https://josuejunior.fleuridor.com/fr).
- Every merge to `main` ships to production through the pipeline, no manual steps.
- Content changes go through the admin panel, not a redeploy.

## What I learned

- Splitting API and front end keeps each side simple and replaceable.
- Signed, expiring links are an easy way to share a document without making it public.
- Backups and scheduled jobs belong in the same Compose file as the app, so they never get forgotten.

*The source code is private. The site itself is the demo.*

[← Back to home](../README.md)
