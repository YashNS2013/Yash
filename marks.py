a=int (input("enter marks in english in /90"))
print("Marks in English:", a)
s=int (input("enter marks in science in /90"))
print("Marks in Science:", s)
m=int (input("enter marks in maths in /90")) 
print("Marks in Maths:", m)
t=int (input("enter marks in samskruta in /90"))
print("Marks in Samskruta:", t)

print("Total Marks:", a + s + m + t ,"/360")
if (a + s + m + t) > 320:
    print ("good job")
elif (a + s + m + t) > 240:
    print ("you can do better")
else:
    print ("you need to work hard")
print("Marks in total:", a + s + m + t)
if(a or s or m or t)== 90:
    print("you have earned a star **")