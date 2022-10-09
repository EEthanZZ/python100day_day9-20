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


def compare(userscore, dealerscore):
    if userscore == dealerscore:
        return "draw"
    elif dealerscore == 0:
        return "you lose, dealer blackjack"
    elif userscore == 0:
        return "you win. blackjack"
    elif userscore > 21:
        return "you lose, you went over"
    elif dealerscore > 21:
        return "you win, dealer went over"
    elif dealerscore > userscore:
        return "dealer win"
    else:
        return "you win"


user_cards = list()
dealer_cards = list()

for i in range(0, 2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

game_on = True
while game_on:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f'your cards: {user_cards}, score is {user_score}')
    print(f'deal cards: {dealer_cards}, score is {dealer_score}')

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        game_on = False
    else:
        one_more = input("one more card?")
        if one_more == 'y':
            user_cards.append(deal_card())
            calculate_score(user_cards)
        if one_more == 'n':
            game_on = False

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

print(dealer_score)
print(compare(user_score, dealer_score))
