import RSISiteWrapper
import os
import json
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
Client = RSISiteWrapper.Client(api_key)

data = Client.get_organization("INVFED")
print(json.dumps(data, indent=4, sort_keys=True))