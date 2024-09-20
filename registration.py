# create a tkinker window with the following fields
#username
# email, password, phone number
# login button 
#registration button
#exit button

#create a login page containing username and password fields
#login, registartio and exit buttom

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#from tkcalendar import Calendar
from validate_email import validate_email
from dbconnect import connect_db
from mysql.connector import Error

#set up the database connection

#define the function to register the user
def register_user():
    user=userentry.get()
    FName=fnameentry.get()
    SName=surnameentry.get()
    Email=emailentry.get()
    Password=passwordentry.get()
    Repassword=repeatpasswordentry.get()
    Gender=gender_var()
    dob=(f"{dob_day.get()},{dob_month.get()},{dob_year.get()}")
    Phone=phoneentry.get()

    if Repassword!=Password:
        messagebox.showerror('Password Error',f'Password Mismatch')
    elif len(Password)<8:
        messagebox.showerror('Password error',f'Password too short')
    elif validate_email(Email)==False:
        messagebox.showinfo('invalid Email',f'Invalid Email. Try again')

    else:
        try:
            db=connect_db()
            cursor=db.cursor()
            sql='insert into registration(user,FName,SName,dob,Gender,Email,Password,Phone) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            val=(user,FName,SName,Gender,dob,Email,Password,Phone)
            cursor.execute(sql,val)
            db.commit()
            result=messagebox.askquestion('Registration Successful','Add new record?')
            if result=='no':
                root.destroy()
            else:
                userentry.destroy(0,tk.END)
                fnameentry.destroy(0,tk.END)
                surnameentry.destroy(0,tk.END)
                emailentry.destroy(0,tk.END)
                passwordentry.destroy(0,tk.END)
                repeatpasswordentry.destroy(0,tk.END)
                phoneentry.destroy(0,tk.END)
                gender_var.set(None)

        except Error as e:
            messagebox.showerror('Database Error',f'Data Could not be saved!')
            cursor.close()#close the database connection
        finally:
            db.close()


root=tk.Tk()
root.geometry('600x300')
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

#date of birth
dob=tk.Label(root ,text='Date of Birth')
dob.grid(row=3 ,column=0, pady=10, padx=10)

day=[str(i)for i in range(1,32)]
dob_day=ttk.Combobox(root,values=day)
dob_day.grid(row=3 ,column=1, pady=10, padx=10)


month=[str(i)for i in range(1,13)]
dob_month=ttk.Combobox(root,values=month)
dob_month.grid(row=3,column=2 ,pady=10, padx=10)

year=[str(i)for i in range(1900,2025)]
dob_year=ttk.Combobox(root,values=year)
dob_year.grid(row=3,column=3, pady=10, padx=10)


#gender
gender_var=tk.StringVar()
gender_var.set(None)
gender_label=tk.Label(root, text='Gender')
gender_label.grid(row=4,column=0)

male=tk.Radiobutton(root, text='Male', variable=gender_var, value='Male')
male.grid(row=4, column=1)

female=tk.Radiobutton(root, text='Female', variable=gender_var, value='Female')
female.grid(row=4, column=2)

rathernotsay=tk.Radiobutton(root, text='Rather Not Say', variable=gender_var, value='Rather not say')
rathernotsay.grid(row=4, column=3)

#email
email=tk.Label(root, text='email ')
email.grid(row=5, column=0)

emailentry=tk.Entry(root)
emailentry.grid(row=5, column=1)

#password
password=tk.Label(root, text='Password')
password.grid(row=6, column=0)

passwordentry=tk.Entry(root)
passwordentry.grid(row=6, column=1)

#repeat password
repeatpassword=tk.Label(root, text='Repeat Password')
repeatpassword.grid(row=7, column=0)

repeatpasswordentry=tk.Entry(root)
repeatpasswordentry.grid(row=7, column=1)

#phone number 
phone=tk.Label(root, text='Phone Number')
phone.grid(row=8, column=0)

phoneentry=tk.Entry(root)
phoneentry.grid(row=8, column=1)

# create a frame to hold the buttons

login=tk.Button(root, text='login')
login.grid(row=9, column=0)


register=tk.Button(root, text='Register', command=register_user)
register.grid(row=9, column=1)

exit=tk.Button(root, text='Exit', command=exit)
exit.grid(row=9, column=2)


root.mainloop()

