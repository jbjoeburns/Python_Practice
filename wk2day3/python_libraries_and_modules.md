## What are they?

Code and functions that are already written, that we can instead download and use in our code.

***Module***: Single file within a library.

***Library***: Collection of modules. Installed with pip (python package manager).

Imports are done by...
``` 
import <name>
```

Useful libraries...

***random***: Adds randomising functionality.
- Docs: https://docs.python.org/3/library/random.html
- Useful functions:
    - random.seed(x): Initialises the random number generator by generating a seed for which random numbers are generated from.
    - random.random(x): Returns random number between 0 and 1
    - random.randint(x, y): returns random number within a given range
    - random.shuffle(x): shuffles list randomly
    - plus many more

***math***: Useful functions for maths.
- Docs: https://docs.python.org/3/library/math.html
- Useful functions:
    - math.pi(): Returns pi
        - Also has varients for e and tau
    - math.sqrt(x): Square root of number
    - math.pow(x, y): Does x to the power of y
    - Also supports sin, cos, tan etc...
    - math.log(x, y): Log of x to base of y

***http***: HTTP related modules
- Docs: https://docs.python.org/3/library/http.client.html
- Useful functions:
    - http.client.HTTPConnection(x): Does a HTTP request
        - You can assign response as a variable to inspect page information
    - Support for GET, POST and PUT requests

***datetime***: Allows you to work with computer clock.
- Docs: https://docs.python.org/3/library/datetime.html
- Useful functions:
  - datetime.datetime.now(): Takes current time based off computer clock
  - Can use strftime() to format the time into different readable formats, parameters in the docs...

***csv***: For working with spreadsheets (comma seperated value files specifically)
- Docs: https://docs.python.org/3/library/csv.html
- Useful functions:
  - csv.reader(): lets you read .csv files
  - Pandas generally does the same thing but better

***os***: Lets you execute command line commands as part of a python script.
- Docs: https://docs.python.org/3/library/os.html
- Useful functions: 
  - os.getcwd(): gets current working directory
  - os.chdir(): for changing directory
- Many other command line level functions!
