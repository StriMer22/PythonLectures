while True:
    x = input("Enter a number: ")
    try:
        if x == 'stop':
            break
        print('x:', x, '\nx^3:', pow(float(x), 3), "\nFor stop, enter: 'stop'")
    except ValueError:
        print("Not a number")
