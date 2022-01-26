<img align="right" width="200" src="https://user-images.githubusercontent.com/70603965/151218771-c3efa2e7-1f79-45fa-975d-b23946a8883f.png"/>

# Star Citizen API Wrapper for Python
![](https://img.shields.io/github/v/release/tkomasa/Star-Citizen-Python-API-Wrapper)
![](https://img.shields.io/website?down_color=red&down_message=API%20Offline&up_color=green&up_message=API%20Online&url=https%3A%2F%2Fstarcitizen-api.com%2Findex.php)
![](https://img.shields.io/github/issues/tkomasa/Star-Citizen-Python-API-Wrapper)
![](https://img.shields.io/github/issues-pr/tkomasa/Star-Citizen-Python-API-Wrapper)
![](https://img.shields.io/github/license/tkomasa/Star-Citizen-Python-API-Wrapper)

This is a ready-to-use and async-enabled API wrapper made in Python, for Python, for the [Star Citizen API](https://starcitizen-api.com/index.php) made by Corentin Urbain. It features full support for dot notation and autocomplete data as well as custom data classes for ease of use.

***
## What is an API wrapper?
An API wrapper can help streamline the process of accessing an API for a particular language, in this one's case, Python. The API it is accessing provides raw JSON data (depending on the queried URL) of information scraped from the official [RSI website](https://robertsspaceindustries.com/).

Here is what it looks like raw:
```txt
{"data":{"affiliation":[],"organization":{"image":"https://robertsspaceindustries.com/media/uh2fvrq9575zvr/heap_infobox/INVFED-Logo.png","name":"Invictus Intergalactic Federation","rank":"Enlisted Member","sid":"INVFED","stars":1},"profile":{"badge":"Grand Admiral","badge_image":"https://media.robertsspaceindustries.com/a6kpgl3byjake/heap_thumb.png","bio":"Flippers on the HOSAS. Check out my main org INVFED!\n\nDiscord: Turtle-12#0001\n\nOrg Website: https://www.invfed.com/home\nOrg RSI Page: https://robertsspaceindustries.com/orgs/INVFED\nOrg Twitter: https://twitter.com/Official_INVFED","display":"Turtle-12","enlisted":"2021-07-30T00:00:00.000000","fluency":["English"],"handle":"Turtle-12","id":"n/a","image":"https://robertsspaceindustries.com/media/xm8k6mibbrgnqr/heap_infobox/Invfed_turtle.png","location":{"country":"United States","region":"California"},"page":{"title":"Turtle-12 | Turtle-12 - Invictus Intergalactic Federation | INVFED (Enlisted Member) - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42","url":"https://robertsspaceindustries.com/citizens/Turtle-12"},"website":"https://twitter.com/invfed_turtle"}},"message":"Not Modified","source":"live","success":1}
```

Frankly, not very readable, maybe that's just me. The wrapper takes that raw stream and converts it into accessible and understandable formats for consumption and use. Instead of scanning the clump of letters for info, you can simply use the `User` object the wrapper makes to access info. Example: `user.user_data.user_profile.page.url` would now display the user's RSI page URL instead: [https://robertsspaceindustries.com/citizens/Turtle-12](https://robertsspaceindustries.com/citizens/Turtle-12). Dot notation or direct dictionary manipulation are acceptable forms of data access. 

## What can I use this for?
Anything you want to get information from the RSI site for. Ship data? Sure. User's profile picture? Yes sir. Full organization's member list? Of course. As soon as it is updated on the RSI site, it will be updated fo your application, as each parse is done to the live site. (Caching options are coming soon.) 
***
## Getting Started:
### Installing:

### Startup Code:
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
user = Client.get_user("Turtle-12") # returns User object of Turtle-12 user page
RSI_page_link = user.user_data.user_profile.page.url # an example of accessing the data using dot notation
```
***
# Functions of the wrapper:
***
## Methods:
***
#### 1. get_user(user)
Will return [User](https://github.com/tkomasa/Star-Citizen-Python-API-Wrapper/blob/main/README.md#user-object) object of the queried user 

##### User Object:
- user: `User`
    - data: `User_Data`
        - affiliation: `list` of the user's affiliation orgs
        - organization `User_Organization`
            - image: `str` returns profile page org image url
            - name: `str` returns full org name
            - rank: `str` returns the user's rank in the org
            - sid: `str` returns the shorthand ID of the org
            - star: `int` returns how many "star" icons the user gets due to their org rank
        - profile: `User_Profile`
            - badge: `str` returns title of displayed badge
            - badge_image: `str` url of badge image
            - bio: `str` returns entire shorthand bio
            - display: `str` returns the user's RSI display name
            - enlisted: `str` returns str format of the date the user enlisted their RSI account
            - fluency: `str` returns str list of fluent languages
            - handle: `str` returns user's RSI handle name
            - id: `str` returns user account ID if applicable
            - image: `str` url of user's profile picture
            - location: `Location`
                - country: `str` returns user's country
                - region: `str` returns user's region
            - page: `Page`
                - title: `str` return full HTML page title
                - url: `str` return user's RSI account page url
            - website: `str` url of user's listed website
    - message: `str` returns message health
    - source: `str` returns the source's version (should always be 'live')
    - success: `int` returns binary boolean of query success (1=True & 0=False)

##### Example:
```python
# query example
user = Client.get_user("Turtle-12")

# example test proof
print("----------Testing----------")
if user.success == 1:
    bool_succ = "Success"
elif user.success != 1:
    bool_succ = "Failure"
print("Success: " + bool_succ + " from " + user.source)
print("User's RSI Handle:    " + user.data.profile.display)
print("User's Organization:  " + user.data.organization.name)
print("User's RSI Page URL:  " + user.data.profile.page.url)
print("---------------------------")
```

This will return the following:

```txt
----------Testing----------
Success: Success from live
User's RSI Handle:    Turtle-12
User's Organization:  Invictus Intergalactic Federation
User's RSI Page URL:  https://robertsspaceindustries.com/citizens/Turtle-12
---------------------------
```
***
#### 2. get_organization(organization_sid)
Will return [Organization]() object of the queried organization shorthand ID

##### Organization Object:

***

## Legal
This a fan-made and community-based project. Tucker Komasa, the [Star Citizen API](https://starcitizen-api.com/index.php), and the SC API Wrapper, have no affiliation with the Cloud Imperium group of companies. This project is made by the community, maintined by the community, and made for the community.

_This is an unofficial Star Citizen fansite, not affiliated with the Cloud Imperium group of companies. All content on this site not authored by its host or users are property of their respective owners. All game content and materials are copyright of Cloud Imperium Rights LLC and Cloud Imperium Rights Ltd.. Star Citizen®, Squadron 42®, Roberts Space Industries®, and Cloud Imperium® are registered trademarks of Cloud Imperium Rights LLC. All rights reserved._

By using this project, you agree to the [terms and conditions of the Star Citizen API](https://starcitizen-api.com/terms/terms-and-conditions.php). The project is a tool based around the [Star Citizen API](https://starcitizen-api.com/index.php), any development, opinions, achievements, issues, etc. centered around the [Star Citizen API](https://starcitizen-api.com/index.php) are its own.

## Links
- [RSI Website](https://robertsspaceindustries.com/)
- [RSI Terms of Service](https://robertsspaceindustries.com/tos)
- [RSI Fandom FAQ](https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793)
- [Star Citizen API](https://starcitizen-api.com/index.php)
- [Star Citizen API Terms & Conditions](https://starcitizen-api.com/terms/terms-and-conditions.php)
