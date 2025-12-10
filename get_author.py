def book_name_with_author():
    # Book author variables
    MAHABHARATAM = "veda vyasa"
    RAMAYANAM = "valmiki"
    BHAGAVAD_GITA = "veda vyasa"
    PURANAS = "vyasa"
    BHAGAVATAM = "vyasa"
    The_Palace_of_Illusions = "Chitra Banerjee Divakaruni"
    The_Inheritance_of_Loss = "Kiran Desai"
    A_Fine_Balance = "Rohinton Mistry"
    The_Namesake = "Jhumpa Lahiri"
    Gitanjali = "Rabindranath Tagore"
    The_Zoya_Factor = "Anuja Chauhan"
    The_Immortals_of_Meluha = "Amish Tripathi"

    # Show book options
    print("Choose a book:")
    print("1. MAHABHARATAM")
    print("2. RAMAYANAM")
    print("3. BHAGAVAD_GITA")
    print("4. PURANAS")
    print("5. BHAGAVATAM")
    print("6. The Palace of Illusions")
    print("7. The Inheritance of Loss")
    print("8. A Fine Balance")
    print("9. The Namesake")
    print("10. Gitanjali")
    print("11. The Zoya Factor")
    print("12. The Immortals of Meluha")

    choice = input("Enter the number of your choice: ")

    # Show author based on choice
    if choice == "1":
        print("Author: " + MAHABHARATAM)
    elif choice == "2":
        print("Author: " + RAMAYANAM)
    elif choice == "3":
        print("Author: " + BHAGAVAD_GITA)
    elif choice == "4":
        print("Author: " + PURANAS)
    elif choice == "5":
        print("Author: " + BHAGAVATAM)
    elif choice == "6":
        print("Author: " + The_Palace_of_Illusions)
    elif choice == "7":
        print("Author: " + The_Inheritance_of_Loss)
    elif choice == "8":
        print("Author: " + A_Fine_Balance)
    elif choice == "9":
        print("Author: " + The_Namesake)
    elif choice == "10":
        print("Author: " + Gitanjali)
    elif choice == "11":
        print("Author: " + The_Zoya_Factor)
    elif choice == "12":
        print("Author: " + The_Immortals_of_Meluha)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    book_name_with_author()

