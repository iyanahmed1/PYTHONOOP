import tkinter as tk
import mysql.connector 


#register user 
def register_person():
    FirstName=Fnameentry.get()
    LastName=Lnameentry.get()
    Email=emailentry.get()
    Mobile=mobileentry.get()
    Gender=genderentry.get()
    dob=dobentry.get()
    password=passwordentry.get()
    confirm_password=confirmpassentry.get()

#first name(label) and entry
FirstName=tk.Label(root,text='First Name')
FirstName.grid(row=0, column=0)

Fnameentry=tk.Entry(root)
Fnameentry.grid(row=0, column=1)

#second name
LastName=tk.Label(root, text='Last Name')
LastName.grid(row=0, column=2)

Lnameentry=tk.Entry(root)
Lnameentry.grid(row=0 ,column=3)

#email
Email=tk.Label(root,text='Email')
Email.grid(row=2, column=0)

emailentry=tk.Entry(root)
emailentry.grid(row=2, column=1)

#mobile
Mobile=tk.Label(root, text='Mobile')
Mobile.grid(row=3 ,column=0)

mobileentry=tk.Entry(root)
mobileentry.grid(row=3,column=1)

#gender
Gender=tk.Label(root, text='Gender')
Gender.grid(row=4, column=0)

genderentry=tk.Radiobutton(root, text='male', variable=Gender, value='Male')
genderentry.grid(row=5, column=1)

genderentry=tk.Radiobutton(root, text='Female', variable=Gender, value='Female')
genderentry.grid(row=5 , column=2)

#date of birth
dob=tk.Label(root ,text='Date of Birth')
dob=
dobentry=tk.Entry(root)
dobentry.grid(row=)