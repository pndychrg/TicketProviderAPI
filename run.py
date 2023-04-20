from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database.db import init_Database

#init
app = Flask(__name__)
app.config['JWT_SECRET_KEY']="flask_api_for_ticket_provider"
jwt = JWTManager(app)
import views

api = Api(app)
from resources.user import *
api.add_resource(UserLogin,'/login')
api.add_resource(UserRegistration,'/register')
api.add_resource(UserLogoutAccess,'/logout')
api.add_resource(TokenRefresh,'/token/refresh')

from resources.admin import *
api.add_resource(AdminLogin,'/admin/login')
api.add_resource(AdminRegistration,'/admin/register')

from resources.venue import *
api.add_resource(AddVenue,'/venue/addVenue')
api.add_resource(GetAllVenue,'/venue/getAllVenues')

if __name__ == "__main__":
    init_Database()
    app.run(debug=True)