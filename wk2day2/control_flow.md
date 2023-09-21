# Control flow

### if, else, elif
Allows you to control flow of your code by using statements.

Can check if conditions are met before running lines of code.

Important as otherwise python would run code from top to bottom, indiscriminately.

Example use:
```
if a == b:
    c = 1
elif a == d:
    c = 2
else:
    c = 3
``` 

![MYelseifelif diagram.jpg](..%2F..%2F..%2F..%2F..%2FDesktop%2FMYelseifelif%20diagram.jpg)

### for loops
For will iterate through the content until complete.

Syntax is `for x in variable_name:` where x is any name (following regular variable naming conventions) and 
denotes the current value in the variable the for loop has iterated to, like an entry in a list.

e.g. will iterate through every item in a list, every key+value pair in a dictionary, etc.
This example will print every value in the list individually.
```
list_example = [1, 2, 3]

for item in list:
    print(item)
```

![MYforloop diagram.PNG](..%2F..%2F..%2F..%2F..%2FDesktop%2FMYforloop%20diagram.PNG)

### while loops
Similar to for loops but will iterate indefinitely until a condition is no longer met.

So, for example, the following code will iterate until counter reaches 10.
```
counter = 0

while counter < 10:
    print(counter)
    counter += 1
```
While loops can be useful for ensuring code is only iterated a certain number of times,
using counter variables, or until a task is completed.

While loops can also be useful for ensuring code loops indefinitely, though this has niche usage and is
generally not recommended in most cases.

``` 
while 1==1:
    print("I will loop forever!")
```

![MYwhileloop diagram.PNG](..%2F..%2F..%2F..%2F..%2FDesktop%2FMYwhileloop%20diagram.PNG)