from flask_restful import Resource,reqparse,abort
from models.userModel import User
from database.userDB import UserDatabaseFunctions


# initiating userDatabseFunctions
userDatabaseFunctions = UserDatabaseFunctions()


class UserRegistration(Resource):
    def post(self):
        # parser for registration
        parser = reqparse.RequestParser()
        parser.add_argument('name',help='This field cannot be blank',required = True)
        parser.add_argument('username',help='This field cannot be blank',required = True)
        parser.add_argument('password',help='This field cannot be blank',required = True)

        data = parser.parse_args()
        new_user = User(name=data['name'],username=data['username'],password=data['password'])
        id = userDatabaseFunctions.add_User(user=new_user)
        if id != False:
            return {"id":id}
        return {'message':"User already Exists"},400
        
class UserLogin(Resource):
    def post(self):
        # parser for login
        parser = reqparse.RequestParser()
        parser.add_argument('username',help='This field cannot be blank',required = True)
        parser.add_argument('password',help='This field cannot be blank',required = True)
        data = parser.parse_args()
        user_db = userDatabaseFunctions.get_UserbyUsername(username= data['username'])
        if user_db != None:
            print(data,flush=True)
            print(user_db.password,flush=True)
            if(user_db.username==data['username'] and user_db.password==data['password']):
                return {'message':"User Login"},200
            else:
                return {'message':"Wrong Credentials"},401
        return {'message':"User doesn't exist"},401
    
class UserLogoutAccess(Resource):
    def post(self):
        return {'message':"User Logout"}
    
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}