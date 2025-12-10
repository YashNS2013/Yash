import turtle

t = turtle.Turtle()

t.color("blue")      
t.begin_fill()       

d = 500
f = 700

t.forward(d)
t.left(90)

t.forward(f)
t.left(90)

t.forward(d)
t.left(90)

t.forward(f)
t.left(90)

t.end_fill()         # 

turtle.done()