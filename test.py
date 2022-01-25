import RSISiteWrapper
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIEN_API_KEY")
Client = RSISiteWrapper.Client(api_key)

data = Client.get_user("Turtle-12")
print(data)