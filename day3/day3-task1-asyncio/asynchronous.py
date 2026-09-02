import asyncio
import aiohttp

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            print(f"Downloaded {url} - {len(data)} bytes")

async def main():
    urls = ["https://api.github.com", "https://api.python.org", "https://httpbin.org/json"]
    await asyncio.gather(*(download_file(url) for url in urls))

asyncio.run(main())
