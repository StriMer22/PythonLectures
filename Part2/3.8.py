list1 = [2, 9, 4, 5, 10, 5]
list2 = [3, 5, 7, 2, 8]

print('Same elements in list1 & list2:', list(set(list1) & set(list2)),
      '\nAll elements from list1 & list2:', list(set(list1 + list2)))
