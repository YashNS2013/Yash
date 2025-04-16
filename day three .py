print("namaste!")
a=("ramah ramau ramaha")
s=("herama heramau heramha")
d=("ramam ramau raman")
f=("ramena ramabhyam ramayhi")
g=("ramay ramabhyam ramebhyh")
h=("ramat ramabhyam ramebhyh")
j=("ramasya ramayoho ramanam")
k=("rame ramayoho rameshu")

promt="""
which vibhakti will you choose
1.
0.
2.
3.
4.
5.
6.
7.
"""
y=input(promt)
print(y)
print(type(y))
y=int(y)
print(type(y))
if y== 1.:
    print(a)
if y== 2.:
    print(d)
if y == 0.:
    print(s)
if y==3.:
    print(f)
if y== 4.:
    print(g)
if y==5.:
    print(h)
if y==6.:
    print(j) 
if y==7.:
    print(k)