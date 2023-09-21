try:
    user_number = float(input("Please input a number: "))
    if user_number % 3 == 0 and user_number % 5 == 0:
        print("FizzBuzz")
    elif user_number % 5 == 0:
        print("Buzz")
    elif user_number % 3 == 0:
        print("Fizz")
except:
    print("Please input a valid number.")