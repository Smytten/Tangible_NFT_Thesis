from world import Flower, Binder, World, Tile
import WORLDCONST as WORLDCONST

tileType = (WORLDCONST.DesertTile,WORLDCONST.NormalWater)
elevation = (-90,90)


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

w = World('6dh2',panels,"Arrakis")
json = w.exportJSON()


print(json)