import turtle

r=int(input("Enter the radius of the circle: "))

u=input("Enter the colour of the circle: ")



def draw_circle(kurma,colour,radius ):
    kurma.color("black")
    # Set the fill color to blue
    kurma.fillcolor(colour)
    # Begin the fill
    kurma.begin_fill()
    # Draw a circle with a radius of 100
    kurma.circle(radius)
    # End the fill
    kurma.end_fill()


wn = turtle.Screen()
wn.bgcolor("light blue")
t =turtle.Turtle()
draw_circle(t,u,r)
turtle.done()