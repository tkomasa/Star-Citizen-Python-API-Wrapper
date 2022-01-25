import asyncio
import aiohttp
url = 'https://api.starcitizen-api.com/{}/v1/live/{}'
    
class Client(object):
    def __init__(self, api_key):
        self.key = api_key
        self.loop = asyncio.get_event_loop()
    
    
    '''
    def get_ITEM(self, ITEM: str):
        return self.loop.run_until_complete(self._get_ITEM(ITEM))
    
    async def _get_ITEM(self, ITEM):
        async with aiohttp.ClientSession() as session:
            r = await session.get(url.format(self.key, "ITEM/{}".format(ITEM)), ssl=False)
            return await r.json()
    '''
    
    
    def get_user(self, user: str):
        return self.loop.run_until_complete(self._get_user(user))
    
    async def _get_user(self, user):
        async with aiohttp.ClientSession() as session:
            r = await session.get(url.format(self.key, "user/{}".format(user)), ssl=False)
            return await r.json()
    
    
    def get_organization(self, organization: str):
        return self.loop.run_until_complete(self._get_organization(organization))
    
    async def _get_organization(self, organization):
        async with aiohttp.ClientSession() as session:
            r = await session.get(url.format(self.key, "organization/{}".format(organization)), ssl=False)
            return await r.json()
