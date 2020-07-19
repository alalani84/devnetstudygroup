#!/usr/bin/env python3

import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random")

joke = response.json()

print(joke['value'])

#line1
#line2
