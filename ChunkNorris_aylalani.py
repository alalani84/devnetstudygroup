#!/usr/bin/env python3

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

joke = response.json()

print(joke['value'])















