from print_me_first import print_me_first
from draw_USA_flag import draw_USA_flag
from ring_sample import make_rings
import turtle
import time

my_screen = turtle.Screen()
my_turtle = turtle.Turtle()

if __name__ == '__main__':
    # Get the "print me first" text and print it to the console
    lab_text = print_me_first(
        lab_info="CNET-142 Lab 7 Olympic Rings - Anish Yarrakonda",
        program_name="olympic.py")

    # Set up the screen to fit the image and drawings
    my_screen.setup(1000, 700)
    my_screen.title("Combined Turtle Graphics")
    
    # Set the background image to the direct path of usa.png
    my_screen.bgpic("/Users/anish/Documents/Python Coding Practice/Intro_to_Python_Course_@Ohlone/olympicRings/usa.png")

    # Set up the turtle for drawing
    my_turtle.speed(0) # Speed up the drawing process
    my_turtle.penup()
    
    # Place the "print me first" text at the top-left, as shown in your image
    my_turtle.goto(400, -500)
    my_turtle.pencolor("blue")
    my_turtle.write(lab_text, font=('Arial', 12, 'normal'), align='right')

    # USA OLYMPICS TEAM text at the top of the screen
    my_turtle.goto(0, 300)
    my_turtle.write("USA", font=('Arial', 64, 'bold'), align='center')
    my_turtle.goto(0, 230)
    my_turtle.write("OLYMPICS TEAM", font=('Arial', 64, 'bold'), align='center')

    
    # Draw the USA flag (placed on the right side)
    flag_start_x = -237
    flag_start_y = 125
    my_turtle.penup()
    draw_USA_flag(my_turtle, flag_start_x, flag_start_y)

    # Draw the Olympic rings (placed on the left side)
    rings_start_x = -400
    rings_start_y = 0
    my_turtle.penup()
    make_rings()
    
    # Hide the turtle and keep the window open for viewing
    my_turtle.hideturtle()
    time.sleep(2)
    turtle.done()