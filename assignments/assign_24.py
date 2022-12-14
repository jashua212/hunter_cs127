
# assignment 24

string =  input('Enter a list of words, separated by a space: ')
#string = 'apple banana cantalope durian shrub'
#string = 'af bce gdfgb agcg edc dade fggga gb'

words = string.split()
totalWords = len(words)
print('number of words:', totalWords)

count = 0
for w in words:
    totalCharacters = len(w)
    #print('totalCharacters:', totalCharacters)

    # get word's last character
    lastChar = w[-1]
    #print('lastChar: ', lastChar)

    if lastChar == 'a' or lastChar == 'b':
        count = count + 1

print('number of words ending with a or b:', count)
print('fraction of words starting with a or b:', round(count/totalWords, 2))
