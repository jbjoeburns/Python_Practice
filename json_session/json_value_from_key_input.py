import json

# reads in json
parsed_json = json.loads(open('example_json.json').read())

# asks for desired key
key = input("Please input key: ")

# if the key is in the json, it will return the associated value, if not it will tell you key wasnt found
if key not in parsed_json:
    print("Key not found...")
else:
    print(parsed_json[key])
