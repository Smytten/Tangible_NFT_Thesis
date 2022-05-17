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

SHRINKING_CYCLES = 10
RAIN_CYCLE_DURATION = 2
WATER = 'water'
LAND = 'land'

WATERFLOW = 3 

RAIN_AMOUNT = 2
EVAPURATE_AMOUNT = 30 #LESS IS MORE IS TEMP - AMOUNT 

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

POLARITY_CONST = [
    {
        "location": [(1,3),(6,5),(10,4),(8,3),(8,4),(8,5)],
        "pol": -40
    },
    {
        "location": [(1,0),(1,1),(1,2),(1,4),(1,5),(10,2),(10,3),(8,2),(3,3),(3,4),(4,2),(4,3),(6,2),(6,3),(6,4)],
        "pol": -20
    },
    {
        "location": [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(6,0),(2,5),(2,4),(7,5),(9,0),(5,1),(5,2),(9,4)],
        "pol": 10
    },
]