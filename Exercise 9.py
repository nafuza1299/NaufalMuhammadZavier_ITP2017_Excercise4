def my_gen(n):
    i = n
    while i >= 0:
        yield i
        i -= 1
g = my_gen(6)
for x in g:
    print(x)
