# ---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino
# ---------------------------------------------

from tkinter import *
import pyfirmata


# ===============================================
# Input to Arduino board for communication

if __name__ == '__main__':
    port = input("Enter COM port Name:  \n")
    comPort = port
    board = pyfirmata.Arduino(comPort)
    print("Communication Successfully Initiated ")

# title
root = Tk()
root.title(" Lights On ")
root.geometry("600x600")  # (length x width)


# ======GET LED PIN ======
pin = '13'
led = board.digital[13]


# ===============================================
# Functions
# -----------

def On():
    led.write(1)


def Off():
    led.write(0)


#  =============================================
# Button Actions
# -----------
Button(root, text="LED ON", width="11", command=On).grid(
    row=1, column=0,   ipadx=2, ipady=2)
Button(root, text="LED OFF", width="11", command=Off).grid(
    row=1, column=2,   ipadx=2, ipady=2)


# ======
root.mainloop()
