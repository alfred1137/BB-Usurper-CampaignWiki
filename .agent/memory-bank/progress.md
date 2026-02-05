# Progress

## What Works

- The basic structure of a Jekyll-based wiki is in place.
- The project is configured to use the `git-wiki-theme`.
- Docker-based local development is set up.
- Kanka.io entities (Journals, Characters, Locations, etc.) have been migrated to the wiki.
- Assets are organized and linked correctly in the content.
- Internal wiki links are resolved to standard Markdown links ([Name](../path/to/Name.md)).
- Automated internal link maintenance via `scripts/apply_links.py` and `scripts/scan_links.py`, now using robust Jekyll-compatible paths (`{{ site.baseurl }}/Basename`).
- **Resolved:** Major issue with broken filesystem-relative links fixed across the entire wiki and blog.
- **Resolved:** Blog post images fixed by renaming `assets/_posts` to `assets/posts` (avoiding Jekyll's underscore ignore rule).
- **Visual Style:** Catppuccin theme (Latte/Macchiato) fully integrated and enforced.
- **Layout Overhaul:** Migrated to a modern 3-column grid with a fixed sidebar, centered main content, and a right-hand metadata/TOC column.
- **Search Bar:** Implemented a full-width search bar with high-quality dropdown results and resolved empty-container border glitches.
- **Build Optimization:** Resolved UTF-8 encoding issues and optimized build speed by excluding irrelevant directories.

## What's Left to Build

- User verification of the new visual style.
- Continued content updates.

## Known Issues

- None at this time.
