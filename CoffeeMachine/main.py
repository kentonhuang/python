from decimal import Decimal

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0.0,
}

coffee_machine_on = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_choice(choice):

    if choice == 'off':
        return False

    if choice == 'report':
        print_report()
        return False

    else:
        return check_resource(choice)


def check_resource(coffee):
    enough_water = resources['water'] - MENU[coffee]['ingredients']['water'] >= 0
    enough_coffee = resources['coffee'] - MENU[coffee]['ingredients']['coffee'] >= 0
    enough_milk = resources['milk'] - MENU[coffee]['ingredients']['milk'] >= 0

    if(enough_coffee and enough_water and enough_milk):
        return True
    else:
        if not enough_water:
            print("Sorry, there is not enough water")
        elif not enough_coffee:
            print("Sorry, there is not enough coffee")
        else:
            print("Sorry, there is not enough milk")

        return False


def calc_coins(quarters, dimes, nickels, pennies, coffee):
    NICKEL_VALUE = 0.05
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10
    PENNY_VALUE = 0.01

    coffee_cost = MENU[coffee]['cost']

    total_value = quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickels * NICKEL_VALUE + pennies * PENNY_VALUE

    if total_value <= coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    else:
        resources['money'] = resources['money'] + coffee_cost
        return True


def give_change(quarters, dimes, nickels, pennies, coffee):
    NICKEL_VALUE = 0.05
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10
    PENNY_VALUE = 0.01

    coffee_cost = MENU[coffee]['cost']

    total_value = quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickels * NICKEL_VALUE + pennies * PENNY_VALUE

    change = Decimal(total_value - coffee_cost).quantize(Decimal("0.00"))

    return change


def modify_resources(coffee):
    coffee_water = MENU[coffee]['ingredients']['water']
    coffee_coffee = MENU[coffee]['ingredients']['coffee']
    coffee_milk = MENU[coffee]['ingredients']['milk']

    resources['water'] = resources['water'] - coffee_water
    resources['coffee'] = resources['coffee'] - coffee_coffee
    resources['milk'] = resources['milk'] - coffee_milk


while coffee_machine_on:

    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == 'off':
        coffee_machine_on = False

    valid_choice = check_choice(prompt)

    if coffee_machine_on and valid_choice:
        print("Please insert coins.")

        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies: "))

        paid = calc_coins(quarters, dimes, nickels, pennies, prompt)

        if paid:
            modify_resources(prompt)
            change = give_change(quarters, dimes, nickels, pennies, prompt)

            print(f"{change} is your change.")
            print(f"Here is your {prompt}. Enjoy!")
