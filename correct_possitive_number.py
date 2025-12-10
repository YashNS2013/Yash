i=0

totalsum=0

while i<5:
    n=int(input("Enter a number of marks for subject: "))
    if n<0:
        print("error or wrong input")
    if n>100:
        print("give marks between 0 to 100")
        continue
    totalsum=totalsum+n
    i=i+1

print("The total marks"" is:", totalsum)
