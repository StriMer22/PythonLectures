"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, 
a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""


def sum_seq(sequence):
    summary = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            summary += sum_seq(x)
        else:
            summary += x
    return summary


assert sum_seq([0, 1, 1, 1, 10]) == 13
assert sum_seq([5, [1, 2, [4, 5, 1]], (1, 2, (2, 2))]) == 25
