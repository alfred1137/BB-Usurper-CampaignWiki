# Active Context

The project has transitioned from a remote Jekyll theme to a locally internalized version of `git-wiki-theme`. This was done to fix dark mode glitches and properly integrate the Catppuccin color scheme.

## Recent Changes

- **Theme Internalization:** Disconnected `remote_theme` and copied essential theme files (`_layouts`, `_includes`, `_sass`, `assets`) locally.
- **Catppuccin Integration:**
  - Created `_sass/_catppuccin.scss` with CSS variables.
  - Modified `_sass/git-wiki-style.scss` to import Catppuccin variables and map them to theme elements (defaulting to Macchiato flavor).
- **Theme Refinement:**
  - Enforced strict usage of **Latte (Light)** and **Macchiato (Dark)** themes only.
  - Removed unused Frappe and Mocha definitions from `_sass/_catppuccin.scss` to reduce size.
  - Removed redundant `assets/css/catppuccin.css` file.
  - Centralized theme switching logic in `_includes/custom_style.html`.
- **Layout & Typography Improvements (2026-02-04):**
  - **Sidebar:** Refactored for better hierarchy. Increased title size/weight, added clear section headers for Pages, Posts, and Menu (Edit), and improved spacing.
  - **Top Bar:** Transformed action links (Add, Edit, Delete, etc.) into prominent button-style elements with interactive states.
  - **Search Bar:** Increased size and prominence, adding focus animations and better rounding.
  - **Table of Contents:** Redesigned as a clear, standalone container with a distinct header and improved list styling.
  - **Headings & Body:** Significantly increased font sizes and weights for H1 and H2. Improved body text readability by increasing base font size to 16px and line height to 1.7.
  - **Footer:** Left-aligned footer text to match the main content alignment and added a top border for separation.
- **Link Management Overhaul (2026-02-04):**
  - **Broken Link Fix:** Resolved a major issue where filesystem-relative links (e.g., `../wiki/path/to/Entity.md`) were breaking due to Jekyll's permalink structure.
  - **New Linking Strategy:** Transitioned to a robust Jekyll-compatible format: `[Name]({{ site.baseurl }}/Basename)`. This format works consistently across all pages, regardless of their directory depth.
  - **Script Updates:** 
    - Updated `scripts/apply_links.py` to automatically fix existing broken links and apply new ones using the new format, while protecting other links from double-nesting.
    - Updated `scripts/scan_links.py` to report potential links in the new format.
  - **Workflow Sync:** Updated `.agent/workflows/scan-wiki-links.md` to document the new linking convention.
- **Fixes:**
  - Removed `darkmode.js` integration to prevent conflicts with the new CSS-based theming.
  - Replaced local font references with Google Fonts (Noto Sans) to avoid missing asset issues.
  - Replaced missing local search script with a CDN link for `simple-jekyll-search`.
- **Migration:** Kanka.io entities were previously migrated to Jekyll structure.

## Next Steps

- User verification of the new visual style and functionality.
- Ongoing maintenance of wiki content and links.