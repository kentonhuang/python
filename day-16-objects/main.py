# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.forward(500)
# timmy.backward(500)
#
# my_screen = Screen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",])
table.add_column("Type", ["Electric", "Water", "Fire",])
table.align = "r"
print(table)
