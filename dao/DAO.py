class DAO:
    def __init__(self):
        pass


    def say(self,message = "hello" ):
        print(message)

    @staticmethod
    def coordinize(strpoint):
        points = str(strpoint).split("(")[1]
        result = []

        p = points.split(" ")

        result.append(p[0])

        result.append(p[1].split(")")[0])

        return result

    @staticmethod
    def timeToText(time):
        if time<24 : return str(time)+"h"
        j = int(time)//24
        h  = int(time) % 24
        return str(j)+"j "+str(h)+"h"