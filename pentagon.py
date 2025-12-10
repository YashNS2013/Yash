from turtle import Turtle, Screen

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

t = Turtle()
draw_pentagon(t, 400)

Screen().mainloop()