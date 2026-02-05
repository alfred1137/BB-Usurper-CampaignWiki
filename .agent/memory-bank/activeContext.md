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
- **Layout Overhaul (2026-02-05):**
  - **3-Column Grid:** Migrated from a 2-column layout to a modern 3-column grid:
    - **Fixed Sidebar (300px):** Full-height fixed navigation.
    - **Main Content (1fr):** Flexible center column for readability.
    - **Right Column (300px):** New column for metadata (Page Information) and Table of Contents (TOC).
  - **Search Bar:** Expanded to full width of the main content area for better usability. Improved dropdown styling and resolved a "strange line" issue caused by the empty search results border.
  - **Page Actions:** Moved action buttons (Edit, History, etc.) to the right-hand metadata column, aligning them to the right.
- **Technical Environment Fixes (2026-02-05):**
  - **UTF-8 Enforcement:** Fixed Sass compilation errors by strictly enforcing UTF-8 encoding in `Dockerfile.github` and `_config.yml`.
  - **Build Performance:** Configured `exclude` in `_config.yml` to skip non-content directories (`.agent`, `.log`, `scripts`, etc.), significantly speeding up Jekyll generation.
- **Content Improvements:**
  - **Index Redirect:** Added `index.md` in the root with a JS redirect to the main Campaign Chronicle to avoid directory index listings.
  - **Markdown Fixes:** Corrected malformed headers (e.g., `## Journals`) in the main chronicle post.
- **Link Management Overhaul (2026-02-04):**
  - **Broken Link Fix:** Resolved a major issue where filesystem-relative links (e.g., `../wiki/path/to/Entity.md`) were breaking due to Jekyll's permalink structure.
  - **New Linking Strategy:** Transitioned to a robust Jekyll-compatible format: `[Name]({{ site.baseurl }}/Basename)`. This format works consistently across all pages, regardless of their directory depth.
  - **Script Updates:** 
    - Updated `scripts/apply_links.py` to automatically fix existing broken links and apply new ones using the new format, while protecting other links from double-nesting.
    - Updated `scripts/scan_links.py` to report potential links in the new format.
  - **Workflow Sync:** Updated `.agent/workflows/scan-wiki-links.md` to document the new linking convention.
- **Asset Management Fix (2026-02-04):**
  - **Folder Rename:** Renamed `assets/_posts` to `assets/posts`. In Jekyll, folders starting with an underscore (outside the root) are ignored during build, causing images in blog posts to break.
  - **Reference Update:** Updated all image links in `_posts` to point to `assets/posts`.
  - **Convention:** Established that post-specific assets should live in `assets/posts` or `assets/images`, avoiding leading underscores in asset subdirectories.
- **Fixes:**
  - Removed `darkmode.js` integration to prevent conflicts with the new CSS-based theming.
  - Replaced local font references with Google Fonts (Noto Sans) to avoid missing asset issues.
  - Replaced missing local search script with a CDN link for `simple-jekyll-search`.
- **Migration:** Kanka.io entities were previously migrated to Jekyll structure.

## Next Steps

- User verification of the new visual style and functionality.
- Ongoing maintenance of wiki content and links.