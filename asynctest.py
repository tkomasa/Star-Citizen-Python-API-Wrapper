import WrappAsync
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
instance = WrappAsync.Client(api_key)

#print(instance.get_user("Turtle-12"))
print(instance.get_organization("INVFED"))