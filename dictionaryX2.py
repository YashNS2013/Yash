

# Variable student_details to store student information information with key as student name & value as dictionary which has keys age, grade, class elective.
student_details = {}

# Add student function to add student information to the student_details dictionary.
def add_student(name, age, grade, elective):
    student_details[name] = {
        "age": age,
        "grade": grade,
        "elective": elective
    }

# Function to remove student information from the student_details dictionary.
def remove_student(name):
    if name in student_details:
        student_details.pop(name)
    else:
        print(f"Student {name} not found.")

# Function to display student information from the student_details dictionary for given name
def display_students(name=None):
    if name:
        if name in student_details:
            print(f"Details of {name}: {student_details[name]}")
        else:
            print(f"Student {name} not found.")
    else:
        for student, details in student_details.items():
            print(f"{student}: {details}")

# Loop to Display menu for add/remove/display student information.
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        elective = input("Enter student elective: ")
        add_student(name, age, grade, elective)
    elif choice == '2':
        name = input("Enter student name to remove: ")
        remove_student(name)
    elif choice == '3':
        # ask name to display specific student or display all students
        name = input("Enter student name to display (or press Enter to display all): ")
        if name:
            display_students(name)
        else:
            display_students()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")