# starcitizen.tools-API-Wrapper
This is an API wrapper made in python, for python, using the [Star Citizen API](https://starcitizen-api.com/) made by Corentin Urbain.


## Getting Started:
1. Step one is getting your API key [here](https://starcitizen-api.com/startup.php#getting-started).
2. Place it into a `.env` file in the main directory containing one line: 

```.env
export STARCITIZEN_API_KEY = "YOUR KEY HERE"
```

3. Now use dotenv package to import the key into your main.py: 

```python
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("STARCITIZEN_API_KEY")
```

4. Start a client object by feeding your key into the `RSI.Client` class:

```python
Client = RSI.Client(api_key)
```

5. You can now use any of the API methods by using dot notation:

```python
data = Client.get_user("Turtle-12") # returns User object of Turtle-12 user page
```

## Methods:
#### get_user(user)
Will return [User]() object of the queried user 

##### User Obj:



```python
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
    message: str
    source: str
    success: int

class User(Prodict):
    data: User_Data
```

