import turtle,time,random
from turtle import Turtle,Screen
import config

screen=Screen()

STARTING_POS = [(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self, position=None):
        if position is not None: #nếu đuôi chạm thức ăn thì thêm đuôi mới
            new_seg=Turtle("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(position)
            self.segments.append(new_seg)

        else:
            for i,pos in enumerate(STARTING_POS): #nếu không thì cứ lặp qua những tọa độ cũ hiện tại
                new_seg=Turtle("square")
                new_seg.penup()
                new_seg.color("white")
                new_seg.goto(pos)
                if i==0:
                    new_seg.shape("arrow")
                self.segments.append(new_seg)

    def new_tail(self): #hàm đuôi mới
        self.tail=self.segments[-1]
        self.create_snake(self.tail.position())

    def move(self):
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(self.segments)-1,0,-1): #start= độ dài của segments mà list thì bắt đầu từ 1 nên phải -1, stop=0, step=-1 
            new_x=self.segments[seg_num-1].xcor() #đuôi đi theo đầu
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(config.MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)