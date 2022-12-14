
# assignment 3

import turtle

wn = turtle.Screen()

myTurtle = turtle.Turtle()

for i in range(9):
    myTurtle.forward(100)
    myTurtle.left(105)
    myTurtle.forward(52)
    myTurtle.left(105)
    myTurtle.forward(100)
    myTurtle.right(170)

wn.exitonclick()
