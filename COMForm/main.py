

from tkinter import *
from tkinter import messagebox
from turtle import width

from pyfirmata import *
from pyfirmata import Arduino


import time


# App title
root = Tk()
root.title(" Arduino Programmer ")
root.configure(background='#0F172A')
root.geometry("600x600")

led = ""
board = ""


# Functions

def setPort():
    messagebox.showinfo(message=ComEntry.get() + "\n Hi", title="Message")
    comPort = ComEntry.get()
    board = Arduino(comPort)

    print("Board Connection Successfully Initiated")


def Blink():
    led = board.digital[13]
    led.write(1)
    time.sleep(2)
    led.write(0)
    time.sleep(1)


def On():
    pin = '13'
    led = board.digital[13]
    led.write(1)


def Off():
    pin = '13'
    led = board.digital[13]
    led.write(0)


# main
w = Label(root, text="Arduino Programmer ", font="50")
w.grid(row=0, column=1)
# w.pack()

ComLabel = Label(root, text="Enter COM PORT ADDRESS")
ComEntry = Entry(root)

Submit = Button(root, text="submit", command=setPort)


ComLabel.grid(row=1, column=1, ipadx=4, ipady=4)
ComEntry.grid(row=1, column=3, ipadx=4, ipady=4)
Submit.grid(row=2, column=2, ipadx=4, ipady=4)


Button(root, text="LED ON", width="11", command=On).grid(
    row=3, column=0,   ipadx=2, ipady=2)

Button(root, text="LED OFF", width="11", command=Off).grid(
    row=3, column=1,   ipadx=2, ipady=2)


Button(root, text="Blink LED", width="11", command=Blink).grid(
    row=3, column=2,   ipadx=2, ipady=2)


root.mainloop()
