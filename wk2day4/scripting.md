## These are some core modules for scripting in python

import os
- `os.getcwd()`
  - returns current working directory
- `os.chdir(<target>)`
  - change directory
- `os.mkdir(<filename>)`
  - make directory

import sys
- `sys.version`
  - returns python version

import subprocess
- `subprocess.run(["python", <filename>])`
  - runs other files

import math
- `math.pi`
  - returns pi

import random
- `random.randrange(x, y)`
  - returns random number between x and y

import datetime
- `datetime.datetime.now()`
  - returns current date (to the millisecond)

import json
- `json.dumps(x)`
  - turns x into json string