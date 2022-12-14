
# assignment 13

import turtle

import math

# allow colors to be given as 0...255
turtle.colormode(255)

wn = turtle.Screen()

# get half the height of the equilateral triangle
radians_for_60_deg = math.pi/3
height = math.tan(radians_for_60_deg) * 100
half_height = height / 2
print('half_height:', half_height)

# create an instance of turtle
t = turtle.Turtle()
t.color(150,75,0)
t.turtlesize(2)

# position turtle so that it draws an equilateral triangle in the center
t.penup()
t.backward(100)
t.right(90)
t.forward(half_height)
t.left(90)

t.pendown()
t.pensize(2)         # may NOT be needed

for i in range(3):
    # draw one side
    t.forward(200)

    # turn turtle to next direction
    t.left(120)

    # stamp turtle
    t.shape('turtle')
    t.stamp()

wn.exitonclick()
