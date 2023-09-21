counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 5 == 0:
        print("Buzz")
    elif counter % 3 == 0:
        print("Fizz")
    counter += 1