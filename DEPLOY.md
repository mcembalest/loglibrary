# Deploy (Cloudflare Pages)

The site is a static MkDocs build. Cloudflare Pages can build and host it for free, rebuilding on every push to `main`.

## One-time setup (needs your Cloudflare login)

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. Select the `mcembalest/loglibrary` repo, production branch `main`.
3. Build settings:
   - Framework preset: **None**
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Build output directory: `site`
   - Environment variable: `PYTHON_VERSION` = `3.12`
4. **Save and Deploy.**

After this, every push to `main` rebuilds and deploys automatically. To use a custom domain, add it under the Pages project's **Custom domains** tab.

## Local preview

```bash
./start_local.zsh      # serves at http://localhost:8000
```

## Regenerate the clog plots

```bash
uv run --with matplotlib --with numpy tools/clogs.py
```
