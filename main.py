from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)


def random_color(tim_turtle):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return tim_turtle.color(r, g, b)


tim = Turtle()
my_screen = Screen()
gap = 5
for i in range(int(360 / gap)):
    tim.speed(0)
    random_color(tim)
    tim.circle(100)
    tim.right(gap)
my_screen.exitonclick()
