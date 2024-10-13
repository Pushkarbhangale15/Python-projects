from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.color("white")
        self.shapesize(5,1)
        self.up()
        self.goto(position)
    def go_up(self):
        new_y_cor=self.ycor()+20
        self.goto(self.xcor(),new_y_cor)
    def go_down(self):
        new_y_cor=self.ycor()-20
        self.goto(self.xcor(),new_y_cor)