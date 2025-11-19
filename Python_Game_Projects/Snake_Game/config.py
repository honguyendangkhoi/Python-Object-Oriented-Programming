from turtle import Turtle,Screen

screen=Screen()
            
MOVE_DIS=20
SPEED=0.1

class level(Turtle):
    def __init__(self):
        super().__init__()
        pass
    def choice(self):
        level=screen.textinput(None,"Choose Level (Easy/Hard): ")
        if level.lower()=='easy':
            pass
        elif level.lower()=='hard':
            global SPEED
            SPEED=0.0001