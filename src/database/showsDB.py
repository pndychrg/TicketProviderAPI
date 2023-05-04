import sqlite3
from sqlite3 import Error
from models.showModel import Show

class ShowsDB:
    def create_showTable(self):
        # tags not implemented yet 
        #TODO: add tags
        create_show_table = '''CREATE TABLE IF NOT EXISTS shows(
                            show_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            rating INTEGER NOT NULL,
                            ticketPrice INTEGER NOT NULL,
                            bookedSeats INTEGER NOT NULL,
                            isFull INTEGER NOT NULL,
                            venue_id INTEGER NOT NULL,
                            FOREIGN KEY(venue_id) REFERENCES venues(venue_id)
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

    def getShowByVenueId(self,venue_id):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM shows WHERE venue_id = ?",(venue_id,))
            rows = cur.fetchall()
            return Show.fromList(listShows=rows)
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()
    
    def addShow(self,show):
        add_show_query = '''INSERT INTO shows(name,rating,ticketPrice,bookedSeats,isFull,venue_id) VALUES(?,?,?,?,?,?)'''
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(add_show_query,show.returnSet())
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

    def getBookedSeats(show_id):
        try:
            #connect 
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            cur.execute("SELECT bookedSeats FROM shows WHERE show_id = ?",(show_id,))
            bookedSeats = cur.fetchone()[0]
            return bookedSeats
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()

