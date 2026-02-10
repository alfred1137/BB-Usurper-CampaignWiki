---
description: Update navigation links between campaign journal entries chronologically.
---

This workflow synchronizes the "Read next chapter" links at the bottom of each campaign journal post (including drafts). It ensures readers can navigate through the story in chronological order.

### Steps

1. **Prerequisites**
   - Ensure new posts follow the naming convention `YYYY-MM-DD-session-X-...md`.
   - Ensure the `scripts/update_post_nav.py` script exists.

// turbo
2. **Execute Update Script**
   Run the navigation update script from the root directory:
   ```powershell
   python scripts/update_post_nav.py
   ```

### Verification
- Check the bottom of the modified files to ensure the `NEXT` or previous link has been replaced with the title of the next chronological session.
- Ensure that the last post in the sequence is either left as "Coming soon..." or handled appropriately.

### Troubleshooting
- If a post isn't being linked, check if its session number can be parsed from the filename or the frontmatter title.
- If links are broken, verify the relative paths between the `_posts` and `_posts/draft` directories.
