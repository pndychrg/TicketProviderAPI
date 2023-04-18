from database.userDB import UserDatabaseFunctions
from database.adminDB import AdminDatabaseFunctions

def init_Database():
    userDatabaseFunctions = UserDatabaseFunctions()
    userDatabaseFunctions.createUserTable()
    adminDatabaseFunctions = AdminDatabaseFunctions()
    adminDatabaseFunctions.createAdminTable()