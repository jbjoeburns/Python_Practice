import requests
import json

# takes dictionary and turns it into valid json associated with the variable
json_body = json.dumps({"postcodes": ["pr85dj", "m456gn"]})

# need to provide some headers, for example, what the request will be formatted as (json)
headers = {"Content-Type": "application/json"}

# need to provide header, and data as keywords
post_codes_get = requests.post("https://postcodes.io/postcodes", headers=headers, data=json_body)

print(post_codes_get.json())