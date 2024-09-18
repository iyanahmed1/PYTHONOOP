import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error
from dbconnect import connect_db
root=tk.Tk()
root.geometry('300x300')
root.resizable(False,False)
root.title('Login Form')

def exit():
    """
    Closes the main window and exits the program.

    This function is called by the 'Exit' button.
    """
    root.destroy()


#define a function of login
def login():
    username=userentry.get()
    password=passwordentry.get()
    try:
    #setup connection to db
        db=connect_db()
        if db:
            cursor=db.cursor()
            cursor.execute('SELECT * FROM registration WHERE user=%s AND Password=%s', (username, password)) 
            result= cursor.fetchone()

        if result:
            messagebox.showinfo('Login Success','Welcome {}'.format(username))
        else:
            messagebox.showinfo('Login failed','Invalid Username or Password')
    except Error as e:
        messagebox.showerror('Database Error',f'Database Connection failed!!:{e}')
    finally:
        db.close()
    

#username and password field
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

login=tk.Button(root, text='login', command= login)
login.grid(row=3, column=0)

register=tk.Button(root, text='register',command='Register')
register.grid(row=3, column=1)

exit=tk.Button(root, text='Exit', command=exit)
exit.grid(row=3, column=2)
root.mainloop()