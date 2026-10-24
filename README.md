# CarbonCraft player wiki (source)

Player-facing wiki, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

- `mkdocs.yml`: site settings and the sidebar order (`nav:`). New pages must be added there.
- `docs/index.md`: home page
- `docs/getting-started/`: joining, first hour, claims, money, voting, commands, rules
- `docs/assets/`: logo, favicon and `extra.css` (CarbonCraft colours)

## Preview locally

One-time setup, from this folder:

```bash
py -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

Then run it and open http://127.0.0.1:8000. Pages reload as you save:

```bash
.venv/Scripts/python.exe -m mkdocs serve -a 127.0.0.1:8000
```

`mkdocs build --strict` writes the finished site to `site/` and fails on broken links.

## Keeping it accurate

Facts come from the **live** server's configs, not test. Each page starts with an HTML
comment naming the config files it was written from and the date it was checked.
When one of those configs changes (vote tiers, rules, claim settings), re-pull it from
the live project and update the page.

The Syndicate images in `docs/assets/syndicates/` are WebP copies (quality 88) of the PNGs
in `../wiki-images/syndicates/`, which `_src/build.py` renders from the menu and item
configs. If you rebuild those PNGs, convert them again rather than editing the WebPs.

The coloured tags on `docs/cosmetics/tags.md` are HTML generated from the live DeluxeTags
`config.yml`, one `<span>` per colour run. To re-render tags after they change in game:

```bash
.venv/Scripts/python.exe -I scripts/render-tags.py "../../LIVE SERVER/server-files/plugins/DeluxeTags/config.yml" flex_cash vote mvp
```

It prints one line per tag ID; paste the HTML into the page's table. The `.mc-tag` chip
style lives in `docs/assets/extra.css`.

## Publishing

The wiki is hosted on GitHub Pages at https://wiki.carboncraft.xyz/, from the
`OverCraftedGames/carboncraft-wiki` repository (this `wiki/` folder is its root).
Every push to `main` runs `.github/workflows/deploy.yml`, which does a strict build and
publishes it. If the build fails (a broken link or anchor), the live site stays on the
last good version; the failure shows in the repository's Actions tab.

The repository is public, so keep anything staff-only out of the pages and their
source comments. `hooks/strip_comments.py` removes the comments from the published
HTML, but they are still readable on GitHub.

DNS for `carboncraft.xyz` is at GoDaddy: `wiki` is a CNAME to `overcraftedgames.github.io`.
