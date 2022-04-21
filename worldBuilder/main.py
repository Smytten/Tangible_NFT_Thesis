
from abc import abstractmethod
import WORLDCONST as WORLDCONST


class Tile():
    def __init__(self, type: str):
        self.__type = type

    def getType(self):
        return self.__type

class Pane():

    @abstractmethod
    def getIdentifyer(self):
        pass

    @abstractmethod
    def getTiles(self):
        pass

    @abstractmethod
    def setIdentifyer(self, id):
        pass

class Flower(Pane):

    def __init__(self, edges,midTile : Tile,location) -> None:
        self.__edges = edges
        self.__midTile = midTile
        self.__location = location
        self.__id = 'none'

    def getIdentifyer(self):
        return WORLDCONST.PROJECT + "/" + self.__id + "/f" + str(self.__location)

    def getTiles(self):
        stringifyedTileSet = self.__midTile.getType()
        for e in self.__edges:
            stringifyedTileSet = stringifyedTileSet + e.getType()
        return stringifyedTileSet

    def setIdentifyer(self, id):
        self.__id = id

class Binder(Pane):

    def __init__(self, location, edges) -> None:
        self.__location = location
        self.__edges = edges


class World():

    def __init__(self, id, panes : list):
        self.__panes = [] 
        for p in panes:
            p.setIdentifyer(id)
            self.__panes.append(p)
        self.__id = id
        self._observers = [] 

    def notify(self, modifier = None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self.__panes)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass 

    def getFace(self) -> str:
        for p in self.__panes:
            pass

    def publishPanes(self) -> list:
        returnList = []
        for pane in self.__panes:
            returnList.append(pane.getTiles())
            #returnList.append(pane.getIdentifyer(self.__id))
    
        return returnList

    def getPaneTileSet(self,id):
        return self.__panes[id].getTiles()

    def turnWorldLft(self):
        pass

    def turnWorldRgt(self):
        pass

    def updateWorld(self):
        pass


class mqttclientboi():
    def update(self, data):
        print(data)
        for d in data:
            print("imma publish this: " + d.getTiles() + " to: " + d.getIdentifyer())


panes = [
    Flower([Tile(WORLDCONST.DeepWater),Tile(WORLDCONST.NormalWater),Tile(WORLDCONST.NormalWater),Tile(WORLDCONST.NormalWater),Tile(WORLDCONST.ShallowWater)], Tile(WORLDCONST.DeepWater),0)
    ]

testWorld = World("6dh2",panes)

mqttClien = mqttclientboi()

testWorld.attach(mqttClien)

testWorld.notify()