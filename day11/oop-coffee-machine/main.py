from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"what would you like? {option}")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient:
            if money_machine.make_payment(drink):
                if coffee_maker.make_coffee(drink.cost):
                    coffee_maker.make_coffee(order=drink)