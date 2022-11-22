
# assignment 47

# the assignment requires import of 'random' library
# but it is never used
import random


# function to get user feedback and to validate it
def validFeedback():
	# print out choices
	print('1: too small   2: too big   3: just right')

	# ask user for feedback
	feedback = int(input('Enter choice 1-3: '))

	# ask user for feedback again if it is not valid
	while feedback < 1 or feedback > 3:
		feedback = int(input('Enter choice 1-3: '))

	# return user feedback if it is valid
	return feedback


# function to make a guess
def makeGuess(start, end):
	guess = ((end - start) // 2) + start
	return guess


# function to run the game
def guessGame():
	# start the game
	start = 0
	end = 100
	print('Pick an integer in [' + str(start) + ', ' + str(end) + '] in your mind.')

	# make 1st guess, show it, and get user feedback
	guess = makeGuess(start, end)
	numGuesses = 1
	print('Guess ' + str(numGuesses) + ': is it ' + str(guess) + '?')
	feedback = validFeedback()

	# while user feedback is not 3
	while feedback != 3:
		# change start or end number based on user feedback
		if feedback == 1:
			start = guess + 1
		else:
			end = guess - 1

		# make a new guess, using new start and new end numbers
		guess = makeGuess(start, end)
		numGuesses = numGuesses + 1

		# new guess is the answer if new start and new end are same number
		if start == end:
			print('Guess ' + str(numGuesses) + ': the answer must be', guess)
			feedback = 3	# set feedback to 3

		# else show the new guess, and get user feedback
		else:
			print('Guess ' + str(numGuesses) + ': is it ' + str(guess) + '?')
			feedback = validFeedback()

	# print answer to exit game
	print('Congratulations! The answer is', guess)


def main():
	guessGame()

if __name__ == '__main__':
	main()
