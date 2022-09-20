# this a cli game where either the user or the computer guesses a number

import random
import time
import sys
import os

if name == "__main__":
    # asking the user if they want to guess the number or if they want the computer to guess the number
    boolval = input("Do you want to guess the number or do you want the computer to guess the number? (y/n): ")
    if boolval == "y":
        # asking the user to input the number
        number = int(input("Please enter the number you want to guess: "))
        # asking the user to input the range of the number
        range = int(input("Please enter the range of the number: "))
        # generating a random number
        random_number = random.randint(0, range)
        # checking if the number is the same as the random number
        if number == random_number:
            # printing the number
            print(f"The number is {number}")
            # exiting the program
            sys.exit()
        else:
            # printing the number
            print(f"The number is {number}")
            # exiting the program
            sys.exit()
    elif boolval == "n":
        # asking the user to input the range of the number
        range = int(input("Please enter the range of the number: "))
        # generating a random number
        while True:
            # generating a random number
            random_number = random.randint(0, range)
            # asking the user to input the number
            number = int(input("Please enter the number you want to guess: "))
            # checking if the number is the same as the random number
            if number == random_number:
                # printing the number
                print(f"The number is {number}")
                # exiting the program
                sys.exit()
            else:
                # printing the number
                print(f"The number is {number}")
                # exiting the program
                sys.exit()
