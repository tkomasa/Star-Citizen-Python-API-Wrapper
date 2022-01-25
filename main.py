import RSI

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
Client = RSI.Client(api_key)

#print(Client.get_user("Turtle-12"))
#print(Client.get_organization("INVFED"))