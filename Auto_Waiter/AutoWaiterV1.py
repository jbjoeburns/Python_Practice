starters = {"Bruschetta": 1.30, "Chicken Wings": 2.10, "Skewers": 2.30, "Soup of the day": 2.50}
mains = {"Spaghetti": 12.20, "Pizza": 11.30, "Burger": 9.90}
desserts = {"Cheesecake": 6.20, "Ice Cream": 3.90, "Apple Pie": 7.30, "Chocolate Cake": 6.20}
drinks = {"Wine": 7.90, "Beer": 6.90, "Coke": 2.30, "Pepsi": 3.30, "Water": 0.00}

print("Welcome to the restaurant! What will you be having today?")
print("Starters: ")
for dish in starters:
    dish_number = list(starters).index(dish) + 1
    print(str(dish_number) + ". " + dish)
starter_number = input("Select the number of the starter you would like:")
starter_choice = list(starters)[int(starter_number) - 1]

print("Thank you, sir!")
for dish in mains:
    dish_number = list(mains).index(dish) + 1
    print(str(dish_number) + ". " + dish)
main_number = input("And for main?:")
main_choice = list(mains)[int(main_number) - 1]

print("Excellent choice.")
for dish in desserts:
    dish_number = list(desserts).index(dish) + 1
    print(str(dish_number) + ". " + dish)
dessert_number = input("And what would you like for dessert?:")
dessert_choice = list(desserts)[int(dessert_number) - 1]

print("Last but not least...")
for dish in drinks:
    dish_number = list(drinks).index(dish) + 1
    print(str(dish_number) + ". " + dish)
drink_number = input("And what do you want to drink?:")
drink_choice = list(drinks)[int(drink_number) - 1]

order_total = starters[starter_choice] + mains[main_choice] + desserts[dessert_choice] + drinks[drink_choice]

print(f"Excellent. An order of {starter_choice},"
      f" followed by a {main_choice},"
      f" and finally {dessert_choice} for dessert,"
      f" with a glass of {drink_choice} coming right up!")

print(f"That'll be a total of £{order_total}")
