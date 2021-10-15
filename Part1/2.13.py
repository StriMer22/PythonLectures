"""
Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
"""

line = "spring winter\t summer\n autumn"

print(sum([len(x) for x in line.split()]))
