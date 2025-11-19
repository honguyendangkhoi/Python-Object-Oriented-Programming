from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.write(f"Your score:{self.score}",move=False,align="center",font=("arial",16,"normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Your score:{self.score}",move=False,align="center",font=("arial",16,"normal"))

    def over(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write("Game Over",move=False,align="center",font=("arial",16,"normal"))
        self.goto(x=0,y=270)
        self.write(f"Your score: {self.score}",move=False,align="center",font=("arial",16,"normal"))