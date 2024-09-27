from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffeeaction = CoffeeMaker()
moneyaction = MoneyMachine()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffeeaction.report()
        moneyaction.report()
    else:
        drink = menu.find_drink(choice)

        if coffeeaction.is_resource_sufficient(drink):
            cost = drink.cost

            if moneyaction.make_payment(cost):
                coffeeaction.make_coffee(drink)
            else:
                print("Insufficient Payment.")
        else:
            print("Insufficient Resources.")
            is_on = False



