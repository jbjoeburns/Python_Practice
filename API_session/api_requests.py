import requests

# get request (remember to include 'https://')
post_codes_req = requests.get("https://postcodes.io/postcodes/pr85dj")

print(post_codes_req)

# print json
print(post_codes_req.json())