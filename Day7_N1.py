import sys

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(10000)

def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
    print()

def main():
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    fibonacci_series(n)

if __name__ == "__main__":
    main()