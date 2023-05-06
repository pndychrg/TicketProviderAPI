from flask_jwt_extended import create_access_token
from flask_restful import Resource,reqparse,abort,request
from models.userModel import User
from database.userDB import UserDatabaseFunctions
from flask import jsonify
import jwt
from functools import wraps
from run import app
from datetime import timedelta
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
                token = create_access_token(identity=data['username'],expires_delta=timedelta(hours=8))
                return {'message':"User Login","token":token},200
            else:
                return {'message':"Wrong Credentials"},401
        return {'message':"User doesn't exist"},401
    

class DeleteUser(Resource):
    def delete(self):
        # getting user_id as a parameter
        user_id = request.args.get("user_id")
        if user_id !=None:
            result = UserDatabaseFunctions.deleteUserByUserId(user_id = user_id)
            if result ==True:
                return {"message":"User Deleted"},200
        else:
            return {"message":"user_id not found"},404

class UserLogoutAccess(Resource):
    def post(self):
        return {'message':"User Logout"}
    
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}