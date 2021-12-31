#!/usr/bin/env python3
from tkinter import *
from subprocess import Popen
import os
root = Tk()
root.geometry("200x200")
def onClick():
    process = None
    if ServerOnOff['text'] == "Server On":
        process = Popen(['python3', os.path.realpath("server.py")])
        ServerStatus.config(text="Server is on")
        ServerOnOff.config(text="Server off")
    else:
        ServerOnOff.config(text="Server on")
        # Uncomment this if you want the process to terminate along with the window
        if process: 
            process.terminate()
            ServerStatus.config(text="Server is off")
        root.destroy()

# Code to add widgets will go here...
ServerStatus = Label(root, text = "Server is off")
ServerOnOff = Button(root, text = "Server on", activebackground="#b9b9b9", activeforeground="#935fe8", command= onClick)
ServerOnOff.place(x=68,y=110)
ServerStatus.pack()
root.mainloop()
