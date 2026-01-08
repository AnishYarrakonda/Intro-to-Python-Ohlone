#https://docs.python.org/2/library/turtle.html

"""
Function name: make_rings
Description: Creates a Olympic Rings using turtle GUI

@param NONE
@return NONE
"""
def make_rings():
    import turtle

    # Named constants
    RADIUS = 70
    STARTING_POINT_X = -200
    STARTING_POINT_Y = -300
    HSHIFT = 100
    VSHIFT = 70


    x = STARTING_POINT_X
    y = STARTING_POINT_Y

    colors = ["blue", "yellow", "black", "green", "red"]
    turtle.hideturtle()
    turtle.pensize(10)
    current_color = 0
    top_row = [0, 2, 4]

    for color in colors:
        turtle.pencolor(color)
        turtle.penup() # when penup is set, drawing is disabled when move the cursor
        turtle.goto(x, y) # move the cursor to (x, y)
        turtle.pendown() #when pendown is setup, drawing is enabled
        turtle.circle(RADIUS) # draw a circle
        
        x += HSHIFT
        if current_color in top_row:
            y -= VSHIFT
        else:
            y += VSHIFT
        
        current_color+=1

if __name__ == '__main__':
    make_rings()