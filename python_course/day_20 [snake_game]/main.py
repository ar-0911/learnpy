from turtle import Screen
from snake import Snake
from food import Food
from scroreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The snake game")
screen.tracer(0)  # 0 is off

snake = Snake()
food = Food()
score = Score()
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)

    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='Down', fun=snake.down)
    screen.onkey(key='Left', fun=snake.left)
    screen.onkey(key='Right', fun=snake.right)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    # detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
