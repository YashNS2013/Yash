

s = input("Enter a string: ")
rev = ""

i = len(s) - 1   
while i >= 0:
    rev += s[i]
    i -= 1

print("Reversed string:", rev)

if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
