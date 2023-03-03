class PK:
    def __init__(self):
        self.id = 0
        self.pk_value = 0
        self.lat = 0
        self.long = 0
        self.idway = 0

    def setFullFields(self,id,pk_value,lat,long,idway):
        self.id = id
        self.pk_value = pk_value
        self.lat = lat
        self.long = long
        self.idway = idway
