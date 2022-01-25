import RSISiteWrapper
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIEN_API_KEY")
sesh = RSISiteWrapper.RSI(api_key)

data = sesh.get_user("Turtle-12")
print(data)