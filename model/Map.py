import webbrowser
from web.webfig import Webfig
import folium

class Map:
    def __init__(self):
        self.__MAP_PAGE__ = Webfig.getBasePath()+"/index.html"
        self.__FOLIUM =folium

        self.set_folium_setting()
        pass

    def set_folium_setting(self):
        pass
    def openMap(self):
        webbrowser.open_new_tab(self.__MAP_PAGE__)


    def openMapIn(self,latitude : float , longitude : float):

        map = self.__FOLIUM.Map(
        )

        marker = self.__FOLIUM.Marker(
            location=[latitude,longitude],
            icon=folium.Icon(icon="home")
        )
        marker.add_to(map)

        map.save(self.__MAP_PAGE__)

        self.openMap()



    def writeInto(self,filename,args):
        file = open(filename,"w")

        file.write(args)

        file.close()

    def execute(self,map):
        map.save(self.__MAP_PAGE__)

        self.openMap()