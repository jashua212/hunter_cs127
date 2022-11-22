
# assignment 48

# import library to generate random number
import random


# function to get user feedback and to validate it
def validUserNumber():
	# get user's number
	userNum = int(input('Enter only 1-6: '))

	# ask user for number again if it is not valid
	while userNum < 1 or userNum > 6:
		print('Input needs to be in 1-6. Re-enter:')
		userNum = int(input('Enter only 1-6: '))

	# return user number if it is valid
	return userNum


# function to run the game
def compareGame():
	# start the game
	user = validUserNumber()

	# generate random number
	computer = random.randint(1, 6)

	# print out user and computer numbers
	print('user:', user)
	print('computer:', computer)

	# calculate sum of both numbers
	sum = user + computer
	print('debug sum:', sum)	# for debugging only

	# compare numbers
	if user == computer:
		print('draw')
	elif sum == 3 or sum == 6 or sum == 7 or sum == 8:
		print('user wins')
	else:
		print('computer wins')


def main():
	compareGame()

if __name__ == '__main__':
	main()
