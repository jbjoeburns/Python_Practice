import json

# reads in json
parsed_json = json.loads(open('example_json.json').read())

key = input("Please input key: ")

if key not in parsed_json:
    print("Key not found...")
else:
    print(parsed_json[key])
