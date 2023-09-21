# import
import random

# picks a random integer between and including 0 and 1 (so either 0 or 1)
# therefore, this has a 50% chance to generate 0, and 50% chance for 1
# essentially, like a coinflip
random_number = random.randint(0, 1)

# just some (bad) ascii art for a coin
print("   ___  ")
print(" /     \\ ")

# if the number generated is 0 then display the heads component for the coin
if random_number == 0:
    print("|  :-)  | <- Heads!")

# if not then display the tails component
else:
    print("|  -=-  | <- Tails!")

print(" \\     /")
print("   --- ")
