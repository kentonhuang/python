from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-60 + (30 * turtle_index))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won, The {winner} turtle is the winner!")
            else:
                print(f"You lose. The {winner} turtle has won.")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(30)
#
# def turn_right():
#     tim.right(30)
#
# def clear_screen():
#     tim.clear()
#
# screen.listen()
# screen.onkey(key="Up", fun=move_forwards)
# screen.onkey(key="Down", fun=move_backwards)
# screen.onkey(key="Left", fun=turn_left)
# screen.onkey(key="Right", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()
