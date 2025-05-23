import math
import sys
import signal

def timeout_handler(signum, frame):
    print("\nNo input received within 10 seconds. Exiting.")
    sys.exit()

# Set the timeout handler
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(10)  # Set timeout to 10 seconds

try:
    user_input = input("Enter a number: ")
    signal.alarm(0)  # Cancel the alarm if input is received
    number = float(user_input)
    print(f"The square root of {number} is {math.sqrt(number)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")

# Demonstrating while loop with less than, greater than, and skip counting

# Initialize variables
start = 1
end = 20
skip = 2

# While loop with less than condition
print("Numbers less than 20 with skip counting:")
current = start
while current < end:
    print(current, end=" ")
    current += skip

print("\n")

# While loop with greater than condition
print("Numbers greater than 0 with skip counting:")
current = end
while current > start:
    print(current, end=" ")
    current -= skip
