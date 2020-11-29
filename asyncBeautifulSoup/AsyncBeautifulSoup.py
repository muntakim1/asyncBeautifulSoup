import asyncio
import aiohttp
from bs4 import BeautifulSoup



async def async_beautifulsoup(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.read()
    return  BeautifulSoup(text,'html.parser')

def get_content(url):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_beautifulsoup(url))
    
