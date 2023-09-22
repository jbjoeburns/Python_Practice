import json
import sys

# usage:
# C:\Users\joe-b\Documents\Coding\Sparta\Code\json_session\json_from_arg_sys.py C:\Users\joe-b\Documents\Coding\Sparta\Code\json_session\example_json.json

# associates argument with variable
argument = sys.argv[1]

# reads in json and makes it a dictionary
parsed_json = json.loads(open(argument).read())

# loops through keys and values
for key in parsed_json:
    print(f"Key: {key}, Value: {parsed_json[key]}")
