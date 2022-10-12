from random import choice
HARD_LEVEL = 5
EASY_LEVEL = 10


def difficulty():
    level = input("difficulty: ")
    if level == '1':
        return HARD_LEVEL
    if level == '2':
        return EASY_LEVEL


def too_high():
    print("too high")
    print(f'you have {attempts -1 - i} attempts remaining')


def too_low():
    print("too low")
    print(f'you have {attempts -1 - i} attempts remaining')


def correct_guess():
    print("you made it")
    pass


attempts = difficulty()
number_to_guess = choice(range(0, 101))
print(f"you have {attempts} attempts to guess the number")
print(number_to_guess)
print(type(attempts))

for i in range(1, attempts + 1):
    guessed_number = int(input("guess:"))
    if guessed_number > number_to_guess:
        too_high()
    elif guessed_number < number_to_guess:
        too_low()
    else:
        correct_guess()
        break
