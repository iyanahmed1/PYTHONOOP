from tkinter import messagebox
import mysql
import mysql.connector
from mysql.connector import Error
class Databaseconnection:
    def file_db():
        try:
            return mysql.connector.connect(
            host= 'localhost',
            user=  'root' ,
            database= 'finance_tracker'
    )
        except Error as e:
            messagebox.showerror('Database Error',f'Database Connection Failed!!!:{e}')
        return None
    
"""def register_user():
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
        messagebox.showerror('Password error',f'Password too short')"""
    

class CRUDoperations:
    def __init__(self,dbconnect):
        self.dbconnect=dbconnect

    def create(self, query,data):
        try
            cursor=self.dbconnect.
        





