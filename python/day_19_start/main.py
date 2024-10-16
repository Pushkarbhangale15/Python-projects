import random
import turtle
screen=turtle.Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="Make Your bet",prompt="Which turtle will win the race? Choose a color:",)
print(user_bet)
colors=["red","yellow","green","blue","purple","orange"]
all_turtles=[]
y_positions=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle=turtle.Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:

                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
         

screen.exitonclick()









