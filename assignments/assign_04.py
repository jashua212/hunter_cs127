
# assignment 4

import turtle

wn = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.shape('circle')
t.right(90)

for i in ['red', 'cyan', 'blue', 'green']:
    t.color(i)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)
    t.left(90)

t.color('red')
wn.exitonclick()
