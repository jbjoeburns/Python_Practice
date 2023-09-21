# try block to insure valid input
try:
    # asks user for year, converts to int so if not a valid input throws to except block instead
    year_selected = int(input("Please input a year (do NOT include AD or BC, just the number): "))

    # this CAN be done without nested if statements and is arguably more simplified if you do it this way
    # you need to check the leap year criteria in a specific order

    # checks if the year is divisible by 400 (and is therefore divisible by both 100 and 4)
    if year_selected % 400 == 0:
        print("This is a leap year")

    # next checks if the year is divisble by 100
    # as being divisible by 400 has already been disproven
    # then this cannot be a leap year if it's divisible by 100
    elif year_selected % 100 == 0:
        print("This is NOT a leap year")

    # finally checks if divisible by 4
    # as the year is known to not be divisible by 100, if this passes it must be a leap year
    elif year_selected % 4 == 0:
        print("This is a leap year")

    # any number remaining cannot be a leap year as it is not divisible by 4
    else:
        print("This is NOT a leap year")

# except block for invalid numbers
except:
    print("Please type out the year you want to check, and only the number.")
