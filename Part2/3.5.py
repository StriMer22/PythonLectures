inputNum = int(input("Enter a number: "))
line = "|"
numbers = "0"

for i in range(inputNum):
    line += "....|"
    numbers += str(i + 1).rjust(5)

line += "\n" + numbers

print(line)
