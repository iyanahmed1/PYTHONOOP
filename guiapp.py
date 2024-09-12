# libraries that we use to create a GUI
# TKinter, wxPython, PyGTK, PyQT
# widgets and tools to crate a user interface

# TK - Tk Interface
# helloworld aplication
import tkinter as tk

root = tk.Tk()#creating an instance of TK
# the main window of Tkinter is called root.you can however use any other name
root.geometry('480x240')
root.resizable(False,False)#fixed size
root.title('Tkinter Example')
# create a widget to display the text hello world
hello = tk.Label(root,text = 'Hello World')
hello.pack()#this embeds the label to the main windw

okay = tk.Button(root,text = 'OK',command=lambda: root.quit())
okay.pack()
# change the possition of the exit button
ipdadx = 5
ipady=5
expand=True

# adding an image to a button

root.mainloop()#the main loop ensures that the main windw remain visible on the screen