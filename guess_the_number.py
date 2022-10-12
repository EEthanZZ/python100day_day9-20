from random import choice


def difficulty():
    level = input("difficulty: ")
    if level == 'easy':
        return 10
    if level == 'hard':
        return 5


attempts = difficulty()
number_to_guess = choice(range(0, 101))
print(f"you have {attempts} attempts to guess the number")
print(number_to_guess)

