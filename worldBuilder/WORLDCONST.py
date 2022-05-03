DeepWater = "1"
ShallowWater = "2"
NormalWater = "3"
DesertTile = "4"
ForrestTile = "5"
SnowyMountain = "6"
RockMountain = "7"
FrozenWater = "8"
FrozenForrest = "9"

WaterRange = (0,40)
IceRange = (-200,-1)
DesertRange = (26,300)
ForrestRange = (0,25)

WATER = 'water'
LAND = 'land'

WATERFLOW = 1 

RAIN_AMOUNT = 2


PROJECT = "mworld"


NEIGHBOURHOOD_CONST_TOP = [
    [1,2,3,4,5],
    [0,2,5,0,0,1],
    [0,1,3,0,0,1],
    [0,2,4,0,0,1],
    [0,3,5,0,0,1], 
    [0,1,4,0,0,1],
]

NEIGHBOURHOOD_CONST_SIDE = [
    [1,2,3,4,5],
    [0,2,5,0,1,2],
    [0,1,3,2,3,4],
    [0,2,4,4,5,0],
    [0,3,5,2,3,5], 
    [0,1,4,0,1,2],
]

NEIGHBOURHOOD_CONST_BINDERS = [
    [0,0,0,0,0]
]