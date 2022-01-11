# Python-miniprojects
1. Make animation using turtle module:
turtle -> Turtle is a Python module that provides a drawing board like feature, which enables users to create pictures and shapes.
turtle.bgcolor("cyan") -> This method is used to set or return background color of the Turtle Screen.
turtle.pensize(1.6) -> This method is used to set or return the line thickness.
turtle.speed(0.25) -> This method is used to change the speed of the turtle by the value of the argument that it takes. Return or set the turtle’s speed
turtle.circle(150) -> This method is used to draw a circle with a given radius.
turtle.left(12) -> This method is used to change the direction of the turtle by the value of the argument that it takes.
turtle.mainloop() -> mainloop tells the window to wait for the user to do something.

2.Convert mp4 file to gif:
install moviepy in the terminal
Import everything needed to edit video clips
VideoFileClip("mp4 file name") -> VideoFileClip object
write_gif("new gif file name") -> write video file into gif

3.Make a notification app using time and plyer modules:
import time module
install plyer in the terminal
from plyer import notification
time: This module works with the time object and is installed by default
Plyer: Plyer module is used to access the features of the hardware. We install this externally.
notification.notify -> Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)
It call the notify method of this class.
title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification
time.sleep() -> sleep function of time module to show that notification again (waiting time)

4.Make a barcode generator
install python_barcode module in terminal and import barcode module
from barcode.writer import ImageWriter module
write and store some of the text in the string format
barcode.get_barcode_class("code128") ->Namespace/Package Name: barcode and Method/Function: get_barcode_class
image = code(text, writer=ImageWriter()) -> code [String] Code 128 string without checksum (added automatically).
writer [barcode.writer Instance] The writer to render the barcode
savedimage = image.save("final barcode") -> barcode.writer.ImageWriter method

5. Internet speed checker
using tkinter library import all the functions
using tkinter library again import message box
install pyspeedtest module in terminal and import it
make a tkinter window and give title using title Method
set background color using config method
using geometry method set the dimansions of the window
give heading of the window using Label function with parametrs as window, text to be written there, font(type,size,bold), background color 
at last use pack function to put out the things line by line in the window
using button method with parameters as window name, text, font(type,size,bold), background color,height,width,command="some function name"
at last again use pack function
declare the function used in the command parameter
using pyspeedtest module use function SpeedTest provide a url
use download and ping function to calculate downloading and pinging speed
showinfo function of messagebox is used for displaying a text while speed is displayed

