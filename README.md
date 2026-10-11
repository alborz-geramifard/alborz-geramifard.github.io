# alborz-geramifard.com

Static personal website. Plain HTML + CSS, no build step.

- `index.html` – home (bio, experience, highlights, service)
- `publications.html` – publications grouped by year, with a client-side filter
- `notes.html` – articles written on LinkedIn, as a timeline (generated)
- `code.html` – released code
- `assets/style.css` – all styling (light/dark via `prefers-color-scheme`)
- `assets/img/` – images

## Preview locally

```sh
python3 -m http.server 8787
# open http://127.0.0.1:8787/
```

## Publish on GitHub Pages (free)

1. Create a public repo named `<github-username>.github.io`.
2. Push this folder to its `main` branch.
3. In the repo: Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. The site goes live at `https://<github-username>.github.io/` within a minute or two.

## Custom domain (alborz-geramifard.com)

1. Add a file named `CNAME` containing `alborz-geramifard.com` to the repo root (Settings → Pages → Custom domain does this for you).
2. At the registrar's DNS panel set:
   - `A` records for `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record for `www` → `<github-username>.github.io`
3. Remove any existing forwarding rules for the domain.
4. In Settings → Pages tick "Enforce HTTPS" once the DNS check passes.

## Updating publications

Edit the `P` list in `tools/build_publications.py`, then run:

```sh
python3 tools/build_publications.py
```

## Updating notes

`data/notes.json` holds one entry per LinkedIn article (`url`, `title`, `desc`, `date`, `read`, `cover`). Add an entry (and drop a cover image in `assets/img/notes/`), then run:

```sh
python3 tools/build_notes.py
```
