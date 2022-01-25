import requests

class Client():
    def __init__(self, api_key):
        session = requests.Session()
        self.session = session
        self.key = api_key
    
    def get_user(self, user):
        return requests.get(f"https://api.starcitizen-api.com/{self.key}/v1/live/user/{user}").json()
    
    def get_organization(self, organization):
        return requests.get(f"https://api.starcitizen-api.com/{self.key}/v1/live/organization/{organization}").json()

