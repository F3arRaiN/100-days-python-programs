

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



profit = 0

# prints report
def report(current_resource, our_profit):
    """ this function takes in the name of the coffee prints out the resources required to make that coffee as well as the money needed"""

    for ingredient in current_resource:
        if ingredient == "water":
            print(f"Water: {current_resource[ingredient]}ml")
        if ingredient == "milk":
            print(f"Milk: {current_resource[ingredient]}ml")
        if ingredient == "coffee":
            print(f"Coffee: {current_resource[ingredient]}g")
    print(f"Money: ${our_profit}\n")

# check if resources are enough
def resource_is_available(resource, coffee):
    """ checks if the resources available are sufficient to make the required coffee"""
    counter_max = 0
    counter = 0
    for item in resource:
        if item in MENU[coffee]["ingredients"]:
            counter_max +=1
            if resource[item] > MENU[coffee]["ingredients"][item]:
                counter += 1
            else:
                print(f"Sorry there is not enough {item}.")
    if counter_max == counter:
        return True
    else:
        return False


# money of customer
def total_money_of_customer(quarters, dimes, nickles, pennies):
    """ this code calculates the total amount that the user has inserted into the coffee machine"""
    total = round((float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickles) * 0.05) + (float(pennies) * 0.01), 2)
    return total

# checks transaction
def transaction(coffee):
    """ Checks if the user has inserted enough money to buy a coffee"""
    global profit
    global resources




    # checks if resources are enough and makes coffee deducting resources

    if resource_is_available(resources, coffee) == False:
        return print("\n")

    else:
        user_money = give_me_money()
        money_processed = False
        if user_money == MENU[coffee]["cost"]:
            profit += MENU[coffee]["cost"]
            money_processed = True
        elif user_money > MENU[coffee]["cost"]:
            print(f"Here is ${round((user_money - MENU[coffee]["cost"]), 2)} dollars in change.")
            profit += MENU[coffee]["cost"]
            money_processed = True

        if money_processed == True:
            for item in resources:
                if item in MENU[coffee]["ingredients"]:
                    resources[item] = resources[item] - MENU[coffee]["ingredients"][item]

            if coffee == "espresso":
                print("Here is your espresso ☕ Enjoy!")
            elif coffee == "latte":
                print("Here is your latte ☕ Enjoy!")
            elif coffee == "cappuccino":
                print("Here is your cappuccino ☕ Enjoy!")

            return resources

        else:
            return "Sorry that's not enough money. Money refunded"

# takes user money
def give_me_money():
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes: ")
    nickles = input("How many nickles: ")
    pennies = input("How many pennies: ")
    return total_money_of_customer(quarters, dimes, nickles, pennies)

def process(coffee):

    transaction(coffee)



running = True
while running:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if type_of_coffee == "off":
        running = False
    elif type_of_coffee == "report":
        report(resources, profit)
    else:
        if type_of_coffee in MENU:
            process(type_of_coffee)
        else:
            print("Please enter a valued Cup of coffee!\n")