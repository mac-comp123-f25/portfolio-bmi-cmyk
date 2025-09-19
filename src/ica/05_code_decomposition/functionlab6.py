import turtle

def drawFiveCircles(turt, radius, centerX, centerY):
    # (Same function as Step 3)
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for _ in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt, centerX, centerY):
    # (Same function as Step 4)
    turt.up()
    turt.goto(centerX, centerY - 15)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

def drawBee(turt, centerX, centerY):
    # (Same function as Step 5)
    turt.up()
    turt.goto(centerX - 2, centerY)
    turt.down()
    turt.stamp()

def drawFlower(sepal_t, petal_t, center_t, stamp_t, centerX, centerY):
    """
    Draws one complete flower, including sepals, petals, center, and bee.
    Inputs:
        sepal_t: The turtle for the sepals.
        petal_t: The turtle for the petals.
        center_t: The turtle for the center circle.
        stamp_t: The turtle for the bee stamp.
        centerX: The x-coordinate of the flower's center.
        centerY: The y-coordinate of the flower's center.
    """
    drawFiveCircles(sepal_t, 50, centerX, centerY)
    drawFiveCircles(petal_t, 25, centerX, centerY)
    drawCenterCircle(center_t, centerX, centerY)
    drawBee(stamp_t, centerX, centerY)

# (Keep the comment from Step 1)

win = turtle.Screen()
win.bgcolor("light sky blue")

# Setup the four turtles (same as before)
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

# Draw all five flowers with one call per flower
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

win.exitonclick()