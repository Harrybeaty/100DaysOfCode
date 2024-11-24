from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
name = ["Tim", "Tom", "Toby", "Tray", "Turbo", "Tyrone", "Trevor"]
y_pos = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

for _ in range(7):
    name[_] = Turtle(shape="turtle")
    name[_].color(colours[_])
    name[_].penup()
    name[_].goto(x=-230, y=y_pos[_])
    all_turtles.append(name[_])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()