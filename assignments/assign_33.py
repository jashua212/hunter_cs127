
# assignment 33

# create main function:
def main():
	# get user inputs:
	string = input('Enter a string: ')
	char = input('Enter a char: ')

	# for testing only - set user inputs (overwriting above):
	string = 'Hello, how are you?'
	char = 'o'

	# initiate count at 0:
	count = 0

	# loop through each character in string:
	for i in string:
		if i == char:
			count = count + 1

	# add quotation marks to be PRINTED around char and string
	# n.b., quotation marks to be printed are different - single
	# quotation marks for char, but double quotation marks for string:
	quotedChar = "'" + char + "'"
	quotedString = '"' + string + '"'

	# show result to user:
	print('number of', quotedChar, 'in', quotedString, 'is', count) 

# call main function:
if __name__ == '__main__':
	main()
