###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

t.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
rgb_list = []
for color in rgb_colors:
    r = color.r
    g = color.g
    b = color.b
    rgb_list.append((r, g, b))

print(rgb_list)

tim = t.Turtle()
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(500)
tim.setheading(0)
tim.hideturtle()

for _ in range(10):

    for _ in range(10):
        tim.dot(30, random.choice(rgb_list))
        tim.forward(80)

    tim.left(90)
    tim.forward(80)
    tim.right(90)
    tim.backward(800)

screen = t.Screen()
screen.exitonclick()
