#include <FastLED.h>
#include <ESP8266WiFi.h>        // Include the Wi-Fi library
#include <PubSubClient.h>
#include <worldconst.h>
#include <networking.h>


// How many leds in your strip?
#define NUM_LEDS 61

// For led chips like WS2812, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
// Clock pin only needed for SPI based chipsets when not using hardware SPI
#define DATA_PIN 2 

// The amount of panels the WEMOS control.
#define PANELS 6

// Define the type of panel
#define PANELTYPE "flower"


// Define the array of leds
CRGB leds[NUM_LEDS];

int currentWavePattern = 0;

long millisdelay = 4;

unsigned long time_now = 0;

int aniCounter = 0;

int panelTileState[PANELS];
int tempTransitionState[PANELS];
int transitionQue[PANELS];

bool hasRecivedNewContent = false;
bool completedTransitionCycle = false;

bool rainfall[6] = { false, false, false, false, false, false};
bool transitioning[6] = { false, false, false, false, false, false };

int panelLEDIndex[PANELS];

boolean active = false;

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;

int status = WL_IDLE_STATUS;     // the starting Wifi radio's status



String macToStr(const uint8_t* mac)
{
  String result;
  for (int i = 0; i < 6; ++i) {
    result += String(mac[i], 16);
    if (i < 5)
      result += ':';
  }
  return result;
}

String composeClientID() {
  uint8_t mac[6];
  WiFi.macAddress(mac);
  String clientId;
  clientId += "esp-";
  clientId += macToStr(mac);
  return clientId;
}

void fillPixel(int from, int to, int r, int g, int b){
  for (int i = from; i < to; i++){
    leds[i].setRGB(g,r,b);
    FastLED.show();
  } 
}

void fillPixelWithPattern(int from, int to, int patternType){
  int toUse = patternType - 1;

  for (int i = from; i < to; i++){ 
    leds[i].setRGB(tileSet[toUse][i-from][1],tileSet[toUse][i-from][0],tileSet[toUse][i-from][2]);
    FastLED.show();
  }
}

void fillPanels(){
  int curPos = 0;
  for (int i = 0; i < PANELS; i++) 
  {
    fillPixelWithPattern(curPos,curPos + panelLEDIndex[i],panelTileState[i]);
    curPos = curPos + panelLEDIndex[i];
  }
}

boolean aReset = false;
void activate(){
  if ( aReset ) {
    fillPanels();
    aReset = false;
  }
}

boolean dReset = false;
void deactivate(){
  if( dReset ) {
    fillPixel(0,NUM_LEDS,0,0,0);
    dReset = false;
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  if ((char)payload[0] == '~'){
   for (int i = 1; i < length; i++) {
     char currentChar = (char)payload[i];
     if(isdigit(currentChar)){
      int value = currentChar - '0';
      Serial.print(value);
      transitionQue[i-1] = value;
     }
    }
    if (active) {
      hasRecivedNewContent = true;
     // aReset = true;
    } else {
      memcpy(panelTileState,transitionQue,sizeof(panelTileState));
    }
  }
  Serial.println();

  if ((char)payload[0] == 'r'){
    for (int i = 0; i < PANELS; i++)
    {
      rainfall[i] = !rainfall[i];
    }
    
  }

  if ((char)payload[0] == 'o') {
    active = !active;
    if ( active ) {
      aReset = true;
    } else {
      dReset = true;
    }
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    String clientId = composeClientID() ;
    clientId += "-";
    clientId += String(micros() & 0xff, 16); // to randomise. sort of

    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      fillPixel(0,NUM_LEDS,0,0,0);
      delay(50);
      fillPixel(0,NUM_LEDS,255,255,255);
      delay(50);
      fillPixel(0,NUM_LEDS,0,0,0);
      delay(50);
      fillPixel(0,NUM_LEDS,255,255,255);
      dReset = true;
      // Once connected, publish an announcement...
      // client.publish(topic, ("connected " + composeClientID()).c_str() , false );
      // ... and resubscribe
      // topic + clientID + in
      String subscription;
      subscription += topic;
      client.subscribe(subscription.c_str() );
      Serial.print("subscribed to : ");
      Serial.println(subscription);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.print(" wifi=");
      Serial.print(WiFi.status());
      Serial.println(" try again in 1 seconds");
      // Wait 5 seconds before retrying
      delay(1000);
    }
  }
}

int animationSkewingBinder[PANELS][11];

void tileTransition(int currentPosition, int panel,int curTileType, int targetTileType){
  for (int i = currentPosition; i < currentPosition + panelLEDIndex[panel]; i++) {
    if (aniCounter <= transitionDuration) {
      int r = tileSet[curTileType][i-currentPosition][0]+(((tileSet[targetTileType][i-currentPosition][0]-tileSet[curTileType][i-currentPosition][0])/(transitionDuration))*aniCounter);
      int g = tileSet[curTileType][i-currentPosition][1]+(((tileSet[targetTileType][i-currentPosition][1]-tileSet[curTileType][i-currentPosition][1])/(transitionDuration))*aniCounter);
      int b = tileSet[curTileType][i-currentPosition][2]+(((tileSet[targetTileType][i-currentPosition][2]-tileSet[curTileType][i-currentPosition][2])/(transitionDuration))*aniCounter); 
      leds[i].setRGB(g,r,b);
      FastLED.show();
    }
  }
}

void animationFadeInOut(int currentPosition, int panel, int curTile, const int AnimationPattern[10][11],const int targetColor[3]){
  for (int i = currentPosition; i < currentPosition + panelLEDIndex[panel]; i++) {
    int skewedAniCounter = animationSkewingBinder[panel][i-currentPosition];
    if (aniCounter > skewedAniCounter && aniCounter < skewedAniCounter + animationDuration) {
      if (AnimationPattern[currentWavePattern][i-currentPosition] == 1) {             
        int r = tileSet[curTile][i-currentPosition][0]+(((targetColor[0]-tileSet[curTile][i-currentPosition][0])/animationDuration)*(aniCounter - skewedAniCounter));
        int g = tileSet[curTile][i-currentPosition][1]+(((targetColor[1]-tileSet[curTile][i-currentPosition][1])/animationDuration)*(aniCounter - skewedAniCounter));
        int b = tileSet[curTile][i-currentPosition][2]+(((targetColor[2]-tileSet[curTile][i-currentPosition][2])/animationDuration)*(aniCounter - skewedAniCounter)); 
        leds[i].setRGB(g,r,b);
        FastLED.show();
       }
      }
      if (aniCounter > skewedAniCounter + animationDuration && aniCounter < (skewedAniCounter + (animationDuration * 2)) + 1) {
        if (AnimationPattern[currentWavePattern][i-currentPosition] == 1) {
          int r = targetColor[0]+(((tileSet[curTile][i-currentPosition][0]-targetColor[0])/animationDuration)*(aniCounter - skewedAniCounter - animationDuration));
          int g = targetColor[1]+(((tileSet[curTile][i-currentPosition][1]-targetColor[1])/animationDuration)*(aniCounter - skewedAniCounter - animationDuration));
          int b = targetColor[2]+(((tileSet[curTile][i-currentPosition][2]-targetColor[2])/animationDuration)*(aniCounter - skewedAniCounter - animationDuration));
          leds[i].setRGB(g,r,b);
          FastLED.show();
        }
      } 
    }
}

void animationRainfall(int currentPosition, int panel, int curTile){
  for (int i = currentPosition; i < currentPosition + panelLEDIndex[panel]; i++) {
    int skewedAniCounter = animationSkewingBinder[panel][i-currentPosition];
    if (aniCounter > skewedAniCounter && aniCounter < skewedAniCounter + rainfallDuration) {
      int r = tileSet[curTile][i-currentPosition][0]+(((rainRgb[0]-tileSet[curTile][i-currentPosition][0])/rainfallDuration)*(aniCounter - skewedAniCounter));
      int g = tileSet[curTile][i-currentPosition][1]+(((rainRgb[1]-tileSet[curTile][i-currentPosition][1])/rainfallDuration)*(aniCounter - skewedAniCounter));
      int b = tileSet[curTile][i-currentPosition][2]+(((rainRgb[2]-tileSet[curTile][i-currentPosition][2])/rainfallDuration)*(aniCounter - skewedAniCounter)); 
      leds[i].setRGB(g,r,b);
      FastLED.show();
    }
    if (aniCounter > skewedAniCounter + rainfallDuration && aniCounter < (skewedAniCounter + (rainfallDuration * 2)) + 1) {
      int r = rainRgb[0]+(((tileSet[curTile][i-currentPosition][0]-rainRgb[0])/rainfallDuration)*(aniCounter - skewedAniCounter - rainfallDuration));
      int g = rainRgb[1]+(((tileSet[curTile][i-currentPosition][1]-rainRgb[1])/rainfallDuration)*(aniCounter - skewedAniCounter - rainfallDuration));
      int b = rainRgb[2]+(((tileSet[curTile][i-currentPosition][2]-rainRgb[2])/rainfallDuration)*(aniCounter - skewedAniCounter - rainfallDuration));
      leds[i].setRGB(g,r,b);
      FastLED.show();
    } 
  }
}

void animation() {
  if (time_now + millisdelay < millis()) {
    time_now = millis();
    
    int currentPosition = 0;

    // Check if tileset should be animated
    for (int panel = 0; panel < PANELS; panel ++){ //Iterate through each panel
      int curTile = panelTileState[panel];

      // Check for transition, if transistion do and return
      if ( transitioning[panel] ) {
        tileTransition(currentPosition,panel,curTile-1,tempTransitionState[panel]-1);
        currentPosition = currentPosition + panelLEDIndex[panel];
        continue;
      }

      if ( curTile == DeepWater || curTile == NormalWater || curTile == ShallowWater ) { // Water Panel, Wave Animation     
        // Do increnment animation for 30 frames
        curTile = curTile - 1;
        animationFadeInOut(currentPosition,panel,curTile,WavePatterns,waveRgb);

      }
      
      if ( curTile == DesertTile ) {
        curTile = curTile - 1;
        if ( rainfall[panel] == true ) {
          animationRainfall(currentPosition,panel,curTile);
        } else {
          animationFadeInOut(currentPosition,panel,curTile,WavePatterns,desertRgb);
        }

      }
      
      if ( curTile == ForrestTile ) {
        curTile = curTile - 1;
        if ( rainfall[panel] == true ){
          animationRainfall(currentPosition,panel,curTile);
        } else {
          animationFadeInOut(currentPosition,panel,curTile,WavePatterns,forestRgb);
        }
      }
      
      if ( curTile == FrozenForrest ) {
        curTile = curTile - 1;
        if ( rainfall[panel] == true ){
          animationRainfall(currentPosition,panel,curTile);
        } else {
          animationFadeInOut(currentPosition,panel,curTile,WavePatterns,frozenForestRbg);
        }
      }
      
      if ( curTile == FrozenWater) {
        curTile = curTile - 1;
        if ( rainfall[panel] == true ){
          animationRainfall(currentPosition,panel,curTile);
        } else {
          animationFadeInOut(currentPosition,panel,curTile,WavePatterns,frozenWaterRgb);
        }
      }


      currentPosition = currentPosition + panelLEDIndex[panel];
    }


    aniCounter ++; 
    if (aniCounter == animationPause) {
      aniCounter = 0;

      // Clear transitioning State
      for (int i = 0; i < PANELS; i++)
      {
        transitioning[i] = false;
      }
      
      // After a complete transition cycle set panel to current
      if ( completedTransitionCycle ) {
        memcpy(panelTileState,tempTransitionState,sizeof(panelTileState));
        completedTransitionCycle = false;
      }

      // Append changes to next animation cycle 
      if ( hasRecivedNewContent ) {
        memcpy(tempTransitionState,transitionQue,sizeof(tempTransitionState));
        
        for (int i = 0; i < PANELS; i++) {
          if (tempTransitionState[i] != panelTileState[i]) {
            transitioning[i] = true;
          }
        }
        completedTransitionCycle = true;
        hasRecivedNewContent = false;
      }




      // Choose new wave animation Pattern
      currentWavePattern = random(3);
      for (int i = 0; i < PANELS; i++) { // init random skewing pattern
        for (int j = 0; j < 11; j ++) {
          animationSkewingBinder[i][j] = random( animationPause - ( animationDuration * 2 ) );
        }
      } 
    }
  }

}


void setup() {
  // Uncomment/edit one of the following lines for your leds arrangement.
  // ## Clockless types ##
  //FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);  // GRB ordering is typical

  FastLED.setBrightness(255);
  fillPixel(0,NUM_LEDS,220,20,60);

  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');
  delay(500);

    
  // fillPixelWithPattern(0,8,DeepWater);
  // fillPixelWithPattern(9,NUM_LEDS,NormalWaterTile);

  panelLEDIndex[0] = 6;
  panelLEDIndex[1] = 11; 
  panelLEDIndex[2] = 11;
  panelLEDIndex[3] = 11;
  panelLEDIndex[4] = 11;
  panelLEDIndex[5] = 11;

  panelTileState[0] = DeepWater; 
  panelTileState[1] = DesertTile; 
  panelTileState[2] = ForrestTile; 
  panelTileState[3] = ForrestTile; 
  panelTileState[4] = DesertTile; 
  panelTileState[5] = DesertTile; 


  // fillPanels();

  Serial.print(composeClientID());

  WiFi.begin(ssid, password);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());  

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  client.subscribe(topic);

  fillPixel(0,NUM_LEDS,255,255,0);
}

void loop() {
  // confirm still connected to mqtt server
  if (!client.connected()) {
     fillPixel(0,NUM_LEDS,255,255,0);
     reconnect();
  }
  client.loop();
  // fillPanels();
  if(active) {
    activate();
    animation();
  } else {
    deactivate();
  }
}
