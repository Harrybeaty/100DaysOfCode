MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource(coffee_ingredients):

    for key in coffee_ingredients:
        if coffee_ingredients[key] >= resources[key]:
            print(f"Insufficient {key}")
            return False
    return True

def process_coins():
    """Returns total money inserted and returns total."""
    print("Please insert coins.")
    total = int(input("How many quarters? "))* 0.25
    total += int(input("How many dimes? "))* 0.1
    total += int(input("How many nickles? "))* 0.05
    total += int(input("How many pennies? "))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """ Return True if money received is larger than the cost of the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"£{change}")
        global revenue
        revenue += drink_cost
        return True
    else:
        print("Sorry you have not inserted enough money.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name}.")
# Get user's input
on = True
revenue = 0
while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        coffee_resource = MENU[user_input]["ingredients"]
        coffee_cost = MENU[user_input]["cost"]
        # Check if there are enough resources to make coffee.
        payment = process_coins()
        if check_resource(coffee_resource):
            # Minus ingredients for a coffee from resources.
            if is_transaction_successful(payment, coffee_cost):
                make_coffee(user_input, coffee_resource)

