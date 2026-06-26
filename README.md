# btch-downloader
[![Pylint](https://github.com/hostinger-bot/btch-downloader-py/actions/workflows/pylint.yml/badge.svg)](https://github.com/hostinger-bot/btch-downloader-py/actions/workflows/pylint.yml)

A lightweight Python library for downloading videos, images, and audio from Instagram, TikTok, YouTube, Capcut, Pinterest, Twitter, X, Google Drive, MediaFire, Douyin, SnackVideo, Xiaohongshu, Cocofun, Spotify, Youtube Search, SoundCloud, Threads, Kuaishou and Facebook.

## Installation

### Python Installation
Install the library using pip:

```bash
pip install btch-downloader
```

### Prerequisites
- Python 3.8 or higher
- Required dependencies: `httpx`
- Full Documentation [Official documentation](https://github.com/hostinger-bot/btch-downloader-py).

## Usage

### Basic Usage
The library provides asynchronous functions to download content from supported platforms.

```python
import asyncio
from btch_downloader import ttdl, igdl, spotify, yts

async def main():
    # TikTok Downloader
    tiktok_result = await ttdl("https://www.tiktok.com/@omagadsus/video/7025456384175017243")
    print("TikTok:", tiktok_result)

    # Spotify Downloader
    spotify_result = await spotify("https://open.spotify.com/track/3zakx7RAwdkUQlOoQ7SJRt")
    print("Spotify:", spotify_result)
    
    # YouTube Search
    yts_result = await yts("movie title 2023")
    print("YouTube Search:", yts_result)

asyncio.run(main())
```

## Supported Platforms and Example URLs

| Function       | Platform       | Example URL / Query                                                                 |
|----------------|----------------|-----------------------------------------------------------------------------------|
| `ttdl`         | TikTok         | `https://www.tiktok.com/@omagadsus/video/7025456384175017243`                     |
| `igdl`         | Instagram      | `https://www.instagram.com/reel/DKPtUL_S9Nh/?igsh=MTE1dTVkb2E4NTFmcw==`           |
| `fbdown`       | Facebook       | `https://www.facebook.com/netflix/videos/1393572814172251/`                       |
| `twitter`      | Twitter/X      | `https://twitter.com/gofoodindonesia/status/1229369819511709697`                  |
| `youtube`      | YouTube        | `https://youtu.be/C8mJ8943X80`                                                    |
| `capcut`       | Capcut         | `https://www.capcut.com/template-detail/7299286607478181121`                      |
| `gdrive`       | Google Drive   | `https://drive.google.com/file/d/1thDYWcS5p5FFhzTpTev7RUv0VFnNQyZ4/view`          |
| `pinterest`    | Pinterest      | `https://pin.it/4CVodSq` or query (e.g., "Zhao Lusi")                             |
| `douyin`       | Douyin         | `https://v.douyin.com/ikq8axJ/`                                                   |
| `xiaohongshu`  | Xiaohongshu    | `http://xhslink.com/o/21DKXV988zp`                                                |
| `xiaohongshu_profile` | Xiaohongshu Profile | `https://www.xiaohongshu.com/user/profile/abc123`                                 |
| `snackvideo`   | SnackVideo     | `https://s.snackvideo.com/p/j9jKr9dR`                                             |
| `cocofun`      | Cocofun        | `https://www.icocofun.com/share/post/379250110809`                                |
| `spotify`      | Spotify        | `https://open.spotify.com/track/3zakx7RAwdkUQlOoQ7SJRt`                           |
| `soundcloud`   | SoundCloud     | `https://soundcloud.com/issabella-marchelina/sisa-rasa-mahalini-official-audio`   |
| `threads`      | Threads        | `https://www.threads.net/@cindyyuvia/post/C_Nqx3khgkI/`                           |
| `kuaishou`     | Kuaishou       | `https://v.kuaishou.com/JT195ZHT`                                                 |
| `yts`          | YT Search      | `movie title 2023` (Query)                                                        |
| `aio`*         | All-in-One     | `https://www.tiktok.com/@omagadsus/video/7025456384175017243`                     |
| `mediafire`*   | MediaFire      | `https://www.mediafire.com/file/941xczxhn27qbby/GBWA_V12.25FF-By.SamMods-.apk/file`|

*\*Unmaintained*

## Features
- Download content from 17+ social media platforms.
- Support for YouTube Search (`yts`).
- Asynchronous API calls using `httpx`.
- Simple and consistent interface across all services.

## License
MIT License
