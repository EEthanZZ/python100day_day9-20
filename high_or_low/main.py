from game_data import data
from random import randint, choice
# construct two compares
compare_a = choice(data)
compare_b = choice(data)
print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
