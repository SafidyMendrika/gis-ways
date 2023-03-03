from model.Layertype import Layertype


class LayerTypeDAO:
    @staticmethod
    def findAll(connection):
        query = "SELECT * FROM layertype "

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Layertype()

            dbo.setFullFields(obj[0], obj[1])

            result.append(dbo)
        cursor.close()

        return result
    @staticmethod
    def findById(connection,idLayer):
        query = "SELECT * FROM layertype where idlayertype = "+str(idLayer)

        cursor = connection.cursor()

        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = Layertype()

            dbo.setFullFields(obj[0], obj[1])

            result.append(dbo)
        cursor.close()

        return result[0]

    @staticmethod
    def countLayerIn(connection,idLayer,idWay,radius):
        query = "SELECT count(*) FROM layerDistinctIn("+str(idWay)+","+str(radius)+") where idLayerType = "+str(idLayer)
#        print("queryyy :::"+str(query))

        cursor = connection.cursor()
        cursor.execute(query)

        objArray = cursor.fetchall()

        result = 0
        for obj in objArray:
            result = obj[0]
        cursor.close()

        return result
