import json
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource,reqparse,abort,request
from models.userModel import User
from database.userDB import UserDatabaseFunctions
from datetime import timedelta
# initiating userDatabseFunctions
userDatabaseFunctions = UserDatabaseFunctions()



class UserRegistration(Resource):
    def options(self):
        response = jsonify({'message': 'Preflight request accepted.'})
        #response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    def post(self):
        # # parser for registration
        # parser = reqparse.RequestParser()
        # parser.add_argument('name',help='This field cannot be blank',required = True)
        # parser.add_argument('username',help='This field cannot be blank',required = True)
        # parser.add_argument('password',help='This field cannot be blank',required = True)

        # data = parser.parse_args()
        data = request.get_json()
        if isinstance(data, str):
            # If the data is a string, attempt to parse it as JSON
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                return {'message': 'Invalid JSON data in the request body'}, 400

        print(data,flush=True)
        if 'name' not in data or 'username' not in data or 'password' not in data:
            return {'message': 'Missing required fields in the request body'}, 400
        print(data["name"],flush=True)
        new_user = User(name=data['name'],username=data['username'],password=data['password'])
        id = userDatabaseFunctions.add_User(user=new_user)
        if id != False:
            return {"message":"User Registered","id":id}, 200
            # , {'Access-Control-Allow-Origin': 'http://localhost:3000'}
           # return json.dumps("User Registered"),200
        return {'message':"User already Exists"},400
        
class UserLogin(Resource):
    def post(self):
        # # parser for login
        # parser = reqparse.RequestParser()
        # parser.add_argument('username',help='This field cannot be blank',required = True)
        # parser.add_argument('password',help='This field cannot be blank',required = True)
        # data = parser.parse_args()
        data = request.get_json()
        # if isinstance(data, str):
        #     # If the data is a string, attempt to parse it as JSON
        #     try:
        #         data = json.loads(data)
        #     except json.JSONDecodeError:
        #         return {'message': 'Invalid JSON data in the request body'}, 400
        data = json.load(data)
        if "username" not in data or "password" not in data:
            return {'message': 'Missing required fields in the request body'}, 400
        print(data,flush=True)
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
    
class UpdateUserByUserId(Resource):
    @jwt_required()
    def put(self):
        # getting user_id as a parameter
        user_id = request.args.get("user_id")
        # getting user in body of the request
        parser = reqparse.RequestParser()
        parser.add_argument('name',help='This field cannot be blank',required = True)
        parser.add_argument('username',help='This field cannot be blank',required = True)
        data = parser.parse_args()
        if user_id !=None:
            user = User(name=data['name'],username=data['username'],password = None,id=None)
            result = UserDatabaseFunctions.updateUserByUserId(user=user, user_id = user_id)
            if result ==True:
                return {"Message":"User Updated"},200
            else:
                return {"Message":"Error Occured"},404
        else:
            return {"Message":"user_id not found"},404


class UserLogoutAccess(Resource):
    def post(self):
        return {'message':"User Logout"}
    
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}