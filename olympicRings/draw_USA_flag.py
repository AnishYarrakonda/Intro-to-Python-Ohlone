import turtle

#
# Python script to create USA flag using turtle.
# Author - [PythonCircle](https://www.pythoncircle.com)
#https://www.pythoncircle.com/post/661/python-script-11-drawing-flag-of-united-states-of-america-using-python-turtle/

# The function is refactored to take a turtle object and a starting position.
# All screen-related setup and the mainloop call are removed so it can be combined with other programs.

"""
Function name: draw_USA_Flag
Description: Creates a USA FLAG using turtle GUI

@param oogway: turtle object passed into function that does the drawing
@param flag_start_x: starting x coord for the top left corner of the flag
@param flag_start_y: starting y coord for the top left corner of the flag

@return NONE
"""
def draw_USA_flag(oogway, flag_start_x, flag_start_y):
    oogway.ht() # hide the turtle for clean drawing
    # flag height to width ratio is 1:1.9
    flag_height = 250
    flag_width = 475

    # starting points
    # The starting points are now parameters, which allows the flag to be drawn anywhere on the screen.
    start_x = flag_start_x
    start_y = flag_start_y

    # For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
    stripe_height = flag_height/13
    stripe_width = flag_width

    # length of one arm of star
    star_size = 10


    def draw_fill_rectangle(x, y, height, width, color):
        oogway.goto(x,y)
        oogway.pendown()
        oogway.color(color)
        oogway.begin_fill()
        oogway.forward(width)
        oogway.right(90)
        oogway.forward(height)
        oogway.right(90)
        oogway.forward(width)
        oogway.right(90)
        oogway.forward(height)
        oogway.right(90)
        oogway.end_fill()
        oogway.penup()

    def draw_star(x,y,color,length) :
        oogway.goto(x,y)
        oogway.setheading(0)
        oogway.pendown()
        oogway.begin_fill()
        oogway.color(color)
        for turn in range(0,5) :
            oogway.forward(length)
            oogway.right(144)
            oogway.forward(length)
            oogway.right(144)
        oogway.end_fill()
        oogway.penup()

    # this function is used to create 13 red and white stripes of flag
    def draw_stripes():
        x = start_x
        y = start_y
        # we need to draw total 13 stripes, 7 red and 6 white
        # so we first create, 6 red and 6 white stripes alternatively    
        for stripe in range(0,6):
            for color in ["red", "white"]:
                draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
                # decrease value of y by stripe_height
                y = y - stripe_height            

        # create last red stripe
        draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
        y = y - stripe_height

    # this function create navy color square
    # height = 7/13 of flag_height
    # width = 0.76 * flag_height
    # check references section for these values
    def draw_square():
        square_height = (7/13) * flag_height
        square_width = (0.76) * flag_height
        draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


    def draw_six_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        # We calculate the y position relative to the starting y
        y = flag_start_y - 13
        # create 5 rows of stars
        for row in range(0,5) :
            # We calculate the x position relative to the starting x
            x = flag_start_x + 15
            # create 6 stars in each row
            for star in range (0,6) :
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines

    def draw_five_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        # We calculate the y position relative to the starting y
        y = flag_start_y - 25
        # create 4 rows of stars
        for row in range(0,4) :
            # We calculate the x position relative to the starting x
            x = flag_start_x + 31
            # create 5 stars in each row
            for star in range (0,5) :
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines

    # draw 13 stripes
    draw_stripes()
    # draw squares to hold stars
    draw_square()
    # draw 30 stars, 6 * 5
    draw_six_stars_rows()
    # draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
    draw_five_stars_rows()

if __name__ == '__main__':
    # Create the screen and turtle for this test
    screen = turtle.Screen()
    screen.setup(800, 600)  # A standard screen size for testing
    screen.title("USA Flag Test")

    my_turtle = turtle.Turtle()
    
    # set the cursor/turtle speed. Higher value, faster is the turtle
    my_turtle.speed(1000)
    my_turtle.penup()
    # decide the shape of cursor/turtle
    my_turtle.shape("turtle")

    # The original starting points for the flag
    start_x = -237
    start_y = 125

    # Call the function with the turtle object and original coordinates
    draw_USA_flag(my_turtle, flag_start_x=start_x, flag_start_y=start_y)
    
    # Keep the window open until it is closed manually
    turtle.done()