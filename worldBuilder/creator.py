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

        tiles = []

        for _ in range(6):
            height = random.randint(highDif[0],highDif[1])
            waterBody = random.randint(water[0],water[1])
            print(f'waterBody: {waterBody}')
            print(f'height: {height}')
            tType =random.randint(0,1) 
            tile = tileType[tType]
            occu = occupents[tType]
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
    w._temp = 5
    return w

w = generateWorld("GG",highDif=(-90,90),water=(0,20))

w.worldStep()

json = w.exportJSON()


print(json)