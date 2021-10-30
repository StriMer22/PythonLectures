"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
"""


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


assert factorial(5) == 120
assert factorial(4) == 24
