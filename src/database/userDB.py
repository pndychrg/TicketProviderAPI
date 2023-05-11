import sqlite3
from sqlite3 import Error
import os
from models.userModel import User

class UserDatabaseFunctions :
    # create User Table
    def createUserTable(self):
        user_table_query = '''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            username TEXT NOT NULL, 
                            password TEXT NOT NULL
        );
        '''

        # CONNECTING THE DATABASE 
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(user_table_query)
            cur.execute("PRAGMA foreign_keys = ON;")
            conn.commit()
        except Error as e:
            print(e)

    def check_UserExists(self,username):
        sql = "SELECT * FROM users WHERE username = ?"
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
    
    def add_User(self,user):
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            if  self.check_UserExists(user.username) != True:
                add_user_query = '''INSERT INTO users(name,username,password) VALUES (?,?,?)'''
                user_values = (user.name, user.username, user.password)
                cur.execute(add_user_query,user_values)
                conn.commit()
                print("user added")
                return cur.lastrowid
            else:
                print("user not added")
                return False
        except Error as e:
            print(e)

    def get_UserbyUsername(self,username):
        sql = "SELECT * FROM users WHERE username = ?"
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(sql,(username,))
            row = cur.fetchone()
            if row != None:
                user = User(name=row[1],username=row[2],password=row[3])
                return user
            else:
                return None
        
        except Error as e:
            print(e)

    def deleteUserByUserId(user_id):
        sql = "DELETE FROM users WHERE user_id = ?"
        try:
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(sql,(user_id,))
            conn.commit()
            return True
        except Error as e:
            print(e)
            return False
        finally:
            cur.close()
            conn.close()

    def updateUserByUserId(user,user_id):
        sql = '''UPDATE users
            SET name = ?,
            username = ?
            WHERE user_id = ?;
            '''
        try:
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            cur.execute(sql,(user.name,user.username,user_id))
            conn.commit()
            return True
        except Error as e:
            print(e)
            return False
        finally:
            cur.close()
            conn.close()
