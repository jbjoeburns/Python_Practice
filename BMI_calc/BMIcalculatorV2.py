try:
    # Allows user to select their preferred units
    # This is important as the BMI formula changes depending on the units used, as imperial needs to be converted to metric for the calculation
    print("Are your units in imperial (lbs, inches) or metric (kilograms, meters)?")
    print("1. Imperial")
    print("2. Metric")

    # I would usually convert the input value to int, as we only require 1 or 2
    # However, this leads to a ValueError if the user provides a value with decimals, which would return an undesired error message
    # Therefore, the user input is converted to a float, then this is checked to be either 1 or 2 using if/else statements
    unit_selection = float(input())

    # Checks if the user requested imperial units
    if unit_selection == 1:
        # Asks for mass
        print("Enter your mass in pounds:")
        mass = float(input())

        # Asks for height
        print("Enter your height in inches:")
        height = float(input())

        # BMI formula using imperial units
        BMI = (mass / (height * height)) * 703
        print(f"Your BMI is {str(round(BMI, 2))} to 2 decimal places.")

    # Checks if the user requested metric units
    elif unit_selection == 2:
        # Asks for mass
        print("Enter your mass in kg:")
        mass = float(input())

        # Asks for height
        print("Enter your height in meters:")
        height = float(input())

        # BMI formula using
        BMI = mass / (height * height)
        print(f"Your BMI is {str(round(BMI, 2))} to 2 decimal places.")

    else:
        print("Please type only 1 or 2, with no decimal places, to make a selection...")

except ValueError:
    print("Please only input numbers.")
