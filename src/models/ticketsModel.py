class Tickets:
    def __init__(self,user_id,show_id,numOfTickets,venue_id,id=None) -> None:
        self.id = id
        self.user_id = user_id
        self.show_id = show_id
        self.venue_id = venue_id
        self.numOfTickets = numOfTickets
        
    def returnSet(self):
        return (self.user_id,self.show_id,self.venue_id,self.numOfTickets)

    def fromArray(row):
        tickets = Tickets(id=row[0],user_id=row[1],show_id=row[2],venue_id=row[3],numOfTickets=row[4])
        return tickets
    

    def fromList(listTickets):
        ret_TicketList = []
        for ticket in listTickets:
            ret_TicketList.append(Tickets.fromArray(ticket))
        return ret_TicketList

    def toJson(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "show_id":self.show_id,
            "venue_id":self.venue_id,
            "numOfTickets":self.numOfTickets
        }
    
    def returnJsonFromList(listTickets):
        ret_TicketList  = []
        for ticket in listTickets:
            ret_TicketList.append(ticket.toJson())
        return ret_TicketList