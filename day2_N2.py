from hashlib import sha256, sha512
from time import sleep

def hash_fn(password):
    hash = sha256(password.encode('utf-8')).hexdigest()
    hash2 = sha512(password.encode('utf-8')).hexdigest()
    
    print(hash, hash2)
    return hash2

passwd = hash_fn(input("Set Password: "))


wrong_count = 0
while True:
    login = hash_fn(input("Enter the same password to continue: "))
    if login == passwd:
        print("Correct password. Loging success!")
        break
    else:
        print("Incorrect password, try again.")
        wrong_count = wrong_count + 1

    if wrong_count > 4:
        print("Too many wrong attempts. Wiat 60 seconds!")
        for j in range(60):
            print("\rWait for ",60-j, end='')
            sleep(1)
        print("")

