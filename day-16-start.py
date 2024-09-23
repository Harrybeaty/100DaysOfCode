# import another_module
#
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.fillcolor("DarkSeaGreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# create a table of pokemon and their types.
# It's hard to format a table like this so let's use a package that someone has made to do it for us.

from prettytable import PrettyTable

pokemon_table = PrettyTable()
pokemon_table.field_names = ["Pokemon name", "Type"]
pokemon_table.add_rows(
    [
        ["Charmander", "Fire"],
        ["Charmealeon", "Fire"],
        ["Charizard", "Fire, Flying"],
    ]
)
pokemon_table.align = "l"
print(pokemon_table)