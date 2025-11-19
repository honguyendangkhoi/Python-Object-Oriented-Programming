import random
import turtle

size=int(input("type a size: "))

timmy_the_turtle=turtle.Turtle()
turtle.colormode(255)

def colors():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    color=(r,b,g)
    return color

timmy_the_turtle.speed("fastest")
timmy_the_turtle.pensize(5)

def draw(size):
    for i in range(int(360/size)):
        timmy_the_turtle.color(colors())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size)
draw(size)

screen=turtle.Screen()
screen.mainloop()