line = "winter spring\t summer\n autumn"


def get_signs(startFrom):
    return ''.join([x[startFrom] for x in line.split()])


print('First signs:', get_signs(0), '\nLast signs:', get_signs(-1))
