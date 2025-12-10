

def which_is_Grater(a,b,c):
 #   a=int(input("Enter first number: "))
  #  b=int(input("Enter second number: "))
   # c=int(input("Enter third number: "))
    if a>b and a>c:
        return a

    elif b>a and b>c:
        return b

    elif c>a and c>b:
        return c
   #equal case
    elif a==b and a>c:
        return a , b

    elif a==c and a>b:
        return a , c
    elif b==c and b>a:
        return b , c 

a=which_is_Grater(4,5,6)#> this is called function parameter or argumant
print(a)