import RSI

import os
from dotenv import load_dotenv
load_dotenv()

# dict classes
import dictionaries.user

# init
api_key = os.getenv("STARCITIZEN_API_KEY")
Client = RSI.Client(api_key)

# query example
user = Client.get_user("Turtle-12")

# example test proof
print("----------Testing----------")
print("User's RSI Handle:    " + user.data.profile.display)
print("User's Organization:  " + user.data.organization.name)
print("User's RSI Page URL:  " + user.data.profile.page.url)
print("---------------------------")

