from flask_restful import Resource,reqparse,request
from flask_jwt_extended import jwt_required
from models.venueModel import Venue
from database.venueDB import VenueDB

#initialising Venue Database Functions
venueDB = VenueDB()

class AddVenue(Resource):
    @jwt_required()
    def post(self):
        # parser for adding venue details
        parser = reqparse.RequestParser()
        parser.add_argument('name',help='This Field is mandatory',required = True)
        parser.add_argument('place',help="This Field is mandatory",required = True)
        parser.add_argument('capacity',help="This Field is mandatory",required = True)
        
        # extracting data
        data = parser.parse_args()
        new_venue = Venue(name=data['name'],place=data['place'],capacity=data['capacity'])
        id = venueDB.addVenue(venue=new_venue)
        if id!=None:
            return {'message':"Venue Added"}
        return {"message":"Error Occured"},404
    
class GetAllVenue(Resource):
    @jwt_required()
    def get(self):
        venueList = venueDB.getAllVenues()
        ret_Json = []
        for venue in venueList:
            ret_Json.append(venue.toJson())
        return ret_Json,200

#TODO GET VENUE BY ID

class DeleteVenueById(Resource):
    @jwt_required()
    def delete(self):
        venue_id = request.args.get("venue_id")
        if venue_id!=None:
            result = VenueDB.deleteVenueByVenueId(venue_id=venue_id)
            if result ==True:
                return {'message':"Venue Deleted"},200
        else:
            return {"message":"venue_id not found"},404
    
class UpdateVenueByeVenueId(Resource):
    @jwt_required()
    def put(self):
        # getting venue_id as a parameter
        venue_id = request.args.get("venue_id")
        # getting updated venue details in body
        parser = reqparse.RequestParser()
        parser.add_argument('name',help='This Field is mandatory',required = True)
        parser.add_argument('place',help="This Field is mandatory",required = True)
        parser.add_argument('capacity',help="This Field is mandatory",required = True)
        
        # extracting data
        data = parser.parse_args()
        new_venue = Venue(name=data['name'],place=data['place'],capacity=data['capacity'])
        if venue_id !=None:
            result = VenueDB.updateVenueByVenueId(venue=new_venue,venue_id=venue_id)
            if result == True:
                return {"message":"Venue Updated"},200
            else:
                {"message":"Error Occured"},404
        else:
            return {"message":"venue_id not found"},404
