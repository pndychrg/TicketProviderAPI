import sqlite3
from sqlite3 import Error
from models.venueModel import Venue


class VenueDB:
    def create_venueTable(self):
        create_venue_table = '''CREATE TABLE IF NOT EXISTS venues(
                            venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            place TEXT NOT NULL,
                            capacity INTEGER NOT NULL
                            );'''
    # CONNECTING THE DATABASE 
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(create_venue_table)
            conn.commit()
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()
 
    def getVenueByName(self,venue_name):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM venues WHERE name = ?",(venue_name,))
            row = cur.fetchone()
            return row
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()
    
    def addVenue(self,venue):
        add_venue_query = '''INSERT INTO venues(name,place,capacity) VALUES(?,?,?)'''
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(add_venue_query,venue.returnSet())
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def getAllVenues(self,):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM venues")
            rows = cur.fetchall()
            return Venue.fromList(listVenues=rows)
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()
