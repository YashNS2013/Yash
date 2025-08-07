def printeven(arr):
    for i in arr:
        if i % 2 == 0:
            print(i)

# Create arr contianing numbers from 1 to 100
arr = list(range(1, 101))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printeven(arr)
a=[]
h=int(input("how many times you need to print a number :"))
i=0

while i< h:
    x=int (input("Enter a number: "))
    a.append(x)
    i=i+1

def multiple_of_eight(a):
    for i in a:
        if  i % 8 == 0:
            print(i,"is multiple of eight")
            
multiple_of_eight(a)
print(multiple_of_eight(a))

