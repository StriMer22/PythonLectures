"""
Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+
"""


v_size = int(input("Vertical: "))
h_size = int(input("Horizontal: "))

horizontal_line = "+"
vertical_line = "|"
square = ""

for i in range(0, h_size):
    horizontal_line += "---+"
    vertical_line += "   |"

square += (horizontal_line + "\n" + vertical_line + "\n") * \
    v_size + horizontal_line


print(square)
