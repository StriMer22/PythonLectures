import random
import math


def calc_pi(n=100):
    inside = 0
    for _ in range(n):
        x = pow(random.random(), 2)
        y = pow(random.random(), 2)
        if(math.sqrt(x + y) <= 1.0):
            inside += 1

    return 4 * (inside / n)


print('for n = 100 pi = ' + str(calc_pi(10)))
print('for n = 1000 pi = ' + str(calc_pi(100)))
print('for n = 10000 pi = ' + str(calc_pi(1000)))
print('for n = 100000 pi = ' + str(calc_pi(10000)))
print('for n = 1000000 pi = ' + str(calc_pi(100000)))
print('for n = 10000000 pi = ' + str(calc_pi(1000000)))
