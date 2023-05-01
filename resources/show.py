from flask_restful import Resource,reqparse,request
from flask_jwt_extended import jwt_required
from models.showModel import Show
from database.showsDB import ShowsDB

# init Database Functions
showsDB = ShowsDB()

class AddShow(Resource):
    @jwt_required()
    def post(self):
        # parser for adding show details
        parser = reqparse.RequestParser()
        parser.add_argument("name",help="This Field is mandatory",required = True)
        parser.add_argument("rating",help="This Field is mandatory",required = True)
        parser.add_argument("ticketPrice",help="This Field is mandatory",required = True)

        # extracting Data
        data = parser.parse_args()
        print(data,flush=True)
        new_show = Show(name=data['name'],rating=data['rating'],ticketPrice=data['ticketPrice'])
        id = showsDB.addShow(show=new_show)
        print(id,flush=True)
        if id!=None:
            return {'message':"Venue Added"}
        return {'message':"Error Occured"},404
    
#TODO get all shows by venue
class GetAllShows(Resource):
    @jwt_required()
    def get(self):
        showsList = showsDB.getAllShows()
        ret_Json = []
        for show in showsList :
            ret_Json.append(show.toJson())
        return ret_Json,200
