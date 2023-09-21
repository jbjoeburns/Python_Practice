# This is a little off track, but I finished early so I thought I'd make a more functional calculator...

# using regular expressions makes it easier to extract sum and number info from string
import re

# this is used to track the previous answer, so ans can be used in the user provided equation
previous_answer = ''

print("Hello, welcome to my calculator. Please input what you would like to calculate.")
print("If you would like to re-use the previous answer, use 'ans' in your equation.")

# allows calculator to loop, so you can use previous answer in next equation
while 1 == 1:
    # accepts input from user
    user_equation = input("User input: ")

    # removes white space and all non-operator characters
    user_equation = user_equation.strip()

    # replaces instances of 'ans' with the previous answer
    user_equation = user_equation.replace("ans", previous_answer)

    # using regex
    user_equation = re.sub("[^0-9+\-/*]", "", user_equation)

    # we then eval the string, this is not a security risk like eval can be, as all characters except operators and numbers are removed
    print(f"Calculation: {user_equation}")

    # prints answer
    answer = str(eval(user_equation))
    print(f"Answer: {answer}")
    previous_answer = answer
