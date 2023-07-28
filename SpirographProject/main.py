import turtle as t
from turtle import Screen
import random

random_turtle = t.Turtle()
t.colormode(255)
random_turtle.speed(12)
random_turtle.pensize(2)


def random_color():
    """Returns a random color for the pencolor."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def spirograph(turtle):
    """Creates a spirograph."""
    for steps in range(250):
        turtle.pencolor(random_color())
        turtle.tilt(steps)
        turtle.circle(100)
        turtle.tilt(steps)
        turtle.left(10)
    screen = Screen()
    screen.exitonclick()


spirograph(random_turtle)


