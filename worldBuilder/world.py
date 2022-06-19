from abc import abstractmethod
import math

if __name__ == "__main__":
    import WORLDCONST as WORLDCONST
elif __name__ == "world":
    import WORLDCONST as WORLDCONST
else:
    import worldBuilder.WORLDCONST as WORLDCONST

import json



class Tile():
    def __init__(self, type: str = WORLDCONST.DesertTile, elevation = 99999, occupent = WORLDCONST.LAND,waterBody=0):
        self._type = type
        self._occupent = occupent
        self._polarity = 0
        self._elevation = elevation
        self._waterBody = waterBody
        self._neighbours = []
        self._nearWater = False

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

    def setNeighbours(self,neighbours : list):
        self._neighbours = neighbours

    def removeWaterFromBody(self,amount):
        self._waterBody -= amount
        if self._waterBody < 0:
            self._waterBody = 0

    def addWaterToBody(self,amount):
        self._waterBody = self._waterBody + amount

    def getWaterBody(self):
        return self._waterBody

    def setWaterBody(self,wb):
        self._waterBody = wb

    def getElevation(self):
        return self._elevation

    def getOccupent(self):
        return self._occupent

    def setOccupent(self,occupent):
        self._occupent = occupent

    def setNearWater(self, nearWater : bool):
        self._nearWater = nearWater

    def isNearWater(self):
        return self._nearWater
    
    def toString(self):
        return "TYPE: `" + self._type + "`" + "TOTAL H: `" + str(self._waterBody + self._elevation) + " WATERBODY: `" + str(self._waterBody) + "`" + " ELEVATION: `" + str(self._elevation) + "`" 

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

    @abstractmethod
    def getLocaiton(self):
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

    def getLocation(self):
        return self._location

    def getTiles(self) -> list:
        return self._tiles

    def setTiles(self, tiles : list):
        self._tiles = tiles

    def getActuationHeight(self):
        height = 0
        for t in self._tiles:
            height += t.getElevation()
        h = ((height / len(self._tiles)) + 90)/2
        a = 0
        if h > 45:
            a = 90
        return a 


class Binder(Pane):

    def __init__(self, tiles : list,location) -> None:
        self._tiles = tiles 
        self._location = location
        self._id = 'none'

    def getIdentifyer(self):
        return WORLDCONST.PROJECT + "/" + self._id + "/b" + str(self._location)

    def getTilesToString(self):
        stringifyedTileSet = "~"
        for e in self._tiles:
            stringifyedTileSet = stringifyedTileSet + e.getType()
        return stringifyedTileSet

    def setIdentifyer(self, id):
        self._id = id

    def getLocation(self):
        return self._location

    def getTiles(self) -> list:
        return self._tiles

    def setTiles(self, tiles : list):
        self._tiles = tiles

class World():

    def __init__(self, id = '404', panes : list = [], name = 'unnamed'):
        self.__id = id
        self._name = name
        if len(panes) > 0:
            self.setPanels(panes)
            self.__applyPolarity()
        self._observers = [] 
        self._temp = 10 
        self._heatSource = 1
        self._prevHeatSource = self._heatSource
        self._shrinkingCounter = 0
        self._rainDuraiton = [0,0,0,0,0,0]

    def setPanels(self, panels : list):
        self._panes = [] 
        for pane in panels:
            pane.setIdentifyer(self.__id)
            self._panes.append(pane)
        self.__setupTileNeighbours()

    def notify(self, modifier = None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self._panes)
    
    def notifyIdentityWithMessage(self, identity, message):
        for o in self._observers:
            o.message(identity,message)

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

    def publishPanes(self) -> list:
        returnList = []
        for pane in self._panes:
            returnList.append(pane.getTilesToString())
            #returnList.append(pane.getIdentifyer(self.__id))
    
        return returnList

    def getTile(self,pos : tuple):
        try:
            return self._panes[pos[0]].getTiles()[pos[1]]
        except:
            return Tile() 

    def __applyPolarity(self):
        for zone in WORLDCONST.POLARITY_CONST:
            for pos in zone['location']:
                self.getTile(pos).setPolarity(zone['pol'])

    def __setupTileNeighbours(self):
        for pane in self._panes:
            neigbourList = self.__convertToNeighbourhoodCoridnate(pane.getLocation())
            flowerTiles = pane.getTiles()
            # print(len(flowerTiles))
            i = 0
            for tile in flowerTiles:
                tile.setNeighbours(neigbourList[i])
                i += 1
            pane.setTiles(flowerTiles)

    def __convertToNeighbourhoodCoridnate(self,panePosition):
        returnList = []
        if panePosition == 0:
            curTile = 0
            for pos in WORLDCONST.NEIGHBOURHOOD_CONST_TOP:
                tempReturnList = []
                #GENRATE NEIBOURHOOD
                if len(pos) == 5:
                    for tilePos in pos:
                        tempReturnList.append((panePosition,tilePos))
                
                if len(pos) == 6:
                    curPointer = 0
                    for tilePos in pos:

                        if curPointer < 3:
                            tempReturnList.append((panePosition,tilePos))
                        elif curPointer == 3:
                            tempReturnList.append((6+(8+curTile)%5,tilePos))
                        else:
                            tempReturnList.append((curTile+5,tilePos))

                        curPointer += 1
                        pass

                curTile += 1
                returnList.append(tempReturnList)
        if panePosition >= 1 and panePosition <= 5:
            for cur, pos in enumerate(WORLDCONST.NEIGHBOURHOOD_CONST_SIDE):
                tempReturnList = []
                if cur == 0:
                    for tilePos in pos:
                        tempReturnList.append((panePosition,tilePos))
                if cur == 1 or cur == 2:
                    curPointer = 0 
                    for tilePos in pos:
                        if curPointer < 3:
                            tempReturnList.append((panePosition,tilePos))
                        if curPointer >= 3:
                            tempReturnList.append((6+(8+panePosition)%5,tilePos))

                        curPointer += 1

                if cur == 3:
                    curPointer = 0 
                    for tilePos in pos:
                        if curPointer < 3:
                            tempReturnList.append((panePosition,tilePos))
                        if curPointer == 3:
                            tempReturnList.append((6+(8+panePosition)%5,tilePos))
                        if curPointer == 4:
                            tempReturnList.append((6+(8+panePosition+1)%5,tilePos))

                        curPointer += 1
                    
                if cur == 4:
                    curPointer = 0 
                    for tilePos in pos:
                        if curPointer < 3:
                            tempReturnList.append((panePosition,tilePos))
                        if curPointer >= 3:
                            tempReturnList.append((6+(8+panePosition+1)%5,tilePos))

                        curPointer += 1
                    
                if cur == 5:
                    curPointer = 0 
                    for tilePos in pos:
                        if curPointer < 3:
                            tempReturnList.append((panePosition,tilePos))
                        elif curPointer == 3:
                            tempReturnList.append((6+(8+panePosition)%5,tilePos))
                        else:
                            tempReturnList.append((6+(8+panePosition+1)%5,tilePos))

                        curPointer += 1
                    
                returnList.append(tempReturnList)
        if panePosition > 5:
            for curTile in range(6):
                tempReturnList = []
                if curTile == 0:
                    tempReturnList.append((0,((1 + panePosition)%6)))
                    tempReturnList.append((panePosition,1))
                    tempReturnList.append((1+(panePosition%5),1))
                    tempReturnList.append((1+(panePosition%5),5))
                    tempReturnList.append((panePosition+1,1+(panePosition%10)))
                    tempReturnList.append((0,1+(panePosition%5)))
                if curTile == 1:
                    tempReturnList.append((0,((1 + panePosition)%6)))
                    tempReturnList.append((6+(8+panePosition)%5,0)) 
                    tempReturnList.append((panePosition-5,5))
                    tempReturnList.append((panePosition,2))
                    tempReturnList.append((1+(panePosition%5),1))
                    tempReturnList.append((panePosition,0))

                if curTile == 2:
                    tempReturnList.append((panePosition,1))
                    tempReturnList.append((panePosition-5,5))
                    tempReturnList.append((panePosition-5,4))
                    tempReturnList.append((panePosition,3))
                    tempReturnList.append((1+(panePosition%5),2))
                    tempReturnList.append((1+(panePosition%5),3))

                if curTile == 3:
                    tempReturnList.append((panePosition,2))
                    tempReturnList.append((panePosition-5,4))
                    tempReturnList.append((panePosition,5))
                    tempReturnList.append((panePosition,4))
                    tempReturnList.append((1+(panePosition%5),2))

                if curTile == 4:
                    tempReturnList.append((1+(panePosition%5),2))
                    tempReturnList.append((panePosition,3))
                    tempReturnList.append((1+(panePosition%5),3))
                
                if curTile == 5:
                    tempReturnList.append((panePosition-5,4))
                    tempReturnList.append((panePosition-5,3))
                    tempReturnList.append((panePosition,3))

                returnList.append(tempReturnList)

        # print(f"Pane position: {panePosition}")
        # print (returnList)
        return returnList 

    def heatWorld(self):
        self._temp = self._temp + 10

    def coolWorld(self):
        self._temp = self._temp - 10

    def getActuationHeights(self) -> list:
        heightList = []
        for i, p in enumerate(self._panes):
            if i < 6:
                heightList.append(p.getActuationHeight())
        return heightList

    def setHeatSrc(self, src : int):
        self._heatSource = src

    def getHeatSrc(self) -> int:
        return self._heatSource

    def worldStep(self):
        # Global Changes
        if self._temp > -273:
            self._temp -= 5
        
        if self._heatSource >= 1:
            self._temp += 5 + int(math.pow(self._heatSource,1.5))
        
        ## Shrinking of heat source
        #if self._heatSource > 0:
        #    if self._prevHeatSource == self._heatSource: 
        #        self._shrinkingCounter += 1
        #        if self._shrinkingCounter > WORLDCONST.SHRINKING_CYCLES:
        #            self._shrinkingCoutner = 0
        #            self._heatSource -= 1
        #self._prevHeatSource = self._heatSource
        
        ## Handle Rainfall
        for i, rd in enumerate(self._rainDuraiton):
            if rd != 0:
                self._rainDuraiton[i] -= 1
                self.rainfall(i,manual=False)
                if self._rainDuraiton[i] == 0:
                    self.notifyIdentityWithMessage(self._panes[i].getIdentifyer(),"r") 


        # Handle Individual Panes
        paneList = []
        for p in self._panes:
            tiles = p.getTiles() 
            newTileList = []

            for tile in tiles: # Update Tile States       
                nh = tile.getNeighbours()

                tileTemp = self._temp + tile.getPolarity()
                # Move water water to lowest low elvation
                if tile.getWaterBody() > 0:
                    largestDiff = 0
                    lowestTile = None
                    for pos in nh:
                        myTileHeight = tile.getElevation() + tile.getWaterBody()
                        tileToCheck = self.getTile(pos).getElevation() + self.getTile(pos).getWaterBody()
                        if tileToCheck >= myTileHeight:
                            continue 

                        diff = myTileHeight - tileToCheck 

                        if diff > largestDiff:
                            largestDiff = diff
                            lowestTile = self.getTile(pos)
                    if largestDiff > 0:
                        tile.removeWaterFromBody(WORLDCONST.WATERFLOW)
                        #print("FLOWING FROM: " + tile.toString() + " ----> " + lowestTile.toString())
                        lowestTile.addWaterToBody(WORLDCONST.WATERFLOW)

                    pass

                # print(tile.toString())
                # Evapurate Water

                # Check if Tile is near Water
                for pos in nh:
                    if self.getTile(pos).getOccupent() == WORLDCONST.WATER:
                        tile.setNearWater(True)
                        break
                
                # Check if Water Amount > 100 and and change to WATERILE
                if tile.getWaterBody () >= 5:
                    tile.setOccupent(WORLDCONST.WATER)
                else:
                    tile.setOccupent(WORLDCONST.LAND)
                
                # Handle Tempature Changes
                if tile.getOccupent() == WORLDCONST.WATER: # HANDLE WATERY TILES
                    if tileTemp >= WORLDCONST.WaterRange[0] and tileTemp < WORLDCONST.WaterRange[1]:
                        waterDepth = tile.getWaterBody()

                        if waterDepth >= 5 and waterDepth < 10:
                            tile.setType(WORLDCONST.DeepWater)
                            newTileList.append(tile)
                            continue
                        
                        if waterDepth >= 10 and waterDepth < 50:
                            tile.setType(WORLDCONST.DeepWater)
                            newTileList.append(tile)
                            continue

                        if waterDepth >= 50:
                            tile.setType(WORLDCONST.DeepWater)
                            newTileList.append(tile)
                            continue

                    if tileTemp >= WORLDCONST.WaterRange[1]:
                        tile.removeWaterFromBody(tileTemp - WORLDCONST.EVAPURATE_AMOUNT)
                        if tile.getWaterBody() < 0:
                            tile.setWaterBody(0)
                            tile.setType(WORLDCONST.DesertTile)
                        newTileList.append(tile)
                        continue

                    else:
                        tile.setType(WORLDCONST.FrozenWater)
                        newTileList.append(tile)
                        continue

                if tile.getOccupent() == WORLDCONST.LAND: # HANDLE LANDY TILES 
                    if tileTemp >= WORLDCONST.ForrestRange[0] and tileTemp < WORLDCONST.ForrestRange[1] and tile.isNearWater():
                        tile.setType(WORLDCONST.ForrestTile)
                        tile.removeWaterFromBody(1)
                        newTileList.append(tile)
                        continue

                    if tileTemp < WORLDCONST.ForrestRange[0]:
                        tile.setType(WORLDCONST.FrozenForrest)
                        newTileList.append(tile)
                        continue

                    tile.setType(WORLDCONST.DesertTile)
                    newTileList.append(tile)
                    continue
                
                else:
                    newTileList.append(tile)

            p.setTiles(newTileList)
            paneList.append(p)
        self.setPanels(paneList)
    
    def rainfall(self,location,manual=True):
        rainPane = self._panes[location]
        updatedList = []

        for tile in rainPane.getTiles():
            tile.addWaterToBody(WORLDCONST.RAIN_AMOUNT)
            updatedList.append(tile)

        rainPane.setTiles(updatedList)
        self._panes[location] = rainPane
        print(f"Made it rain on {location}")
        # notify
        if manual:
            id = rainPane.getIdentifyer()
            if self._rainDuraiton[location] == 0:
                self.notifyIdentityWithMessage(id,"r")
            self._rainDuraiton[location] = WORLDCONST.RAIN_CYCLE_DURATION

    def getPaneTileSet(self,id):
        return self._panes[id].getTilesToString()

    def getTotalWater(self):
        hum = 0
        for pane in self._panes:
            for t in pane.getTiles():
                hum += t.getWaterBody()
        return hum

    def exportJSON(self):
        jf = {}
        jf['name'] = self._name
        jf['id'] = self.__id 
        jf['temp'] = self._temp
        jf['heatSource'] = self._heatSource
        jf['totalWaterBody'] = self.getTotalWater()
        panes = {}
        for pane in self._panes:
            curPane = {}
            curPane['location'] = pane.getLocation()
            tiles = []
            for tile in pane.getTiles():
                jTile = {}
                jTile['type'] = tile.getType()
                jTile['elevation'] = tile.getElevation()
                jTile['waterBody'] = tile.getWaterBody()
                jTile['occupent'] = tile.getOccupent()
                tiles.append(jTile)

            curPane['tiles'] = tiles            
            panes[f'p{pane.getLocation()}'] = curPane
        jf['panes'] = panes
        x = json.dumps(jf)
        return x
    
    def importJSON(self,jf):
        self.__id = jf['id']
        self._name = jf['name']
        self._temp = jf['temp']
        self._heatSource = jf['heatSource']
        panels = []
        for i, pane in enumerate(jf['panes']):
            loc = jf['panes'][pane]['location']
            tileList = []
            for tile in jf['panes'][pane]['tiles']:
                #print(tile)
                t = Tile(tile['type'],tile['elevation'],tile['occupent'],tile['waterBody'])
                tileList.append(t)

            if i < 6:
                f = Flower(tileList,loc)
                panels.append(f)
            else:
                b = Binder(tileList,loc)
                panels.append(b)

        self.setPanels(panels)
        self.__applyPolarity()

class mqttclientboi():
    def update(self, data):
        print(data)
        for d in data:
            print("imma publish this: " + d.getTilesToString() + " to: " + d.getIdentifyer())

    def power(self, data):
        print("Switching PowerState")

    def message(self,data,message):
        pass

if __name__ == "__main__":

    import broker as broker


    realBroker = broker.MQTTBroker()

    testWorld = World()

    f = open('world.json')
    jf = json.load(f)
    testWorld.importJSON(jf)

    testWorld.exportJSON()

    mqttClien = mqttclientboi()

    testWorld.attach(mqttClien)
    testWorld.attach(realBroker)

    # testWorld.notify()
    print(testWorld.getTotalWater())


    while(True):
        state = input(f'Planet {testWorld._name}: ~~ ')
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
        if state == 'r':
            testWorld.rainfall(0)
            testWorld.worldStep()
            testWorld.notify()
        if state == 's':
            testWorld.worldStep()
            testWorld.notify()
