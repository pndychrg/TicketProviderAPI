from database.userDB import UserDatabaseFunctions

def init_Database():
    userDatabaseFunctions = UserDatabaseFunctions()
    userDatabaseFunctions.createUserTable()