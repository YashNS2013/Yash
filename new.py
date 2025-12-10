import turtle

def setwindowsize(x=160, y=160):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)

def drawpixel(x, y, color, pixelsize=10):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize, y*pixelsize)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def showimage():
    turtle.hideturtle()
    turtle.update()

# Mario pixel art (16x16 grid)
mario = [
    "................",
    "................",
    ".....RRRR.......",
    "....RYYYYR......",
    "...RYYYYYYR.....",
    "...RYYBYYR......",
    "..RRRRRRRRR.....",
    "..RRRRRRRRR.....",
    "..RBBBBBBR......",
    "..RBBBBBBR......",
    ".RRRRRRRRRR.....",
    ".RBBBBBBBBR.....",
    "RRRR....RRRR....",
    "RBBR....RBBR....",
    "RBBR....RBBR....",
    "RRRR....RRRR...."
]

colors = {
    ".": (0,0,0),        # background (black)
    "R": (200,0,0),      # red (hat, shirt)
    "Y": (255,220,150),  # skin (face, hands)
    "B": (0,0,200)       # blue (pants)
}

setwindowsize(160, 160)

for y, row in enumerate(mario):
    for x, pixel in enumerate(row):
        if pixel != ".":
            drawpixel(x, 15-y, colors[pixel])

showimage()
turtle.done()