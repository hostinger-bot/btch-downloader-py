# btch-downloader

A Python library for downloading content from various social media platforms.

## Installation

```bash
pip install btch-downloader
```

## Usage

```python
import asyncio
from btch_downloader import ttdl, igdl, twitter, youtube, fbdown, aio, mediafire, capcut, gdrive, pinterest

async def main():
    # TikTok
    result = await ttdl("https://www.tiktok.com/@user/video/123456")
    print(result)

    # Instagram
    result = await igdl("https://www.instagram.com/p/abcdef/")
    print(result)

asyncio.run(main())
```

## Features
- Download from TikTok, Instagram, Twitter, YouTube, Facebook, MediaFire, Capcut, Google Drive, Pinterest
- Asynchronous API calls using httpx
- Simple and consistent interface

## Documentation
For detailed usage, visit [https://github.com/hostinger-bot/btch-downloader-py](https://github.com/hostinger-bot/btch-downloader-py).

## License
MIT License