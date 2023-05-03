import sqlite3
from sqlite3 import Error
from models.ticketsModel import Tickets

class TicketsDB:
    def create_ticketTable(self):
        create_tickets_table = '''CREATE TABLE IF NOT EXISTS tickets(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                show_id INTEGER NOT NULL,
                                numOfTickets INTEGER NOT NULL,
                                FOREIGN KEY(user_id) REFERENCES users(user_id),
                                FOREIGN KEY(show_id) REFERENCES shows(show_id)
        );'''

         # CONNECTING THE DATABASE 
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(create_tickets_table)
            conn.commit()
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def create_trigger(self):
        # Connect to the database
        conn = sqlite3.connect('ticketProvider.db')

        # Create the trigger
        conn.execute('''
            CREATE TRIGGER IF NOT EXISTS prevent_overbooking
            BEFORE INSERT ON tickets
            FOR EACH ROW
            WHEN (
                SELECT bookedSeats
                FROM shows
                WHERE show_id = NEW.show_id
            ) >= (
                SELECT capacity
                FROM venues
                WHERE venue_id = (
                    SELECT venue_id
                    FROM shows
                    WHERE show_id = NEW.show_id
                )
            )
            BEGIN
                SELECT RAISE(ABORT, 'Cannot book more tickets than the venue capacity allows');
            END;
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def addTicket(self,ticket):
        add_ticket_query = '''INSERT INTO tickets(user_id,show_id,numOfTickets) VALUES (?,?,?)'''
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute(add_ticket_query,ticket.returnSet())
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def getAllTickets(self):
        try:
            # connnect
            conn =  sqlite3.connect("ticketProvider.db")
            cur =  conn.cursor()
            cur.execute("SELECT * FROM tickets")
            rows = cur.fetchall()
            return Tickets.fromList(listTickets=rows)
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()