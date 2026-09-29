# Social banners

Three designs, each sized for X, LinkedIn and Facebook. The ready-to-upload files are in `export/`.

| Design | X header (1500×500) | LinkedIn background (1584×396) | Facebook cover (1640×624) |
|---|---|---|---|
| **A · Network mesh** | [A-x.png](export/A-x.png) | [A-li.png](export/A-li.png) | [A-fb.png](export/A-fb.png) (FR) |
| **B · Terminal** | [B-x.png](export/B-x.png) | [B-li.png](export/B-li.png) | [B-fb.png](export/B-fb.png) (FR) |
| **C · Light roadmap** | [C-x.png](export/C-x.png) | [C-li.png](export/C-li.png) | [C-fb.png](export/C-fb.png) (FR) |

Every file is under 250 KB, well inside the upload limits (X 2 MB, LinkedIn 8 MB, Facebook 10 MB).

## Safe zones

The layouts keep text clear of what each platform covers:

- **X:** the profile photo sits over the bottom-left corner (about 40–375 px across). Phones can crop about 60 px off the top and bottom.
- **LinkedIn:** the profile photo sits over the bottom-left (about 48–348 px across, lower half).
- **Facebook:** phones show only the centre, about 265–1375 px across. The profile photo sits over the bottom-left on desktop.

## Regenerate

The banners are built from code, so a new stat or job title is a one-line change in `generate.py`.
You need Python 3 and Docker. `render.mjs` uses the Chromium and Puppeteer that ship in the website's web image.

```bash
cd brand/banners
python3 generate.py
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp -v "$PWD":/w -w /app \
  --entrypoint node ghcr.io/jun101/personalwebsite-web:latest /w/render.mjs
```

`src/img/` holds the avatar cut-outs (backgrounds removed, transparent padding trimmed).
