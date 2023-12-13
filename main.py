from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race ? Enter a color: ")
game_on = True
colors = ["red","orange","yellow","green","blue","purple"]

#Initialize turles
turtle_list = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=(-120+(50*i)))
    turtle_list.append(new_turtle)

#Move turtles
while game_on:
    for turtle in turtle_list:
        step_distance = random.randint(0,10)
        turtle.forward(step_distance)
        if(turtle.xcor() > 220):
            screen.clear()
            turtle.home()
            if(turtle.color()[0] == user_bet):
                turtle.write("You won", True, align="center")
            else:
                turtle.write(f"You lose : the {turtle.color()[0]} turtle won the game", True, align="center")
            game_on = False
            break
screen.exitonclick()