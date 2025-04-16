# Welcome message
print("jay shree Ram")    
print("welcome to the restaurant")
 
to = 0  # Initialize total bill amount

while True:
    # Display menu options
    y = int(input("press 1 for idli ,2 for dosa , 3 for vada , 4 for exit: "))
    if y == 1:
        print("idli is selected")
        print("price of idli is 50")
        to += 50  # Add idli price to total
    elif y == 2:
        print("dosa is selected")
        print("price of dosa is 100")
        to += 100  # Add dosa price to total
    elif y == 3:
        print("vada is selected")
        print("price of vada is 30")
        to += 30  # Add vada price to total
    elif y == 4:
        # Exit and display total bill
        print("######")
        print(to)
        print("pay bill", to)
        break
    else:
        # Handle invalid input
        print("wrong button is pressed")
        break

# Thank you message
print("thank you for visiting")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("jay shree Ram")
print("want to order again press ctrl+F5")

# Exit prompt
s = input("out door press 5: ")
if s == "5":
    print("thank you for visiting")


