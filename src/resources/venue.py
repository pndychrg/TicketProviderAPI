from flask_restful import Resource,reqparse,request
from flask_jwt_extended import jwt_required
from models.venueModel import Venue
from database.venueDB import VenueDB
from flask import jsonify
import json

#initialising Venue Database Functions
venueDB = VenueDB()

class AddVenue(Resource):
    def options(self):
        response = jsonify({'message': 'Preflight request accepted.'})
        #response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    @jwt_required()
    def post(self):
        # parser for adding venue details
        # parser = reqparse.RequestParser()
        # parser.add_argument('name',help='This Field is mandatory',required = True)
        # parser.add_argument('place',help="This Field is mandatory",required = True)
        # parser.add_argument('capacity',help="This Field is mandatory",required = True)
        
        # # extracting data
        # data = parser.parse_args()
        data = request.get_json()
        print("data first ",data,flush=True)
        if isinstance(data,str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                return {'message': 'Invalid JSON data in the request body'}, 400
        if "name" not in data or "place" not in data or "capacity" not in data:
            return {'message':'Invalid JSON '},400
        print(data,flush=True)
        new_venue = Venue(name=data['name'],place=data['place'],capacity=data['capacity'])
        id = venueDB.addVenue(venue=new_venue)
        if id!=None:
            print('Venue Added')
            return {'message':"Venue Added"},200
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
