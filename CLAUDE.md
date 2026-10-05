# Coding interview prep

Python implementations of data structures and algorithms, plus revision notes. The repo is pushed to GitHub, and the notes are meant to be read there.

## Layout

- `graph/`: graph code (`traversal_list.py` for the adjacency list, `traversal_matrix.py` for the adjacency matrix)
- `cheatsheet/`: one Markdown cheatsheet per topic, with `README.md` as the index
- `images/`: generated images plus generator scripts; `images/README.md` maps each image to its code

New topics (arrays, trees, dynamic programming, ...) get their own code folder and their own `cheatsheet/<topic>.md`.

## Keep the cheatsheets in sync (important)

The code changes often. **Whenever code in a topic folder is added or changed, update that topic's cheatsheet in the same change:**

1. Update the code snippets in `cheatsheet/<topic>.md` so they match the code.
2. Add any new important points the change brings up.
3. For a new topic, create `cheatsheet/<topic>.md` and add a row to `cheatsheet/README.md`.
4. If an image in `images/` shows the changed code, update its generator script, rerun it, and fix the paths in `images/README.md`.

## Cheatsheet format

Keep sheets minimal. The user rejected a long format with tables, diagrams and traces.

1. Title and links to the source files
2. **Important points**: one line each
3. **Brief code** per algorithm: shortest form of the repo's code, with each variant (for example, adjacency list and matrix) as its own labeled block

Use GitHub-flavored Markdown and relative links.

## Code style

- Keep comments very brief: one line, saying why rather than what.
- Each file runs on its own: `python3 graph/traversal_list.py`.
