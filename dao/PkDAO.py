import psycopg2

from dao.DAO import DAO
from model.PK import PK

class PkDAO:
    @staticmethod
    def findFromWay(connection, idway):
        query  = "select  idpk,pk_value,st_astext(coordinate),pk_idway from pk where pk_idway = "+str(idway)+" order by pk_value asc"

        cursor = connection.cursor()
        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = PK()

            coord = DAO.coordinize(obj[2])

            dbo.setFullFields(obj[0],obj[1],coord[0],coord[1],obj[3])
            result.append(dbo)
        cursor.close()

        return result

    @staticmethod
    def findBetween(connection,start,end):
        query  = "select idpk,pk_value,st_astext(coordinate),pk_idway from pk where pk_value between "+str(start)+" and "+str(end)+" "

        cursor = connection.cursor()
        cursor.execute(query)

        objArray = cursor.fetchall()

        result = []
        for obj in objArray:
            dbo = PK()

            coord = DAO.coordinize(obj[2])

            dbo.setFullFields(obj[0], obj[1], coord[0], coord[1], obj[3])
            result.append(dbo)
        cursor.close()
        cursor.close()