import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(6)
tim.speed("fastest")
t.colormode(255)
angle_list = (0, 90, 180, 270)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

for i in range(600):
    tim.color(random_colour())
    angle = random.choice(angle_list)
    tim.right(angle)
    tim.forward(30)

screen = t.Screen()
screen.exitonclick()