
# assignment 37

import turtle

# create function that draws one petal and then calls
# itself (i.e., recursion) to draw the next petal
def flowerRecursion(t, n):
	if n > 0:
		# draw one one petal
		t.forward(100)
		t.left(105)
		t.forward(52)
		t.left(105)
		t.forward(100)

		# turn turtle so that it is pointed in the
		# correct direction when it draws the next petal
		t.right(170)

		# this function will now call itself so it draws
		# the next petal
		# the 'n' variable that gets passed in on the recursive
		# call MUST BE DECREASED by 1 - otherwise, this function
		# will keep calling itself forever in an infinite loop
		flowerRecursion(t, n-1)


def main():
	wn = turtle.Screen()
	t = turtle.Turtle()

	# for testing only - increase turtle's size and speed
	t.pensize(2)
	t.speed(10)

	# call flowerRecursion function, passing in n = 9,
	# to draw a flower with 9 petals
	flowerRecursion(t, 9)

	wn.exitonclick()


if __name__ == '__main__':
	main()
