
# assignment 15

# get a phrase from user
#phrase = input('Enter a phrase: ')
phrase = 'Ding dong the wicked witch is dead!'

# split phrase (a string) into a list of words
words = phrase.split()
print('words:', words)

# get number of words in the list of words
numberOfWords = len(words)
#print('numberOfWords: ', numberOfWords)

# create a list of indices in reverse order for the list of words
reversedIndices = range(numberOfWords, 0, -1)

# print
for x in reversedIndices:
    print(' '.join(words[:x]))


# create a list of indices for the list of words
# KEY -- need to add 1 to numberOfWords (below) because in the case of SLICE function, it only goes up to BUT DOES NOT INCLUDE the 2nd index number -- e.g., the 'y' in words[:y] will exclude 2, as well as (7 + 1) !!!
indices = range(2, numberOfWords + 1)
#print(indices)

for y in indices:
    print(' '.join(words[:y]))
