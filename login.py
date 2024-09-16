import tkinter as tk
root=tk.Tk()
root.geometry('300x300')
root.resizable(False,False)
root.title('Login Form')

def exit():





title=tk.Label(root, text='Please enter your username and password to login')
title.grid(row=0, column=0, columnspan=2)

username=tk.Label(root,text='Username')
username.grid(row=1, column=0)

userentry=tk.Entry(root)
userentry.grid(row=1, column=1)

password=tk.Label(root, text='Password')
password.grid(row=2, column=0)

passwordentry=tk.Entry(root)
passwordentry.grid(row=2, column=1)


exit=tk.Button(root, text='Exit')
exit.grid(row=4, column=3)
root.mainloop()