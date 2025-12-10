from turtle import Turtle, Screen

t = Turtle()

# Ask user for radii
radius1 =200 
radius2 =200


# Draw first circle
t.penup()
t.goto(-radius1 - 20, 0)  # Move to left for first circle
t.pendown()
t.circle(radius1)

# Draw second circle
t.penup()
t.goto(radius2 + 20, 0)   # Move to right for second circle
t.pendown()

Turtle.done()