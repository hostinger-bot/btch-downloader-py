"""Bulk integration tests for btch-downloader against live backend.

Tests all platform functions using official example URLs.
"""
# pylint: disable=W0718

import asyncio
import json
from btch_downloader import (
    ttdl, igdl, twitter, youtube, fbdown,
    aio, mediafire, capcut, gdrive, pinterest,
    douyin, xiaohongshu, xiaohongshu_profile,
    snackvideo, cocofun, spotify, yts,
    soundcloud, threads, kuaishou,
)

# Test cases for each platform using official examples
TEST_CASES = {
    "ttdl": "https://www.tiktok.com/@omagadsus/video/7025456384175017243",
    "igdl": "https://www.instagram.com/reel/DKPtUL_S9Nh/?igsh=MTE1dTVkb2E4NTFmcw==",
    "twitter": "https://twitter.com/gofoodindonesia/status/1229369819511709697",
    "youtube": "https://youtu.be/C8mJ8943X80",
    "fbdown": "https://www.facebook.com/netflix/videos/1393572814172251/",
    "capcut": "https://www.capcut.com/template-detail/7299286607478181121",
    "gdrive": "https://drive.google.com/file/d/1thDYWcS5p5FFhzTpTev7RUv0VFnNQyZ4/view",
    "pinterest": "https://pin.it/4CVodSq",
    "douyin": "https://v.douyin.com/ikq8axJ/",
    "xiaohongshu": "http://xhslink.com/o/21DKXV988zp",
    "xiaohongshu_profile": "https://xhslink.com/m/mHN7PjTniV",
    "snackvideo": "https://s.snackvideo.com/p/j9jKr9dR",
    "cocofun": "https://www.icocofun.com/share/post/379250110809",
    "spotify": "https://open.spotify.com/track/3zakx7RAwdkUQlOoQ7SJRt",
    "yts": "movie title 2023",
    "soundcloud": "https://soundcloud.com/issabella-marchelina/sisa-rasa-mahalini-official-audio",  # pylint: disable=line-too-long
    "threads": "https://www.threads.net/@cindyyuvia/post/C_Nqx3khgkI/?xmt=AQGzpsCvidh8IwIqOvq4Ov05Zd5raANiVdvCujM_pjBa1Q",  # pylint: disable=line-too-long
    "kuaishou": "https://v.kuaishou.com/JT195ZHT",
    "aio": "https://www.tiktok.com/@omagadsus/video/7025456384175017243",
}

async def run_test(name, func, url):
    """Run a single platform test and return (name, status)."""
    print("\n" + "="*30)
    print(f" TESTING: {name.upper()}")
    print("="*30)
    print(f"URL/Query: {url}")

    try:
        result = await func(url)
        print("RESULT (JSON):")
        print(json.dumps(result, indent=2))

        if isinstance(result, list):
            return name, "SUCCESS" if len(result) > 0 else "EMPTY"
        if isinstance(result, dict) and result.get("status") is False:
            return name, f"FAILED: {result.get('message', 'Unknown Error')}"
        return name, "SUCCESS"

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return name, f"ERROR: {str(e)}"

async def main():
    """Run all platform tests and print summary."""
    print("="*60)
    print("   BTCH-DOWNLOADER BULK TEST (OFFICIAL EXAMPLES)")
    print("="*60)

    functions = {
        "ttdl": ttdl, "igdl": igdl, "twitter": twitter, "youtube": youtube,
        "fbdown": fbdown, "aio": aio, "mediafire": mediafire,
        "capcut": capcut, "gdrive": gdrive, "pinterest": pinterest,
        "douyin": douyin, "xiaohongshu": xiaohongshu,
        "xiaohongshu_profile": xiaohongshu_profile,
        "snackvideo": snackvideo, "cocofun": cocofun,
        "spotify": spotify, "yts": yts,
        "soundcloud": soundcloud, "threads": threads, "kuaishou": kuaishou,
    }

    results = []
    for name_key, test_url in TEST_CASES.items():
        res = await run_test(name_key, functions[name_key], test_url)
        results.append(res)

    print("\n" + "="*60)
    print("   SUMMARY REPORT")
    print("="*60)
    for name, status in results:
        print(f"{name:15}: {status}")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
