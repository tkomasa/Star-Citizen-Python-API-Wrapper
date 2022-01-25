import asyncio
import aiohttp
import os
import json

from dotenv import load_dotenv
load_dotenv

api_key = os.getenv("STARCITIZEN_API_KEY")
url = 'https://api.starcitizen-api.com/{}/v1/live/{}'

async def get_user():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://api.starcitizen-api.com/IBsT8GkNryFDkYHJNYKjV7lBhbBvIvbW/v1/live/users/Turtle-12", ssl=False)
        data = await response.json()
        return data
    
class Client(object):
    def __init__(self, api_key):
        self.key = api_key
    
    async def get_user(self, user):
        async with aiohttp.ClientSession() as session:
            r = await session.get(url.format(self.key, "/user/{}".format(user)), ssl=False)
            return await r.json()
    
    async def get_organization(self, organization):
        async with aiohttp.ClientSession() as session:
            r = await session.get(f"https://api.starcitizen-api.com/{self.key}/v1/live/organization/{organization}")
            return await r.json()

async def main():
    _instance = Client("IBsT8GkNryFDkYHJNYKjV7lBhbBvIvbW")
    
    task1 = asyncio.create_task(coro=_instance.get_user("Turtle-12"))
    task2 = asyncio.create_task(coro=_instance.get_organization("INVFED"))
    
    await task1
    await task2
    
    print(task1)
    print(task2)

if __name__ == "__main__":
    #asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
