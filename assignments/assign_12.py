
# assignment 12

import turtle

# allow colors to be given as 0...255
turtle.colormode(255)

wn = turtle.Screen()

t = turtle.Turtle()

t.penup()
t.backward(250)
t.pendown()

# create range of 0,10,...,250
rangeList = range(0,255,10)

# draw right, increasing in size
for item in rangeList:
    t.forward(10)             # move forward by 10
    t.pensize(item)           # set the drawing size to be item (larger each time)
    t.color(item,0,item)      # set the red & blue channels to be item (brighter each time)

# create reverse range of 255,245,...,5
reversedRangeList = range(255,0,-10)

# draw right, decreasing in size
for item in reversedRangeList:
    t.forward(10)             # move forward by 10
    t.pensize(item)           # set the drawing size to be item (smaller each time)
    t.color(item,0,item)      # set the red & blue channels to be item (darker each time)

# make a turtle stamp at end
t.shape('turtle')
t.stamp()

wn.exitonclick()
