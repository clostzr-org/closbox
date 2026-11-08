#!/usr/bin/env python3
"""Batch-rename files in a directory.

Usage: bren.py [directory|tcg]
"""

import os
import subprocess
import sys
from pathlib import Path


def create_windows_command_file():
    if os.name != "nt":
        return

    script_path = Path(__file__).resolve()
    command_path = script_path.with_suffix(".cmd")
    if command_path.exists():
        return

    contents = (
        "@echo off\r\n"
        f'python "%~dpn0.py" %*\r\n'
        "exit /b %errorlevel%\r\n"
    )
    command_path.write_text(contents, encoding="utf-8", newline="")
    print(f"Created command file: {command_path}")


def get_directory(argument):
    if argument == "tcg":
        result = subprocess.run(
            ["termux-clipboard-get"],
            capture_output=True,
            text=True,
            check=True,
        )
        argument = result.stdout.strip()

    if argument:
        directory = Path(argument).expanduser()
        if not directory.is_dir():
            raise ValueError(f"Not a directory: {argument}")
    else:
        directory = Path.cwd()

    return directory.resolve()


def get_rename_options():
    old_text = input("Text to replace (blank to skip): ")
    new_text = input("Replace with: ") if old_text else ""
    if old_text and not new_text:
        print("Replacement text is empty; matching text will be removed.")

    prefix = input("Prefix (blank for none): ")
    suffix = input("Suffix (blank for none): ")
    return old_text, new_text, prefix, suffix


def build_changes(directory, old_text, new_text, prefix, suffix):
    changes = []
    for source in sorted(directory.iterdir()):
        if not source.is_file():
            continue

        name = source.name.replace(old_text, new_text) if old_text else source.name
        if prefix:
            name = f"{prefix}_{name}"
        if suffix:
            stem, extension = os.path.splitext(name)
            name = f"{stem}_{suffix}{extension}"
        if name != source.name:
            changes.append((source, source.with_name(name)))

    return changes


def validate_changes(changes):
    destinations = set()

    for source, destination in changes:
        if destination in destinations:
            raise ValueError(f"Multiple files would be renamed to: {destination.name}")
        destinations.add(destination)
        if destination.exists():
            raise ValueError(f"Destination already exists: {destination.name}")


def batch_rename(directory):
    print(f"Batch Renamer\nDirectory: {directory}")
    old_text, new_text, prefix, suffix = get_rename_options()
    changes = build_changes(directory, old_text, new_text, prefix, suffix)

    if not changes:
        print("No files need renaming.")
        return 0

    try:
        validate_changes(changes)
    except ValueError as error:
        print(f"Cannot rename files: {error}", file=sys.stderr)
        return 1

    print("\nPreview:")
    for source, destination in changes:
        print(f"{source.name} -> {destination.name}")

    if input("\nConfirm rename (y/n)? ").strip().lower() != "y":
        print("Rename cancelled.")
        return 0

    failed = False
    for source, destination in changes:
        try:
            source.rename(destination)
            print(f"Renamed '{source.name}' to '{destination.name}'.")
        except OSError as error:
            failed = True
            print(f"Error renaming '{source.name}': {error}", file=sys.stderr)

    print("Batch renaming complete.")
    return 1 if failed else 0


def main():
    try:
        create_windows_command_file()
        if len(sys.argv) > 2:
            print(f"Usage: {Path(sys.argv[0]).name} [directory|tcg]", file=sys.stderr)
            return 2
        directory = get_directory(sys.argv[1] if len(sys.argv) == 2 else "")
        return batch_rename(directory)
    except (OSError, subprocess.SubprocessError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nRename cancelled.", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
