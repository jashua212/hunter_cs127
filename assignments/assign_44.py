
# assignment 44

import turtle


# function to draw a petal at the angle specified
def petal(color, angle):
	# create a new turtle, hiding its arrow
	t = turtle.Turtle(visible=False)

	# turn turtle
	t.left(angle)

	# draw a petal
	for i in range(0, 255, 10):
		# move turtle forward by 10
		t.forward(10)

		# set turtle's pensize (larger each time)
		t.pensize(i)

		# set turtle's color (greater intensity each time)
		if color == 'red':
			t.color(i, 0, 0)
		elif color == 'green':
			t.color(0, i, 0)
		elif color == 'blue':
			t.color(0, 0, i)
		elif color == 'yellow':
			t.color(i, i, 0)
		elif color == 'purple':
			t.color(i, 0, i)
		elif color == 'cyan':
			t.color(0, i, i)
		else:
			t.color(0, i, 0)  # default color is green


# function to draw flower
def flower(color, num):
	angleStep = 360 / num

	# draw 'num' of petals in 'color'
	for i in range(num):
		angle = i * angleStep
		petal(color, angle)


# main function
def main():
	# allow colors to be given as 0...255
	turtle.colormode(255)

	# turn on turtle screen mode
	wn = turtle.Screen()

	# set color of petals
	color = 'green'

	# set number of petals
	num = 9

	# call flower function, passing in color and num
	flower(color, num)

	# allow exit on user click
	wn.exitonclick()


if __name__ == '__main__':
	main()
