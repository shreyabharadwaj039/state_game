import turtle
import pandas

screen=turtle.Screen()
screen.title("Indian State/Uniostate_gamen teritory Game")
image="state_game\pic.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("state_game\India States-UTs.csv")
all_states=data.State.to_list()
guess=[]
while len(guess)<32:
  answer=screen.textinput(title=f"{len(guess)}/32" ,prompt="States/Capital's Name: ").title()
  if answer=="Exit":
    missing=[]
    for state in all_states:
      if state not in guess:
        missing.append(state)
    print(missing)
    break
  if answer in all_states:
    guess.append(answer)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data.State==answer]
    t.goto(state_data.x.item(),state_data.y.item())
    t.write(answer)
   
screen.exitonclick()