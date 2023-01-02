import secrets
import string

password_length = int(input("Please enter the length of the password(CANNOT BE HIGHER THAN 9999999): "))

alphabet = string.ascii_letters + string.digits
symbols = "`~!@#$%^&*()_+|\}{:?><,./;'[]"
password = ''.join(secrets.choice(alphabet + symbols) for i in range(password_length))
#password max cap
if password_length >= 10000000:
    print("Password length cannot be higher than 9999999!")
    int(input("Please enter the length of the password(CANNOT BE HIGHER THAN 9999999): "))
    print(password)
else:
    print(password)

#enter to exit (OMG!!!)
x = input("Done, press Enter to exit")
