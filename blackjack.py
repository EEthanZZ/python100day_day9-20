from random import choice


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return choice(cards)


user_cards = list()
dealer_cards = list()
for i in range(0, 2):
    deal_card()
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
print(user_cards)
print(dealer_cards)
print(sum(user_cards))