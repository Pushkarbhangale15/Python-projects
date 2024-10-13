# import colorgram
# colors=colorgram.extract("hirst.jpg",20)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)
from turtle import Turtle,Screen,colormode
import random
colormode(255)
color_list=[(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42)]
tim=Turtle()
tim.up()
tim.hideturtle()
tim.speed(0)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)
screen=Screen()
screen.exitonclick()