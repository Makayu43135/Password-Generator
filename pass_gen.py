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
    print("alr cool goodbye")
    time.sleep(2)
    sys.exit()

if copy_password == "y":
    pyp.copy(password)
    print("Password Copied!")

print("i've done my stuff, goodbye!!")
time.sleep(3)
sys.exit()
