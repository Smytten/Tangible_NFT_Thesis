
#ifndef worldconst.h
#define worldconst.h

#define DeepWater 1
#define ShallowWater 2
#define NormalWater 3
#define DesertTile 4
#define ForrestTile 5
#define SnowyMountain 6
#define RockMountain 7
#define FrozenWater 8
#define FrozenForrest 9

#define FLOWER 1
#define BINDER 2


const int tileSet[9][11][3] = {
    {
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255},
        {0,0,255}
    },
    {
        {64,165,179},
        {64,165,179},
        {64,165,179},
        {64,165,179},
        {242,239,211},
        {64,165,179},
        {64,165,179},
        {64,165,179},
        {64,165,179},
        {64,165,179},
        {64,165,179},
    },
    {
        {28,91,255},
        {18,91,255},
        {18,71,255},
        {38,91,255},
        {38,61,255},
        {28,91,255},
        {18,81,255},
        {18,91,255},
        {28,91,255},
        {28,61,255},
        {28,91,255},
    },
    {
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
        {115,69,22},
    },
    {
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
        {0,255,0},
    },    
    {
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {192,192,192},
        {192,192,192},
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
    },
    {
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {204,102,0},
        {153,76,0},
        {204,102,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
        {255,128,0},
    },
    {
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
        {204,229,255},
    },
    {
        {255,255,255},
        {51,25,0},
        {255,255,255},
        {255,255,255},
        {51,25,0},
        {255,255,255},
        {51,25,0},
        {51,25,0},
        {255,255,255},
        {255,255,255},
        {51,25,0},
    }     
};


const int WavePatterns[10][11] = {
    {1,0,0,1,1,0,0,0,1,0,1},
    {0,1,0,1,0,1,1,1,0,1,1},
    {1,1,1,0,1,0,0,0,0,1,0},
    };

const int waveRgb[3] = {255,255,255};


const int animationDuration = 40;
const int animationPause = 500;

const int animationSkewing = 10;
#endif 