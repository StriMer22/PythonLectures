
"""
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
"""

import math


def simple(n, d):
    gcd = math.gcd(n, d)
    return [n / gcd, d / gcd]


def add_frac(frac1, frac2):
    n = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    d = frac1[1] * frac2[1]
    return simple(n, d)


def sub_frac(frac1, frac2):
    n = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    d = frac1[1] * frac2[1]
    return simple(n, d)


def mul_frac(frac1, frac2):
    n = frac1[0] * frac2[0]
    d = frac1[1] * frac2[1]
    return simple(n, d)


def div_frac(frac1, frac2):
    n = frac1[0] * frac2[1]
    d = frac1[1] * frac2[0]
    return simple(n, d)


def is_positive(frac):
    return frac[0] > 0


def is_zero(frac):
    return not frac[0]


def cmp_frac(frac1, frac2):
    if frac2float(frac1) > frac2float(frac2):
        return 1
    elif frac2float(frac1) == frac2float(frac2):
        return 0
    else:
        return -1


def frac2float(frac):
    return float(frac[0] / frac[1])
