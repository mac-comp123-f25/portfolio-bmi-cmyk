import turtle
window = turtle.Screen()
window.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):

    t.pencolor(colors[i % 6])

    t.circle(100)

    t.right(10)

t.hideturtle()

window.exitonclick()