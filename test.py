from turtle import *


color('red', 'yellow')
begin_fill()
while True:

    forward(200)
    left(170)
    speed(10)
    bgcolor('black')
    if abs(pos()) < 1:
        break
end_fill()
done()
