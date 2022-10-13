from game_data import data
from random import randint, choice
from art import *
score = 0
compare_b = choice(data)


def check_answer(a, b):
    if a > b:
        return "a"
    else:
        return "b"


# construct two compares
game_on = True
while game_on:

    compare_a = compare_b
    compare_b = choice(data)

    while compare_a == compare_b:
        compare_b = choice(data)
    print(f"your score is {score}")
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    a_followers = compare_a['follower_count']
    b_followers = compare_b['follower_count']
    print(a_followers)
    print(b_followers)
    x = input("who has more followers? ")
    answer = check_answer(a_followers, b_followers)
    if answer == x:
        score += 1
    else:
        game_on = False
# check the answer:
# if a > b, return a / if b > a, return b

