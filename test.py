import asyncio
from btch_downloader import ttdl, igdl, twitter, youtube, fbdown, aio, mediafire, capcut, gdrive, pinterest

async def main():
    # Instagram
    result = await igdl("https://www.instagram.com/p/ByxKbUSnubS/?utm_source=ig_web_copy_link")
    print(result)

asyncio.run(main())
