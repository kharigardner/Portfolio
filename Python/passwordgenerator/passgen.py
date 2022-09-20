# this module is used to generate a secure, random password, along with a hashed object of the password, it also includes a CLI interface

# import modules
import random
import re
import hashlib
import string
import os
import sys
import time

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
    print("This module is not meant to be run directly, please run the main.py file instead.")
    sys.exit()

# creating classes

class Password:
    def __init__(self, password):
        self.password = password
    
    # defining the hashed password subclass
    class HashedPassword:
        def __init__(self, password):
            self.password = password
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

        def get_hashed_password(self):
            return self.hashed_password

# defining the password generator function

def password_generator(length):
    # defining the password length
    password_length = length
    # defining the password characters
    password_characters = string.ascii_letters + string.digits + string.punctuation
    # generating the password
    password = "".join(random.choice(password_characters) for _ in range(password_length))
    # returning the password
    PasswordClass = Password(password)
    return PasswordClass



