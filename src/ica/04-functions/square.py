import turtle

def turtle_square(sqTurt, side_len):
    """
    Commands the given turtle (sqTurt) to draw a square
    with sides of length (side_len).
    """
    for i in range(4):
        sqTurt.forward(side_len)
        sqTurt.left(90)

win = turtle.Screen()
tim = turtle.Turtle()

turtle_square(tim, 50)
turtle_square(tim, 100)
turtle_square(tim, 25)

win.exitonclick()