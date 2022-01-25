import asyncio
import aiohttp
import os

api_key = os.getenv("STARCITIEN_API_KEY")
url = f'https://api.starcitizen-api.com/{api_key}/v1/live/user/Turtle-12'

async def get_user():
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, ssl=False)
        return response

asyncio.run(get_user)
