import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

text = turtle.Turtle()
text.penup()
text.hideturtle()


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

print(answer_state)







turtle.mainloop()