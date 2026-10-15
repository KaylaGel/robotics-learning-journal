# GitHub Pages

The website source is `docs/`. It uses GitHub Pages' built-in Jekyll build, with a shared responsive layout and navigation. The repository's Markdown documents remain the editable source of the learning material.

After changing journal content:

```bash
python3 scripts/build_pages.py
```

Commit the updated source and generated `docs/` files together. Enable GitHub Pages with the `main` branch and `/docs` folder as its source. Future pushes will rebuild the site.

Expected URL after deployment: https://kaylagel.github.io/robotics-learning-journal/

GitHub Pages websites on personal accounts are public even when their source repository is private. Private-source Pages requires a supported paid plan. Do not add private journal entries, credentials, or unreviewed recordings to the website source. Enabling Pages requires approval of that public website audience.

The generator copies the README, roadmap, and Markdown files under guides, projects, journal, resources, and templates. Review those folders before publishing changes.
