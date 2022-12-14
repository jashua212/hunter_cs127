
# assignment 16

# get a semicolon-separated string of names from user
#namesString = input('Enter a list of names, separated by semicolon: ')
namesString = 'George Washington;John Adams;Thomas Jefferson;James Madison;James Monroe'

# split string into a list of names
names = namesString.split(';')
print('names:', names)


for item in names:
    words = item.split()

    firstName = words[0].upper()
    firstInitial = firstName[0:1]

    lastName = words[1].lower()
    lastInitCap = lastName[0:1].upper() + lastName[1:]

    print(firstInitial + '. ' + lastInitCap)
