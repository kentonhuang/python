import turtle
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


colors = ["blue", "light sea green", "hot pink", "orange", "lawn green", "dark gray", "dark violet", "tomato", "sienna", "medium slate blue", "dodger blue"]
turn_angles = [90, 180, 270, 360]
tim.speed("fastest")

# for _ in range(60):
#     angle = random.choice(turn_angles)
#     tim.color(random_color())
#     tim.setheading(angle)
#     tim.forward(20)

def spirograph(size_of_gap):
    angle = 360 / size_of_gap
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)


spirograph(2)

screen = t.Screen()
screen.exitonclick()
