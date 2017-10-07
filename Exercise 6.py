import math

def calculator(operation, format=float, *args):

    result = args[0]

    for n in args[1:]:
        if operation == "+":
            result += n
        if operation == "/":
            result /= n
        if operation == "*":
            result *= n
        if operation == '-':
            result -= n
    if format == float:
        result = float(result)
    elif format == int:
        result = math.round(result)

    return result


print(calculator(str(input("Operation: ")), float, 1, 4))
