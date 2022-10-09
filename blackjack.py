from random import choice


cards_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return choice(cards_list)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards = list()
dealer_cards = list()
for i in range(0, 2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

print(calculate_score(user_cards))
print(calculate_score(dealer_cards))
print(f'your cards: {user_cards}')
print(f'deal cards: {dealer_cards}')