class WayConstDetals:
    def __init__(self):
        self.way = None
        self.layerType = None
        self.value = 0
        self.constParam = None

    def setFullFields(self,way,layerType,value,constParam):
        self.way = way
        self.layerType = layerType
        self.value = value
        self.constParam = constParam