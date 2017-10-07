import math
def hypo(c, d):
    try:
        return math.sqrt(c**2+ d**2)
    except TypeError:
        return None
print(hypo(1, 4))
print(hypo("1", "3"))
print(hypo("1", 4))
