import sqlite3
from sqlite3 import Error
from models.showModel import Show

class ShowsDB:
    def create_showTable():
        # tags not implemented yet 
        #TODO: add tags
        create_show_table = '''CREATE TABLE IF NOT EXISTS shows(
                            show_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            rating INTEGER NOT NULL,
                            ticketPrice INTEGER NOT NULL
                            );'''
    
        # CONNECTING THE DATABASE 
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(create_show_table)
            conn.commit()
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def getShowByName(self,show_name):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM shows WHERE name = ?",(show_name,))
            row = cur.fetchone()
            return Show.fromArray(row=row)
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()
    
    def addShow(self,show):
        add_venue_query = '''INSERT INTO shows(name,rating,ticketPrice) VALUES(?,?,?)'''
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(add_venue_query,show.returnSet())
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def getAllShows(self,):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM shows")
            rows = cur.fetchall()
            return Show.fromList(listShows=rows)
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()


