from dao.DAO import DAO
from dao.PkDAO import PkDAO
from model.DmgWay import DmgWay
from model.PK import PK


class DmgWayDAO:
    def __init__(self):
        pass



    # @staticmethod
    # def findById(connection  ,object : DmgWay):
    #     id = object.getId()
    #     query = "SELECT * FROM dmg_way_detals WHERE iddmgway = "+str(id)

    #     cursor = connection.cursor()

    #     cursor.execute(query)

    #     objArray = cursor.fetchall()

    #     result = []
    #     for obj in objArray:
    #         dbo = DmgWay()
    #         way = Way()
    #         way.setFullFields(obj[1],obj[10],obj[9])

    #         dbo.setFullFields(obj[0],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7],obj[8],way)

    #         result.append(dbo)
    #     cursor.close()

    #     return result[0]

    # @staticmethod
    # def findAll(connection):
    #     query = "SELECT * FROM dmg_way_detals "

    #     cursor = connection.cursor()

    #     cursor.execute(query)

    #     objArray = cursor.fetchall()

    #     result = []
    #     for obj in objArray:
    #         dbo = DmgWay()
    #         way = Way()
    #         way.setFullFields(obj[1],obj[10],obj[9])

    #         dbo.setFullFields(obj[0],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7],obj[8],way)

    #         result.append(dbo)
    #     cursor.close()

    #     return result

    def findDmgwayOf(connection,idWay):
        query  = "select * from dmg_way_detals where idway = "+str(idWay)
        print("querrryyyyyy : "+str(query))
        cursor = connection.cursor()
        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = DmgWay()

            coordstart = DAO.coordinize(obj[9])
            pkstart = PK()
            pkstart.setFullFields(obj[2],obj[6],coordstart[0],coordstart[1],obj[8])


            coordend = DAO.coordinize(obj[10])
            pkend = PK()
            pkend.setFullFields(obj[3],obj[7],coordend[0],coordend[1],obj[8])


            dbo.setFullFields(obj[0],obj[1],pkstart,pkend)

            dbo.pks = PkDAO.findBetween(connection,dbo.pk_start.pk_value,dbo.pk_end.pk_value)
            result.append(dbo)
        cursor.close()

        return result



        return result
    def countDmgWayIn(connection,idWay):
        query = "SELECT count(*) FROM dmg_way_detals where idway= "+str(idWay)

        cursor = connection.cursor()
        cursor.execute(query)

        objArray = cursor.fetchall()

        result = 0
        for obj in objArray:
            result = obj[0]
        cursor.close()

        return result



