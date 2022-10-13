from game_data import data
from random import randint, choice
from art import *


def check_answer(a, b):
    if a > b:
        return a
    else:
        return b
# construct two compares
compare_a = choice(data)
compare_b = choice(data)
print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
print(vs)
print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
a_followers = compare_a['follower_count']
b_followers = compare_b['follower_count']
x = input("who has more followers? ")
check_answer(a_followers, b_followers)
# check the answer:
# if a > b, return a / if b > a, return b

