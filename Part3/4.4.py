"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
"""


def fibonacci(n):
    fibs = [0, 1, 1]
    for f in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]


assert fibonacci(10) == 55
assert fibonacci(15) == 610
