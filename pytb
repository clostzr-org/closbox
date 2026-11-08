#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run_ytdlp(arguments, *, capture_output=False):
    try:
        return subprocess.run(
            ["yt-dlp", *arguments],
            check=True,
            capture_output=capture_output,
            text=True,
        )
    except FileNotFoundError as error:
        raise RuntimeError("yt-dlp is required. Install it and ensure it is on PATH.") from error
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() if error.stderr else str(error)
        raise RuntimeError(f"yt-dlp failed: {detail}") from error


def playlist_entries(playlist_url):
    result = run_ytdlp(
        ["--flat-playlist", "--dump-single-json", "--no-warnings", playlist_url],
        capture_output=True,
    )
    try:
        playlist = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"yt-dlp returned invalid playlist data: {error}") from error

    entries = playlist.get("entries") or []
    videos = []
    for entry in entries:
        if not entry:
            continue
        video_id = entry.get("id")
        url = entry.get("webpage_url") or entry.get("url")
        if not url or not url.startswith(("http://", "https://")):
            if not video_id:
                continue
            url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": entry.get("title") or video_id or url, "url": url})
    return playlist.get("title") or "Playlist", videos


def parse_selection(selection, video_count):
    if not selection:
        return list(range(video_count))

    indexes = []
    for number in selection:
        if number < 1 or number > video_count:
            raise ValueError(f"Video number out of range: {number} (choose 1-{video_count})")
        index = number - 1
        if index not in indexes:
            indexes.append(index)
    return indexes


def prompt_selection(video_count):
    while True:
        choice = input(
            "Enter video numbers separated by commas, 'a' for all, or 'q' to quit: "
        ).strip().lower()
        if choice == "q":
            return []
        if choice == "a":
            return list(range(video_count))
        try:
            return parse_selection([int(part.strip()) for part in choice.split(",")], video_count)
        except ValueError as error:
            print(f"Invalid selection: {error}")


def build_download_arguments(videos, output_dir, audio_only, resolution):
    arguments = ["--no-warnings", "--output", str(output_dir / "%(title)s.%(ext)s")]
    if audio_only:
        arguments.extend(["--extract-audio", "--audio-format", "mp3"])
    elif resolution != "highest":
        height = resolution.removesuffix("p")
        if not height.isdigit() or int(height) < 1:
            raise ValueError("Resolution must be 'highest' or a height such as '720p'.")
        arguments.extend(
            ["--format", f"bestvideo[height<={height}]+bestaudio/best[height<={height}]"]
        )
    arguments.extend(video["url"] for video in videos)
    return arguments


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="List and download videos from a playlist with yt-dlp."
    )
    parser.add_argument("playlist_url", help="YouTube playlist URL")
    parser.add_argument(
        "-s",
        "--selection",
        nargs="+",
        type=int,
        metavar="NUMBER",
        help="1-based video numbers to download (downloads all by default)",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Prompt to select videos interactively",
    )
    parser.add_argument(
        "-r",
        "--resolution",
        default="highest",
        help="Maximum video height, e.g. 720p, or 'highest' (video mode only)",
    )
    parser.add_argument(
        "-a",
        "--audio",
        action="store_true",
        help="Extract audio as MP3 instead of downloading video",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="Download directory (defaults to downloads for audio, current directory for video)",
    )
    args = parser.parse_args(argv)

    if args.selection and args.interactive:
        parser.error("--selection and --interactive cannot be used together")

    if not shutil.which("yt-dlp"):
        parser.error("yt-dlp is required. Install it and ensure it is on PATH.")

    try:
        title, videos = playlist_entries(args.playlist_url)
    except RuntimeError as error:
        parser.error(str(error))
    if not videos:
        print(f"No videos found in playlist: {title}")
        return 1

    print(f"Playlist: {title}")
    print("-" * 40)
    for number, video in enumerate(videos, start=1):
        print(f"{number}. {video['title']}")

    try:
        indexes = (
            prompt_selection(len(videos))
            if args.interactive
            else parse_selection(args.selection, len(videos))
        )
        if not indexes:
            print("No videos selected.")
            return 0
        output_dir = args.output_dir or Path("downloads" if args.audio else ".")
        output_dir.mkdir(parents=True, exist_ok=True)
        download_arguments = build_download_arguments(
            [videos[index] for index in indexes],
            output_dir,
            args.audio,
            args.resolution,
        )
        run_ytdlp(download_arguments)
    except (OSError, RuntimeError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    print("Download complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
