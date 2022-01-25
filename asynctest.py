import WrappAsync
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
sesh = WrappAsync.Client(api_key)

sesh.get_user("Turtle-12")
