print("Enter your mass in kilograms:")
mass_kg = float(input())
print("Enter your height in meters:")
height_m = float(input())
BMI = mass_kg / (height_m * height_m)
print("Your BMI is: " + str(BMI))