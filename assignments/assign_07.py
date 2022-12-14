
# assignment 7

# get user's name
nameResponse = input('Enter name in format firstName lastName: ')

# split user's name into first and last names
names = nameResponse.split()
firstName = names[0]
lastName = names[1]

# make lastName upper case
lastUpper = lastName.upper()

# alternative 1 for init capping first name
# firstInitCap = firstName[0].upper() + firstName[1:].lower()

# alternative 2 for init capping first name
firstInitCap = ''
for i in range(len(firstName)):
    print(i)
    if i == 0:
        firstInitCap = firstName[i].upper()
    else:
        firstInitCap += firstName[i].lower()

# print user's last and first names
print('name in LASTNAME, firstName format: ' + lastUpper + ', ' + firstInitCap)


# get user's email name
userNameResponse = input('Enter user name of email: ')
userName = userNameResponse.lower()

# print user's email address
print('email: ' + userName + '@hunter.cuny.edu')
