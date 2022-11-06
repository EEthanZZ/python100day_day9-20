
menu = {
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
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


def coins():
    print("please put in the coins")
    a = int(input("$1: "))
    b = int(input("$0.5: "))
    return a + b*0.5


def resources_suff():
    for i in coffee_ingredients:
        if coffee_ingredients[i] >= resources[i]:
            print(f"there is not enough {i}")
            return False
    return True


def tran_seccuss(money_received, drink_cost):
    if money_received > drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f'here is ${change} for change')
        global profit
        profit += drink_cost
        return True
    else:
        print("money not enough")
        return False


def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"here is your {drink_name} ")


turn_off = False
while not turn_off:
    order = input("what would you like: ")
    if order == 'report':
        for i in resources:
            print(f'{i}: {resources[i]}')
        print(profit)
    elif order == 'off':
        turn_off = True
    else:
        drink = menu[order]
        coffee_ingredients = drink['ingredients']
        if resources_suff():
            payment = coins()
            if tran_seccuss(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])
