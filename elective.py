

violin=[]
mrudanga=[]
flute=[]
karate=[]
drama=[]
yakshagana=[]
#j=0
#o=int (input("enter the number of students who want to choose elective: "))
#if o==0:
#    print("no students are choosen elective")
 #   exit()
j=0
#print("the available electives are: violin, mrudanga, flute")
while(3>j):
    j=j+1

    print("the available electives are: violin, mrudanga, flute, karate, drama, yakshagana")
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
    elif n=="karate":
        karate.append(m)
        print("you have choosen karate")
        print("the students who choosen karate are: ",karate)
    elif n=="drama":
        drama.append(m)
        print("you have choosen drama")
        print("the students who choosen drama are: ",drama)

    elif n=="yakshagana":
        yakshagana.append(m)
        print("you have choosen yakshagana")
        print("the students who choosen yakshagana are: ",yakshagana)
    
    print("list of mrudanga:",len(mrudanga))
    for i in range(len(mrudanga)):
        print(i,mrudanga[i])
    print("list of violin:",len(violin))
    for i in range(len(violin)):
        print(i,violin[i])
    print("list of flute:",len(flute))
    for i in range(len(flute)):
        print(i,flute[i])
    print("list of karate:",len(karate))
    for i in range(len(karate)):
        print(i,karate[i])
    print("list of drama:",len(drama))
    for i in range(len(drama)):
        print(i,drama[i])
    print("list of yakshagana:",len(yakshagana))
    for i in range(len(yakshagana)):
        print(i,yakshagana[i])

print("total number of students who choosen flute are: ",len(flute))
print("total number of students who choosen mrudanga are: ",len(mrudanga))

print("total number of students who choosen violin are: ",len(violin))
print("total number of students who choosen karate are: ",len(karate))
print("total number of students who choosen drama are: ",len(drama))
print("total number of students who choosen yakshagana are: ",len(yakshagana))
exit()