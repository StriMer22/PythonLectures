"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście 
od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). 
Rozważyć wersję iteracyjną i rekurencyjną.
"""

# iteration


def odwracanie_i(L, left, right):
    while left < right:
        helper = L[left]
        L[left] = L[right]
        L[right] = helper
        left += 1
        right -= 1
    return L


# recursion
def odwracanie_r(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        return odwracanie_r(L, left + 1, right - 1)
    else:
        return L


list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
list3 = [1, 2, 3, 4, 5, 6]
assert odwracanie_i(list1, 0, 2) == [3, 2, 1, 4, 5, 6]
assert odwracanie_r(list2, 0, 7) == [8, 7, 6, 5, 4, 3, 2, 1]
assert odwracanie_i(list3, 0, 5) == [6, 5, 4, 3, 2, 1]
assert odwracanie_r(list3, 0, 5) == [1, 2, 3, 4, 5, 6]
