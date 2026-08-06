import argparse
import os

from ui import PlantifyUI


def parse_source(value: str) -> int | str:
    if value.isdigit():
        return int(value)
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Plantify AI with a mobile camera stream.")
    parser.add_argument(
        "--source",
        default=parse_source(os.environ.get("PHONE_STREAM_URL", "0")),
        type=parse_source,
        help="Camera source: device index or stream URL. Defaults to PHONE_STREAM_URL or 0.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app = PlantifyUI(camera_source=args.source)
    app.run()


if __name__ == "__main__":
    main()
