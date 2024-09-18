#set up the database connection
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
def connect_db():
    #to prevent the system from crassing
    # enclose in a try finally block
    try:
        return mysql.connector.connect(
        host= 'localhost',
        user=  'root' ,
        database= 'retail'
    )
    except Error as e:
        messagebox.showerror('Database Error',f'Database Connection Failed!!!:{e}')
        return None