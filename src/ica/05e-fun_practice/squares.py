import turtle
def draw_nested_squares(t):
    for side_length in range(10, 81, 10):

        for i in range(4):
            # Turtle commands:
            t.forward(side_length)
            t.left(90)


win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()