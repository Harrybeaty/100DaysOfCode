import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(1)
tim.speed("fastest")
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

for i in range(90):
    angle =+ 4
    tim.color(random_colour())
    tim.circle(160)
    tim.right(angle)

screen = t.Screen()
screen.exitonclick()