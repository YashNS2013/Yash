a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def add ():
    return a + b


c=int(input("enter first number: "))
d=int(input("enter second number: "))

def sub():
    return c - d

t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,]
# Gretest number in array simple function

def greatest_in_array(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
    
def printing():
    I=0
    while I<10:
        I=I+1
        print("jAI SHREE RAM")  


a=add()
c=sub()
max_value =greatest_in_array(t)
printing()
print("Addition is:",a)
print("Subtraction is:",c)
print("Greatest number in array is:",max_value)