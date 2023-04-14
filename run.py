from flask import Flask
from flask_restful import Api
from resources.user import *
from database.db import init_Database

#init
app = Flask(__name__)
import views
api = Api(app)

api.add_resource(UserLogin,'/login')
api.add_resource(UserRegistration,'/register')
api.add_resource(UserLogoutAccess,'/logout')
api.add_resource(TokenRefresh,'/token/refresh')


if __name__ == "__main__":
    init_Database()
    app.run(debug=True)