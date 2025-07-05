
# List to store dictionary of name & their details for use in student details tracking
student_details = []

# Function to add a new student
def add_student(name, age, grade):
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    student_details.append(student)
    print(f"Student {name} added successfully.")

# Test add_student function
if __name__ == "__main__":
    add_student("Yash", 11, "5")
    add_student("Riddhi", 8, "4")
    
    # Print the student details to verify
    for student in student_details:
        print(student)

print(student_details)


c = [5, 10, 15, 20, 25, "asdf"]
print("List c:", c)