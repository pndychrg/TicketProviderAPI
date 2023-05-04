from database.showsDB import ShowsDB
from database.userDB import UserDatabaseFunctions
from database.adminDB import AdminDB
from database.venueDB import VenueDB
from database.ticketDB import TicketsDB

def init_Database():
    userDatabaseFunctions = UserDatabaseFunctions()
    userDatabaseFunctions.createUserTable()
    adminDatabaseFunctions = AdminDB()
    adminDatabaseFunctions.createAdminTable()
    venueDatabaseFunctions = VenueDB()
    venueDatabaseFunctions.create_venueTable()
    showDatabaseFunctions = ShowsDB()
    showDatabaseFunctions.create_showTable()
    ticketDatabaseFunctions = TicketsDB()
    ticketDatabaseFunctions.create_ticketTable()
    ticketDatabaseFunctions.create_triggers()