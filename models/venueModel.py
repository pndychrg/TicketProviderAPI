class Venue:
    def __init__(self,name,place,capacity,id=None):
        self.id = id
        self.name = name
        self.place = place
        self.capacity = capacity

    def returnSet(self):
        return (self.name,self.place,self.capacity)
    
    def fromList(listVenues):
        ret_VenueList = []
        for venue in listVenues:
            ret_VenueList.append(Venue(id=venue[0],name=venue[1],place=venue[2],capacity=venue[3]))
        return ret_VenueList
