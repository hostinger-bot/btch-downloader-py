---

# btch-downloader

A Python library for downloading content from various social media platforms asynchronously.

## Installation

### Python Installation
Install the library using pip:

```bash
pip install btch-downloader
```

### Node.js Installation
If using a Node.js project, you can install the `btch-downloader` package from npm:

```bash
npm install btch-downloader
```

For Node.js usage details, refer to the [official npm package documentation](https://hostinger-bot.github.io/btch-downloader/).

### Prerequisites
- Python 3.8 or higher (for Python usage)
- Required dependencies: `httpx`, `asyncio` (for Python)
- Some platforms (e.g., Instagram, Twitter) may require authentication or API keys for full functionality. Refer to the [official Python documentation](https://github.com/hostinger-bot/btch-downloader-py) for setup details.

## Usage

### Python Usage
The library provides asynchronous functions to download content from supported platforms. Below is an example demonstrating how to use each downloader function:

```python
import asyncio
from btch_downloader import ttdl, igdl, twitter, youtube, fbdown, aio, mediafire, capcut, gdrive, pinterest

async def main():
    # TikTok Downloader
    tiktok_result = await ttdl("https://vm.tiktok.com/ZGJAmhSrp/")
    print("TikTok:", tiktok_result)

    # Instagram Downloader
    instagram_result = await igdl("https://www.instagram.com/p/ByxKbUSnubS/?utm_source=ig_web_copy_link")
    print("Instagram:", instagram_result)
    
    # YouTube Downloader
    youtube_result = await youtube("https://www.youtube.com/watch?v=Z28dtg_QmFw")
    print("YouTube:", youtube_result)
    
    # Facebook Downloader
    facebook_result = await fbdown("https://www.facebook.com/watch/?v=1393572814172251")
    print("Facebook:", facebook_result)
    
    # AIO (All-in-One) Downloader
    aio_result = await aio("https://www.facebook.com/watch/?v=1393572814172251")
    print("AIO:", aio_result)
    
    # MediaFire Downloader
    mediafire_result = await mediafire("https://www.mediafire.com/file/941xczxhn27qbby/GBWA_V12.25FF-By.SamMods-.apk/file")
    print("MediaFire:", mediafire_result)
    
    # Capcut Downloader
    capcut_result = await capcut("https://www.capcut.com/template-detail/7299286607478181121?template_id=7299286607478181121&share_token=80302b19-8026-4101-81df-2fd9a9cecb9c&enter_from=template_detail®ion=ID&language=in&platform=copy_link&is_copy_link=1")
    print("Capcut:", capcut_result)
    
    # Google Drive Downloader
    gdrive_result = await gdrive("https://drive.google.com/file/d/1thDYWcS5p5FFhzTpTev7RUv0VFnNQyZ4/view?usp=drivesdk")
    print("Google Drive:", gdrive_result)
    
    # Pinterest Downloader
    pinterest_result = await pinterest("https://pin.it/4CVodSq")
    print("Pinterest:", pinterest_result)
    
    # Pinterest Search
    pinterest_search_result = await pinterest("Zhao Lusi")
    print("Pinterest Search:", pinterest_search_result)
    
    # Twitter Downloader
    twitter_result = await twitter("https://twitter.com/gofoodindonesia/status/1229369819511709697")
    print("Twitter:", twitter_result)

asyncio.run(main())
```

### Error Handling Example
To handle potential errors (e.g., invalid URLs or network issues), save the following code to a file named `test.py` and run it with a URL or keyword as an argument. Below is an example for all supported functions:

```python
import asyncio
import json
import sys
from btch_downloader import ttdl, igdl, twitter, youtube, fbdown, aio, mediafire, capcut, gdrive, pinterest

async def main(url, function_name):
    try:
        if function_name == "ttdl":
            result = await ttdl(url)
        elif function_name == "igdl":
            result = await igdl(url)
        elif function_name == "twitter":
            result = await twitter(url)
        elif function_name == "youtube":
            result = await youtube(url)
        elif function_name == "fbdown":
            result = await fbdown(url)
        elif function_name == "aio":
            result = await aio(url)
        elif function_name == "mediafire":
            result = await mediafire(url)
        elif function_name == "capcut":
            result = await capcut(url)
        elif function_name == "gdrive":
            result = await gdrive(url)
        elif function_name == "pinterest":
            result = await pinterest(url)
        elif function_name == "pinterest_search":
            result = await pinterest(url)  # For search, URL is a keyword
        else:
            raise ValueError("Invalid function name")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Please provide a function name and URL/keyword"}), file=sys.stderr)
        sys.exit(1)
    function_name = sys.argv[1]
    url = sys.argv[2]
    asyncio.run(main(url, function_name))
```

Run the script with a specific function and URL/keyword, for example:

```bash
python3 test.py ttdl "https://vm.tiktok.com/ZGJAmhSrp/"
python3 test.py igdl "https://www.instagram.com/p/ByxKbUSnubS/?utm_source=ig_web_copy_link"
python3 test.py youtube "https://www.youtube.com/watch?v=Z28dtg_QmFw"
python3 test.py fbdown "https://www.facebook.com/watch/?v=1393572814172251"
python3 test.py aio "https://www.facebook.com/watch/?v=1393572814172251"
python3 test.py mediafire "https://www.mediafire.com/file/941xczxhn27qbby/GBWA_V12.25FF-By.SamMods-.apk/file"
python3 test.py capcut "https://www.capcut.com/template-detail/7299286607478181121?template_id=7299286607478181121&share_token=80302b19-8026-4101-81df-2fd9a9cecb9c&enter_from=template_detail®ion=ID&language=in&platform=copy_link&is_copy_link=1"
python3 test.py gdrive "https://drive.google.com/file/d/1thDYWcS5p5FFhzTpTev7RUv0VFnNQyZ4/view?usp=drivesdk"
python3 test.py pinterest "https://pin.it/4CVodSq"
python3 test.py pinterest_search "Zhao Lusi"
python3 test.py twitter "https://twitter.com/gofoodindonesia/status/1229369819511709697"
```

## Features
- Download content from TikTok, Instagram, Twitter, YouTube, Facebook, MediaFire, Capcut, Google Drive, and Pinterest.
- Asynchronous API calls using `httpx` for efficient performance (Python).
- Simple and consistent interface across all platforms.
- Support for Pinterest search by keyword.

## API Reference

Each downloader function accepts a URL (or keyword for Pinterest search) and returns a dictionary containing the downloaded content details.

### Common Parameters
- `url` (str): The URL of the content to download (e.g., video, image, or file link). For Pinterest search, provide a keyword instead.
- Optional: Some functions may accept additional parameters (e.g., authentication tokens). Check the [official Python documentation](https://github.com/hostinger-bot/btch-downloader-py) or [Node.js documentation](https://github.com/hostinger-bot/btch-downloader) for details.

### Return Value
Each function returns a dictionary with the following possible keys:
- `url` (str): Direct URL to the downloaded content (e.g., video or image file).
- `metadata` (dict): Additional information about the content (e.g., title, author, or resolution).
- `error` (str): Error message if the download fails (only in case of failure).

### Supported Platforms and Functions
| Function     | Platform       | Description                                      |
|--------------|----------------|--------------------------------------------------|
| `ttdl`       | TikTok         | Downloads videos or images from TikTok.          |
| `igdl`       | Instagram      | Downloads posts, reels, or stories from Instagram.|
| `twitter`    | Twitter        | Downloads media from Twitter posts.              |
| `youtube`    | YouTube        | Downloads videos or audio from YouTube.          |
| `fbdown`     | Facebook       | Downloads videos from Facebook.                  |
| `aio`        | All-in-One     | Attempts to download from any supported platform. |
| `mediafire`  | MediaFire      | Downloads files from MediaFire links.            |
| `capcut`     | Capcut         | Downloads templates or videos from Capcut.       |
| `gdrive`     | Google Drive   | Downloads files from Google Drive.               |
| `pinterest`  | Pinterest      | Downloads pins or searches for content by keyword.|

### Notes
- Some platforms may require authentication or have rate limits. Ensure you comply with each platform's terms of service.
- The `aio` function automatically detects the platform from the URL but may be slower than platform-specific functions.
- For large files or slow networks, ensure proper error handling and timeouts.

## Documentation
- For detailed Python usage, including advanced configuration and authentication setup, visit [https://github.com/hostinger-bot/btch-downloader-py](https://github.com/hostinger-bot/btch-downloader-py).
- For Node.js usage, refer to [https://github.com/hostinger-bot/btch-downloader](https://github.com/hostinger-bot/btch-downloader).

## License
MIT License

---