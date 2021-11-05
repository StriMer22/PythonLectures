"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, 
tylko korzystać z argumentów.
"""


def linear(length):
    line = "|"
    numbers = "0"

    for i in range(length):
        line += "....|"
        numbers += str(i + 1).rjust(5)

    line += "\n" + numbers
    return line


def rectangle(rows, cols):

    horizontal_line = "+"
    vertical_line = "|"

    for _ in range(0, cols):
        horizontal_line += "---+"
        vertical_line += "   |"

    return (horizontal_line + "\n" + vertical_line + "\n") * rows + horizontal_line


print(linear(10))
print(rectangle(2, 4))
