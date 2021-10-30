"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence),
 która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, 
 a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print ( flatten(seq) )   # [1,2,3,4,5,6,7,8,9]
"""


def flatten(sequence):
    list1 = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            list1 += flatten(x)
        else:
            list1.append(x)
    return list1


assert flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [
    1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([1, 2, 3, [4, [5, 6], [7, 8]], (9, (10, 11))]) == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert flatten((1, (((2, 3, 4)), 5, (6, 7, 8, 9), [10]))) == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
