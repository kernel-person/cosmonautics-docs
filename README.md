# Cosmonautics Docs

Public player and administrator documentation for the Cosmonautics Minecraft plugin.

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.

## Content policy

The public wiki is manually curated from Cosmonautics release documentation. Keep supported beta features separate from coming-soon content, and do not publish license keys, internal diagnostics, developer commands, or marketplace-only material.

Place finished screenshots in `docs/images/` and reference them from the existing pages. `IMAGE-CHECKLIST.md` records the intended shots without placing unfinished imagery on the public site.

## Crafting diagrams

The diagrams in `docs/images/recipes/` use Minecraft's crafting GUI, vanilla item textures, and the custom head skins used by Cosmonautics. Their small source assets and recipe definitions are checked in so the images can be regenerated without running Minecraft or fetching textures during a site build.

See [the recipe renderer](tools/recipe-renderer/README.md) for asset sources, regeneration, and validation. Keep the diagrams, written ingredients, and image descriptions in sync when recipes change.

## Publish

The GitHub Actions workflow builds the site in strict mode and publishes it to the `gh-pages` branch after a push to `main`.

After creating `kernel-person/cosmonautics-docs` on GitHub and pushing this repository:

1. Wait for the **Deploy MkDocs** workflow to succeed.
2. In the repository's Pages settings, select **Deploy from a branch**.
3. Select the `gh-pages` branch and `/ (root)` folder.
4. Visit `https://kernel-person.github.io/cosmonautics-docs/`.
