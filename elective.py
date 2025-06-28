violin=["anish"]
mrudanga=["aditya"]
flute=["akshobhya"]
j=0
o=int (input("enter the number of students who want to choose elective: "))
if o==0:
    print("no students are choosen elective")
    exit()
print("the available electives are: violin, mrudanga, flute")
while(o>j):
    j=j+1

    print("the available electives are: violin, mrudanga, flute")
    n=input("enter the which elective you want to choose: ")
    m=input("enter your name: ")
    if n=="violin":
        violin.append(m)
        print("you have choosen violin")
        print("the students who choosen violin are: ",violin)
    elif n=="mrudanga":
        mrudanga.append(m)
        print("you have choosen mrudanga")
        print("the students who choosen mrudanga are: ",mrudanga)
    elif n=="flute":
        flute.append(m)
        print("you have choosen flute")
        print("the students who choosen flute are: ",flute)
    print("list of mrudanga:",len(mrudanga))
    for i in range(len(mrudanga)):
        print(i,mrudanga[i])
    print("list of violin:",len(violin))
    for i in range(len(violin)):
        print(i,violin[i])
    print("list of flute:",len(flute))
    for i in range(len(flute)):
        print(i,flute[i])
print("total number of students who choosen flute are: ",len(flute))
print("total number of students who choosen mrudanga are: ",len(mrudanga))
print("total number of students who choosen violin are: ",len(violin))
