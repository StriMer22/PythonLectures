def romanToInt(romanChar) -> int:
    Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Int = 0
    n = len(romanChar)

    for index in range(n - 1):
        if Roman2Int[romanChar[index]] < Roman2Int[romanChar[index + 1]]:
            Int -= Roman2Int[romanChar[index]]
        else:
            Int += Roman2Int[romanChar[index]]

    return Int + Roman2Int[romanChar[-1]]


print(romanToInt('MDVI'))
