
import worldBuilder.CONST as CONST


class Tile():
    def __init__(self, type):
        self.__type = type

class World():

    def __init__(self, id, flowers, binders):
        self.__flowers = flowers 
        self.__binders = binders 
        self.__id = id

    def getFace(self):
        pass

    def getFlowerAsData(self,id) -> list:
        return None 

    def turnWorldLft(self):
        pass

    def turnWorldRgt(self):
        pass

    def updateWorld(self):
        pass

class Flower():

    def __init__(self, edges,midTile,location) -> None:
        self.__edges = edges
        self.__midTile = midTile
        self.__location = location

class Binder():

    def __init__(self, location, edges) -> None:
        self.__location = location
        self.__edges = edges



flowers = [Flower(None, Tile(CONST.DeepWater),0)]
binders = []
testWorld = World("3hch1",flowers,binders )

testWorld.getFace()