import RSI

# dict classes
import dictionaries.user

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
Client = RSI.Client(api_key)

user = Client.get_user("Turtle-12")

# testing proof
print("----------Testing----------")
print("User's RSI Handle:    " + user.data.profile.display)
print("User's Organization:  " + user.data.organization.name)
print("User's RSI Page URL:  " + user.data.profile.page.url)
print("---------------------------")

