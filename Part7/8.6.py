values = {(0, 0): 0.5}


def p(i, j):
    if i < 0 or j < 0:
        raise ValueError("Arguments must be greater or equal to 0.")

    if (i, j) in values.keys():
        return values.get((i, j))

    if (i > 0) and (j == 0):
        return 0.0
    elif (i == 0) and (j > 0):
        return 1.0
    elif (i > 0) and (j > 0):
        values[(i, j)] = 0.5 * (p(i - 1, j) + p(i, j - 1))
        return values.get((i, j))


assert p(1, 0) == 0.0
assert p(3, 1) == 0.125
assert p(3, 2) == 0.3125
assert p(0, 0) == 0.5
assert p(0, 1) == 1.0
assert p(7, 3) == 0.08984375


# the dynamic version is faster than the recursive version, because it stores the already known results and does not
# waste time calculating them - the function simply returns them from the dictionary
