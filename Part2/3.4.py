"""
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz
trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. 
Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
"""

while True:
    x = input("Enter a number: ")
    try:
        if x == 'stop':
            break
        print('x:', x, '\nx^3:', pow(float(x), 3), "\nFor stop, enter: 'stop'")
    except ValueError:
        print("Not a number")
