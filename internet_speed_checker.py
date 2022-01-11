from tkinter import *
from tkinter import messagebox
# pip install pyspeedtest
import pyspeedtest

def fun():
    speed = pyspeedtest.SpeedTest("www.google.com")
    var1 = (str(speed.download())+"[bytes per sec]")
    messagebox.showinfo("Your download speed", var1)

root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="pink")
root.geometry("500x250")

label1 = Label(root, text="Internet Speed Checker", font=("ALGERIAN", 20, "bold"), bg="cyan").pack()
button1 = Button(root, text="Click!!", font=("Arial", 12, "bold"), bg="red", height = 1, width=20, command=fun).pack()

root.mainloop()
