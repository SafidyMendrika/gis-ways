import flask.json
import psycopg2
import folium

from dao.DmgWayDAO import DmgWayDAO
from dao.PkDAO import PkDAO


class Way:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.width = 0
        self.wayType = None

    def setFullFields(self,id,name,width,wayType):
        self.id = id
        self.name = name
        self.width = width
        self.wayType = wayType

    def mapIn(self,connection,container):
        pks = PkDAO.findFromWay(connection,self.id)

        locationarray = []
        for pk in pks:
            locationarray.append([float(pk.lat),float(pk.long)])

        #if len(locationarray) != 0:
         #   folium.PolyLine(locationarray,color="gray",weight=12).add_to(container)

        #damaged way
        dmgways = DmgWayDAO.findDmgwayOf(connection,self.id)

        for dmgway in dmgways:
            locationarray = [[float(dmgway.pk_start.lat),float(dmgway.pk_start.long)],[float(dmgway.pk_end.lat),float(dmgway.pk_end.long)]]
            folium.PolyLine(locationarray, color="red",weight=(dmgway.dest_degree/5)).add_to(container)
            dmgway.mapIn(container)

    def getConstructParameters(self,connection):
        dmgWay = DmgWayDAO.findDmgwayOf(connection, self.id)
        amount = 0
        duration = 0
        volume = 0
        for dmg in dmgWay:
            amount += dmg.getCout(self.wayType.cost, self.width)
            #print("dmg : "+str(dmg.id)+str(amount)+" amount : "+str(amount))
            #dmg.desc()
            duration += dmg.getConstructDuration(self.width, self.wayType.duration)
            volume += dmg.getDestVolume(self.width)

        parameter = []

        parameter.append(len(dmgWay)) # count dmgway of self
        parameter.append(int(amount)) # amount of construction of a way
        parameter.append(duration) # duration of construction of a way
        parameter.append(volume) # volume of dmg way of self

        return parameter