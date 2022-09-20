# this script is used to display the time on the screen, using the "textual" module for gui development

from datetime import datetime
import sys
import os
import time

# building the clock class

class Clock():
    def __init__(self, hour = datetime.now().hour , minute = datetime.now().minute , second = datetime.now().second):
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.second = datetime.now().second

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def display(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    #TODO: check if this is still needed 
    def __str__(self):
        # checking if the window is open or not
        self.tick()
        self.display()
        return self.display()

# command line script to display the time on the screen
if __name__ == "__main__":
    clock = Clock()
    # accepting a command line argument to set how long the clock should run for
    print("How long do you want the clock to run for?") 
    userinput = input()
    # converting user input to minutes
    runtime = int(userinput)
    # looping the clock for the specified time
    while runtime != 0:
        clock.tick()
        print(clock.display())
        time.sleep(60)
        runtime -= 1