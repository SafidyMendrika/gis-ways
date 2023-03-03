from flask import Flask , render_template , redirect , request
from folium import folium, LatLngPopup, LayerControl, FeatureGroup
from connector.DBConnector import DBConnector
from flask_cors import CORS

from dao.DmgWayDAO import DmgWayDAO
from dao.WayDAO import WayDAO
from dao.LayerTypeDAO import LayerTypeDAO
from dao.LayerDAO import LayerDAO
from model.Layer import Layer
from model.WayConstDetals import WayConstDetals
from dao.DAO import DAO


def create_app():
    app = Flask(__name__,template_folder="../web/", static_folder="../web/assets/")
    CORS(app)

    # a simple page that says hello
    @app.route('/')
    def index():

        pg = DBConnector()
        conn = pg.connect()

        ways = WayDAO.findAll(conn)

        conn.close()
        return render_template("index.html",data = ways)


    @app.route('/traitement')
    def traitement():
        pass
     
    @app.route('/simplemap')
    def getSimpleMap():

        folmap = createMap()

        strmap = folmap._repr_html_()

        return strmap

    @app.route('/controlPanel')
    def controlPanel():

        pg = DBConnector()
        conn = pg.connect()

        layerType = LayerTypeDAO.findAll(conn)

        conn.close()

        return render_template("control.html",data=layerType)

    @app.route('/constDetals',methods = ["GET","POST"])
    def constDetals():

        if len(request.form["way"]) == 0 : return "<h2>construction detals</h2>"

        id = int(request.form["way"])
        radius = 200

        if len(request.form["radius"]) != 0 : radius = int(request.form["radius"])

        pg = DBConnector()
        conn = pg.connect()

        way = WayDAO.findById(conn,id)

        label = labels(conn,way,radius)
        conn.close()
        return label

    @app.route("/orderRN" , methods = ["POST"])
    def orderRN():
        radius = 200
        if len(request.form["radius"]) != 0 : radius = int(request.form["radius"])

        idLayerType = int(request.form["layerType"])

        pg = DBConnector()
        conn = pg.connect()

        wayConstDetals = WayDAO.orderRnBy(conn,idLayerType,radius)

        conn.close()

        wayConstDetals
        return  render_template("control-table.html",data=wayConstDetals)




    # @app.route('/formQuery',methods = ["GET","POST"])
    # def getRequestedMap():
    #     type = request.form["entity"]
    #     radius = request.form["radius"]
    #     materialPrice = request.form["material"]
    #     duration = request.form["duration"]

    #     if len(materialPrice) == 0 : materialPrice = 6000
    #     if len(duration) == 0 : duration = 6

    #     pg = DBConnector()
    #     conn = pg.connect()


    #     if type =="all": entityArray = EntityDAO.findAll(conn)
    #     else : entityArray = EntityDAO.findByType(conn,type)


    #     wayArray = []


    #     folmap = createMap()

    #     for entity in entityArray:

    #         entity.mapIn(folmap, radius=radius)
    #         if type == "all":wayArray += DmgWayDAO.findNear(conn,"all",radius)
    #         else :
    #             wayArray += DmgWayDAO.findNear(conn,entity,radius)
    #     conn.close()

    #     for dw in wayArray :
    #         dw.mapIn(folmap,float(materialPrice),float(duration))

    #     return  folmap._repr_html_()

    @staticmethod
    def createMap():
        m = folium.Map(
            zoom_start=8,
            location=[ -18.9032 ,47.5210]
        )
        LatLngPopup().add_to(m)

        pg = DBConnector()
        conn = pg.connect()

        pinAll(conn,m)

        LayerControl().add_to(m)

        return m

    @staticmethod
    def pinAll(connection,container):
        layerTypes = LayerTypeDAO.findAll(connection)

        for layertype in layerTypes:
            layerBox = FeatureGroup(layertype.layerlabel)
            layers = LayerDAO.findByType(connection, layertype.id)

            for layer in layers:
                layer.mapIn(layerBox)

                layerBox.add_to(container)

        ways = WayDAO.findAll(connection)

        for way in ways :
            layerBox = FeatureGroup(way.name)
            way.mapIn(connection,layerBox)

            layerBox.add_to(container)




    #@staticmethod
    @staticmethod
    def labels(connection,way,radius):
        p1 = "<p>Nom : <strong>"+str(way.name)+"</strong></p>"
        # cont all layers
        layers = LayerTypeDAO.findAll(connection)

        nb = 0
        p2 = ""
        for layer in layers :
            nb = LayerTypeDAO.countLayerIn(connection,layer.id,way.id,radius)
            p2 += "<p>Nombre de(') "+str(layer.layerlabel)+" : <strong>"+str(nb)+"</strong></p>"

        wayParameter = way.getConstructParameters(connection)

        p3 = "<p>nombre de routes detruites : <strong>" + str(wayParameter[0]) + "</strong></p>"


        p4 = "<p>Cout de reparation : <strong>"+str(wayParameter[1])+"Ar </strong></p>"

        p5 = "<p>volume endomagé : <strong>" + str(wayParameter[2]) + "</strong> m3</p>"

        p6 = "<p>Derée de reparation : <strong>"+str(wayParameter[3])+"</strong> </p>"




        return p1+p2+p3+p4+p5+p6


    return app

