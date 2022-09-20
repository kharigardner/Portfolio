# this script builds a gui for the weather app
from tkinter import *

# create the window
import weathermodule
from weathermodule import WeatherGrabber
from weathermodule import utils

# create the gui
gui = Tk()
gui.title("Weather App")
gui.geometry("500x500")
gui.configure(background="lightblue")
gui.resizable(False, False)
gui.iconbitmap("weather\weather.ico")
gui.wm_attributes("-topmost", True)
gui.wm_attributes("-disabled", True)
gui.wm_attributes("-transparentcolor", "lightblue")

# create the weather grabber
weather = WeatherGrabber()
