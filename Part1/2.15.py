"""
Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
"""
L = [1, 2, 3, 4, 5]

print(''.join([str(number) for number in L]))
