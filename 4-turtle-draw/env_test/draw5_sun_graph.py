# draw5_sun_graph

from turtle import *
from math import *

length = 100
angle = 360 / 8

# 函数：画菱形
def draw_diamond():
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180 - angle)

speed(0) 
# turtle中的speed()函数可设置海龟移动的速度为 0..10 表示的整型数值。如未指定参数则返回当前速度。
# 如果输入数值大于 10 或小于 0.5 则速度设为 0。速度字符串与速度值的对应关系如下:
    # "fastest": 0 最快
    # "fast": 10 快
    # "normal": 6 正常
    # "slow": 3 慢
    # "slowest": 1 最慢

# 画八个相邻的菱形
for i in range(8):
    if i % 2 == 0:
        color('red')
    else: 
        color('blue')
    begin_fill()
    draw_diamond()
    end_fill()
    left(angle)

# 画正八边形
forward(length)
angle_base = (180 - angle) / 2
left(180 - angle_base)

alpha = angle * pi/180 # Python中的三角函数需要以弧度为参数，需要先转换角度为弧度
step = 2 * length * sin(alpha / 2) # 八边形边长

color('yellow')
begin_fill()
for i in range(8):
    forward(step)
    left(angle)
end_fill()
hideturtle()
done()