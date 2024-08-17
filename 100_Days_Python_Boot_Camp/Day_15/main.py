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

request = input("what do you like : ")


def check_resources(req, menu):
    if request == "report":
        print("Water:", resources["water"], "\nmilk:", resources["milk"], "\ncoffe:", resources["coffee"])

    if request == "espresso":
        espresso_water = MENU["espresso"]["ingredients"]["water"]
        espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

        if espresso_water <= resources["water"] and espresso_coffee <= resources["coffee"]:
            return True
        else:
            return False

    if request == "latte":
        latte_water = MENU["latte"]["ingredients"]["water"]
        latte_milk = MENU["latte"]["ingredients"]["milk"]
        latte_coffee = MENU["latte"]["ingredients"]["coffee"]

        if (latte_water <= resources["water"] and latte_milk <= resources["milk"]
                and latte_coffee <= resources["coffee"]):
            return True
        else:
            return False

    if request == "cappuccino":
        espresso_water = MENU["cappuccino"]["ingredients"]["water"]
        espresso_milk = MENU["cappuccino"]["ingredients"]["milk"]
        espresso_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

        if (espresso_water <= resources["water"] and espresso_milk <= resources["milk"]
                and espresso_coffee <= resources["coffee"]):
            return True
        else:
            return False
# and request != "report"


if check_resources(request, resources) :
    print(f"There are enough resources to make {request}.")
else:
    print(f"Sorry, there are not enough resources to make {request}.")


def process_coins():
    # Collecting user input for the number of coins
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    # Calculate total value in dollars
    total_value = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_value


# Call the function and display the result
total = process_coins()
print(f"The total value of your coins is: ${total:.2f}")

def get_price(i, ):
    if i == "espresso":
        espresso_cost = MENU["espresso"]["cost"]
    if i == "cappuccino":
        cappuccino_cost = MENU["cappuccino]["cost"]
    if i == "latte":
        latte_cost = MENU["latte"]["cost"]
        print(latte_cost)

def check_transaction_successful(m):
    if total <= m:
        total -= m
        print("Transaction Successful! ")
    else:
        print("Sorry That’s not enough money, Money refunded.")


check_transaction_successful(total)



# # Collecting user input for the number of coins
# quarters = int(input("How many quarters? "))
# dimes = int(input("How many dimes? "))
# nickels = int(input("How many nickels? "))
# pennies = int(input("How many pennies? "))
#
# def process_coins(q, d, n, p):
#     # Calculate total value in dollars
#     total_value = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
#     return total_value
#
# # Call the function and display the result
# total = process_coins(quarters, dimes, nickels, pennies)
# print(f"The total value of your coins is: ${total:.2f}")

    # if request == "latte":
    #
    # if request == "cappuccino":
    #
    #     espresso_water = MENU["espresso"]["ingredients"]["water"]
    #
    #     espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    #
    #     latte_water = MENU["espresso"]["ingredients"]["water"]
    #
    #     latte_milk = MENU["espresso"]["ingredients"]["milk"]
    #
    #     latte_coffee = MENU["espresso"]["ingredients"]["coffee"]
    #
    #     espresso_water = MENU["espresso"]["ingredients"]["water"]
    #
    #     espresso_milk = MENU["espresso"]["ingredients"]["milk"]
    #
    #     espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]


        # "water"
        # "milk"
        # "coffee"

# print(request)

# Update data
# resources["water"] = ["water"] -

# TODO : Print Report
# TODO : Check resources sufficient?
# TODO : Process Coins
# TODO : Check Transaction Successful?
# TODO : Make Coffee
