
# assignment 8

# get phrase from user
phrase = input('Enter a phrase: ')

# print header for table
print('letter ASCII next_two_letter')

# print a row for each character
for char in phrase:
    asciiCode = ord(char)
    nextTwoLetter = chr(asciiCode + 2)

    print('%6c %5i %15c'%(char, asciiCode, nextTwoLetter))
