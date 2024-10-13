import turtle

import pandas as pd
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(f"{len(guessed_states)}/50 states guessed correctly","What's another states name?").title()
    if answer_state =="Exit":
        missing_state=[state for state in all_states if state not in guessed_states]
        # missing_state=[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data=pd.DataFrame((missing_state))
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim=turtle.Turtle()
        tim.up()
        tim.hideturtle()
        state_data=data[data.state==answer_state]
        tim.goto(int(state_data.x),int(state_data.y))
        tim.write(answer_state)






