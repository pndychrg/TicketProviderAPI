from flask_restful import Resource,reqparse,abort,request
from models.userModel import User
from database.userDB import UserDatabaseFunctions
from flask import jsonify
import jwt
from functools import wraps
from run import app
# initiating userDatabseFunctions
userDatabaseFunctions = UserDatabaseFunctions()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = userDatabaseFunctions.get_UserbyUsername(username=data['username'])
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
    return decorated

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
            return {"message":"User Registered","id":id}
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
            if(user_db.username==data['username'] and user_db.password==data['password']):
                token = jwt.encode({'username':user_db.username},app.config['SECRET_KEY'])
                return {'message':"User Login","token":token},200
            else:
                return {'message':"Wrong Credentials"},401
        return {'message':"User doesn't exist"},401
    
class UserLogoutAccess(Resource):
    def post(self):
        return {'message':"User Logout"}
    
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}