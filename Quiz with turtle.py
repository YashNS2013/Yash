import turtle

t=turtle.Turtle()
import time
t.speed(2000)
screen = turtle.Screen()
t.hideturtle()
screen.bgcolor("lightblue")

t.color("blue")

t.write("welcome to the quiz of Ramayana ! ", align='center', font=('Arial', 16, 'normal'))


time.sleep(2)
t.clear()

t.color("red")

t.write("Let's start the quiz ! ", align='center', font=('Arial', 16, 'normal'))    
time.sleep(2)
t.clear()

t.color("black")

t.penup()
t.goto(100, -50)
t.pendown()
t.write(" 1. how was the aothor  of Ramayana ?", align="right", font=("Arial", 16, "normal"))

w=turtle.textinput("Question 1", "a) Valmiki ,b) Tulsidas ,c) Ved Vyas, Enter your answer (a/b/c): ")
time.sleep(3)
t.clear()


p=0


if w=='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("green")
    t.write("Correct answer ! ", align="right", font=("Arial", 16, "normal"))
    p=p+1
time.sleep(2)
t.clear()    

if w!='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("red")
    t.write("Incorrect answer ! The correct answer is a) Valmiki ", align="right", font=("Arial", 16, "normal"))
time.sleep(3)

t.clear()
t.color("black")
t.penup()
t.goto(100, -50)
t.pendown()
t.write(" 2. Who is the wife of Lord Rama ?", align="right", font=("Arial", 16, "normal"))
w=turtle.textinput("Question 2", "a) Sita ,b) Radha ,c) Ganga, Enter your answer (a/b/c): ")
time.sleep(3)
t.clear()
if w=='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("green")
    t.write("Correct answer ! ", align="right", font=("Arial", 16, "normal"))
    p=p+1
time.sleep(2)
t.clear()
if w!='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("red")
    t.write("Incorrect answer ! The correct answer is a) Sita ", align="right", font=("Arial", 16, "normal"))
time.sleep(3)
t.clear()
t.color("black")
t.penup()
t.goto(100, -50)
t.pendown()
t.write(" 3. Who is the Mother of Lord Rama ?", align="right", font=("Arial", 16, "normal"))
w=turtle.textinput("Question 3", "a) Kaikeyi ,b) Kausalya ,c) Sumitra, Enter your answer (a/b/c): ")
time.sleep(3)
t.clear()
if w=='b':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("green")
    t.write("Correct answer ! ", align="right", font=("Arial", 16, "normal"))
    p=p+1
time.sleep(2)
t.clear()
if w!='b':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("red")
    t.write("Incorrect answer ! The correct answer is b) Kausalya ", align="right", font=("Arial", 16, "normal"))
time.sleep(3)
t.clear()
t.color("black")
t.penup()
t.goto(100, -50)
t.pendown()
t.write(" 4. Who is the brother of Lord Rama went to vana vasa with him ?", align="right", font=("Arial", 16, "normal"))
w=turtle.textinput("Question 4", "a) Lakshman ,b) Bharat ,c) Shatrughan, Enter your answer (a/b/c): ")
time.sleep(3)
t.clear()
if w=='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("green")
    t.write("Correct answer ! ", align="right", font=("Arial", 16, "normal"))
    p=p+1
time.sleep(2)
t.clear()
if w!='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("red")
    t.write("Incorrect answer ! The corre is a) Lakshman ", align="right", font=("Arial", 16, "normal"))
time.sleep(3)
t.clear()
t.color("black")
t.penup()
t.goto(100, -50)
t.pendown()
t.write(" 5. Who is the King of Lanka ?", align="right", font=("Arial", 16, "normal"))
w=turtle.textinput("Question 5", "a) Ravana ,b) Vibhishan ,c) Kumbhakarna, Enter your answer (a/b/c): ")
time.sleep(3)
t.clear()
if w=='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("green")
    t.write("Correct answer ! ", align="right", font=("Arial", 16, "normal"))
    p=p+1
time.sleep(2)
t.clear()
if w!='a':
    t.penup()
    t.goto(100, -80)
    t.pendown()
    t.color("red")
    t.write("Incorrect answer ! The correct answer is a) Ravana ", align="right", font=("Arial", 16, "normal"))
time.sleep(3)
t.clear()

t.color("black")
t.screen.bgcolor("lightgreen")
t.write("you got points in quiz:", align='center', font=('Arial', 16, 'normal'))
time.sleep(2)
t.clear()
t.write(p, align='right', font=('Arial', 16, 'normal'))
time.sleep(5)
t.clear()


t.write("thank you ! ", align='center', font=('Arial', 16, 'normal'))








turtle.done()



