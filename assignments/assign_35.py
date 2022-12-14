
# assignment 35

# create main function:
def main():
	hour = input('Enter hour (in 24 hour time): ')
	num = int(hour) % 24

	if num < 12:
		response = 'Good Morning'
	elif num < 17:
		response = 'Good Afternoon'
	else:
		response = 'Good Evening'

	print(response)


# call main function:
if __name__ == '__main__':
	main()
