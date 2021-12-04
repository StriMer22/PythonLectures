def solve(a, b, c):
    if(a == 0 and b != 0):
        y = -c / b
        print("x is any, y =", str(y))
    elif(a != 0 and b == 0):
        x = -c / a
        print("y is any, x = ", str(x))
    elif(a != 0 and b != 0):
        y = "(-" + str(a) + "* x -" + str(c) + "/b"
        print("The solution belongs to the interval (x,", str(y), ")",
              "x belongs to the set of real numbers.")

    elif(a == 0 and b == 0 and c == 0):
        print("An equation has infinitely many solutions")

    elif(a == 0 and b == 0 and c != 0):
        print("Conflicting equation")


solve(0, 0.5, -1)
solve(63, -7, 14)
