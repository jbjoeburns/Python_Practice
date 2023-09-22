## json notes

Most common file format for API responses!

First, need to import the json module:

`import json`

Then we need to parse it (parsing means making it more understandable) which is done by : 

`parsed_json = json.loads(open("x.json").read())` 

`open().read` opens the json file to read, and `json.loads` converts json string in a file into a python dictionary where x is the filename of the json file.

You can then access specific information from the json string we just assigned to a variable by:

`value = json["name"]`

This example in particular assigns the value associated with the 'name' key from the dictionary based on our json, to a variable to be used later in the script.



