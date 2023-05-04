from flask_restful import Resource,reqparse,abort,request
from models.adminModel import Admin
from database.adminDB import AdminDB
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

# initiating userDatabseFunctions
adminDatabaseFunctions = AdminDB()


class AdminRegistration(Resource):
    def post(self):
        # parser for registration
        parser = reqparse.RequestParser()
        parser.add_argument('username',help='This field cannot be blank',required = True)
        parser.add_argument('password',help='This field cannot be blank',required = True)
        data = parser.parse_args()
        new_admin = Admin(username=data['username'],password=data['password'])
        id = adminDatabaseFunctions.add_Admin(admin=new_admin)
        if id != False:
            return {"message":"Admin Registered","id":id}
        return {'message':"Admin already Exists"},400
        
class AdminLogin(Resource):
    def post(self):
        # parser for login
        parser = reqparse.RequestParser()
        parser.add_argument('username',help='This field cannot be blank',required = True)
        parser.add_argument('password',help='This field cannot be blank',required = True)
        data = parser.parse_args()
        admin_db = adminDatabaseFunctions.get_AdminbyUsername(username= data['username'])
        if admin_db != None:
            if(admin_db.username==data['username'] and admin_db.password==data['password']):
                token = create_access_token(identity=data['username'],expires_delta=timedelta(hours=8))
                return {'message':"User Login","token":token},200
            else:
                return {'message':"Wrong Credentials"},401
        return {'message':"User doesn't exist"},401
