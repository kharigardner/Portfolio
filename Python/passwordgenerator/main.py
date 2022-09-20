# this is the command line wrapper of the password generator

import sys
import os
import passgen
import time

# defining the main function
if __name__ == "__main__":
    # defining the password length
    print("Please enter the length of the password you want to generate.")
    password_length = int(sys.argv[1])
    # generating the password
    password = passgen.password_generator(password_length)
    # printing the password
    print(f"Your password is: {password.password}")
    # printing the hashed password
    print(f"Your hashed password is: {password.HashedPassword(password.password).get_hashed_password()}")
    # waiting for 5 seconds
    time.sleep(5)
    # exiting the program
    sys.exit()
