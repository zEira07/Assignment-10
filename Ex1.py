import urllib.request
import json
import ssl

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"


    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    req = urllib.request.Request(url, headers=headers)

    context = ssl._create_unverified_context()

    try:
        with urllib.request.urlopen(req, context=context) as response:
            data = json.loads(response.read().decode())
            print(data["value"])
    except Exception as e:
        print("Error:", e)

get_random_joke()