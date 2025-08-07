from sys import exit

def calculate_third_angle():
    print("#########################################################################################")
    print("           welcome to the program 3 angle.py           ")
    print("#########################################################################################")
    I = int(input("give firstangle of triangle it should be below 180: "))
    N = int(input("give second angle of triangle it should be below 180: "))

    if (I < 0 or I >= 180) or (N < 0 or N >= 180):
            print("Invalid input. Angles must be between 0 and 180 degrees.")
            exit(1)

    if (I + N) >= 180:
        print("The sum of the first two angles must be less than 180 degrees.")
        exit(1)
        
    third_angle = 180 - (I + N)
    print("The third angle of the triangle is", third_angle, "degrees.")
    print("#####################################################################################")
    if I<90 and N<90 and third_angle<90:
        print("The triangle is an acute triangle.")
    if I==90 or N==90 or third_angle==90:
        print("The triangle is a right triangle.")
    if I>90 or N>90 or third_angle>90:
        print("The triangle is an obtuse triangle.")

    # Check for equilateral triangle. Equilateral triangle has all angles equal.
    if I==N and I==third_angle:
        print("The triangle is an equilatral triangle.")
    # Check for isosceles triangle. Isosceles triangle has at least two angles equal.
    elif I==N or I==third_angle or N==third_angle:
        print("The triangle is an isocles triangle.")
    # If the triangle is not equilateral or isosceles, it must be scalene.
    elif I!=N and I!=third_angle and N!=third_angle: # Can also use else since if a triangle is not equilateral or isosceles, it must be scalene.
        print("The triangle is a scalene triangle.")
calculate_third_angle()

