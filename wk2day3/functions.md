## Functions

Allows reuse of code, makes code more succinct.

In python, functions are made by...

``` 
def example_function():
    print("The function is running!")
```

Function then needs to be called for its contents to be executed. This is done by...

``` 
example_function()
```

This can be done any number of times in the code, making the function contents infinitely reuseable.

## Functions with arguments

Some functions require arguments. You can set this up with... 

``` 
def example_function(argument_example1, argument_example2):
    print(f"This requires the arguments {argument_example1} and {argument example2}")
```

Then you call the function with arguments.
``` 
example_function("these are", "example inputs")
```

This will not run without required arguments. However, you can set default arguments, that can be overwritten.

``` 
def example_function(argument_example1 = "default1", argument_example2 = "default2"):
    print(f"This requires the arguments {argument_example1} and {argument example2}")

example_function()
```
This will print `This requires the arguments default1 and default2`

Additionally, you can have an indefinitely large number of arguments a function will except using the wildcard character.

```
def multi_args(*arguments):
    for argument in arguments:
        print(argument)

multi_args(1, 2, 3, 4)
```

This will print the numbers, ***1***, ***2***, ***3*** and ***4*** in sequence!

*Sidenote: 'arguments' is a tuple in this case.*

## Return statements

To take (changed) values that only exist within the function, out of the function, you need to use a ***return*** statement.

In this example, the result of the function to calculate John's velocity will not be printed as the value is contained within the function, and not returned.
``` 
john_displacement = 3
john_time = 4

def sum_function(displacement, time):
    displacement / time
    
print(sum_function(john_displacement, john_time))
```

***This just returns 'None', as no data is returned!***

However, this will work as intended!
``` 
john_displacement = 3
john_time = 4

def sum_function(displacement, time):
    return displacement / time
    
print(sum_function(john_displacement, john_time))
```

The 'displacement / time' equation is returned, and therefore 'print' receives the value/answer.

