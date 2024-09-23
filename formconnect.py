import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
def connect_db():
    try:
        return mysql.connector(
            host='localhost',
            user='root',
            database='Form'
        )
    except Error as e:
        messagebox.showerror('Database Failed',f'Database Connection')


        