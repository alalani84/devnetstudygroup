#!/usr/bin/env python

import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random")

joke = response.json()

print(joke)

print("joke1")