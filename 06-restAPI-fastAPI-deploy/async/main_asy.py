import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com"] * 10  # Lista de URLs para fetch
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response[:100])  # Printa os primeiros 100 caracteres de cada resposta

asyncio.run(main())
