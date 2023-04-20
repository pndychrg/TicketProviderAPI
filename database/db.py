from database.showsDB import ShowsDB
from database.userDB import UserDatabaseFunctions
from database.adminDB import AdminDB
from database.venueDB import VenueDB
from models.venueModel import Venue

def init_Database():
    userDatabaseFunctions = UserDatabaseFunctions()
    userDatabaseFunctions.createUserTable()
    adminDatabaseFunctions = AdminDB()
    adminDatabaseFunctions.createAdminTable()
    venueDatabaseFunctions = VenueDB()
    venueDatabaseFunctions.create_venueTable()
    showDatabaseFunctions = ShowsDB()
    showDatabaseFunctions.create_showTable()