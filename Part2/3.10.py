"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) 
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący 
całą liczbę [funkcja roman2int()].
"""

Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Firtst method


def romanToInt(number):
    result = 0
    temp_num = 0
    for c in number:
        result += Roman2Int[c]
        if Roman2Int[c] > temp_num:
            result -= temp_num * 2
        temp_num = Roman2Int[c]
    return result

# Second method for only one roman number


def roman2int(number):
    return Roman2Int.get(number)


print(romanToInt('MDVI'))
print(roman2int('D'))
