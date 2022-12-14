import sys
print(sys.version+'\n')

# assignment 25

# CONVERT A STRING TO A DECIMAL NUMBER


string =  input('Enter a string with 0 or 1 only: ')
string = '100101'
#string = 'abcdef'

# initialize num at zero
num = 0

# set base to be the base of binary number
BASE = 2

# initialize weight at 1, for the least significant digit
weight = 1

# set length to be the number of letters of string
length = len(string)

# reverse string
#reversedString = string[::-1]

for i in range(length-1, -1, -1):
	ch = string[i]
	print('at index', i, 'of the string is character', ch)

	if ch == '1':
		# increase num by weight
		num = num + weight

	elif ch != '0':
		# exit program because user input is not a binary string
		print('Letter', ch, 'is not allowed in a binary string')
		quit()

	# update weight by multiplying it with base
	# n.b., this increased weight will be applied to the NEXT character
	weight = weight * BASE

print('weight for next character =', weight)
print('num =', num)
