import turtle

size = int(input("Enter the size of the triangle: "))
color = input("Enter the colour of the triangle: ")

def draw_triangle(t, color, size):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

wn = turtle.Screen()
wn.bgcolor("light blue")
tri = turtle.Turtle()
draw_triangle(tri, color, size)
turtle.done()