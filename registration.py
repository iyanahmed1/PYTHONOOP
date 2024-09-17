# create a tkinker window with the following fields
#username
# email, password, phone number
# login button 
#registration button
#exit button

#create a login page containing username and password fields
#login, registartio and exit buttom

import tkinter as tk
import mysql.connector#this is for connection to the database

#set up the database connection
def connect_db():
    return mysql.connector.connect(
        host= 'Local host',
        user=  'root'
        
    )

#define the function to register the user
def register_user():
    user=userentry.get()
    FName=fnameentry.get()
    SName=surnameentry.get()
    Email=emailentry.get()
    Password=passwordentry.get()
    Repassword=repeatpasswordentry.get()
    Phone=phoneentry.get()

    if Repassword!=Password:
        print('Password Mismatch')

    else:
        print('Registration successful')






root=tk.Tk()
root.geometry('300x300')
root.resizable(False,False)
root.title('Registration Form')
#username(label) and userenter (textbox)
username=tk.Label(root,text='Username')
username.grid(row=0, column=0)

userentry=tk.Entry(root)
userentry.grid(row=0 , column=1)

#first name (label) and entry(textbox)
fname=tk.Label(root, text='First Name ')
fname.grid(row=1, column=0)

fnameentry=tk.Entry(root)
fnameentry.grid(row=1, column=1)

#surname
surname=tk.Label(root, text='Surname ')
surname.grid(row=2, column=0)

surnameentry=tk.Entry(root)
surnameentry.grid(row=2, column=1)

#email
email=tk.Label(root, text='email ')
email.grid(row=3, column=0)

emailentry=tk.Entry(root)
emailentry.grid(row=3, column=1)

#password
password=tk.Label(root, text='Password')
password.grid(row=4, column=0)

passwordentry=tk.Entry(root)
passwordentry.grid(row=4, column=1)

#repeat password
repeatpassword=tk.Label(root, text='Repeat Password')
repeatpassword.grid(row=5, column=0)

repeatpasswordentry=tk.Entry(root)
repeatpasswordentry.grid(row=5, column=1)

#phone number 
phone=tk.Label(root, text='Phone Number')
phone.grid(row=6, column=0)

phoneentry=tk.Entry(root)
phoneentry.grid(row=6, column=1)

# create a frame to hold the buttons

login=tk.Button(root, text='login')
login.grid(row=7, column=0)


register=tk.Button(root, text='Register')
register.grid(row=7, column=1)

exit=tk.Button(root, text='Exit', command=exit)
exit.grid(row=7, column=2)


root.mainloop()
