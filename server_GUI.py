from tkinter import *
from subprocess import Popen
import os
#!/usr/bin/env python
root = Tk()

def onClick():
    process = None
    if ServerOnOff['text'] == "Server On":
        process = Popen(os.path.realpath("server.py"))
        ServerOnOff.config(text="Server Off")
    else:
        ServerOnOff.config(text="Server On")
        # Uncomment this if you want the process to terminate along with the window
        if process: 
            process.terminate()
        root.destroy()

# Code to add widgets will go here...
ServerOnOff = Button(root, text = "Server On", activebackground="#b9b9b9", activeforeground="#935fe8", command= onClick)
ServerOnOff.place(x=68,y=110)

root.mainloop()