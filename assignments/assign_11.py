
# assignment 11

import turtle

# allow colors to be given as 0...255
turtle.colormode(255)

wn = turtle.Screen()

t = turtle.Turtle()

t.penup()
t.backward(100)
t.left(90)
t.backward(100)
t.right(90)                   # you fill in a degree in ??
t.pendown()

# create range of 10,20,...,250 -- NOT starting from 0
rangeList = range(10,255,10)

# draw right shade
for item in rangeList:
    t.forward(10)             # move forward by 10
    t.pensize(item)           # set the drawing size to be item (larger each time)
    t.color(0,item,item)      # set the blue channel to be item (brighter each time)

# move to the start direction of up shade
t.penup()
t.backward(250)               # go backward 5 less than 255
t.left(90)
t.pendown()
t.pensize(0)
t.color(0,0,0)

# draw up shade
for item in rangeList:
    t.forward(10)             # move forward by 10
    t.pensize(item)           # set the drawing size to be item (larger each time)
    t.color(0,item,item)      # set the blue channel to be item (brighter each time)

wn.exitonclick()