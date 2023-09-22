import json
parsed_json = json.loads(open('example_json.json').read())
value = json["name"]
print(value)