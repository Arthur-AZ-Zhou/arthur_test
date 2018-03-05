#Drawing a Car
import turtle
t = turtle.Pen()
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()
#Color Things In
t.reset()
t.color(1,1,0)
t.begin_fill()
t.circle(50)
t.end_fill()
#Draw a filled circle w/ function
def mycircle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
mycircle(0,1,0)

mycircle(0,0.5,0)

mycircle(0,0,1)

mycircle(0,0,0.5)

mycircle(0.9,0.75,0)

mycircle(1,0.7,0.75)

mycircle(1,0.5,0)

mycircle(0.9,0.5,0.15)

mycircle(0,0,0)

mycircle(1,1,1)

#Square drawing function
t.reset()
def mysquare(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)
mysquare(50)
t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)
#Drawing filled squares
t.reset()
t.begin_fill()
mysquare(50)
t.end_fill()
#Square filling functions
t.reset
def mysquare(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
mysquare(50,True)
mysquare(150,False)
#Drawing filled stars
t.reset
def mystar(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
t.color(0.9,0.75,0)
mystar(120,True)
t.color(0,0,0)
mystar(120,False)
