from turtle import Turtle, Screen

def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

t = Turtle()
t.penup()
t.goto(-150, 0)
t.pendown()

colors = ['blue', 'green', 'red']

for i, color in enumerate(colors):
    draw_rectangle(t, 100, 40, color)
    t.penup()
    t.forward(100 + 10)  # Move to next rectangle position (width +