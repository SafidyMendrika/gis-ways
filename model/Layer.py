import folium as folium
from folium import FeatureGroup


class Layer :
    def __init__(self):
        self.id = 0
        self.layername = ""
        self.latitude = 0
        self.longitude = 0
        self.value = 0
        self.type = None

    def setFullFields(self,id,layername,latitude,longitude,value,type):
        self.id = id
        self.layername = layername
        self.latitude = latitude
        self.longitude = longitude
        self.value = value
        self.type = type


    def mapIn(self ,container,radius = 0):

        marker = folium.Marker(
            location=[self.latitude, self.longitude],
            icon=folium.Icon(color=self.getColor(),prefix="fa",icon=self.getIcon()),
        )
        if radius != 0 : folium.Circle(location=[self.latitude,self.longitude],color=self.getColor(),fill=True,radius=radius).add_to(container)



        label = str(self.layername)

        if self.value != 0 : label += " : "+str(self.value)

        popup = folium.Popup(label, parse_html=True)
        marker.add_child(popup)

        marker.add_to(container)

    def getColor(self):
        if self.type.layerlabel == "School":return "blue"
        if self.type.layerlabel == "Hospital":return "red"
        if self.type.layerlabel == "Hotel"  or self.type.layerlabel == "Restaurant" : return "green"
        if self.type.layerlabel == "Population": return "pink"

    def getIcon(self):
        if self.type.layerlabel == "School":return "school"
        if self.type.layerlabel == "Hospital":return "hospital"
        if self.type.layerlabel == "Hotel" or self.type.layerlabel == "Restaurant": return "hotel"
        if self.type.layerlabel == "Population": return "pink"
        if self.type.layerlabel == "Village": return "home"
        return self.type.layerlabel
