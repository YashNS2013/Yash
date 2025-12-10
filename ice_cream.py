def ice_cream():
    print("====================================================================================")
    print("Welcome to the Ice Cream Shop!")
    print("We have the following flavors available:")
    print("1. Vanilla 20$")
    print("2. mango 30$")
    print("3. straberry 25$")
    print("4. stop, send bill")
    cart=0
    t=100
    while t>0:

        choice =int( input("Please enter the number of your choice: "))

        if choice == 1:
            cart=cart+20
            print("You have selected Vanilla. Your current total is: ",cart)
        elif choice == 2:
            cart=cart+30
            print("You have selected mango. Your current total is: ",cart)
        elif choice == 3:
            cart=cart+25
            print("You have selected straberry. Your current total is: ",cart)
        elif choice == 4:
            print("Thank you for your order. Your final total is: ",cart)
            print("####################################################################################")
            break
        
        t=t-1
    print("====================================================================================") 
ice_cream()          