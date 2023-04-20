#TODO Add Tags 
class Show:
    def __init__(self,name,rating,ticketPrice,id=None):
        self.id = id
        self.name = name
        self.rating = rating
        #self.tags = tags
        self.ticketPrice = ticketPrice
    
    def returnSet(self):
        return (self.name,self.rating,self.ticketPrice)
    
    def fromArray(row):
        show = Show(id=row[0],name=row[1],rating=row[2],ticketPrice=row[3])
        return show
    
    def fromList(listShows):
        ret_ShowList = []
        for show in listShows:
            ret_ShowList.append(Show.fromArray(show))
        return ret_ShowList