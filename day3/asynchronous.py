import asyncio
import aiohttp

async def download_file(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                data = await response.read()
                print(f"Downloaded {url} - {len(data)} bytes")
    except Exception as e:
        print(f"Failed {url} : {e}")

async def main():
    urls = [
        "https://api.github.com",
        "https://httpbin.org/json",
        "https://jsonplaceholder.typicode.com/posts/1"
    ]
    await asyncio.gather(*(download_file(url) for url in urls))

asyncio.run(main())