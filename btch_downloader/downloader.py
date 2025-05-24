import httpx
import json

# Config
__version__ = "4.0.14"
BASE_URL = "https://backend1.tioo.eu.org"

async def _fetch_api(endpoint, url):
    """Fetch API."""
    async with httpx.AsyncClient() as client:
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
            raise Exception(f"Error fetching from {endpoint}: {str(error)}")

# TikTok Downloader
async def ttdl(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Instagram Downloader
async def igdl(url):
    try:
        data = await _fetch_api("igdl", url)
        
        if not data or (isinstance(data, dict) and data.get("status") is False):
            return {
                "developer": "@prm2.0",
                "status": False,
                "message": data.get("msg", "Result Not Found! Check Your Url Now!") if isinstance(data, dict) else "Result Not Found! Check Your Url Now!",
                "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
            }
        
        if isinstance(data, list):
            return [
                {
                    "developer": item.get("creator", "@prm2.0"),
                    "thumbnail": item.get("thumbnail"),
                    "url": item.get("url"),
                    "resolution": item.get("resolution", "unknown"),
                    "shouldRender": item.get("shouldRender", True)
                } for item in data
            ]
        
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": "Invalid data format received",
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }
            
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": f"Request Failed: {str(error)}",
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Twitter Downloader
async def twitter(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# YouTube Downloader
async def youtube(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Facebook Downloader
async def fbdown(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# AIO Downloader
async def aio(url):
    try:
        data = await _fetch_api("aio", url)
        return {
            "developer": "@prm2.0",
            "url": data.get("url")
        }
    except Exception as error:
        return {
            "developer": "@prm2.0",
            "status": False,
            "message": str(error),
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# MediaFire Downloader
async def mediafire(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Capcut Downloader
async def capcut(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Google Drive Downloader
async def gdrive(url):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }

# Pinterest Downloader
async def pinterest(mdl):
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
            "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
        }