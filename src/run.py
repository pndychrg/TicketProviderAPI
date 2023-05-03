from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database.db import init_Database
# from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'

#init
app = Flask(__name__)
app.config['JWT_SECRET_KEY']="flask_api_for_ticket_provider"
jwt = JWTManager(app)

# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )

# app.register_blueprint(swaggerui_blueprint)
# #Now point your browser to localhost:5000/api/docs/
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

from resources.show import *
api.add_resource(AddShow,'/show/addShow')
api.add_resource(GetAllShows,'/show/getAllShows')

from resources.tickets import *
api.add_resource(AddTicket,'/ticket/addTicket')
api.add_resource(GetAllTickets,'/ticket/getAllTickets')

if __name__ == "__main__":
    init_Database()
    app.run(debug=True)