import turtle 

t=turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("white")
t.left(90)
t.speed(1000)
def tree(i):
	if i<10:
		return
	else:
		t.forward(i)
		t.left(30)
		tree(3*i/4)
		t.right(60)
		tree(3*i/4)
		t.left(30)
		t.backward(i)
		
tree(100)
turtle.done()
