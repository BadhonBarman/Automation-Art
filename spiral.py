'''
from turtle import *

#import turtle 
color('red', 'yellow')
setup(500,500)

tl = Turtle()

tl.hideturtle()

for i in range(250):
	tl.forward(i)
	tl.right(50)
	tl.speed(0)

done()
'''

import turtle

colors = ['red','yellow','green','purple','blue','orange']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(300):
	t.pencolor(colors[x%6])
	t.width(x/100+1)
	t.forward(x)
	t.left(91)
	t.speed(10000000000)

turtle.done()


#4.43 😔