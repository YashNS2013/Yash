# Removed unnecessary variable 'i' and redundant print statements. Simplified the loop and fixed input validation.
print("jay shree Ram")    
print("welcome to the restaurant")
 
to = 0

while True:
    y = int(input("press 1 for idli ,2 for dosa , 3 for vada , 4 for exit: "))
    if y == 1:
        print("idli is selected")
        print("price of idli is 50")
        to += 50
    elif y == 2:
        print("dosa is selected")
        print("price of dosa is 100")
        to += 100
    elif y == 3:
        print("vada is selected")
        print("price of vada is 30")
        to += 30
    elif y == 4:
        print("######")
        print(to)
        print("pay bill", to)
        break
    else:
        print("wrong button is pressed")
        break

print("thank you for visiting")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("jay shree Ram")
print("want to order again press ctrl+F5")

s = input("out door press 5: ")
if s == "5":
    print("thank you for visiting")


