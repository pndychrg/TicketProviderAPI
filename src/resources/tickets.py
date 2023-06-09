from flask_restful import Resource,reqparse,request
from flask_jwt_extended import jwt_required
from models.ticketsModel import Tickets
from database.ticketDB import TicketsDB

# init Database Functions
ticketsDB = TicketsDB()

class AddTicket(Resource):
    @jwt_required()
    def post(self):
        # parser for adding ticket details
        parser = reqparse.RequestParser()
        parser.add_argument("user_id",help="This Field is mandatory",required = True)
        parser.add_argument("show_id",help="This Field is mandatory",required = True)
        parser.add_argument("venue_id",help="This Field is mandatory",required = True)
        parser.add_argument("numOfTickets",help="This Field is mandatory",required = True)

        # extracting Data
        data = parser.parse_args()
        print(data,flush=True)
        new_ticket = Tickets(user_id=data['user_id'],show_id=data["show_id"],venue_id=data['venue_id'],numOfTickets=data['numOfTickets'])
        id = ticketsDB.addTicket(ticket=new_ticket)
        print(id,flush=True)
        if id!=None:
            return {'message':"Ticket Added"},200
        return {'message':"Error Occured"},404
    
class GetAllTickets(Resource):
    @jwt_required()
    def get(self):
        ticketList = ticketsDB.getAllTickets()
        ret_Json = []
        for ticket in ticketList:
            ret_Json.append(ticket.toJson())
        return ret_Json,200

class GetTicketsByUserId(Resource):
    @jwt_required()
    def get(self):
        # getting user_id through args
        user_id = request.args.get("user_id")
        if(user_id!=None):
            print(user_id,flush=True)
            ticketList = TicketsDB.getAllTicketsByUserId(user_id=user_id)
            if ticketList!=None:
                ret_Json = Tickets.returnJsonFromList(ticketList)
                return ret_Json,200
            else:
                return {"message":"user_id doesn't exist"}
            
