from turtle import Turtle


MOVE_DISTANCE=20
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y) 
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.up()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



    def extend(self):
        #Add segment to the snake
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
            