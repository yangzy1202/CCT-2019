# lsystem_test1

from turtle import * 

length = 10
angle  = 90

def draw_path(path):
    for symbol in path:
        if symbol == 'F':
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)

def apply_rule(path):
    rule = 'F-F+F+FF-F-F+F'
    return path.replace('F', rule)

speed(0)

path = 'F-F-F-F'

for i in range(2):
    path = apply_rule(path)

draw_path(path)
hideturtle()
done()