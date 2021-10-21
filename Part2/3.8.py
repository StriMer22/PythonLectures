"""
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie 
w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""

list1 = [2, 9, 4, 5, 10, 5]
list2 = [3, 5, 7, 2, 8]

print('Same elements in list1 & list2:', list(set(list1) & set(list2)),
      '\nAll elements from list1 & list2:', list(set(list1 + list2)))
