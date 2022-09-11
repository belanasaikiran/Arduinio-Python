# ---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino
# ---------------------------------------------

from tkinter import *
import pyfirmata


# ===============================================
# Arduino board connected to serial port COM3

# port = input("Select Correct Port: COM")
# comPort = "COM" + port
# board = pyfirmata.Arduino("/dev/ttyACM0")


if __name__ == '__main__':
    board = pyfirmata.Arduino('/dev/ttyACM0')
    print("Communication Successfully Initiated ")

# title
root = Tk()
root.title("Lights On", font=(18, 'Arial')
root.geometry("500x400")  # (length x width)


# ======GET LED PIN ======
pin='13'
led=board.digital[13]


# ===============================================
# Functions
# -----------

def On():
    led.write(1)


def Off():
    led.write(0)


Button(root, text="LED ON", width="11", command=On).grid(
    row=1, column=0,   ipadx=2, ipady=2)
Button(root, text="LED OFF", width="11", command=Off).grid(
    row=1, column=2,   ipadx=2, ipady=2)


root.mainloop()
