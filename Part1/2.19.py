"""
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków,
gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
"""
L = [1, 22, 333, 44, 555, 6, 77, 8, 99, 10]

print(' '.join([str(number).zfill(3) for number in L]))

