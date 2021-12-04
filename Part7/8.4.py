import math


def heron(a, b, c):
    if(a+b < c or a+c < b or b+c < a or a < 0 or b < 0 or c < 0):
        raise ValueError("This is not a triangle!")
    semi_perimeter = 1/2 * (a + b + c)
    return round(math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)), 2)


assert '9.8' == str(heron(4, 5, 7))
assert '8.79' == str(heron(9, 3, 7))
assert '5.56' == str(heron(2, 6, 7))
assert '12.79' == str(heron(4, 6.5, 7))
