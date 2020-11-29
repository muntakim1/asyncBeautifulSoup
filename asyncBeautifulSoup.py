import asyncio
import aiohttp
from bs4 import BeautifulSoup



class AsyncBeautifulSoup:
    def __init__(self,url):
        return self.url = url

    def get_stock_content():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_beautifulsoup())
        
    async def async_beautifulsoup(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                text = await resp.read()
        return  BeautifulSoup(text,'html.parser')