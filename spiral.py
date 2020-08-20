from turtle import *
import turtle

colors = ['red','yellow','green','purple','blue','orange']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(300):
	t.pencolor(colors[x%5])
	t.width(x/100)
	t.forward(x)
	t.left(61)
	t.speed(10000000000)

turtle.done()

