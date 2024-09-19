import tkinter as tk
import mysql.connector 
from mysql.connector import Error
from tkinter import messagebox

#from formconnect import connect_db

def connect_db():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            database='Form'
        )
    except Error as e:
        messagebox.showerror('Database Failed',f'Database Connection')
        return None


#register user 
def register_person():
    Firstname=Fnameentry.get()
    Lastname=Lnameentry.get()
    Email=emailentry.get()
    Mobile=mobileentry.get()
    Gender=gender.get()
    dob=dobentry.get()
    password=passwordentry.get()
    confirm_password=confirmpassentry.get()

    if password != confirm_password:
        messagebox.showerror('Password Error',f'Password Mismatch')

    else:
        try:
            db=connect_db()
            cursor=db.cursor()
            sql='insert INTO details (Firstname,Lastname,Email,Mobile,Gender, dob,password) values(%s,%s,%s,%s,%s,%s,%s)'
            val=(Firstname,Lastname,Email,Mobile,Gender, dob,password)
            cursor.execute(sql,val)
            db.commit()
            messagebox.showinfo('Successful',f'Registration Successful')
        except Error as er:
            messagebox.showerror('Unsuccessful',f'Registration Unsucceful:{er}')
            cursor.close()
        finally:
            db.close()

#creating the window
root=tk.Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Registration Form')
root.configure(bg='light grey')

#title
title=tk.Label(root, text='Registrartion Form',font=('Arial',20),bg='light grey', fg='dark red')
title.grid(row=0, column=1, columnspan=2, pady=10,padx=10)
#first name(label) and entry
FirstName=tk.Label(root,text='First Name' ,bg='light grey',fg='black')
FirstName.grid(row=1, column=0, pady=10, padx=10)

Fnameentry=tk.Entry(root)
Fnameentry.grid(row=1, column=1, pady=10, padx=10)

#second name
LastName=tk.Label(root, text='Last Name',bg='light grey',fg='black')
LastName.grid(row=1, column=2, pady=10, padx=10)

Lnameentry=tk.Entry(root)
Lnameentry.grid(row=1 ,column=3, pady=10, padx=10)

#email
email=tk.Label(root,text='Email',bg='light grey',fg='black')
email.grid(row=2, column=0, pady=10, padx=10)

emailentry=tk.Entry(root)
emailentry.grid(row=2, column=1,pady=10, padx=10)

#mobile
mobile=tk.Label(root, text='Mobile',bg='light grey',fg='black')
mobile.grid(row=3 ,column=0, pady=10, padx=10)

mobileentry=tk.Entry(root)
mobileentry.grid(row=3,column=1, pady=10, padx=10)

#gender
gender=tk.StringVar
gender=tk.Label(root, text='Gender',bg='light grey',fg='black')
gender.grid(row=4, column=0, pady=10, padx=10)

gender=tk.Radiobutton(root, text='male', variable=gender, value='Male',bg='light grey',fg='black')
gender.grid(row=4, column=1, pady=10, padx=10)

gender=tk.Radiobutton(root, text='Female', variable=gender, value='Female',bg='light grey',fg='black')
gender.grid(row=4 , column=2, pady=10, padx=10)

#date of birth
dob=tk.Label(root ,text='Date of Birth',bg='light grey',fg='black')
dob.grid(row=5 ,column=0, pady=10, padx=10)

dobentry=tk.Entry(root)
dobentry.grid(row=5 ,column=1, pady=10, padx=10)

#password
password=tk.Label(root,text='Password',bg='light grey',fg='black')
password.grid(row=6 ,column=0, pady=10, padx=10)

passwordentry=tk.Entry(root ,show='*')
passwordentry.grid(row=6, column=1, pady=10, padx=10)

#confirm password
confirmpassword=tk.Label(root, text='Confirm Password',bg='light grey',fg='black')
confirmpassword.grid(row=7 ,column=0, pady=10, padx=10)

confirmpassentry=tk.Entry(root ,show='*')
confirmpassentry.grid(row=7 ,column=1, pady=10, padx=10)

#submit button
submit=tk.Button(root, text='SUBMIT', font=("Arial",8) ,bg='Red' ,fg= 'black', command=register_person)
submit.grid(row=8 ,column=1, pady=10, padx=10)

root.mainloop()