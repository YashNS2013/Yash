


# List of students names only
students = []


# Loop to display menu & ask user for input like exit, add, remove, display
while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student's name to add: ")
        students.append(name)
        print(f"Added {name}.")
        
    elif choice == '2':
        name = input("Enter student's name to remove: ")
        if name in students:
            students.remove(name)
            print(f"Removed {name}.")
        else:
            print(f"{name} not found.")
            
    elif choice == '3':
        if students:
            print("Students list:")
            for student in students:
                print(student)
        else:
            print("No students in the list.")
            
    elif choice == '4':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice, please try again.")
