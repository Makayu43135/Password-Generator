import secrets
import string

password_length = int(input("Please enter the length of the password: "))

alphabet = string.ascii_letters + string.digits
symbols = "`~!@#$%^&*()_+|\}{:?><,./;'[]"
password = ''.join(secrets.choice(alphabet + symbols) for i in range(password_length))
print("Generated Password: " + password)

x = input("Done, press Enter to exit")
# simple code isnt it?
