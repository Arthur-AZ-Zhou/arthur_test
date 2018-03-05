#Making a clickable button
def hello():
    print("Hello there!")
from tkinter import *
tk = Tk()
btn = Button(tk,text="click me", command = hello)
btn.pack()
#Using named parameters
def person(width,height):
    print('I am %s feet wide and I am %s feet high' %(width,height))
person(3,6)
#Canvas for Drawing
from tkinter import *
tk = Tk()
canvas = Canvas(tk,width = 500,height = 500)
canvas.pack()
#Drawing Lines
from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=500,height = 500)
canvas.pack()
canvas.create_line(0,0,500,500)
#Drawing boxes
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.create_rectangle(10,10,50,50)
canvas.create_rectangle(10,10,300,50)
canvas.create_rectangle(10,10,50,300)
canvas.pack()
#Lots of rectangles
from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width = 400,height=400)
canvas.pack()
def random_rectangle(width,height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)
for x in range(1,100):
    random_rectangle(400,400)
