class Tickets:
    def __init__(self,user_id,show_id,numOfTickets,id=None) -> None:
        self.id = id
        self.user_id = user_id
        self.show_id = show_id
        self.numOfTickets = numOfTickets
        
    def returnSet(self):
        return (self.user_id,self.show_id,self.numOfTickets)

    def fromArray(row):
        tickets = Tickets(user_id=row[1],show_id=row[2],numOfTickets=row[3])
        return tickets
    

    def fromList(listTickets):
        ret_TicketList = []
        for ticket in listTickets:
            ret_TicketList.append(Tickets.fromArray(ticket))
        return ret_TicketList

    def toJson(self):
        return {
            "user_id":self.user_id,
            "show_id":self.show_id,
            "numOfTickets":self.numOfTickets
        }