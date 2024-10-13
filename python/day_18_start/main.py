import turtle
import random
tim=turtle.Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
tim.speed(0)

tim.shape("turtle")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(10)
# def drawshape(num_of_sides):
#         angle=360/num_of_sides
#         for _ in range(num_of_sides):
#             tim.forward(100)
#             tim.right(angle)

# for _ in range(3,11):
#     tim.color(random.choice(colours))
#     drawshape(_)

screen=turtle.Screen()
screen.exitonclick()