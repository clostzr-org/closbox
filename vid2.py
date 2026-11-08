#!/usr/bin/env python3
import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path


VIDEO_EXTENSIONS = {".avi", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".webm"}
MP4_INPUT_EXTENSIONS = VIDEO_EXTENSIONS - {".mp4"} | {".gif"}


def build_command(mode, input_path, output_path, interval):
    command = ["ffmpeg", "-hide_banner", "-nostdin", "-n", "-i", str(input_path)]

    if mode == "gif":
        command.extend(
            [
                "-filter_complex",
                "[0:v]fps=15,scale=480:-1:flags=lanczos,split[s0][s1];"
                "[s0]palettegen[p];[s1][p]paletteuse[v]",
                "-map",
                "[v]",
                "-loop",
                "0",
            ]
        )
    elif mode == "mp4":
        command.extend(
            [
                "-movflags",
                "+faststart",
                "-pix_fmt",
                "yuv420p",
                "-vf",
                "fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2",
                "-g",
                "30",
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "23",
            ]
        )
    else:
        command.extend(
            [
                "-vf",
                f"fps=1/{interval:g}",
                "-fps_mode",
                "vfr",
                "-start_number",
                "1",
                str(output_path / "image-%03d.jpg"),
            ]
        )
        return command

    command.append(str(output_path))
    return command


def convert_file(mode, input_path, output_dir, interval):
    if mode == "images":
        output_path = output_dir / f"{input_path.stem}-images"
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        extension = ".gif" if mode == "gif" else ".mp4"
        output_path = output_dir / f"{input_path.stem}{extension}"
        if input_path.resolve() == output_path.resolve():
            print(f"[SKIPPED] Output would overwrite input: {input_path}")
            return False
        if output_path.exists():
            print(f"[SKIPPED] Output already exists: {output_path}")
            return False

    command = build_command(mode, input_path, output_path, interval)
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        raise RuntimeError("ffmpeg is required. Install it and ensure it is on PATH.")
    except subprocess.CalledProcessError as error:
        print(f"[ERROR] Conversion failed for {input_path} (exit code {error.returncode}).", file=sys.stderr)
        return True

    print(f"[DONE] {input_path} -> {output_path}")
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert videos to GIF/MP4 or extract frames using FFmpeg."
    )
    parser.add_argument("mode", choices=("gif", "mp4", "images"), help="Conversion to perform")
    parser.add_argument("path", type=Path, help="Input video file or directory")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="Output directory (defaults to the input file's or directory's parent)",
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=float,
        default=64,
        help="Seconds between extracted frames in images mode (default: 64)",
    )
    args = parser.parse_args(argv)

    input_path = args.path.expanduser().absolute()
    if not input_path.exists():
        parser.error(f"input path does not exist: {input_path}")
    if not input_path.is_file() and not input_path.is_dir():
        parser.error(f"input path is not a file or directory: {input_path}")
    if not math.isfinite(args.interval) or args.interval <= 0:
        parser.error("interval must be a positive finite number")
    if not shutil.which("ffmpeg"):
        parser.error("ffmpeg is required. Install it and ensure it is on PATH.")

    output_dir = args.output_dir.expanduser().absolute() if args.output_dir else (
        input_path.parent if input_path.is_file() else input_path
    )
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        parser.error(f"cannot create output directory {output_dir}: {error}")

    if input_path.is_file():
        inputs = [input_path]
    else:
        allowed_extensions = {
            "gif": VIDEO_EXTENSIONS,
            "mp4": MP4_INPUT_EXTENSIONS,
            "images": VIDEO_EXTENSIONS,
        }[args.mode]
        inputs = sorted(
            path
            for path in input_path.iterdir()
            if path.is_file() and path.suffix.lower() in allowed_extensions
        )

    if args.mode == "mp4":
        inputs = [path for path in inputs if path.suffix.lower() in MP4_INPUT_EXTENSIONS]
    elif args.mode in ("gif", "images"):
        inputs = [path for path in inputs if path.suffix.lower() in VIDEO_EXTENSIONS]

    if not inputs:
        print("No supported input videos found.")
        return 0

    failures = 0
    try:
        for source in inputs:
            failures += convert_file(args.mode, source, output_dir, args.interval)
    except (OSError, RuntimeError) as error:
        print(error, file=sys.stderr)
        return 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
