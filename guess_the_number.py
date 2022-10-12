from random import choice
HARD_LEVEL = 5
EASY_LEVEL = 10


def difficulty():
    level = input("difficulty: ")
    if level == '1':
        return HARD_LEVEL
    if level == '2':
        return EASY_LEVEL


def check_answer(numberToGuess, guessedNumber, turn):
    if guessedNumber > numberToGuess:
        print(f"too high")
        return turn - 1
    elif guessedNumber < numberToGuess:
        print(f"too low")
        return turn - 1
    else:
        print(f"you got it. the number is {numberToGuess}")

def game():
    attempts = difficulty()
    number_to_guess = choice(range(0, 101))
    print(number_to_guess)
    guessed_number = 0
    while number_to_guess != guessed_number:
        guessed_number = int(input("guess a number: "))
        attempts = check_answer(number_to_guess, guessed_number, attempts)
        print(f"you have {attempts} attempts to guess the number")
        if attempts == 0:
            print("your lose")
            return


game()