import folium as folium


class DmgWay:
    def __init__(self):
        self.id = 0
        self.dest_degree = 0
        self.pk_start = None
        self.pk_end = None
        self.pks = None

    ##### GETTERS AND SETTERS

    def desc(self):
        string = "id : "+str(self.id)+" dest : "+str(self.dest_degree)+" pk s "+str(self.pk_start.pk_value)+" pk e "+str(self.pk_end.pk_value)
        print(string)
    def setDestDegree(self,value : int):
        if value < 0 or value > 100 : raise Exception("invalid value of dest degree")
        self.__DEST_DEGREE = value


    def setFullFields(self, id,dest_degree, pk_start, pk_end):  # for new fully instance
        self.id = id
        self.dest_degree = dest_degree
        self.pk_start = pk_start
        self.pk_end = pk_end


    def getCout(self,materialPrice,waywidth):

       return float(self.getDestVolume(waywidth)) * float(materialPrice)

    def getDestVolume(self,waywidth): #m3
        dest_length = float(self.pk_end.pk_value) - float(self.pk_start.pk_value)
        result = float(dest_length*1000) * float(waywidth) *float((self.dest_degree/10)/100)

        return result


    def getConstructDuration(self,duration,waywidth):
        value = self.getDestVolume(waywidth) * float(duration)

        return value

    def intoCentimeter(self, value, current_unit):
        result = 0
        if current_unit == "km":
            result = value * 100 * 1000
        if current_unit == "m":
            result = value * 100
        return result

    def intoMeter(self, value, current_unit):
        result = 0
        if current_unit == "km":
            result = value / 1000
        if current_unit == "cm":
            result = value * 100
        return result


    def mapIn(self,container):
        #start
        marker = folium.Marker(
            popup=self.getHtmlStringMap(),
            location=[self.pk_start.lat, self.pk_start.long],
            icon=folium.Icon(color="red",prefix="fa",icon="road")
        )

        marker.add_to(container)

        #end
        marker = folium.map.Marker(
            popup=self.getHtmlStringMap(isPkEnd=True),
            location=[self.pk_end.lat, self.pk_end.long],
            icon=folium.Icon(color="red",prefix="fa",icon="road")
        )

        marker.add_to(container)




    def getHtmlStringMap(self,isPkEnd = False):
        pk = self.pk_start.pk_value
        pkLabel = "PK (START): "+str(self.pk_start.pk_value)

        if isPkEnd == True :
            pk = self.pk_end.pk_value
            pkLabel = "PK (END): " + str(self.pk_end.pk_value)

        string  = pkLabel

        return string