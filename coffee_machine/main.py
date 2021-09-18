machine_is_on = 1
machine_resources = {"milk": 300, "water": 300, "coffee": 100, "change": 10}
item_prices = {"espresso": 1, "latte": 2.50, "weird coffee": 3.00}
item_requirements = {"espresso": {"milk": 0, "water": 20, "coffee": 13},
                     "latte": {"milk": 30, "water": 25, "coffee": 20},
                     "weird coffee": {"milk": 40, "water": 25, "coffee": 25}, }


def give_user_options():
    selected_option = input("Hello, welcome to the coffee machine ☕️ ! \n Here are the options : \n 1. Espresso  \n "
                            "2. Latte \n 3. Weird "
                            "coffee \n 4. Report \n 5. off \n")
    return selected_option


def check_resources(needed_resources, current_machine_resources):
    if needed_resources["milk"] < current_machine_resources["milk"] and needed_resources["coffee"] < \
            current_machine_resources["coffee"] and \
            needed_resources["water"] < current_machine_resources["water"]:
        return 1
    return 0


def update_machine_resources(needed_resources, curren_machine_resources, item_price, transaction_change):
    new_milk_value = curren_machine_resources["milk"] - needed_resources["milk"]
    new_water_value = curren_machine_resources["water"] - needed_resources["water"]
    new_coffee_value = curren_machine_resources["coffee"] - needed_resources["coffee"]
    new_change_value = update_machine_change(item_price, transaction_change, curren_machine_resources["change"])
    return {"milk": new_milk_value, "water": new_water_value, "coffee": new_coffee_value, "change": new_change_value}


def update_machine_change(item_price, transaction_change, current_change):
    return current_change + item_price - transaction_change


def process_payment(amount_to_pay):
    paid_amount = 0
    while not paid_amount >= amount_to_pay:
        print("Amount due $", amount_to_pay - paid_amount)
        inserted_coin = input("Please insert either $0.25 or $0.10 or $0.05 \n")
        if inserted_coin == "0.25" or inserted_coin == "0.10" or inserted_coin == "0.05":
            paid_amount += float(inserted_coin)
        else:
            print("Unsupported coin please enter a valid coin ❌")
    return paid_amount - amount_to_pay


def process_user_order(user_order):
    print("Great choice")
    print("An", user_order, "will cost you", item_prices[user_order])
    if check_resources(item_requirements[user_order], machine_resources):
        receipts_value = process_payment(item_prices[user_order])
        print("====Receipts====")
        print("\t You ordered", user_order, "\t $", item_prices[user_order])
        print("\t You paid \t", "$", item_prices[user_order] + receipts_value)
        print("Your change is \t ", "$", receipts_value)
        print("================")

        new_machine_resources = update_machine_resources(item_requirements[user_order], machine_resources,
                                                         item_prices[user_order], receipts_value)
        print("Preparing your drink ...")
        print("Enjoy your order ! ")
        return new_machine_resources
    else:
        print("Sadly the machine does not have the sufficient resources to fill your order ð")


while machine_is_on:
    selected_user_option = give_user_options().lower()

    if selected_user_option == "espresso" or selected_user_option == "1":
        machine_resources = process_user_order("espresso")
    elif selected_user_option == "latte" or selected_user_option == "2":
        machine_resources = process_user_order("latte")
    elif selected_user_option == "weird coffee" or selected_user_option == "3":
        machine_resources = process_user_order("weird coffee")
    elif selected_user_option == "report" or selected_user_option == "4":
        print("=======Report=======")
        print("Milk: ", machine_resources["milk"], "ml")
        print("Water: ", machine_resources["water"], "ml")
        print("Coffee: ", machine_resources["coffee"], "ml")
        print("Change: $", machine_resources["change"])
        print("=======End of report=======")
    elif selected_user_option == "Off" or selected_user_option == "off" or selected_user_option == "5":
        print("Turning off ... !")
        print("See you another time !")
        machine_is_on = 0
    else:
        machine_is_on = 0
        print("Unsupported command ❌")
        give_user_options()
