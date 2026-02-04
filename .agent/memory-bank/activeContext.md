# Active Context

The project has transitioned from a remote Jekyll theme to a locally internalized version of `git-wiki-theme`. This was done to fix dark mode glitches and properly integrate the Catppuccin color scheme.

## Recent Changes

- **Theme Internalization:** Disconnected `remote_theme` and copied essential theme files (`_layouts`, `_includes`, `_sass`, `assets`) locally.
- **Catppuccin Integration:**
  - Created `_sass/_catppuccin.scss` with CSS variables.
  - Modified `_sass/git-wiki-style.scss` to import Catppuccin variables and map them to theme elements (defaulting to Macchiato flavor).
- **Fixes:**
  - Removed `darkmode.js` integration to prevent conflicts with the new CSS-based theming.
  - Replaced local font references with Google Fonts (Noto Sans) to avoid missing asset issues.
  - Replaced missing local search script with a CDN link for `simple-jekyll-search`.
- **Migration:** Kanka.io entities were previously migrated to Jekyll structure.

## Next Steps

- User verification of the new visual style and functionality.
- Ongoing maintenance of wiki content and links.