"""
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
"""

line = 'The sum() adds start and items of the given iterable from left to right.'

longestWord = max(line.split(), key=len)

print('Longest word:', longestWord, '\nChars in longest word:', len(longestWord))
