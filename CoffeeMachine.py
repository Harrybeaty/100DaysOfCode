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

def check_resource(ingredients, coffee):

    for key in ingredients:
        if ingredients[key] < coffee[key]:
            print(f"Insufficient {key}")
            return False

def process_coins(q, d ,n, p):
    total = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    return total

# Get user's input
on = True
while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g ")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        coffee_resource = MENU[user_input]["ingredients"]
        coffee_cost = MENU[user_input]["cost"]
        # Check if there are enough resources to make coffee.
        if check_resource(resources, coffee_resource) != False:
            # Minus ingredients for a coffee from resources.
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total = process_coins(quarters, dimes, nickles, pennies)
            if total >= coffee_cost:
                for key in resources:
                    resources[key] = resources[key] - coffee_resource[key]
                revenue =+ coffee_cost
                change = total - coffee_cost
                print(f"You're change is ${change}.")
            else:
                print("Insufficient Money")
