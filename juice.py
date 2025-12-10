
print("========================================================================================")
print("                               WELCOME TO JUICE SHOP                                 ")
print("========================================================================================")

def juice_menu():
    print("Available Juice Flavors:")
    print(" 1 sapota,2 mango,3 sugercane and 4 exit ")
    o=int(input("Enter the number of juice flavors available: "))
    if o==0:
        print("No juice flavors available")
        exit()
    return o                    
    for j in range(o):
        n=input("Enter the juice flavor you want to choose: ")
        m=input("Enter your name: ")
        if n=="sapota":
            print("You have chosen sapota juice")
        elif n=="mango":
            print("You have chosen mango juice")
        elif n=="sugercane":
            print("You have chosen sugercane juice")
        elif n=="exit":
            print("Exiting the juice shop")
            exit()
print("Thank you for visiting the juice shop!")


print(juice_menu())

