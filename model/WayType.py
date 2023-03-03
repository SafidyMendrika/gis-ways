class WayType:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.cost = 6000
        self.duration = 6

    def setFullFields(self,id,name,cost,duration): # for new fully instance
        self.id = id
        self.name = name
        self.cost = cost
        self.duration = duration