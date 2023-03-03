import psycopg2

from model.Layer import Layer

from dao.DAO import DAO
from model.Layertype import Layertype


class LayerDAO:
    @staticmethod
    def findAll(connection):
        query = "SELECT * FROM layer_detals "

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Layer()
            type = Layertype()
            type.setFullFields(obj[3],obj[6])

            coord = DAO.coordinize(obj[7])

            dbo.setFullFields(obj[0], obj[1], coord[0], coord[1],
                              obj[4],type)

            result.append(dbo)
        cursor.close()

        return result

    @staticmethod
    def findByType(connection,idLayerType):
        query = "SELECT * FROM layer_detals where idlayertype = "+str(idLayerType)

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Layer()
            type = Layertype()
            type.setFullFields(obj[3],obj[6])

            coord = DAO.coordinize(obj[7])

            dbo.setFullFields(obj[0], obj[1], coord[0], coord[1],
                              obj[4],type)

            result.append(dbo)
        cursor.close()

        return result
