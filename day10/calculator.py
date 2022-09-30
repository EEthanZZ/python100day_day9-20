

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

num_1 = int(input("what is the first nunber: "))
for i in operations:
    print(i)
symbol = input("what is your opeartor? ")
num_2 = int(input("what is the second nunber: "))

function = operations[symbol]
answer = function(num_1, num_2)
print(answer)
