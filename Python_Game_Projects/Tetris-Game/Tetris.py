import turtle, time, random
from turtle import Screen, Turtle #turtle nhỏ là hàm bự của Turtle hoa

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Tetris mini")
screen.tracer(0)

ava_colors=["red","green","white","purple","blue","yellow"]
cl=ava_colors
segments=[]

class block:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def square(self,x,y):
        rand=random.choice(ava_colors)

        segment_1=Turtle("square")
        segment_1.penup()
        segment_1.color(rand) #hàm thì phải gán bằng () chứ ko dùng dấu = được
        segment_1.goto(x,y)
        segments.append(segment_1)
        
        segment_2=segment_1.clone()
        segment_2.goto(x-20, y)
        segments.append(segment_2)

        segment_3=segment_1.clone()
        segment_3.goto(x-20, y-10)
        segments.append(segment_3)
 
        segment_4=segment_1.clone()
        segment_4.goto(x, y-10)
        segments.append(segment_4)

        ava_colors.pop(0)

class movement(block):
    def fall(self):
        bottom_y=-10
        step_size=20
        over=False
        
        if not over:
            for seg in segments:
                x=seg.xcor()
                y=seg.ycor()-step_size
                seg.goto(x,y)
            screen.update()
            screen.ontimer(self.fall,200)
            
        if y<=bottom_y:
            over=True
        
#truyền 0,0 vì x,y bắt đầu là 0,0

fall=movement()
fall.square(0,0)
fall.fall()

screen.exitonclick()