"""btch-downloader-py: Social media downloader client SDK.

All functions delegate to backend1.tioo.eu.org — no direct scraping.

Notes:
    This module uses broad exception handling throughout because all platform
    functions follow the same pattern — catch any error and return a dict with
    ``status: False`` instead of propagating.

    The internal ``_fetch_api`` raises ``Exception`` (not a custom type) for
    the same reason: every error from the backend becomes the caller's error
    message directly.
"""

# pylint: disable=W0718,W0719

import httpx
from btch_downloader import __version__

# Config
BASE_URL = "https://backend1.tioo.eu.org"
DOC_NOTE = "See https://github.com/hostinger-bot/btch-downloader-py"

async def _fetch_api(endpoint, url):
    """Fetch API."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.get(
                f"{BASE_URL}/{endpoint}",
                params={"url": url},
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": f"btch/{__version__}"
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as error:
            raise Exception(f"Error fetching from {endpoint}: {str(error)}") from error
# TikTok Downloader
async def ttdl(url):
    """Download media from TikTok."""
    try:
        data = await _fetch_api("ttdl", url)
        return {
            "developer": "@prm2.0",
            "title": data.get("title"),
            "title_audio": data.get("title_audio"),
            "thumbnail": data.get("thumbnail"),
            "video": data.get("video"),
            "audio": data.get("audio")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Instagram Downloader
async def igdl(url):
    """Download media from Instagram."""
    try:
        data = await _fetch_api("igdl", url)

        if not data or (isinstance(data, dict) and data.get("status") is False):
            return {
                "developer": "@prm2.0",
                "status": False,
                "message": (data.get("msg", "Not Found! Check Url!") if isinstance(data, dict)
                            else "Not Found! Check Url!"),
                "note": DOC_NOTE
            }

        if isinstance(data, list):
            return [
                {
                    "developer": item.get("creator", "@prm2.0"),
                    "thumbnail": item.get("thumbnail"),
                    "url": item.get("url"),
                } for item in data
            ]

        return {
            "developer": "@prm2.0",
            "status": False,
            "message": "Invalid data format received",
            "note": DOC_NOTE
        }

    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": f"Request Failed: {str(error)}",
            "note": DOC_NOTE
        }

# Twitter Downloader
async def twitter(url):
    """Download media from Twitter/X."""
    try:
        data = await _fetch_api("twitter", url)
        return {
            "developer": "@prm2.0",
            "title": data.get("title"),
            "url": data.get("url")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# YouTube Downloader
async def youtube(url):
    """Download media from YouTube."""
    try:
        data = await _fetch_api("youtube", url)
        return {
            "developer": "@prm2.0",
            "title": data.get("title"),
            "thumbnail": data.get("thumbnail"),
            "author": data.get("author"),
            "mp3": data.get("mp3"),
            "mp4": data.get("mp4")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Facebook Downloader
async def fbdown(url):
    """Download media from Facebook."""
    try:
        data = await _fetch_api("fbdown", url)
        return {
            "developer": "@prm2.0",
            "Normal_video": data.get("Normal_video"),
            "HD": data.get("HD")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# AIO Downloader (Unmaintained)
async def aio(url):
    """Download media from any supported platform (unmaintained)."""
    try:
        data = await _fetch_api("aio", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# MediaFire Downloader (Unmaintained)
async def mediafire(url):
    """Download files from MediaFire (unmaintained)."""
    try:
        data = await _fetch_api("mediafire", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Capcut Downloader
async def capcut(url):
    """Download templates from CapCut."""
    try:
        data = await _fetch_api("capcut", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Google Drive Downloader
async def gdrive(url):
    """Download files from Google Drive."""
    try:
        data = await _fetch_api("gdrive", url)
        return {
            "developer": "@prm2.0",
            "result": data.get("data")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Pinterest Downloader
async def pinterest(mdl):
    """Download pins or search results from Pinterest."""
    try:
        data = await _fetch_api("pinterest", mdl)
        return {
            "developer": "@prm2.0",
            "result": data.get("result")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Douyin Downloader
async def douyin(url):
    """Download media from Douyin."""
    try:
        data = await _fetch_api("douyin", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Xiaohongshu Downloader
async def xiaohongshu(url):
    """Download media from Xiaohongshu."""
    try:
        data = await _fetch_api("rednote", url)
        return {
            "developer": "@prm2.0",
            "result": data.get("result") if data.get("result") else data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Xiaohongshu Profile Downloader
async def xiaohongshu_profile(url):
    """Download profile data from Xiaohongshu."""
    try:
        data = await _fetch_api("rednote-profile", url)
        return {
            "developer": "@prm2.0",
            "result": data.get("result") if data.get("result") else data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }


# SnackVideo Downloader
async def snackvideo(url):
    """Download media from SnackVideo."""
    try:
        data = await _fetch_api("snackvideo", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Cocofun Downloader
async def cocofun(url):
    """Download media from Cocofun."""
    try:
        data = await _fetch_api("cocofun", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Spotify Downloader
async def spotify(url):
    """Download tracks from Spotify."""
    try:
        data = await _fetch_api("spotify", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# YouTube Search
async def yts(query):
    """Search YouTube for videos."""
    try:
        data = await _fetch_api("yts", query)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# SoundCloud Downloader
async def soundcloud(url):
    """Download tracks from SoundCloud."""
    try:
        data = await _fetch_api("soundcloud", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Threads Downloader
async def threads(url):
    """Download media from Threads."""
    try:
        data = await _fetch_api("threads", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }

# Kuaishou Downloader
async def kuaishou(url):
    """Download media from Kuaishou."""
    try:
        data = await _fetch_api("kuaishou", url)
        return {
            "developer": "@prm2.0",
            "result": data
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": DOC_NOTE
        }
