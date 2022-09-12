# ---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino
# ---------------------------------------------

from tkinter import *
import pyfirmata
import time
from tkinter import messagebox


# ===============================================
# Input to Arduino board for communication

if __name__ == '__main__':
    # port = input("Enter COM port Name:  \n")
    comPort = "/dev/ttyACM0"
    board = pyfirmata.Arduino(comPort)
    print("Communication Successfully Initiated ")

# title
root = Tk()
root.title(" Delay Lights ")
root.geometry("600x600")  # (length x width)


# ======GET LED PIN ======
pin = '13'
led = board.digital[13]


# ===============================================
# Functions
# -----------

def Blink():
    led.write(1)
    time.sleep(2)
    led.write(0)
    time.sleep(1)


def On():
    led.write(1)


def Off():
    led.write(0)


# def msgbox():
#     messagebox.showinfo(title="A Message", message="Hello World!")


#  =============================================
# Button Actions
# -----------


Button(root, text="LED ON", width="11", command=On).grid(
    row=1, column=0,   ipadx=2, ipady=2)

Button(root, text="LED OFF", width="11", command=Off).grid(
    row=1, column=1,   ipadx=2, ipady=2)


Button(root, text="Blink LED", width="11", command=Blink).grid(
    row=1, column=2,   ipadx=2, ipady=2)


# Button(root, text="msgbox", command=msgbox).grid(
#     row=3, column=3, ipadx=4, ipady=4)


# ======
root.mainloop()
