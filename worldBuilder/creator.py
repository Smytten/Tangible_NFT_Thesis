from world import Flower, Binder, World, Tile
import WORLDCONST as WORLDCONST
import random

tileType = (WORLDCONST.DesertTile,WORLDCONST.NormalWater)
occupents = (WORLDCONST.LAND,WORLDCONST.WATER)
elevation = (-90,90)
waterBody = (0,30)




panels = [
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            0
    ),
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            1
    ),
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            2
    ),
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            3
    ),
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            4
    ),
    Flower(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            5
    ),
    Binder(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            6
    ),    
    Binder(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            7
    ),    
    Binder(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            8
    ),    
    Binder(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
            9
    ),    
    Binder(
        [
            Tile(WORLDCONST.FrozenForrest, elevation=70,occupent=WORLDCONST.LAND, waterBody=0),
            Tile(WORLDCONST.FrozenWater, elevation=-40,occupent=WORLDCONST.WATER,waterBody=40),
            Tile(WORLDCONST.FrozenForrest, elevation=10),
            Tile(WORLDCONST.FrozenForrest, elevation=20),
            Tile(WORLDCONST.FrozenForrest, elevation=50),
            Tile(WORLDCONST.FrozenForrest, elevation=40),
        ],
           10 
    ),    
]


def generateWorld(name, id = '6dh2', highDif = (-90,90),water = (0,40)):

    panels = []

    for i in range(11):
        height = random.randint(highDif[0],highDif[1])
        waterBody = random.randint(water[0],water[1])
        print(waterBody)
        tType =random.randint(0,1) 
        tile = tileType[tType]
        occu = occupents[tType]

        tiles = []

        for _ in range(6):
            t = Tile(tile,height,occu,waterBody)
            tiles.append(t)

        if i < 6:
            f = Flower(
                tiles,i
            )
            panels.append(f)
        else:
            b = Binder(tiles,i)
            panels.append(b)

    w = World(name=name,panes=panels,id=id)
    return w

w = generateWorld("Arrakis",highDif=(-20,30),water=(0,5))

w.worldStep()

json = w.exportJSON()


print(json)