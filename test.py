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
