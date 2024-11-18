import colorgram
import turtle
import random

rgb_colours = []
colours = colorgram.extract("Day_18_Turtle _Art/200430102527-01-damien-hirst-severed-spots.jpg", 30)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb = (r, g, b)
    rgb_colours.append(rgb)

colour_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")

# set starting point
tim.penup()
tim.setpos(-355, -300)

for i in range(13):
    for j in range(15):
        colour = random.choice(colour_list)
        tim.dot(20, (colour))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(750)
    tim.left(180)

screen = turtle.Screen()
screen.exitonclick()