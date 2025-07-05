# Program to take input of chapters in different subjects and display them

Math=[]
Science=[]
English=[]
Social=[]
Hindi=[]
Sanskrit=[]
TDP=[]

s=0
o=int(input("how many chapters are there in Math: "))
while(o>s):
    s=s+1
    if o==0:
        print("no chapters in Math")
        
    m=input("enter the chapter name: ")
    Math.append(m)
p=0
a=int(input("how many chapters are there in Science: "))
while(a>p):
    p=p+1
    if a==0:
        print("no chapters in Science")
        
    n=input("enter the chapter name: ")
    Science.append(n)
q=0
s=int(input("how many chapters are there in English: "))
while(s>q):
    q=q+1
    if s==0:
        print("no chapters in English")
        
    r=input("enter the chapter name: ")
    English.append(r)
w=0
d=int(input("how many chapters are there in Social: "))
while(d>w):
    w=w+1
    if d==0:
        print("no chapters in Social")
        
    t=input("enter the chapter name: ")
    Social.append(t)

e=0
f=int(input("how many chapters are there in Hindi: "))
while(f>e):
    e=e+1
    if f==0:
        print("no chapters in Hindi")
        
    u=input("enter the chapter name: ")
    Hindi.append(u)
g=0
h=int(input("how many chapters are there in Sanskrit: "))
while(h>g):
    g=g+1
    if h==0:
        print("no chapters in Sanskrit")
        
    v=input("enter the chapter name: ")
    Sanskrit.append(v)
i=0
j=int(input("how many chapters are there in TDP: "))
while(j>i):
    i=i+1
    if j==0:
        print("no chapters in TDP")
        
    x=input("enter the chapter name: ")
    TDP.append(x)

print("Total chapters in Math:", len(Math) )
for i in range(1, len(Math)):
    print(i, Math[i])
print("Total chapters in Science:", len(Science))
for i in range(1, len(Science)):
    print(i, Science[i])
print("Total chapters in English:", len(English) )
for i in range(1, len(English)):
    print(i, English[i])
print("Total chapters in Social:", len(Social) )
for i in range(1, len(Social)):
    print(i, Social[i])
print("Total chapters in Hindi:", len(Hindi) )
for i in range(1, len(Hindi)):
    print(i, Hindi[i])
print("Total chapters in Sanskrit:", len(Sanskrit) )
for i in range(1, len(Sanskrit)):
    print(i, Sanskrit[i])
print("Total chapters in TDP:", len(TDP) )
for i in range(1, len(TDP)):
    print(i, TDP[i])

