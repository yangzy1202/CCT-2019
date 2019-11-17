# l-system_test2

from turtle import * 

length = 10
angle  = 90

def split_path(path):
    i = 0
    list = []
    while i < len(path):
        if path[i] == 'F':
            list.append(path[i:i+2])
            i += 2
        else:
            list.append(path[i])
            i += 1
    return list

def apply_rule(path, rules):
    list = split_path(path)
    for i in range(len(list)):
        symbol = list[i]
        if symbol in rules:
            list[i] = rules[symbol]
    path = ''.join(list) 
    return path  

def draw_path(path):
    list = split_path(path)
    for symbol in list:
        if symbol in ['Fl','Fr']:
            forward(length)
        elif symbol == '-':
            right(angle)
        elif symbol == '+':
            left(angle)
    
rules = {
    'Fl': 'Fl+Fr+',
    'Fr': '-Fl-Fr'
}

path = 'Fl'

for i in range(10):
    path = apply_rule(path, rules)

setup(800,600)
speed(0)
draw_path(path)
hideturtle()
done()