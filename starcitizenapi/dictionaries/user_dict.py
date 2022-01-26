from prodict import Prodict

class User_Organization(Prodict):
    image: str
    name: str
    rank: str
    sid: str
    star: int

class Location(Prodict):
    country: str
    region: str

class Page(Prodict):
    title: str
    url: str

class User_Profile(Prodict):
    badge: str
    badge_image: str
    bio: str
    display: str
    enlisted: str
    fluency: str
    handle: str
    id: str
    image: str
    location: Location
    page: Page
    website: str
    
class User_Data(Prodict):
    affiliation: str
    organization: User_Organization
    profile: User_Profile

class User(Prodict):
    data: User_Data
    message: str
    source: str
    success: int
    

# this is for testing:
'''
response = {
    "data": {
        "affiliation": [],
        "organization": {
            "image": "https://robertsspaceindustries.com/media/uh2fvrq9575zvr/heap_infobox/INVFED-Logo.png",
            "name": "Invictus Intergalactic Federation",
            "rank": "Enlisted Member",
            "sid": "INVFED",
            "stars": 1
        },
        "profile": {
            "badge": "Grand Admiral",
            "badge_image": "https://media.robertsspaceindustries.com/a6kpgl3byjake/heap_thumb.png",
            "bio": "Flippers on the HOSAS. Check out my main org INVFED!\n\nDiscord: Turtle-12#0001\n\nOrg Website: https://www.invfed.com/home\nOrg RSI Page: https://robertsspaceindustries.com/orgs/INVFED\nOrg Twitter: https://twitter.com/Official_INVFED",
            "display": "Turtle-12",
            "enlisted": "2021-07-30T00:00:00.000000",
            "fluency": [
                "English"
            ],
            "handle": "Turtle-12",
            "id": "n/a",
            "image": "https://robertsspaceindustries.com/media/xm8k6mibbrgnqr/heap_infobox/Invfed_turtle.png",
            "location": {
                "country": "United States",
                "region": "California"
            },
            "page": {
                "title": "Turtle-12 | Turtle-12 - Invictus Intergalactic Federation | INVFED (Enlisted Member) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42",
                "url": "https://robertsspaceindustries.com/citizens/Turtle-12"
            },
            "website": "https://twitter.com/invfed_turtle"
        }
    },
    "message": "ok",
    "source": "live",
    "success": 1
}

user = User_Data.from_dict(response)

#print(user.data.profile.handle) #returns <Turtle-12>
'''
