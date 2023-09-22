## json notes

Most common file format for API responses!

First, a script should be made to check if a json file is valid.

```
import json
import os
import sys

# checks if arguments are given
if len(sys.argv) > 1:
    # checks if the file is valid
    if os.path.exists(sys.argv[1]):
        # reads file
        file = open(sys.argv[1], "r")

        # use load instead of loads as we don't need to convert into dictionary, we're just checking if file is valid
        json.load(file)

        # closes file
        file.close()

        # if no error occured, then json must be valid!
        print("JSON is valid!")

    else:
        print(f"{sys.argv[1]} is not found")
else:
    print("Usage: check_json.py <file>")
```

***sys.argv[1]***: It's **VERY** important to note how sys.argv works. It takes any argument provided from the command line. The [1] is the index of the argument. So for example, if you typed `C:\documents\argtest.py C:\documents\json.json` into the terminal, it will run `argtest.py` and the index 1 argument will be the filepath of the `json.json` file!

This allows us to fully automate the process of pulling json data with less user input than using `input()`, even less so if text files are used to run the script multiple times and provide many arguments.

Example of using sys.arg in this context.
```
import json
import sys

user_json_file = sys.argv[1]

```

Need to import the json module:

`import json`

Then we need to parse it (parsing means making it more understandable) which is done by: 

`parsed_json = json.loads(open("x.json").read())` 

- Sidenote about loads, you can use `json.load(open("filename", "r"))` instead to just read the file. Can use different parameters like `"w"` to write to it too.

`open().read` opens the json file to read, and `json.loads` converts json string in a file into a python dictionary where x is the filename of the json file.

You can then access specific information from the json string we just assigned to a variable by:

`value = json["name"]`

This example in particular assigns the value associated with the 'name' key from the dictionary based on our json, to a variable to be used later in the script.

Can be used to parse files from online with the `urllib.request` library:
```
import urllib.request
import json
with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data) 
```

Can also convert json into other filetypes like yaml

For yaml do this:
 `yaml_file = yaml.dump("json_file.json")`

Then need to write variable to file doing this: 
```
    # opens the file
    yaml_output = open("filename", "r")
    yaml_output.write(yaml_file)
    yaml_output.close()
```

Same logic as opening/writing/closing files I did with pandas!