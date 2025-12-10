import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

# Create the turtle
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.pensize(2)

# Define colors for the spirograph
colors = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

# Draw the spirograph
for i in range(36): # Number of circles to draw
    t.color(colors[i % len(colors)]) # Cycle through colors
    t.circle(100) # Draw a circle with radius 100
    t.left(10) # Turn left by 10 degrees after each circle

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()