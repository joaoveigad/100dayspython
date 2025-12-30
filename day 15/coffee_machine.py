MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def compare_resources(user_choice):
    for resource, amount in MENU[user_choice]["ingredients"].items():
        if resources[resource] < amount:
            print(f'Sorry, there is not enough {resource}. Please try again.')
            refill_resources()
            return False
    print("yes you did it... you did order your coffee... oh yes... coffee ordered. ok good yes.")
    return True

def subtract_resources(user_choice):
    for resource, amount in MENU[user_choice]["ingredients"].items():
        resources[resource] -= amount

def refill_resources():
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100

def transaction(user_choice):
    pennies = int(input("How many one (1) cent pennies would you like to insert? "))
    nickles = int(input("How many five (5) cent nickles would you like to insert? "))
    dimes = int(input("How many ten (10) cent dimes would you like to insert? "))
    quarters = int(input("How many twenty-five (25) cent quarters would you like to insert? "))

    value_inserted = (
        pennies * 0.01 +
        nickles * 0.05 +
        dimes * 0.10 +
        quarters * 0.25
    )

    if value_inserted < MENU[user_choice]["cost"]:
        print("Not enough cash! Stranger...")
        return False
    elif value_inserted > MENU[user_choice]["cost"]:
        change = round(value_inserted - MENU[user_choice]["cost"], 2)
        print(f'Your change: {change}')
        resources["money"] += MENU[user_choice]["cost"]
        subtract_resources(user_choice)
        return True
    resources["money"] += MENU[user_choice]["cost"]
    subtract_resources(user_choice)
    return True


def turn_on():
    while True:
        user_choice = input("What would you like? (espresso / latte / cappuccino): ").lower()
        match user_choice:
            case "report":
                print(resources)
            case "espresso" | "latte" | "cappuccino":
                print(f'You chose: {user_choice}')
                compare_resources(user_choice)
                transaction(user_choice)
                print("Coffee ordered!")
            case "off":
                return
            case _:
                print("Invalid option")



turn_on()

