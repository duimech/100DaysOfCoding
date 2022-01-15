# This program is the object oriented programming version of a digital coffee machine that calculates money, change, and resources of the machine.
# Author: Ray Bolin
# Date: 1/15/2022
# 100DaysOfCoding


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:

    choice = input(f"What drink would you like {menu.get_items()}:  ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)