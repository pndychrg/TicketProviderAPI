from flask_restful import Resource,reqparse
from models.adminModel import Admin
from database.adminDB import AdminDB
from flask_restful import request
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import jsonify
import json

# initiating userDatabseFunctions
adminDatabaseFunctions = AdminDB()


class AdminRegistration(Resource):
    def options(self):
        response = jsonify({'message': 'Preflight request accepted.'})
        #response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    def post(self):
        # parser for registration
        # parser = reqparse.RequestParser()
        # parser.add_argument('username',help='This field cannot be blank',required = True)
        # parser.add_argument('password',help='This field cannot be blank',required = True)
        # data = parser.parse_args()
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return {'message': 'Invalid JSON data in the request body'}, 400
        if "username" not in data or "password" not in data:
            return {'message':'Invalid JSON '},400
        print(data,flush=True)
        new_admin = Admin(username=data['username'],password=data['password'])
        id = adminDatabaseFunctions.add_Admin(admin=new_admin)
        if id != False:
            return {"message":"Admin Registered","id":id}
        return {'message':"Admin already Exists"},400
        
class AdminLogin(Resource):
    def post(self):
        # parser for login
        # parser = reqparse.RequestParser()
        # parser.add_argument('username',help='This field cannot be blank',required = True)
        # parser.add_argument('password',help='This field cannot be blank',required = True)
        # data = parser.parse_args()

        if isinstance(data, str):
            # If the data is a string, attempt to parse it as JSON
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                return {'message': 'Invalid JSON data in the request body'}, 400

        admin_db = adminDatabaseFunctions.get_AdminbyUsername(username= data['username'])
        if admin_db != None:
            if(admin_db.username==data['username'] and admin_db.password==data['password']):
                token = create_access_token(identity=data['username'],expires_delta=timedelta(hours=8))
                return {'message':"User Login","token":token},200
            else:
                return {'message':"Wrong Credentials"},401
        return {'message':"User doesn't exist"},401
    
class DeleteAdmin(Resource):
    def delete(self):
        # getting admin_id as a parameter
        admin_id = request.args.get('admin_id')
        if admin_id!=None:
            result = AdminDB.deleteAdminByAdminId(admin_id=admin_id)
            if result ==True:
                return {"message":"Admin Deleted"},200
        else:
            return {'message':"admin_id not found"},404
        