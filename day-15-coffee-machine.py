MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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


profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def add_resources():
    global resources
    resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    }
    
def make_coffee(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    coffee_water = ingredients['water']
    coffee_milk = ingredients['milk']
    coffee = ingredients['coffee']
    cost = MENU[coffee_type]["cost"]
    
    if resources["water"] >= coffee_water and resources["milk"] >= coffee_milk and resources['coffee'] >= coffee:
        print("resources available")
        print(f"{coffee_type} costs ${cost}. Please enter coins.")
        money = process_coins()
        if money >= cost:
            resources["water"] -= coffee_water
            resources["milk"] -= coffee_milk
            resources["coffee"] -= coffee
            change = money-cost
            
            print(f"Here is your {coffee_type}. Enjoy")
            global profit
            profit += cost
            print(f"Here is your change {change:.2f}")
        else:
            print(f"Insufficient money. {coffee_type} costs {cost} but you paid {money:.2f}.")
            print(f"{money:.2f} refunded.")
    else:
        print(f"Resources not available for {coffee_type}")
        print(f"Available resources are {resources}")
        add = input("Do you want to add resources: Type 'Y' for yes and 'N' for no: ").lower()
        if add == 'y':
            add_resources()
            make_coffee(user_input)
    return profit
        

while True:
    user_input = input("What would you like to have? Espresso/ latte/ cappuccino: ").lower()

    if user_input == 'report':
        print(f"Resources available {resources}")
        print(f"Here is your total profit {profit}")
    elif user_input == 'off':
        break
    elif user_input == 'latte' or 'espresso' or 'cappuccino':
        make_coffee(user_input)





