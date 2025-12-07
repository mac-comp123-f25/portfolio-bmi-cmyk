def draw_fractal(a_turtle, l_system_string, angle, step):
    """
    Instructs a turtle to draw a fractal based on an L-system string.
    'F': Move forward by 'step'
    '+': Turn left by 'angle'
    '-': Turn right by 'angle'
    '[': Save the current state (position and heading)
    ']': Restore the last saved state
    """
    # This list will act as a stack to save turtle states
    states = []

    for char in l_system_string:
        if char == 'F':
            a_turtle.forward(step)
        elif char == 'f': # Also support 'f' for moving without drawing
            a_turtle.penup()
            a_turtle.forward(step)
            a_turtle.pendown()
        elif char == '+':
            a_turtle.left(angle)
        elif char == '-':
            a_turtle.right(angle)
        elif char == '[':
            # Save current position and heading
            position = a_turtle.position()
            heading = a_turtle.heading()
            states.append((position, heading))
        elif char == ']':
            # Restore the most recent position and heading
            if states:
                position, heading = states.pop()
                a_turtle.penup()
                a_turtle.setposition(position)
                a_turtle.setheading(heading)
                a_turtle.pendown()

def apply_rules(axiom, rules, iterations):
    """
    Applies the L-system rules for a given number of iterations.
    """
    result = axiom
    for _ in range(iterations):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result