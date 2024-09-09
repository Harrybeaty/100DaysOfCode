MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

def check_resources(ingredients, coffees, user_choice):

    for key in ingredients:
        if ingredients[key] >= coffees[user_choice]["ingredients"][key]:
            print(f"Insufficient {key}")
# Stuck here i need to return false


# Get user's input
user_input = input("What would you like? (espresso/latte/cappuccino): ")

user_choice_water = MENU[user_input]["ingredients"]["water"]
user_choice_milk = MENU[user_input]["ingredients"]["milk"]
user_choice_coffee = MENU[user_input]["ingredients"]["coffee"]

if user_input == "off":
    exit()
elif user_input == "report":
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g ")
elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
    # Check if there are enough resources to make coffee.
    if resources["water"] >= user_choice_water and resources["milk"] >= user_choice_milk and resources["coffee"] >= user_choice_coffee:
        # Minus ingredients for a coffee from resources.
        for key in resources:
            resources[key] = resources[key] - MENU[user_input]["ingredients"][key]
    else:
        print("insufficient")