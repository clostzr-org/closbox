#!/usr/bin/env python3
"""Open Android Settings' app dashboard or running-services screen.

Usage: apps.py [dashboard|services]
"""

import argparse
import subprocess


ACTIVITIES = {
    "dashboard": "com.android.settings/.Settings$AppDashboardActivity",
    "services": "com.android.settings/.RunningServices",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "screen",
        nargs="?",
        choices=ACTIVITIES,
        default="services",
        help="Settings screen to open (default: services)",
    )
    args = parser.parse_args()

    try:
        return subprocess.run(
            ["am", "start", "-n", ACTIVITIES[args.screen]],
            check=False,
        ).returncode
    except OSError as error:
        parser.exit(1, f"Unable to start Android activity: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
