import turtle

window = turtle.Screen()
turt = turtle.Turtle()
turt.color("green")

turt.begin_fill()

for _ in range(3):
    turt.forward(150)
    turt.left(120)

turt.end_fill()

window.exitonclick()