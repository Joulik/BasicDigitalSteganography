from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog
import os
import cv2
import numpy as np

#select message and carrier images - encryption
def encrypt():
    #select image to hide
    def buttonImageToHide():
        #use global variable
        global answerHide
        global filenameHide
        #get file location from user
        answerHide = filedialog.askopenfilename(parent=winEncrypt,
                                    initialdir=os.getcwd(),
                                    title="Please select file:")
        #print name of file and image size in window
        aa = answerHide.split("/")
        label = Label(winEncrypt, text=aa[-1])
        label.place(x=50, y=50)
        imageToHide = cv2.imread(answerHide)
        height = imageToHide.shape[0]
        width = imageToHide.shape[1]
        sizeOfImage = "Image size: {} x {}"
        label = Label(winEncrypt, text=sizeOfImage.format(height,width), fg="blue")
        label.place(x=50, y=75)
        #print name of file and size in console
        print("Image to Hide: ", aa[-1])
        print(sizeOfImage.format(height, width))
        #save file name
        filenameHide = aa[-1]
        #show image
        img = cv2.imread(answerHide)
        cv2.imshow('Image to hide',img)

    #select carrier image
    def buttonImageCarrier():
        #use global variable
        global answerCarrier
        global filenameCarrier
        #get file location from user
        answerCarrier = filedialog.askopenfilename(parent=winEncrypt,
                                    initialdir=os.getcwd(),
                                    title="Please select file:")
        #print name of file and size of image in window
        aa = answerCarrier.split("/")
        label = Label(winEncrypt, text=aa[-1])
        label.place(x=50, y=140)
        imageCarrier = cv2.imread(answerCarrier)
        height = imageCarrier.shape[0]
        width = imageCarrier.shape[1]
        sizeOfImage = "Image size: {} x {}"
        label = Label(winEncrypt, text=sizeOfImage.format(height,width), fg="blue")
        label.place(x=50, y=165)
        #print name of file and size of image in console
        print("Carrier image: ", aa[-1])
        print(sizeOfImage.format(height, width))
        #save file name
        filenameCarrier = aa[-1]
        #show image
        img = cv2.imread(answerCarrier)
        cv2.imshow('Carrier image',img)

    #generate and save image with embedded message
    def buttonGenerateMessage():
        #use global variable
        global answerHide
        global answerSupport
        global filenameHide
        global filenameSupport
        #print name of files on console
        print(filenameHide,filenameCarrier)
        #load carrier image
        supportImage = cv2.imread(answerCarrier)
        #load black and white image to hide
        imageToHide = cv2.imread(answerHide)
        #Turn parity of array elements into array of booleans
        supportImageBool = supportImage % 2 == 1
        imageToHideBool = imageToHide % 2 == 1
        #construct parity array to filter carrier image
        filterBool = np.bitwise_xor(supportImageBool, imageToHideBool)
        #turn filter boolean array into 0s and 1s array
        filter = np.where(filterBool, 1, 0)
        #construct message array
        message = supportImage - filter
        message = np.absolute(message)

        #get name of file to save from user
        answerSave = filedialog.asksaveasfilename(parent=winEncrypt,
                                      initialdir=os.getcwd(),
                                      title="Please select a file name for saving:",
                                      defaultextension='.png')
        filenameMessage = answerSave
        cv2.imwrite(filenameMessage, message)
        windowMessage = 'Image with embedded data'
        img = cv2.imread(filenameMessage)
        cv2.imshow(windowMessage, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #encryption window buttons
    winEncrypt = Toplevel(mainWindow)
    winEncrypt.title('Encrypt')
    winEncrypt.geometry("400x300")
    winEncrypt.minsize(400,300)

    myFont = font.Font(family='Helvetica', size=12)
    buttonA = Button(winEncrypt, text='Select file with BLACK AND WHITE image to hide', command=buttonImageToHide)
    buttonA['font'] = myFont
    buttonA.pack(pady=10)

    buttonB = Button(winEncrypt, text='Select file with carrier image', command=buttonImageCarrier)
    buttonB['font'] = myFont
    buttonB.pack(pady=50)

    buttonC = Button(winEncrypt, text='Generate image with hidden message', command=buttonGenerateMessage)
    buttonC['font'] = myFont
    buttonC.pack(pady=10)

    buttonD = Button(winEncrypt, text='Quit', command=winEncrypt.destroy)
    buttonD['font'] = myFont
    buttonD.pack(pady=10)

    ##winEncrypt.transient(mainWindow)
    ##winEncrypt.grab_set()
    ##mainWindow.wait_window(winEncrypt)

#select image with hidden message and decipher
def decipher():
    #select image
    def buttonDecipher():
        answerDecipher = filedialog.askopenfilename(parent=winDecipher,
                                    initialdir=os.getcwd(),
                                    title="Please select file:")

        #load message image
        message = cv2.imread(answerDecipher)
        #show embedded image
        embeddedImage = message%2 * 255
        cv2.imwrite('embeddedImageDeciphered.png', embeddedImage)
        img = cv2.imread('embeddedImageDeciphered.png')
        cv2.imshow("Deciphered embedded image", img)
        ##cv2.waitKey(0)
        ##cv2.destroyAllWindows()

    #decipher window buttons    
    winDecipher = Toplevel(mainWindow)
    winDecipher.title('Decipher')
    winDecipher.geometry("300x100")
    winDecipher.minsize(300,100)
    
    myFont = font.Font(family='Helvetica', size=12)
    buttonA = Button(winDecipher, text='Select file with embedded message', command=buttonDecipher)
    buttonA['font'] = myFont
    buttonA.pack(pady=10)
    
    buttonD = Button(winDecipher, text='Quit', command=winDecipher.destroy)
    buttonD['font'] = myFont
    buttonD.pack(pady=10)

    ##winDecipher.transient(mainWindow)
    ##winDecipher.grab_set()
    ##mainWindow.wait_window(winDecipher)

#main window of application
mainWindow = Tk()
mainWindow.title('Basic steganography')
mainWindow.geometry('300x140')

#initialize global variables
filenameHide=''
filenameCarrier=''

#buttons
buttonEncrypt = Button(mainWindow, text='Encrypt', command=encrypt).pack(pady=10)
buttonDecipher = Button(mainWindow, text='Decipher', command=decipher).pack(pady=10)
buttonDone = Button(mainWindow, text="Quit", command=mainWindow.destroy).pack(pady=10)

mainWindow.mainloop()