# Try/Except block is to test if an integer is inputted, as decimals and non-numbers cannot be odd/even
try:
    # takes input and converts to integer, if not integer an error will be thrown and moves to except block
    user_number = int(input("Type a number: "))

    # if a number is divisible by 2 with no remainder then it's even, that's what this block is testing for
    if user_number % 2 == 0:
        print(f"{user_number} is even!")

    # if not, it's odd
    else:
        print(f"{user_number} is odd!")

# upon error, informs user that input is not valid
except:
    print("Please input a valid, whole, number.")

