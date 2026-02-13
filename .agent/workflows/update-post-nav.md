---
description: Standardize navigation links in campaign journal entries using Liquid templates.
---

This workflow standardizes the "Read next chapter" navigation table at the bottom of each campaign journal post. It replaces static links with dynamic Liquid filters (`page.next`) to ensure the navigation automatically updates based on the chronological order of posts.

### Steps

1. **Prerequisites**
   - Ensure the `scripts/update_post_nav.py` script exists.
   - Ensure the `_posts` directory contains the target markdown files.

// turbo
2. **Execute Update Script**
   Run the navigation standardization script from the root directory:
   ```powershell
   python scripts/update_post_nav.py
   ```

### Verification
- Check the bottom of the modified files to ensure the static table has been replaced with the Liquid code block.
- Verify that the Liquid code correctly renders the "Next" link or "Coming soon..." message when the site is built.
- **Note:** Since `page.next` relies on Jekyll's date sorting, ensure that posts on the same day have appropriate timestamps or naming to preserve order.

### Troubleshooting
- If the table is not updated, check if the regex in the script matches the existing table format (e.g., check for typos in "Journals" or "Chapter").
