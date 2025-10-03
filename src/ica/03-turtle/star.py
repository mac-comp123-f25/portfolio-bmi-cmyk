import turtle

window = turtle.Screen()

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("gold")

turtle1.forward(100)
turtle1.right(144)
turtle1.forward(100)
turtle1.right(144)
turtle1.forward(100)
turtle1.right(144)
turtle1.forward(100)
turtle1.right(144)
turtle1.forward(100)
turtle1.right(144)

turtle2 = turtle.Turtle()
turtle2.shape("classic")
turtle2.color("red")

turtle2.penup()
turtle2.goto(-150, 0)
turtle2.pendown()

turtle2.forward(100)
turtle2.right(144)
turtle2.forward(100)
turtle2.right(144)
turtle2.forward(100)
turtle2.right(144)
turtle2.forward(100)
turtle2.right(144)
turtle2.forward(100)
turtle2.right(144)

window.exitonclick()