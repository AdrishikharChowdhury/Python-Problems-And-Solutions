import random
import string
password=""
rando=string.ascii_letters+string.digits+string.punctuation
len=int(input("Enter the password length: "))
for i in range(len):
    password+=random.choice(rando)
print("Your suggested password is:",password)