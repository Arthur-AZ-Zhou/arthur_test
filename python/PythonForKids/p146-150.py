#Square loop
import turtle
t= turtle.Pen()
for x in range(1,5):
    t.forward(50)
    t.left(90)
#Stars
import turtle
t = turtle.Pen()
for x in range(1,9):
    t.forward(100)
    t.left(225)
#Sharp Star
import turtle
for x in range(1,38):
    t.forward(100)
    t.left(175)
#Strange Star
import turtle
for x in range(1,20):
    t.forward(100)
    t.left(95)
#Equation Star
t.reset()
for x in range(1,19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
    
