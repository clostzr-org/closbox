# closbox

Personal collection of scripts — built, tuned, and iterated on with AI assistance.

## Layout

```
closbox/
├── bin/            # executable entrypoints (what you run directly)
├── lib/            # shared helpers / sourced modules (not executables)
├── scripts/        # work-in-progress scripts, organized by language
│   ├── bash/
│   ├── python/
│   └── js/
├── docs/           # notes per script
└── .github/workflows/  # CI (lint via shellcheck / ruff / eslint as needed)
```

## Conventions

- One task per script; name things verb-first (`backup.sh`, `rename-batch.py`).
- Bash scripts start with `set -euo pipefail` and pass `shellcheck`.
- Python scripts target 3.10+, standard library first; deps documented in the script header.
- Each script gets a short header comment: purpose, usage, author notes.

## Usage

Scripts in `bin/` are meant to be self-contained and safe to symlink into your `PATH`:

```sh
ln -s "$PWD/bin/"* ~/.local/bin/
```

## Status

Freshly cleaned up. Add your first scripts under `scripts/`, promote the stable ones to `bin/`.
