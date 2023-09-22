import json

# reads in json
parsed_json = json.loads(open('example_json.json').read())

# loops through each key in parsed_json and prints key and associated value
for key in parsed_json:
    print(f"Key: {key}, Value: {parsed_json[key]}")

