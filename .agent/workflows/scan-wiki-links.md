---
description: scan existing files for potential wiki links
---

# Scan Wiki Links

This workflow helps identify mentions of wiki entities (characters, locations, etc.) in blog posts and other wiki pages that are not yet linked to their respective wiki pages.

## Steps

1. **Verify Entity List**: Ensure all wiki entities are correctly named and placed in the `wiki/` directory.
2. **Run Scan Script**: Execute the helper script to find potential links.

   ```bash
   python scripts/scan_links.py
   ```

3. **Review Matches**: Examine the output of the scan script. Look for:
   - Proper names that should be linked.
   - False positives (common words that happen to match entity names).
   - Occurrences that are already part of a link but weren't caught by the script's simple regex.
4. **Apply Links**: For each valid match, replace the plain text with a Jekyll-compatible link.
   - Format: `[Name]({{ site.baseurl }}/Basename)`
   - *Note*: Use the entity's filename (without `.md`) as the Basename.
5. **Verify**: Use Jekyll's local preview (if available) to ensure the links work correctly.
6. **Automated Application**: Alternatively, run the application script to fix existing links and apply new ones automatically:
   ```bash
   python scripts/apply_links.py
   ```
