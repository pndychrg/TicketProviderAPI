from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database.db import init_Database
from flask_cors import CORS
# from flask_swagger_ui import get_swaggerui_blueprint

# SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# API_URL = 'http://petstore.swagger.io/v2/swagger.json'

#init
app = Flask(__name__)
app.config['JWT_SECRET_KEY']="flask_api_for_ticket_provider"
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000/"}})


api = Api(app)
from resources.user import *
api.add_resource(UserLogin,'/login')
api.add_resource(UserRegistration,'/register')
api.add_resource(DeleteUser,'/delete')
api.add_resource(UpdateUserByUserId,'/update')
api.add_resource(UserLogoutAccess,'/logout')
api.add_resource(TokenRefresh,'/token/refresh')

from resources.admin import *
api.add_resource(AdminLogin,'/admin/login')
api.add_resource(AdminRegistration,'/admin/register')
api.add_resource(DeleteAdmin,'/admin/delete')

from resources.venue import *
api.add_resource(AddVenue,'/venue/addVenue')
api.add_resource(GetAllVenue,'/venue/getAllVenues')
api.add_resource(DeleteVenueById,'/venue/deleteVenue')
api.add_resource(UpdateVenueByeVenueId,'/venue/updateVenue')

from resources.show import *
api.add_resource(AddShow,'/show/addShow')
api.add_resource(GetAllShows,'/show/getAllShows')
api.add_resource(GetShowsByVenueId,'/show/getShowsByVenueId')
api.add_resource(DeleteShowByShowId,'/show/deleteShow')
api.add_resource(UpdateShowByShowId,'/show/updateShow')

from resources.tickets import *
api.add_resource(AddTicket,'/ticket/addTicket')
api.add_resource(GetAllTickets,'/ticket/getAllTickets')
api.add_resource(GetTicketsByUserId,'/ticket/getTicketsByUserId')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  print("origin added",flush=True)
  return response


if __name__ == "__main__":
    init_Database()
    app.run(host='127.0.0.1',port=8080,debug=True)