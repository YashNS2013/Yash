import turtle
import random
import time
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(width=1000, height=700)
screen.tracer(0)

bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.width(3)

def draw_grass():
    bg.penup()
    bg.goto(-500, -250)
    bg.pendown()
    bg.color("forest green")
    bg.begin_fill()
    for _ in range(2):
        bg.forward(1000)
        bg.right(90)
        bg.forward(250)
        bg.right(90)
    bg.end_fill()

def draw_house():
    bg.penup()
    bg.goto(-250, -120)
    bg.pendown()
    bg.color("orange")
    bg.begin_fill()
    for _ in range(2):
        bg.forward(250)
        bg.left(90)
        bg.forward(150)
        bg.left(90)
    bg.end_fill()
    # Roof
    bg.penup()
    bg.goto(-250, 30)
    bg.pendown()
    bg.color("brown")
    bg.begin_fill()
    bg.goto(-125, 180)
    bg.goto(0, 30)
    bg.goto(-250, 30)
    bg.end_fill()
    # Door
    bg.penup()
    bg.goto(-180, -120)
    bg.pendown()
    bg.color("red")
    bg.begin_fill()
    for _ in range(2):
        bg.forward(50)
        bg.left(90)
        bg.forward(80)
        bg.left(90)
    bg.end_fill()
    # Windows
    for wx, wy in [(-220, -40), (-70, -40)]:
        bg.penup()
        bg.goto(wx, wy)
        bg.pendown()
        bg.color("lightblue")
        bg.begin_fill()
        for _ in range(4):
            bg.forward(40)
            bg.left(90)
        bg.end_fill()

def draw_tree(x, y):
    bg.penup()
    bg.goto(x, y)
    bg.pendown()
    bg.color("saddlebrown")
    bg.begin_fill()
    for _ in range(2):
        bg.forward(20)
        bg.left(90)
        bg.forward(60)
        bg.left(90)
    bg.end_fill()
    bg.penup()
    bg.goto(x-30, y+60)
    bg.pendown()
    bg.color("forest green")
    bg.begin_fill()
    bg.circle(40)
    bg.end_fill()

def draw_cloud(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(6):
        t.circle(25)
        t.penup()
        t.forward(35)
        t.pendown()
    t.end_fill()

def draw_sun(t, x, y, smile=True, wink=False):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    # Sun rays
    for i in range(16):
        t.penup()
        t.goto(x, y+60)
        t.setheading(i * 22.5)
        t.pendown()
        t.forward(40)
    # Sun face
    if smile:
        # Eyes
        t.penup()
        t.goto(x-20, y+80)
        t.pendown()
        t.color("black")
        t.begin_fill()
        if wink:
            t.circle(7, 180)
        else:
            t.circle(7)
        t.end_fill()
        t.penup()
        t.goto(x+20, y+80)
        t.pendown()
        t.begin_fill()
        t.circle(7)
        t.end_fill()
        # Smile
        t.penup()
        t.goto(x-20, y+65)
        t.pendown()
        t.setheading(-60)
        t.width(4)
        t.circle(25, 120)
        t.width(1)

def draw_flower(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.width(3)
    t.setheading(-90)
    t.forward(30)
    t.width(1)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(6):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.left(60)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(7)
    t.end_fill()

def draw_ball_face(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    # Eyes
    t.penup()
    t.goto(x-15, y+50)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(x+15, y+50)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    # Smile
    t.penup()
    t.goto(x-15, y+35)
    t.pendown()
    t.setheading(-60)
    t.width(3)
    t.circle(20, 120)
    t.width(1)

def draw_rainbow(t, x, y):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for i, color in enumerate(colors):
        t.penup()
        t.goto(x, y-i*10)
        t.pendown()
        t.width(10)
        t.color(color)
        t.setheading(60)
        t.circle(150-i*10, 120)
    t.width(1)

def draw_pond(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("deepskyblue")
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    # Draw ripples
    for i in range(1, 5):
        t.penup()
        t.goto(x, y - i*10)
        t.pendown()
        t.color("lightblue")
        t.circle(80 + i*5, 120)

def animate_bird_wings(bird, frame):
    if frame % 20 < 10:
        bird.shapesize(stretch_wid=1, stretch_len=2)
    else:
        bird.shapesize(stretch_wid=2, stretch_len=2)

# Draw static background
draw_grass()
draw_house()
draw_tree(350, -120)
draw_tree(400, -100)
draw_tree(-400, -130)
draw_tree(-350, -110)

# Animated objects
sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)

cloud1 = turtle.Turtle()
cloud1.hideturtle()
cloud1.speed(0)
cloud2 = turtle.Turtle()
cloud2.hideturtle()
cloud2.speed(0)
cloud3 = turtle.Turtle()
cloud3.hideturtle()
cloud3.speed(0)

ball = turtle.Turtle()
ball.hideturtle()
ball.speed(0)

bird = turtle.Turtle()
bird.shape("triangle")
bird.color("black")
bird.penup()
bird.goto(-500, 150)
bird.setheading(60)
bird.speed(1)

pond = turtle.Turtle()
pond.hideturtle()
pond.speed(0)

flower_turtles = []
flower_positions = [(-300, -220), (-200, -230), (-100, -210), (0, -225), (100, -215), (200, -230), (300, -220)]
flower_colors = ["red", "magenta", "blue", "cyan", "green", "yellow", "purple"]
for i in range(len(flower_positions)):
    ft = turtle.Turtle()
    ft.hideturtle()
    ft.speed(0)
    flower_turtles.append(ft)

rainbow = turtle.Turtle()
rainbow.hideturtle()
rainbow.speed(0)

# Animation loop (~1 minute)
start_time = time.time()
cloud1_x, cloud1_y = -350, 250
cloud2_x, cloud2_y = 0, 300
cloud3_x, cloud3_y = 350, 220
sun_x, sun_y = 350, 200
ball_x, ball_y = -100, -160
ball_dy = 4
bird_x, bird_y = -500, 150
rainbow_visible = False
wink = False
frame = 0

while time.time() - start_time < 60:
    sun.clear()
    draw_sun(sun, sun_x, sun_y, smile=True, wink=wink)
    sun_x -= 0.3
    if int(time.time() - start_time) % 10 == 0:
        wink = not wink

    cloud1.clear()
    draw_cloud(cloud1, cloud1_x, cloud1_y)
    cloud1_x += 1
    if cloud1_x > 500:
        cloud1_x = -500

    cloud2.clear()
    draw_cloud(cloud2, cloud2_x, cloud2_y)
    cloud2_x += 0.7
    if cloud2_x > 500:
        cloud2_x = -500

    cloud3.clear()
    draw_cloud(cloud3, cloud3_x, cloud3_y)
    cloud3_x += 0.5
    if cloud3_x > 500:
        cloud3_x = -500

    ball.clear()
    draw_ball_face(ball, ball_x, ball_y)
    ball_y += ball_dy
    if ball_y > -80 or ball_y < -180:
        ball_dy *= -1

    bird.forward(7)
    bird.right(random.choice([-2, 2]))
    if bird.xcor() > 500:
        bird.goto(-500, 150)
    animate_bird_wings(bird, frame)
    frame += 1

    pond.clear()
    draw_pond(pond, 250, -180)

    # Animate flowers growing and swaying
    for i, ft in enumerate(flower_turtles):
        ft.clear()
        sway = math.sin(time.time()*2 + i) * 10
        grow = min(1, (time.time() - start_time)/10)
        draw_flower(ft, flower_positions[i][0]+sway, flower_positions[i][1]+grow*30, flower_colors[i])

    # Rainbow appears and fades every 15 seconds
    rainbow.clear()
    if int(time.time() - start_time) % 30 < 15:
        draw_rainbow(rainbow, -100, 0)

    screen.update()
    time.sleep(0.03)

# Hide turtles and keep window open
sun.hideturtle()
cloud1.hideturtle()
cloud2.hideturtle()
cloud3.hideturtle()
ball.hideturtle()
bird.hideturtle()
pond.hideturtle()
rainbow.hideturtle()
for ft in flower_turtles:
    ft.hideturtle()
turtle.done()


# Add near the top, after your imports
class Butterfly:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(x, y)
        self.t.color(color)
        self.angle = random.randint(0, 360)
        self.t.showturtle()
    def move(self):
        self.angle += random.randint(-30, 30)
        self.t.setheading(self.angle)
        self.t.forward(random.randint(5, 15))
        # Draw wings
        self.t.clear()
        self.t.dot(20, self.t.color()[0])
        self.t.dot(10, "black")

butterflies = [Butterfly(random.randint(-400,400), random.randint(-100,200), random.choice(["purple","orange","blue","pink"])) for _ in range(5)]

class Leaf:
    def __init__(self, x, y):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(x, y)
        self.t.color("darkgreen")
        self.t.showturtle()
        self.dy = random.uniform(-2, -0.5)
        self.dx = random.uniform(-1, 1)
    def fall(self):
        self.t.clear()
        self.t.goto(self.t.xcor() + self.dx, self.t.ycor() + self.dy)
        self.t.dot(10, "darkgreen")
        if self.t.ycor() < -250:
            self.t.goto(random.randint(-500,500), random.randint(100,300))

leaves = [Leaf(random.randint(-500,500), random.randint(100,300)) for _ in range(20)]

# Add this in your animation loop:
for b in butterflies:
    b.move()
for leaf in leaves:
    leaf.fall()


def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

stars = []
for _ in range(30):
    st = turtle.Turtle()
    st.hideturtle()
    st.speed(0)
    stars.append(st)

# In your animation loop, after sunset (e.g., after 30 seconds):
if time.time() - start_time > 30:
    for st in stars:
        st.clear()
        x = random.randint(-500, 500)
        y = random.randint(100, 300)
        draw_star(st, x, y, random.randint(5, 15), "white")    

