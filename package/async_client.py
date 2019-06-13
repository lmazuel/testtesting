import aiohttp

class AsyncClient():

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()
