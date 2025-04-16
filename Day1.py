import sys

print("namste")
print("my name taiking computer I like to talk with you .")
x=input("enter your name: ")
print("ok your name is")
print(x)
prompt="""
Which cartoon do you like ?
1. Chota Bheem
2. Lost in OZ
"""
y=input(prompt)
a="chotabheem"
s="lost,inn,oz"

print(y)
print(type(y))
y = int(y)
print(y)
print(type(y))

if y == 1:
    print("ok So you like Choota Bheem. Nice!")
elif y == 2:
    print("ok So you like Lost in OZ. Nice!")
else:
    print("Invalid input")
    if y == 3:
        print("Are you jocking ?")
prompt="""
ok now I will ask a quetion you have to answer it.
India is in which contenent:
1.antartic
2.north america 
3.asia
"""

b=input(prompt)
print(b)
print(type (b))
b=int(b)
print(b)
print(type (b))

if b == 1:
    print("wrong answer")
elif b == 2:
    print("wrong answer")
elif b == 3:
    print("correct answer")

print("ok my time  is exceeded so I will log out")