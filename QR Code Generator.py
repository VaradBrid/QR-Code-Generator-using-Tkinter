

#This Program will create a QR - Code of any text entered by the user:



#Importing the following packages: png, time, sys, pyqrcode, PIL & tkinter:
#From PIL, tkinter and pyqrcode we import "Image - ImageTk", "messagebox as MB" & "QRCode" respectively:
import png
import time
import sys

import pyqrcode
from pyqrcode import QRCode

import PIL.Image
from PIL import Image, ImageTk

from tkinter import *
from tkinter import messagebox as MB



sys.tracebacklimit = 0
window = Tk()

#Setting the TITLE of the Interface:
window.title("QR Code Generator")
window.geometry('302x302')
window.eval('tk::PlaceWindow . center')
window['bg'] = 'dark orchid'

#Creating a Label to act as an Instruction for the user:
label = Label(window, text="\n\n\n\n\n\n\nPlease enter a URL or a Statement to make a QR Code of", bg = 'dark orchid', fg = 'yellow')
label.grid(column=0, row=0)

#Using the "Entry()" function to accept String from user:
URLorSTRING = StringVar()
entry = Entry(window, width=20, textvariable = URLorSTRING)
entry.grid(column=0, row=2, pady = 10)



#Function to create the QR Code:
def generate():
    #Comparing length in order to continue:
    if len(URLorSTRING.get()) != 0:
        #Creating the QR Code:
        url = pyqrcode.create(URLorSTRING.get())
        #Saving the QR Code in ".png" format:
        url.png ('Your QR - Code.png', scale = 10)        
    #If the length = 0, then it will show a WARNING MESSAGE:
    else:
        MB.showwarning('WARNING !!', 'Complete all the fields')



#Function to show a successfull generation MESSAGEBOX:
def successfull_generation():
    if len(URLorSTRING.get())!= 0:
        time.sleep(1)
        MB.showinfo("QR Code Generator", "Please wait while your QR Code is being generated")
        time.sleep(1.5)
        MB.showinfo("QR Code Generator", "Your QR Code has been successfully generated")
    else:
        window.quit()



#Function to display the QR Code generated on the screen:
def showingQRcode():
    #To display the code when the variable isn't empty:
    if len(URLorSTRING.get())!= 0:
        global my_img
        top = Toplevel()
        #Setting the TITLE of the Window:
        top.title("Generated Code")
        #Displaying Image:
        my_img = ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\Palande\Desktop\KJ Somaiya COE\1st year ME\Semester - 2\Python Programming [PP]\Mini Project\Your QR - Code.png'))
        label = Label(top, image = my_img).pack()
        #Initimation while exiting:
        OK = MB.showwarning("QR Code Generator", "Thank You for using the QR Code Generator")
        if (OK == 'ok'):
            MB.showinfo("QR Code Generator", "\tProject By:\n\n\tVarad Rajesh Brid\t\t[16010521008]")
            window.destroy()
        else:
            window.destroy()
    #To exit the code when the variable is empty:
    else:
        window.quit()



#Creating a Button "Enter" to act as a Switch to start the Generation:
#Using "lambda []" function to combine 3 functions together:
button = Button(window, text = "Enter", width=10, command = lambda: [generate(), successfull_generation(), showingQRcode()])
button.grid(column=0, row=4)



#To end the TKINTER Program:
window.mainloop()



#Programmer  : VRB
#Branch      : Mechanical [I - 1]
#Roll Number : 16010521008

