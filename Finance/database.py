from tkinter import messagebox
import mysql
import mysql.connector
from mysql.connector import Error

class DatabaseConnection():
    def __init__(self, host='local host',user='root', database='finance_tracker'):
        self.host=host
        self.user=user
        self.database=database
        self.connection= None
    
    def connect(self):
        try:
            self.connection=mysql.connector.connect(
            host=self.host,
            user=self.user,
            database=self.database
        )
            print('Database connected successfully!')
        except Error as e:
            messagebox.showerror(f'error:{e}')

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            messagebox.showinfo('Database connection close.') 

    
class CRUDoperations:
    def __init__(self):
        self.connection=connection

    def create(self,query,values):
        cursor=self.connection.cursor()
        cursor.execute(query,values)
        self.connection.commit()

    def read(self,query):
        cursor=self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchhall()

    def update(self,query,values):
        cursor=self.connection.cursor()
        cursor.execute(query,values)
        self.connection.commit()

    def delete(self,query,values):
        cursor=self.connection.cursor()
        cursor.execute(query,values)
        self.connection.commit()



        
                                                                                                               




