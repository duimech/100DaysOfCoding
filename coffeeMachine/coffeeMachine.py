# This program is a digital coffee machine that calculates money, change, and resources of the machine.
# Author: Ray Bolin
# Date: 1/14/2022
# 100DaysOfCoding

import menu

# Machine starts with the following
machine_resources = {
    "total_water": 300, 
    "total_coffee": 100, 
    "total_milk": 200
}

total_money = 0
total_transaction = 0


# Print report - how many resources are left including money
def show_report(machine_resources, total_money):
    print(f"Water: {machine_resources['total_water']}")
    print(f"Coffee: {machine_resources['total_coffee']}")
    print(f"Milk: {machine_resources['total_milk']}")
    print("Money: {:.2f}".format(total_money))


# Process coins - ask for quantity of each coin - make sure its enough or refund the money
def insert_coins():
    total = 0
    total += int(input("How many quarters:  ")) * 0.25
    total += int(input("How many dimes:  ")) * 0.10
    total += int(input("How many nickles:  ")) * 0.05
    total += int(input("How many pennies:  ")) * 0.01
    return total


# Check price of drink and calculate change
def check_price_get_change(user_drink, total_transaction):
    money = total_transaction - menu.MENU[user_drink]["cost"]
    return money

# Check resources - needs to determine if there are enough resources for the recipie requested  
def check_machines_resources(user_drink, machine_resources):
    total_water = machine_resources["total_water"]
    total_coffee = machine_resources["total_coffee"]
    total_milk = machine_resources["total_milk"]

    if user_drink != "espresso":
        total_milk -= menu.MENU[user_drink]["ingredients"]["milk"]
    
    total_water -= menu.MENU[user_drink]["ingredients"]["water"]
    total_coffee -= menu.MENU[user_drink]["ingredients"]["coffee"]

    if total_water >= 0 and total_coffee >= 0 and total_milk >= 0:
        machine_resources["total_water"] = total_water
        machine_resources["total_coffee"] = total_coffee
        machine_resources["total_milk"] = total_milk
        resource = "good"
        return resource
    else:
        if total_water < 0:
            resource = "water"
        elif total_coffee < 0:
            resource = "coffee"
        elif total_milk < 0:
            resource = "milk"
        
        return resource
    

more_coffee = True
while more_coffee == True:
    user_drink = input("What would you like? (espresso/latte/cappuccino):  ")

    # turn machine off / end program
    if user_drink == "off":
        more_coffee = False
    elif user_drink == "report":
        show_report(machine_resources, total_money)
    else:
        print("Please insert coins.")
        total_transaction = insert_coins()
        money_change = check_price_get_change(user_drink, total_transaction)

        # Only check the resources if they have enough money
        if money_change >= 0:
            resources = check_machines_resources(user_drink, machine_resources)

            if resources == "good":
                # Only update the total money if they have enough money and we have enough resources
                total_money += total_transaction - money_change
                print(f"Here is ${money_change} in change.")
                print(f"Here is your {user_drink}. Enjoy!")
            else:
                print(f"Sorry, there is not enough {resources}.")
        else:
            print("Sorry that's not enough money. Money refunded.")
            