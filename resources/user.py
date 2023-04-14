from flask_restful import Resource,reqparse,abort
from models.userModel import User
from database.userDB import UserDatabaseFunctions


parser = reqparse.RequestParser()
parser.add_argument('name',help='This field cannot be blank',required = True)
parser.add_argument('username',help='This field cannot be blank',required = True)
parser.add_argument('password',help='This field cannot be blank',required = True)

# initiating userDatabseFunctions
userDatabaseFunctions = UserDatabaseFunctions()


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = User(id=None,name=data['name'],username=data['username'],password=data['password'])
        id = userDatabaseFunctions.add_User(user=new_user)
        if id != False:
            return {"id":id}
        return {'message':"User already Exists"},400
        
class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message':"User Login"}
    
class UserLogoutAccess(Resource):
    def post(self):
        return {'message':"User Logout"}
    
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}