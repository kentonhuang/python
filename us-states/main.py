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


data = pandas.read_csv("50_states.csv")

game_is_on = True

states_set = set()
all_states = data.state.to_list()

while len(states_set) < 50:

    answer_state = screen.textinput(title=f"{len(states_set)} / 50 States Correct", prompt="What's another state's name?").capitalize()


    if answer_state == "Exit":
        # missing_states = []
        missing_states = [state for state in all_states if state not in states_set]
        # for state in all_states:
        #     if state not in states_set:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    data_state = data[data["state"] == answer_state]

    if len(data_state) > 0 and answer_state not in states_set:
        text.goto(int(data_state['x']), int(data_state['y']))
        text.write(answer_state)
        states_set.add(answer_state)

#states_to_learn.csv
