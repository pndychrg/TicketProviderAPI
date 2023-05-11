import sqlite3
from sqlite3 import Error
from models.ticketsModel import Tickets
from database.showsDB import ShowsDB
from database.venueDB import VenueDB


class TicketsDB:
    def create_ticketTable(self):
        create_tickets_table = '''CREATE TABLE IF NOT EXISTS tickets(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                show_id INTEGER NOT NULL,
                                venue_id INTEGER NOT NULL,
                                numOfTickets INTEGER NOT NULL,
                                FOREIGN KEY(user_id) REFERENCES users(user_id),
                                FOREIGN KEY(show_id) REFERENCES shows(show_id),
                                FOREIGN KEY(venue_id) REFERENCES venues(venue_id)
        );'''

        # CONNECTING THE DATABASE
        try:
            # connnect
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            cur.execute(create_tickets_table)
            conn.commit()
        except Error as e:
            print(e)
            return None
        finally:
            conn.close()

    def create_triggers(self):
        # Connect to the database
        conn = sqlite3.connect('ticketProvider.db')
        conn.execute('''CREATE TRIGGER IF NOT EXISTS update_booked_seats
                        AFTER INSERT ON tickets
                        FOR EACH ROW
                        BEGIN
                            UPDATE shows
                            SET bookedSeats = (
                                SELECT SUM(numOfTickets)
                                FROM tickets
                                WHERE show_id = NEW.show_id
                            )
                            WHERE show_id = NEW.show_id;
                    END;
                    ''')
        conn.execute('''CREATE TRIGGER IF NOT EXISTS set_show_full AFTER INSERT ON tickets
                    BEGIN
                        UPDATE shows SET isFull = 1 WHERE
                            show_id = NEW.show_id AND
                            (SELECT SUM(numOfTickets) FROM tickets WHERE show_id = NEW.show_id) = 
                            (SELECT capacity FROM venues WHERE venue_id = NEW.venue_id);
                    END;''')
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def addTicket(self, ticket):
        # getting total number of bookedSeats already
        bookedSeats = ShowsDB.getBookedSeats(show_id = ticket.show_id)

        capacity = VenueDB.getVenueCapacity(venue_id=ticket.venue_id)
        if int(bookedSeats)+int(ticket.numOfTickets) > int(capacity):
            return None
       # capacity = VenueDB.getVenueCapacity(venue_id=)
        try:
            # connnect
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            add_ticket_query = '''INSERT INTO tickets(user_id,show_id,venue_id,numOfTickets) VALUES (?,?,?,?)'''
            cur.execute(add_ticket_query, ticket.returnSet())
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
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM tickets")
            rows = cur.fetchall()
            return Tickets.fromList(listTickets=rows)
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()

    def getAllTicketsByUserId(user_id):
        try:
            # connnect
            conn = sqlite3.connect("ticketProvider.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM tickets WHERE user_id = ?",(user_id,))
            rows = cur.fetchall()
            return Tickets.fromList(listTickets=rows)
        except Error as e:
            print(e)
            return None
        finally:
            cur.close()
            conn.close()

    # def deleteTicketByTicketId(ticket_id):
    #     sql = "DELETE FROM tickets WHERE ticket_id = ?"
    #     try:
    #         conn =  sqlite3.connect("ticketProvider.db")
    #         cur =  conn.cursor()
    #         cur.execute(sql,(ticket_id,))
    #         conn.commit()
    #         return True
    #     except Error as e:
    #         print(e)
    #         return False
    #     finally:
    #         cur.close()
    #         conn.close()
