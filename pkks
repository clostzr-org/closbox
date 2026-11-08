#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u31f0-\u31ff\u3400-\u4dbf\u4e00-\u9fff]")
INVALID_FILENAME_RE = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WHITESPACE_RE = re.compile(r"\s+")
NAME_SEPARATOR = "_-_"


def setup_converter():
    try:
        import pykakasi
    except ImportError as error:
        raise RuntimeError("pykakasi is required. Install it with: pip install pykakasi") from error
    return pykakasi.kakasi()


def has_japanese(text):
    return bool(JAPANESE_RE.search(text))


def convert_to_kunrei(text, converter):
    return "".join(fragment["kunrei"] for fragment in converter.convert(text))


def translate_text(text, translator, cache):
    if not translator:
        return ""
    if text in cache:
        return cache[text]

    try:
        result = subprocess.run(
            [translator, "-brief", "-to", "en", "-no-warn", text],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"[WARNING] Translation failed for {text!r}: {error}", file=sys.stderr)
        cache[text] = ""
        return ""

    if result.returncode:
        message = result.stderr.strip() or f"translator exited with status {result.returncode}"
        print(f"[WARNING] Translation failed for {text!r}: {message}", file=sys.stderr)
        cache[text] = ""
        return ""

    cache[text] = result.stdout.strip()
    return cache[text]


def clean_component(text):
    text = WHITESPACE_RE.sub("_", text.strip())
    return INVALID_FILENAME_RE.sub("_", text).rstrip(" .")


def process_filename(filename, converter, translator=None, translation_cache=None):
    name, extension = os.path.splitext(filename)
    if not has_japanese(name) or NAME_SEPARATOR in name:
        return filename

    original = clean_component(name)
    romaji = clean_component(convert_to_kunrei(name, converter))
    if not original or not romaji:
        return filename

    parts = [original, romaji]
    if translation_cache is None:
        translation_cache = {}
    english = clean_component(translate_text(name, translator, translation_cache))
    if english and english.casefold() not in {original.casefold(), romaji.casefold()}:
        parts.append(english)

    return NAME_SEPARATOR.join(parts) + extension


def rename_path(path, converter, translator, translation_cache):
    new_name = process_filename(path.name, converter, translator, translation_cache)
    if new_name == path.name:
        print(f"[SKIPPED] Already formatted or no Japanese: {path.name}")
        return False

    destination = path.with_name(new_name)
    if os.path.lexists(destination):
        print(f"[ERROR] Destination already exists: {destination}", file=sys.stderr)
        return True

    try:
        path.rename(destination)
    except OSError as error:
        print(f"[ERROR] Could not rename {path}: {error}", file=sys.stderr)
        return True

    print(f"[RENAMED] {path.name}\n       -> {new_name}")
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Rename Japanese file and directory names to Original_-_Kunrei_-_English."
    )
    parser.add_argument("path", type=Path, help="File or directory to process recursively")
    parser.add_argument(
        "--no-translate",
        action="store_true",
        help="Skip English translation and only add the original and Kunrei names",
    )
    args = parser.parse_args()

    target = args.path.expanduser().absolute()
    if not target.exists():
        parser.error(f"path does not exist: {target}")
    if not target.is_file() and not target.is_dir():
        parser.error(f"path is not a file or directory: {target}")

    translator = None
    if not args.no_translate:
        translator = shutil.which("trans")
        if not translator:
            print(
                "[WARNING] translate-shell ('trans') not found; "
                "continuing without English translations.",
                file=sys.stderr,
            )

    try:
        converter = setup_converter()
    except RuntimeError as error:
        parser.error(str(error))

    translation_cache = {}
    errors = 0
    if target.is_file():
        errors += rename_path(target, converter, translator, translation_cache)
    else:
        # Process deepest paths first so renaming a directory cannot invalidate its children.
        paths = sorted(target.rglob("*"), key=lambda path: len(path.parts), reverse=True)
        for path in paths:
            if path.is_file() or path.is_dir():
                errors += rename_path(path, converter, translator, translation_cache)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
