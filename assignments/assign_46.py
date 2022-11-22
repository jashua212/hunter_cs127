
# assignment 46

def isPerfect(num):
	# convert num from string to integer
	num = int(num)

	if num <= 0:
		return False
	else:
		# initiate total at 0
		total = 0

		# use range() to create an array from 1 through num/2
		# need to add 1 to 'stop' number because it is excluded
		testers = range(1, (num//2)+1, 1)

		for i in testers:
			# add i to total if i is a factor of n
			if num % i == 0:
				total = total + i

		# return True if num == total; else return False
		return num == total


def main():
	num = input('Enter a perfect integer: ')
	result = isPerfect(num)

	while result == False:
		# get another number from user
		num = input(num + ' is not a perfect number. Re-enter: ')

		# check if new number is a perfect number
		result = isPerfect(num)

	print('Congratulations!', num, 'is a perfect number.')


if __name__ == '__main__':
	main()
