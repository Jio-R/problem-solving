import random

def rnd7():
    return random.randint(1,7)

def rnd5():
    nums = list(range(1, 6))
    start = rnd7()
    if start < 6:
        return start
    return nums[(rnd7()-1) % 5]

def test(f):
    d = [0] * 5
    for i in range(100000):
        d[f()-1] += 1
    print(d)

def rnd5v2():
    nums = list(range(1, 6))
    start = rnd7()
    while start > 6:
        start=

test(rnd5)