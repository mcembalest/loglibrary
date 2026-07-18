# Deploy (Cloudflare Workers)

The site is a static MkDocs build served from Cloudflare Workers via the `assets`
block in `wrangler.jsonc` — an assets-only Worker (no Worker code). Same pattern
as runway-atlas, stripped to the static case.

## Recommended: git-connected auto-deploy (Workers Builds)

Every push to `main` — including from Claude Code on your phone — rebuilds and
deploys automatically. **Needs your Cloudflare login (one-time).**

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Import a repository**.
2. Select `mcembalest/loglibrary`, production branch `main`.
3. Build settings:
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Deploy command: `npx wrangler deploy`
   - (Cloudflare reads `wrangler.jsonc` for the rest.)
4. **Save and Deploy.**

Lands at `loglibrary.<your-subdomain>.workers.dev`. Add a custom domain under the
Worker's **Settings → Domains & Routes**.

## Alternative: deploy from the CLI

Faster to stand up, but each deploy needs a terminal (won't fire from a phone):

```bash
wrangler login                       # one-time auth
mkdocs build && npx wrangler deploy  # build, then push
```

## Local preview

```bash
./start_local.zsh      # serves at http://localhost:8000
```

## Regenerate the clog plots

```bash
uv run --with matplotlib --with numpy tools/clogs.py
```
