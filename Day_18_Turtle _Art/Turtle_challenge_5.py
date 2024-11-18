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
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(157)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()