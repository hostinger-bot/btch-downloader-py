"""CLI entry point for testing individual btch-downloader platforms.

"""

# pylint: disable=W0718

import asyncio
import json
import sys
from btch_downloader import (
    ttdl, igdl, twitter, youtube, fbdown,
    aio, mediafire, capcut, gdrive, pinterest,
    douyin, xiaohongshu, snackvideo,
    cocofun, spotify, yts, soundcloud,
    threads, kuaishou
)

FUNCTIONS = {
    "ttdl": ttdl,
    "igdl": igdl,
    "twitter": twitter,
    "youtube": youtube,
    "fbdown": fbdown,
    "aio": aio,
    "mediafire": mediafire,
    "capcut": capcut,
    "gdrive": gdrive,
    "pinterest": pinterest,
    "pinterest_search": pinterest,
    "douyin": douyin,
    "xiaohongshu": xiaohongshu,
    "snackvideo": snackvideo,
    "cocofun": cocofun,
    "spotify": spotify,
    "yts": yts,
    "soundcloud": soundcloud,
    "threads": threads,
    "kuaishou": kuaishou,
}


async def main(url, function_name):
    """Call the selected platform function and print result as JSON."""
    func = FUNCTIONS.get(function_name)
    if func is None:
        raise ValueError("Invalid function name")
    try:
        result = await func(url)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        MSG = "Please provide a function name and URL/keyword"
        print(json.dumps({"error": MSG}), file=sys.stderr)
        sys.exit(1)
    fn_name = sys.argv[1]
    target_url = sys.argv[2]
    asyncio.run(main(target_url, fn_name))
