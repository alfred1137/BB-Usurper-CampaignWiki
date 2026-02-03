# Active Context

The migration of Kanka.io entities to the Jekyll wiki structure has been completed. This involved:

- Converting 7 Kanka journals to Jekyll `_posts/` with correct dates and slugs.
- Converting 51 Kanka entities (Characters, Locations, Races, etc.) to Jekyll `wiki/` pages.
- Organizing gallery assets into `assets/characters/`, `assets/_posts/`, etc.
- Resolving internal Kanka links to wiki-style `[[Name]]` links.

The migration was performed using a custom Python script `migrate_kanka.py`.

Next steps:

- User verification of the migrated content.
- Potential cleanup of the migration script.
