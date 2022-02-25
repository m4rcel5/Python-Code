"""
    author: m4rcel5
    19.02.2022
    password generator
"""
import os
import string
import time
import random

os.system("cls")

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

length = input("Enter the length of your password (empty input stops the program): ")
while length != "":
    if int(length) <= 90 and int(length) >= 8:
        password = "".join(random.sample(chars, int(length)))
        print(f"Your password is: {password}")
        time.sleep(2)
        length = input("Enter the length of your password (empty input stops the program): ")
    else:
        print("The length must not be greater than 90 and not smaller than 8!")
