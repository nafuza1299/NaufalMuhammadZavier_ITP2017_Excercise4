import math
d = lambda x: x ** 2
print(d (2))
c = lambda x, y : (x ** 2 + y ** 2) ** .5
print(c (2, 1))
d = lambda x, y, z: (x + y + z)/3
print(d (1, 2, 3))

t = lambda i:" ".join(set(i))
print(t("Hello"))

def square(x):
    x ** 2
    print(x)
square(3)

def sqrroot(a, b):
    c = (a ** 2 + b ** 2) ** .5
    print(c)
sqrroot(5, 3)

def avg(t, u, i):
    avg = (t + u + i)/3
    print(avg)
avg(9,10,13)

def unique(x):
    i = " ".join(set(x))
    print(i)
unique("Hello")
