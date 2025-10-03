import turtle

def drawFiveCircles(turt, radius, centerX, centerY):
    """
    Tells a turtle to draw five filled circles in a star pattern.
    Inputs:
        turt: The turtle object to do the drawing.
        radius: The radius of each circle.
        centerX: The x-coordinate of the center of the pattern.
        centerY: The y-coordinate of the center of the pattern.
    """
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for _ in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

# (Keep the comment from Step 1)

win = turtle.Screen()
win.bgcolor("light sky blue")

# Setup the four turtles
sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

# --- Flower 1 (Center) ---
drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)

centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, 0)
stampTurtle.down()
stampTurtle.stamp()

# --- Flower 2 (Top) ---
drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, 220)
stampTurtle.down()
stampTurtle.stamp()

# --- Flower 3 (Right) ---
drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218, 0)
stampTurtle.down()
stampTurtle.stamp()

# --- Flower 4 (Bottom) ---
drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, -220)
stampTurtle.down()
stampTurtle.stamp()

# --- Flower 5 (Left) ---
drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222, 0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()