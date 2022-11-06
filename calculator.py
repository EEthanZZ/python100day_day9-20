

def addition(a, b):
    return a + b


def substruct(a, b):
    return a - b


def multiply(a, b):
    return a * b


def devide(a, b):
    return a / b


operations = {
    "+": addition,
    "-": substruct,
    "*": multiply,
    "/": devide
}


def calculation():
    num_1 = int(input("what is the first nunber: "))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue:
        symbol = input("what is your opeartor? ")
        num_2 = int(input("what is the second nunber: "))

        function = operations[symbol]
        answer = function(num_1, num_2)
        print(f'{num_1}{symbol}{num_2} = {answer}')
        if input("continue yes or no") == 'y':
            num_1 = answer
        else:
            should_continue = False
            calculation()


if input("start the calculator? ") == "y":
    calculation()

