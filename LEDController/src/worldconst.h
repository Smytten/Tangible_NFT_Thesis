
#ifndef worldconst.h
#define worldconst.h

#define DeepWater 1
#define ShallowWater 2
#define NormalWater 3
#define DessertTile 4
#define ForrestTile 5
#define SnowyMountain 6
#define RockMountain 7

#define FLOWER 1
#define BINDER 2





const int DeepWaterTile[11][3]= {{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255},{0,0,255}};  
const int ShallowWaterTile[11][3]={{1,2,3},{2,3,4},{3,4,5},{4,5,6}};  
const int NormalWaterTile[11][3]={
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
};  

const int tileSet[7][11][3] = {
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
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
        {255,0,0},
    }   
};


const int WavePatterns[10][11] = {
    {1,0,0,1,1,0,0,0,1,0,1},
    {0,1,0,1,0,1,1,1,0,1,1},
    {1,1,1,0,1,0,0,0,0,1,0},
    };

const int waveRgb[3] = {255,255,255};


const int animationDuration = 30;
const int animationPause = 240;
#endif 