# Ask the user to input the number of stars
num_stars = int(input("How many stars would you like to print? "))

# Print the stars
for _ in range(num_stars):
    print("*", end="")
print()