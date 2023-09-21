# this is used to track the previous answer, so ans can be used in the user provided equation
previous_answer = ''

print("Hello, welcome to my calculator.")

supported_operations = ["+", "-", "/", "*"]

# operation selecting function
def operation_picker():
    while 1==1:
        operation_selected = input("Operation: ")
        if operation_selected in supported_operations:
            return operation_selected
        else:
            print("Please provide a valid operation")

def addition_function(selected_numbers):
    final_answer = 0
    for item in selected_numbers:
        print(item)
        final_answer = final_answer + float(item)
        print(final_answer)
    return str(final_answer)

def subtraction_function(selected_numbers):
    # final answer is set as the first value in selected numbers to start, to allow for subtraction calculations
    final_answer = selected_numbers[0]
    # then remove this from the list so it's not factored twice into calculations
    del selected_numbers[0]
    for item in selected_numbers:
        final_answer = float(final_answer) - float(item)
    return str(final_answer)

def multiplication_function(selected_numbers):
    final_answer = 1
    for item in selected_numbers:
        final_answer = float(item) * float(final_answer)
    return str(final_answer)

def division_function(selected_numbers):
    # final answer is set as the first value in selected numbers to start, to allow for division calculations
    final_answer = selected_numbers[0]
    # then remove this from the list so it's not factored twice into calculations
    del selected_numbers[0]
    for item in selected_numbers:
        final_answer = float(final_answer) / float(item)
    return str(final_answer)

# allows calculator to loop, so you can use previous answer in next equation
while 1 == 1:
    # asks for operation
    print("Please input what operation you would like. Supports +, -, / and *.")
    operation_selected = operation_picker()

    # accepts input from user
    print("Please type the numbers you want to use, seperated by a space. If you would like to re-use the previous answer, use 'ans' in your equation.")
    user_equation = input("User input: ")

    # replaces instances of 'ans' with the previous answer
    user_equation = user_equation.replace("ans", previous_answer)

    # seperates numbers into a list
    user_equation = user_equation.split(" ")

    # we then eval the string, this is not a security risk like eval can be, as all characters except operators and numbers are removed
    print(f"Numbers selected: {user_equation}")

    # operations functions, selected based on operation choice
    if operation_selected == "+":
        print("addition")
        answer = addition_function(user_equation)

    if operation_selected == "-":
        print("subtraction")
        answer = subtraction_function(user_equation)

    if operation_selected == "*":
        print("multiplication")
        answer = multiplication_function(user_equation)

    if operation_selected == "/":
        print("division")
        answer = division_function(user_equation)

    # prints answer
    print(f"Answer: {answer}")
    previous_answer = answer
