# This will calculate the price of pizza based in size, ingredients, and extra cheese
# Author: Ray Bolin
# Date: 1/1/2022
# 100DaysOfCoding

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

total = 0

if size == "S":
    total += 15
    if add_pepperoni == "Y":
        total += 2
    if extra_cheese == "Y":
        total += 1
elif size == "M":
    total += 20
    if add_pepperoni == "Y":
        total += 3
    if extra_cheese == "Y":
        total += 1
else:
    total += 25
    if add_pepperoni == "Y":
        total += 3
    if extra_cheese == "Y":
        total += 1

print(f"Your final bill is: ${total}.")
