
from abc import abstractmethod
import WORLDCONST as WORLDCONST
import broker as broker


class Tile():
    def __init__(self, type: str, elevation = 0, occupent = WORLDCONST.LAND):
        self._type = type
        self._occupent = occupent
        self._polarity = 0
        self._elevation = elevation
        self._waterLevel = 0
        self._neighbours = []

    def getType(self):
        return self._type

    def setType(self,tileType):
        self._type = tileType 

    def getPolarity(self):
        return self._polarity

    def setPolarity(self, polarity):
        self._polarity = polarity

    def getNeighbours(self):
        return self._neighbours

    def getWaterAmount(self):
        return self._waterLevel

    def getElevation(self):
        return self._elevation

    def getOccupent(self):
        return self._occupent

    def nearWater(self):
        return True

class Pane():

    @abstractmethod
    def getIdentifyer(self):
        pass

    @abstractmethod
    def getTilesToString(self):
        pass

    @abstractmethod
    def getTiles(self) -> list:
        pass

    @abstractmethod
    def setIdentifyer(self, id):
        pass

    @abstractmethod
    def setTiles(self, tiles):
        pass

class Flower(Pane):

    def __init__(self, tiles : list,location) -> None:
        self._tiles = tiles 
        self._location = location
        self._id = 'none'

    def getIdentifyer(self):
        return WORLDCONST.PROJECT + "/" + self._id + "/f" + str(self._location)

    def getTilesToString(self):
        stringifyedTileSet = "~"
        for e in self._tiles:
            stringifyedTileSet = stringifyedTileSet + e.getType()
        return stringifyedTileSet

    def setIdentifyer(self, id):
        self._id = id

    def getTiles(self) -> list:
        return self._tiles

    def setTiles(self, tiles : list):
        self._tiles = tiles

class Binder(Pane):

    def __init__(self, location, edges) -> None:
        self.__location = location
        self.__edges = edges

class World():

    def __init__(self, id, panes : list):
        self.__id = id
        self.setPanels(panes)
        self._observers = [] 
        self._temp = -50

    def setPanels(self, panels : list):
        self._panes = [] 
        for pane in panels:
            pane.setIdentifyer(self.__id)
            self._panes.append(pane)

    def notify(self, modifier = None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self._panes)

    def power(self, modifer = None):
        for observer in self._observers:
            observer.power(self._panes)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass 

    def getFace(self) -> str:
        for p in self._panes:
            pass

    def publishPanes(self) -> list:
        returnList = []
        for pane in self._panes:
            returnList.append(pane.getTilesToString())
            #returnList.append(pane.getIdentifyer(self.__id))
    
        return returnList

    def heatWorld(self):
        self._temp = self._temp + 10

    def coolWorld(self):
        self._temp = self._temp - 10

    def worldStep(self):
        paneList = []
        for p in self._panes:
            tiles = p.getTiles() 
            newTileList = []

            for tile in tiles: # Update Tile States       
                
                # Move water water to lowest state

                # Evapurate Water

                # Check if Water Amount > 100 and and change to WATERILE
                if tile.getWaterLevel >= 100:
                    tile.setOccupent(WORLDCONST.WATER)
                else:
                    tile.setOccupent(WORLDCONST.LAND)

                if tile.getOccupent() == WORLDCONST.WATER: # HANDLE WATERY TILES
                    if self._temp >= WORLDCONST.WaterRange[0] and self._temp < WORLDCONST.WaterRange[1]:

                        if tile.getElevation() < 0 and tile.getElevation() > -10:
                            tile.setType(WORLDCONST.ShallowWater)
                            newTileList.append(tile)
                            continue
                        
                        if tile.getElevation() < -10 and tile.getElevation() > -50:
                            tile.setType(WORLDCONST.NormalWater)
                            newTileList.append(tile)
                            continue

                        if tile.getElevation() < -50:
                            tile.setType(WORLDCONST.DeepWater)
                            newTileList.append(tile)
                            continue

                    if self._temp >= WORLDCONST.WaterRange[1]:
                        tile.setType(WORLDCONST.DesertTile)
                        newTileList.append(tile)
                        continue

                    else:
                        tile.setType(WORLDCONST.FrozenWater)
                        newTileList.append(tile)
                        continue

                if tile.getOccupent() == WORLDCONST.LAND: # HANDLE LANDY TILES 
                    if self._temp >= WORLDCONST.ForrestRange[0] and self._temp < WORLDCONST.ForrestRange[1] and tile.nearWater():
                        tile.setType(WORLDCONST.ForrestTile)
                        newTileList.append(tile)
                        continue

                    if self._temp < WORLDCONST.ForrestRange[0]:
                        tile.setType(WORLDCONST.FrozenForrest)
                        newTileList.append(tile)
                        continue

                    tile.setType(WORLDCONST.DesertTile)
                    newTileList.append(tile)
                    continue

                
                else:
                    newTileList.append(tile)


                #simple tile change

               # if tile.getType() == WORLDCONST.FrozenWater:
               #     if self._temp > WORLDCONST.WaterRange[0]:
               #         newTileList.append(Tile(WORLDCONST.NormalWater))
               #         continue

               # if tile.getType() == WORLDCONST.NormalWater:
               #     if self._temp < WORLDCONST.WaterRange[0]:
               #         newTileList.append(Tile(WORLDCONST.FrozenWater))
               #         continue

               #     if self._temp > WORLDCONST.WaterRange[1]:
               #         newTileList.append(Tile(WORLDCONST.DesertTile))
               #         continue

               # if tile.getType() == WORLDCONST.DesertTile:
               #     if self._temp < WORLDCONST.WaterRange[1]:
               #         newTileList.append(Tile(WORLDCONST.NormalWater))
               #         continue
               # 
               # newTileList.append(tile)


            p.setTiles(newTileList)
            paneList.append(p)
        self.setPanels(paneList)
        
    def getPaneTileSet(self,id):
        return self._panes[id].getTilesToString()



class mqttclientboi():
    def update(self, data):
        print(data)
        for d in data:
            print("imma publish this: " + d.getTilesToString() + " to: " + d.getIdentifyer())

    def power(self, data):
        print("Switching PowerState")

realBroker = broker.MQTTBroker()

panels = [
    Flower([Tile(WORLDCONST.FrozenWater,elevation=-200,occupent=WORLDCONST.WATER),Tile(WORLDCONST.FrozenWater,elevation=-40,occupent=WORLDCONST.WATER),Tile(WORLDCONST.FrozenForrest),Tile(WORLDCONST.FrozenForrest),Tile(WORLDCONST.FrozenForrest),Tile(WORLDCONST.FrozenForrest)],0)
    ]

testWorld = World("6dh2",panels)

mqttClien = mqttclientboi()

testWorld.attach(mqttClien)
testWorld.attach(realBroker)

# testWorld.notify()

PilotTiles = [
    [
        Flower(
                [
                    Tile(WORLDCONST.FrozenWater),
                    Tile(WORLDCONST.FrozenWater),
                    Tile(WORLDCONST.FrozenWater),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.FrozenWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.DeepWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.DeepWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.ForrestTile),
                    Tile(WORLDCONST.ForrestTile),
                    Tile(WORLDCONST.ForrestTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.DeepWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.NormalWater),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ],
    [
        Flower(
                [
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile),
                    Tile(WORLDCONST.DesertTile)
                ], 
                    0
            )
    ]
]


while(True):
    state = input('PlanetState: [F,LF,WD,WF,WD,DW,D] ~~ ')
    if state == '1':
        panes = PilotTiles[0]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '2':
        panes = PilotTiles[1]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '3':
        panes = PilotTiles[2]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '4':
        panes = PilotTiles[3]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '5':
        panes = PilotTiles[4]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '6':
        panes = PilotTiles[5]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == '7':
        panes = PilotTiles[6]
        testWorld.setPanels(panes)
        testWorld.notify()
    if state == 'o':
        testWorld.power()
    if state == 'h':
        testWorld.heatWorld()
        testWorld.worldStep()
        print(testWorld._temp)
        testWorld.notify()
    if state == 'c':
        testWorld.coolWorld()
        testWorld.worldStep()
        print(testWorld._temp)
        testWorld.notify()
