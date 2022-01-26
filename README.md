# starcitizen.tools-API-Wrapper
This is an API wrapper made in python, for python, using the [Star Citizen API](https://starcitizen-api.com/) made by Corentin Urbain.


## Getting Started:
1. Step one is getting your API key [here](https://starcitizen-api.com/startup.php#getting-started).
2. Place it into a `.env` file in the wrapper folder as one line: 

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
data = Client.get_user("Turtle-12")
```

## Methods:
#### get_user()

