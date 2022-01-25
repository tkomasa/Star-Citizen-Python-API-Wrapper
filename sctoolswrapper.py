import requests
# https://starcitizen.tools/rest.php/v1/page/Gladius

class Page():
    def __init__(self):
        session = requests.Session()
        self.session = session
        
    def get_page(self, page):
        request = requests.get(f"https://starcitizen.tools/rest.php/v1/page/{page}")
        info = request.json
        return info