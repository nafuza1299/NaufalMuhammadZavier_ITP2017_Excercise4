import math
def calculate(a, b, c, d):
    if c == "+":
        e = a + b
    elif c== "/":
        e = a / b
    elif c == "*":
        e = a * b
    elif c == "-":
        e = a - b
    else:
        e = a + b
    if e == a / b:
        e = d
        print(float(d))
    if d == "Int":
            d = int(e)
            print(int(d))
    if d == 'Float':
            d = int(e)
            print(float(d))

calculate(float(input("A = ")), float(input("B = ")), str(input("Operation: ")), str(input("Int or Float? ").title().strip()))
