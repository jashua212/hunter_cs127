
# assignment 38

import turtle
import math

# create recursive function that draws one pentagon
def drawPantegon(t, length, numEdges):
	if numEdges > 0:
		# draw one side of a pentagon
		t.forward(length)
		t.left(72)

		# call itself again to draw another side, but with numEdges reduced by 1
		drawPantegon(t, length, numEdges-1)

# create recursive function to draw multiple pentagons from bottm left corner
def cornerPantegon(t, length):
	if length >= 25:
		# draw 1st pentagon to be the outer pentagon
		drawPantegon(t, length, 5)

		# call itself again to draw another pentagon, but with length reduced by half
		cornerPantegon(t, length/2)

# create recursive function to draw multiple nested pentagons
def nestedPantegon(t, length):
	if length >= 25:
		# draw 1st pentagon to be the outer pentagon
		drawPantegon(t, length, 5)

		# move turtle forward along the drawn pentagon's 1st side by length/2
		t.up()
		t.forward(length/2)
		t.down()

		# turn turtle left by 36 degrees
		t.left(36)

		# call itself again to draw another pentagon, but with a smaller length
		nestedPantegon(t, length * math.sin(54/180 * math.pi))


def main():
	wn = turtle.Screen()
	t = turtle.Turtle()

	# for testing only - increase turtle's size and speed
	t.pensize(2)
	t.speed(10)

	# draw blue corner pentagon
	t.left(90)
	t.up()
	t.forward(50)
	t.down()
	t.right(90)
	t.color('blue')
	cornerPantegon(t, 200)

	# draw green nested pentagon
	t.right(90)
	t.up()
	t.forward(350)
	t.down()
	t.left(90)
	t.color('green')
	nestedPantegon(t, 200)

	# move turtle offscreen when finished
	t.up()
	t.left(180)
	t.forward(200)
	t.color('white')

	wn.exitonclick()


if __name__ == '__main__':
	main()
