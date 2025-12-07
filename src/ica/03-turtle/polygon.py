import turtle

window = turtle.Screen()
turt = turtle.Turtle()
turt.color("purple")

n = 6

angle = 360 / n

turt.begin_fill()

for _ in range(n):
    turt.forward(100)
    turt.left(angle)

turt.end_fill()

window.exitonclick()