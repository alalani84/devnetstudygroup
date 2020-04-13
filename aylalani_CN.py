#!/usr/bin/env python3

import os
import sys
import json
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

joke = response.json()

print(joke['value'])















