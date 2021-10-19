square = ""
size = range(int(input("Vertical:")))
size2 = range(int(input("Horizontal:")))
for x in size:
    square += "+---" * len(size2) + "+\n"
    square += "|   " * (len(size2) + 1) + "\n"
    if x == len(size) - 1:
        square += "+---" * len(size2) + "+\n"
print(square)
