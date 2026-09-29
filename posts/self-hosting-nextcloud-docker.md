# How I self-host my own cloud with Nextcloud and Docker

*[TODO: publish date] · ~5 min read*

I wanted my files, photos, and calendar in one place. And I wanted to own that place.
So I built my own cloud at home with Nextcloud and Docker.
Here's how I think about it, in plain terms.

---

## Why self-host?

- **Control.** My data lives on hardware I own.
- **Learning.** Every problem teaches me something about Linux, networking, or security.
- **Cost.** [TODO: your take on cost vs. paid cloud storage]

[TODO: add the moment or reason you decided to start]

## The building blocks

| Piece | What it does, in one line |
|---|---|
| **Debian** | A stable Linux system that runs everything. |
| **Docker** | Runs each app in its own container, so they don't step on each other. |
| **Nextcloud** | The "cloud" itself: files, calendar, contacts, in a web app. |
| **PostgreSQL** | The database Nextcloud stores its data in. |
| **WireGuard** | A private VPN tunnel, so I can reach my stuff safely from anywhere. |

## How it fits together (the big picture)

1. Debian runs on my home server.
2. Docker runs Nextcloud and its database as separate containers.
3. A reverse proxy handles secure (HTTPS) connections. [TODO: which one you like, in general terms]
4. When I'm away, I connect through a VPN instead of opening my server to the whole internet.

> 💡 **Beginner tip:** Start with Docker Compose. One file describes all your containers, so you can rebuild your setup in minutes.

## Security basics I care about

- Keep the system and containers updated.
- Don't expose more than you need. A VPN is your friend.
- Use strong, unique passwords and turn on two-factor login.
- Keep secrets (passwords, keys) in files that never go into Git.
- Back up. Then test that the backup actually restores.

[TODO: one thing you learned the hard way]

## What I learned

- [TODO: lesson 1]
- [TODO: lesson 2]
- [TODO: lesson 3]

## If you want to try it

1. Get an old PC or a small mini PC.
2. Install Debian (or any Linux you like).
3. Install Docker and Docker Compose.
4. Follow the official Nextcloud Docker guide.
5. Break things, fix them, and take notes. That's the real course.

## What's next

[TODO: what you want to add or improve next]

---

*Questions? Reach out through the links on my [home page](../README.md#-connect-with-me).*

[← All posts](README.md)
