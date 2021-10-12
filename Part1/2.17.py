line = 'Visit these pages \nto learn more about'

print('Alphabet sort:', sorted(line.split(), key=lambda word: word.lower()), '\nLength sort:',
      sorted(line.split(), key=len))
