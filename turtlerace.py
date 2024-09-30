from turtle import Turtle, Screen
print("hello google")


tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
tam = Turtle(shape="turtle")
tum = Turtle(shape="turtle")
tim.color("red")
tom.color("blue")
tam.color("violet")
tum.color("yellow")
screen = Screen()
screen.setup(500,400)
a =screen.textinput('make your bet',"which turtle will win the race")
tim.penup()
tom.penup()
tam.penup()
tum.penup()
tim.goto(-230,-100)
tom.goto(-230,-70)
tam.goto(-230,-40)
tum.goto(-230,-10)


screen.exitonclick()
