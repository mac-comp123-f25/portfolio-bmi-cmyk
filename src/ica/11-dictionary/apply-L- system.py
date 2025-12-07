def draw_fractal(a_turtle, l_system_string, angle, step):
    """
    Instructs a turtle to draw a fractal based on an L-system string.
    'F': Move forward by 'step'
    '+': Turn left by 'angle'
    '-': Turn right by 'angle'
    '[': Save the current state (position and heading)
    ']': Restore the last saved state
    """
    states = []

    for char in l_system_string:
        if char == 'F':
            a_turtle.forward(step)
        elif char == 'f':
            a_turtle.penup()
            a_turtle.forward(step)
            a_turtle.pendown()
        elif char == '+':
            a_turtle.left(angle)
        elif char == '-':
            a_turtle.right(angle)
        elif char == '[':
            position = a_turtle.position()
            heading = a_turtle.heading()
            states.append((position, heading))
        elif char == ']':
            if states:
                position, heading = states.pop()
                a_turtle.penup()
                a_turtle.setposition(position)
                a_turtle.setheading(heading)
                a_turtle.pendown()

def apply_l_system(l_system_info):
    """
    Applies the L-system rules for a given number of iterations.
    Accepts a single dictionary containing the axiom, rules, and n.
    """
    # Assertions to check the input dictionary
    assert isinstance(l_system_info, dict), "Input must be a dictionary."
    expected_keys = {'axiom', 'rules', 'n'}
    assert set(l_system_info.keys()) == expected_keys, "Dictionary must contain exactly 'axiom', 'rules', and 'n' keys."

    # Extract data from the dictionary
    axiom = l_system_info['axiom']
    rules = l_system_info['rules']
    iterations = l_system_info['n']

    result = axiom
    for _ in range(iterations):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result