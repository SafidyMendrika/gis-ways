import psycopg2

from dao.LayerTypeDAO import LayerTypeDAO
from model.DmgWay import DmgWay
from model.Way import Way
from model.WayConstDetals import WayConstDetals
from model.WayType import WayType


class WayDAO:
    def __init__(self):
        pass

    # @staticmethod
    # def fullSave(connection  ,object : DmgWay):
    #     query = "INSERT INTO dmgway VALUES (default,"+str(object.getDestDegree())+","+str(object.getIdPK_START())+","+str(object.getIdPK_END())+","+str(object.getIdWay())+")";

    #     cursor = connection.cursor()
    #     cursor.execute(query)

    #     cursor.close()
    #     pass

    # @staticmethod
    # def findById(connection  ,object : DmgWay):
    #     id = object.getId()
    #     query = "SELECT * FROM dmgway WHERE iddmgway = "+str(id)

    #     cursor = connection.cursor()

    #     cursor.execute(query)

    #     objArray = cursor.fetchall()

    #     result = []
    #     for obj in objArray:
    #         dbo = DmgWay()
    #         dbo.setFullFields(obj[0],obj[1],obj[2],obj[3],obj[4])

    #         result.append(dbo)
    #     cursor.close()

    #     return result

    @staticmethod
    def findAll(connection):
        query = "SELECT * FROM way_detals "

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Way()

            waytype = WayType()
            waytype.setFullFields(obj[3],obj[5],obj[6],obj[7])

            dbo.setFullFields(obj[0],obj[1],obj[2],waytype)

            result.append(dbo)
        cursor.close()

        return result
    
    @staticmethod
    def findPk(connection):
        query = "SELECT * FROM  "

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Way()
            dbo.setFullFields(obj[0],obj[1],obj[2],obj[3],obj[4])

            result.append(dbo)
        cursor.close()

        return result

    staticmethod

    def findById(connection,id):
        query = "SELECT * FROM way_detals where idway = "+str(id)

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Way()

            waytype = WayType()
            waytype.setFullFields(obj[3], obj[5], obj[6], obj[7])

            dbo.setFullFields(obj[0], obj[1], obj[2], waytype)

            result.append(dbo)
        cursor.close()

        return result[0]

    @staticmethod
    def orderRnBy(connection,idLayer,radius):
        query = "SELECT * FROM wayWithLayerCount("+str(idLayer)+","+str(radius)+") order by value desc"
        print("queryyyyy ::: "+str(query))

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        rnFirstResult = []
        for obj in objArray:
            rnFirstResult.append([obj[0],obj[1]])
        cursor.close()

        result = []
        for rn in rnFirstResult:
            way = WayDAO.findById(connection,rn[0])
            layerType = LayerTypeDAO.findById(connection,idLayer)

            wayConstDet = WayConstDetals()

            param = way.getConstructParameters(connection)
            wayConstDet.setFullFields(way,layerType,rn[1],param)

            result.append(wayConstDet)
        cursor.close()

        return result


