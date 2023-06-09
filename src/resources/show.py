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
        parser.add_argument("bookedSeats",help="This Field is mandatory",required = True)
        parser.add_argument("isFull",help="This Field is mandatory",required = True)
        parser.add_argument("venue_id",help="This Field is mandatory",required = True)
        
        # extracting Data
        data = parser.parse_args()
        new_show = Show(name=data['name'],rating=data['rating'],ticketPrice=data['ticketPrice'],bookedSeats=data['bookedSeats'],isFull=data['isFull'],venue_id=data['venue_id'])
        id = showsDB.addShow(show=new_show)
        if id!=None:
            return {'message':"Show Added"}
        return {'message':"Error Occured"},404
    

class GetAllShows(Resource):
    @jwt_required()
    def get(self):
        showsList = showsDB.getAllShows()
        ret_Json = []
        for show in showsList :
            ret_Json.append(show.toJson())
        return ret_Json,200

class GetShowsByVenueId(Resource):
    @jwt_required()
    def get(self):
        # getting venueId through args
        venue_id = request.args.get("venue_id")
        if venue_id !=None:
            showsList = showsDB.getShowByVenueId(venue_id=venue_id)
            print(showsList,flush=True)
            if len(showsList) > 0:
                retJson = Show.returnJsonFromList(listShows = showsList)
                return retJson, 200
            else:
                return {"message":"venue_id doesn't exist"},404
        else:
            return {"message":"venue_id not found"},404

class DeleteShowByShowId(Resource):
    @jwt_required()
    def delete(self):
        # getting the show_id 
        show_id = request.args.get("show_id")
        if show_id!=None:
            result = ShowsDB.deleteShowByShowId(show_id=show_id)
            if result ==True:
                return {"message":"Show Deleted successfully"},200
        else:
            return {"message":"show_id not found"},404
        
class UpdateShowByShowId(Resource):
    @jwt_required()
    def put(self):
        # getting the show id as a parameter
        show_id = request.args.get("show_id")
        #getting the show as a body
        parser = reqparse.RequestParser()
        parser.add_argument("name",help="This Field is mandatory",required = True)
        parser.add_argument("rating",help="This Field is mandatory",required = True)
        parser.add_argument("ticketPrice",help="This Field is mandatory",required = True)
        parser.add_argument("bookedSeats",help="This Field is mandatory",required = True)
        parser.add_argument("venue_id",help="This Field is mandatory",required = True)
        # extracting Data
        data = parser.parse_args()
        new_show = Show(name=data['name'],rating=data['rating'],ticketPrice=data['ticketPrice'],bookedSeats=data['bookedSeats'],isFull=None,venue_id=data['venue_id'])
        if show_id!=None:
            result = ShowsDB.updateShowByShowId(show=new_show,show_id=show_id)
            if result ==True:
                return {"message":"Show Updated"},200
            else:
                return {"message":"Error occured"},404
        else:
            return {"message":"show_id not found"},404
        