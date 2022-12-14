
# assignment 10

# get phrase from user
#phrase = input('input: ')

#debug test
phrase = 'City Univ of New York'

# alternative 1 — reverse letters of phrase
reversedPhrase_1 = phrase[::-1]
print('reversedPhrase_1:', reversedPhrase_1)




# alternative 2 — reverse letters of phrase
reversedPhrase_2 = ''
for letter in phrase:
    reversedPhrase_2 = letter + reversedPhrase_2

# print reversed phrase and in all capitals
print('') # new line
print('user reverse:', reversedPhrase_2)
print('user reverse upper:', reversedPhrase_2.upper())

# split phrase into separate words
words = phrase.split()

# create abbreviation
abbreviation = ''
for word in words:
    abbreviation = abbreviation + word[0].upper()

print('abbreviation:', abbreviation)
