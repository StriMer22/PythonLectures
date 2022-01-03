"""
Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
(a) różne liczby int od 0 do n-1 w kolejności losowej,
(b) różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
(c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności,
(d) n liczb float w kolejności losowej o rozkładzie gaussowskim,
(e) n liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < n, np. k^2 = n).
"""

import random
import numpy as np

# podpunkt a


def unsortedArr(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    random_data = []

    while n > 0:
        index = random.randint(0, n - 1)
        random_data.append(numbers[index])
        del numbers[index]
        n -= 1
    return random_data

# podpunkt b


def nearlySortedArr(n):
    unsorted_arr = unsortedArr(n)
    part_len = n - n // 4
    for i in range(part_len):
        for j in range(0, part_len - i - 1):
            if unsorted_arr[j] > unsorted_arr[j + 1]:
                unsorted_arr[j], unsorted_arr[j +
                                              1] = unsorted_arr[j + 1], unsorted_arr[j]
    return unsorted_arr

# podpunkt c


def reversedNSA(n):
    return list(reversed(nearlySortedArr(n)))

# podpunkt d


def gaussian(n):
    return list(np.random.randn(n))

# podpunkt e


def arrK_set(n):
    k_set = unsortedArr(random.randint(1, n - 1))
    random_k_data = []

    for i in range(n):
        random_k_data.append(k_set[random.randint(0, len(k_set) - 1)])
    return random_k_data


# print(unsortedArr(5))
# print(nearlySortedArr(5))
# print(reversedNSA(5))
# print(gaussian(5))
# print(arrK_set(5))
