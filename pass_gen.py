import secrets as sc
import string as strg
import sys
import pyperclip as pyp
import time

alphabet = strg.ascii_letters + strg.digits + strg.punctuation

password_length = int(input("Please enter the length of the password you want to generate (CANNOT BE HIGHER THAN 9999999): "))

if password_length > 9999999:
    print("an error occured")
    time.sleep(3)
    sys.exit()
    
password = "".join(sc.choice(alphabet) for _ in range(password_length))

print(f"Your generated password is: {password}")

copy_password = input("Do you want to copy the password to your clipboard? (y/n) ")
copy_password.lower

while copy_password != "y" and copy_password != "n":
    copy_password = input("Incorrect answer! Please enter if you want to copy the password or not: ")

if copy_password == "n":
    print("alr cool")

if copy_password == "y":
    pyp.copy(password)
    print("Password Copied!")

#more
gen_another_pass = input("Do you want to generate another password? (y/n): ")

while True:
    while gen_another_pass == "y":
        password_length = int(input("Please enter the length of the password you want to generate (CANNOT BE HIGHER THAN 9999999) (press q to quit): "))
        
        if password_length > 9999999:
            print("told ya")
            sys.exit()

        password = "".join(sc.choice(alphabet) for _ in range(password_length))
        print(f"Your generated password is: {password}")

        copy_password = input("do you want to copy the password? (y/n): ")
        copy_password.lower

        while copy_password != "y" and copy_password != "n":
            copy_password = input("Incorrect answer! Please enter if you want to copy the password or not: ")
        
        if copy_password == "n":
            print("alr cool uh")

        if copy_password == "y":
            pyp.copy(password)
            print("Password Copied!")
    if gen_another_pass == "n":
        print("i've done my stuff, goodbye!!")
        time.sleep(3)
        sys.exit()
    else:
        gen_another_pass = input("ALERT!! INCORRECT ANSWER!!!! please answer again PLEASE.....(y/n): ")
