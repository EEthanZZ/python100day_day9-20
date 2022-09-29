
from replit import clear


print("welcome to the auction")

customers = []


def auction():
    name = input("name:   ")
    bid = input("bid:   ")
    customers.append({name: bid})


auction()
game_on = True
while game_on:

    game_again = input("any more bid?")
    if game_again == 'y':
        clear()
        auction()
    else:
        last_bid = customers[-1]
        a, b = list(last_bid.items())[0]
        print(a + " has the highest bid " + b)
        game_on = False
