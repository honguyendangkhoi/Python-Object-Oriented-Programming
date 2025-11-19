import turtle, time, random, config
from turtle import Turtle, Screen
from Snake import snake
from food import food
from score_board import Score_board
from config import level

screen = Screen()

lv=level()
lv.choice()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on =True

snake = snake()
food = food()
scoreboard=Score_board()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

while game_on:
    screen.update()
    time.sleep(config.SPEED)
    snake.move()

    if snake.head.distance(food)<20:
        food.refresh()
        snake.new_tail()
        config.MOVE_DIS+=0.1
        config.SPEED*=0.9
        scoreboard.increase()

    if snake.head.xcor() > 299 or snake.head.xcor() <-299 or snake.head.ycor()>299 or snake.head.ycor()<-299:
        game_on = False
        scoreboard.over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False
            scoreboard.over()

screen.exitonclick()