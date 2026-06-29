---
name: btch-downloader-py
description: "Use this skill whenever the user wants to download media (videos, images, audio) from social media platforms using the btch-downloader Python client SDK. Triggers include: downloading from Instagram, TikTok, YouTube, Facebook, Twitter/X, Pinterest, Spotify, SoundCloud, Threads, CapCut, Google Drive, MediaFire, Douyin, SnackVideo, Xiaohongshu, Xiaohongshu Profile, Cocofun, or Kuaishou using Python; using the igdl, ttdl, fbdown, youtube, twitter, xiaohongshu_profile, or aio functions; building a media downloader bot or app in Python. Do NOT use for JavaScript/TypeScript-based downloaders."
license: MIT
---

# btch-downloader-py

## Overview

`btch-downloader-py` is a lightweight Python client SDK by [@BOTCAHX](https://github.com/hostinger-bot) for fetching downloadable media links from social media platforms. It does **not** directly scrape platforms — all resolution is handled by the backend service at `backend1.tioo.eu.org`. Each function is an async coroutine returning a dict with media URLs and metadata.

- **PyPI:** `btch-downloader`
- **GitHub:** `hostinger-bot/btch-downloader-py`
- **Backend API:** `https://backend1.tioo.eu.org`

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.8+ |
| Dependency | httpx >= 0.24.0 |

## Installation

```bash
pip install btch-downloader
```

## Quick Reference — All Functions

| Function | Platform | Input |
|----------|----------|-------|
| `igdl` | Instagram | Post/reel URL |
| `ttdl` | TikTok | Video URL |
| `fbdown` | Facebook | Video/watch URL |
| `twitter` | Twitter / X | Tweet URL |
| `youtube` | YouTube | Video URL |
| `mediafire` | MediaFire | File URL (unmaintained) |
| `capcut` | CapCut | Template URL |
| `gdrive` | Google Drive | Share URL |
| `pinterest` | Pinterest | Pin URL or search query |
| `douyin` | Douyin (抖音) | Video URL |
| `xiaohongshu` | Xiaohongshu (小红书) | Post URL |
| `xiaohongshu_profile` | Xiaohongshu Profile | Profile URL |
| `snackvideo` | SnackVideo | Video URL |
| `cocofun` | Cocofun | Post URL |
| `spotify` | Spotify | Track URL |
| `yts` | YouTube Search | Search query string |
| `soundcloud` | SoundCloud | Track URL |
| `threads` | Threads | Post URL |
| `kuaishou` | Kuaishou | Video URL |
| `aio` | Auto-detect | Any supported URL (unmaintained) |

## Usage

All functions share the same signature: `async fn(url: str) -> dict`

```python
import asyncio
from btch_downloader import ttdl, igdl, spotify, yts

async def main():
    # TikTok
    result = await ttdl("https://www.tiktok.com/@omagadsus/video/7025456384175017243")
    print(result)

    # Spotify
    result = await spotify("https://open.spotify.com/track/3zakx7RAwdkUQlOoQ7SJRt")
    print(result)

    # YouTube Search
    result = await yts("movie title 2023")
    print(result)

asyncio.run(main())
```

### Error Handling

Every function returns a dict. On failure, the dict contains `"status": False` and a `"message"` key. Always check the response:

```python
result = await ttdl(url)
if isinstance(result, dict) and result.get("status") is False:
    print(f"Error: {result['message']}")
else:
    # use result
    pass
```

## Important Notes

- Only public media can be downloaded. Private content is not accessible.
- This SDK is not affiliated with or endorsed by any of the supported platforms.
- Always ensure you have the right to download and use the media before doing so.
- `mediafire` and `aio` support are **no longer maintained**.
- The backend (`backend1.tioo.eu.org`) must be reachable; all actual resolution happens there.
