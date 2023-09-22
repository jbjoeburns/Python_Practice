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