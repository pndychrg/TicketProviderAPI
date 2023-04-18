import sqlite3
from sqlite3 import Error
import os
from models.adminModel import Admin

class AdminDatabaseFunctions :
    
    # create Admin Table
    def createAdminTable(self):
        admin_table_query = '''CREATE TABLE IF NOT EXISTS admin (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL, 
                            password TEXT NOT NULL
        );'''
        # CONNECTING THE DATABASE 
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(admin_table_query)
            conn.commit()
        except Error as e:
            print(e)

    def check_AdminExists(self,username):
        sql = "SELECT * FROM admin WHERE username = ?"
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(sql,(username,))
            rows = cur.fetchone()
            if rows !=None:
                return True
            else:
                return False
        except Error as e:
            print(e)
    
    def add_Admin(self,admin):
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            if  self.check_AdminExists(admin.username) != True:
                add_user_query = '''INSERT INTO admin(username,password) VALUES (?,?)'''
                user_values = (admin.username, admin.password)
                cur.execute(add_user_query,user_values)
                conn.commit()
                print("admin added")
                return cur.lastrowid
            else:
                print("admin not added")
                return False
        except Error as e:
            print(e)

    def get_AdminbyUsername(self,username):
        sql = "SELECT * FROM admin WHERE username = ?"
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(sql,(username,))
            row = cur.fetchone()
            if row != None:
                admin = Admin(username=row[1],password=row[2])
                return admin
            else:
                return None
        
        except Error as e:
            print(e)