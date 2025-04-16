
def hash_fn(password):
    sum = 0
    xor = 0
    for i in range(len(password)):
        sum = sum + ord(password[i]) 
        xor = xor ^ ord(password[i])

    print(sum + xor)
    return sum + xor

passwd = hash_fn(input("Set Password: "))



while True:
    login = hash_fn(input("Enter the same password to continue: "))
    if login == passwd:
        print("Correct password. Loging success!")
        break
    else:
        print("Incorrect password, try again.")

