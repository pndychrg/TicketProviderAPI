
class Show:
    def __init__(self,name,rating,ticketPrice,bookedSeats,isFull,venue_id=None,id=None):
        self.id = id
        self.name = name
        self.rating = rating
        #self.tags = tags
        self.ticketPrice = ticketPrice
        self.bookedSeats = bookedSeats
        self.isFull = isFull
        self.venue_id = venue_id
    
    def returnSet(self):
        return (self.name,self.rating,self.ticketPrice,self.bookedSeats,self.isFull,self.venue_id)
    
    def fromArray(row):
        show = Show(id=row[0],name=row[1],rating=row[2],ticketPrice=row[3],bookedSeats=row[4],isFull=row[5],venue_id=row[6])
        return show
    
    def fromList(listShows):
        ret_ShowList = []
        for show in listShows:
            ret_ShowList.append(Show.fromArray(show))
        return ret_ShowList
    
    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "rating":self.rating,
            "ticketPrice":self.ticketPrice,
            "bookedSeats":self.bookedSeats,
            "isFull":self.isFull,
            "venue_id":self.venue_id
        }

    def returnJsonFromList(listShows):
        ret_ShowList = []
        for show in listShows:
            ret_ShowList.append(Show.toJson(show))
        return ret_ShowList
