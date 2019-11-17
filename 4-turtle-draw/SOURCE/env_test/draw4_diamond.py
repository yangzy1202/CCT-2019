# draw4_diamond

from turtle import *
length = 100
angle = 360 / 8
for i in range(2):
    forward(length)
    left(angle)
    forward(length)
    left(180 - angle)
exitonclick()