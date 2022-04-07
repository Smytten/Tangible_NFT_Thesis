#include <FastLED.h>
#include <ESP8266WiFi.h>        // Include the Wi-Fi library
#include <PubSubClient.h>
#include <worldconst.h>


const char* ssid     = "AU-Gadget";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "augadget";     // The password of the Wi-Fi network

const char* mqtt_server = "public.mqtthq.com";
const char* topic = "mworld/6dh2/f0";    


// How many leds in your strip?
#define NUM_LEDS 11 

// For led chips like WS2812, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
// Clock pin only needed for SPI based chipsets when not using hardware SPI
#define DATA_PIN 2 

// The amount of panels the WEMOS control.
#define PANELS 6

// Define the array of leds
CRGB leds[NUM_LEDS];

int currentWavePattern = 0;

long millisdelay = 16;

unsigned long time_now = 0;

int aniCounter = 0;

int panelTileState[PANELS];


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

void fillPixelWithPattern(int from, int to, const int (&pattern)[11][3]){
  for (int i = from; i < to; i++){ 
    leds[i].setRGB(pattern[i][1],pattern[i][0],pattern[i][2]);
    FastLED.show();
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  if ((char)payload[0] == NormalWater) {
    panelTileState[0] = NormalWater;
    fillPixelWithPattern(0,11,NormalWaterTile);
    Serial.print("normalWater");
  }
  if ((char)payload[0] == '2') {
    fillPixel(0,11,0,0,255);
    Serial.print("do it :)");
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
      fillPixel(0,11,173,216,230);
      // Once connected, publish an announcement...
      client.publish(topic, ("connected " + composeClientID()).c_str() , true );
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


void animation() {
  if (time_now + millisdelay < millis()) {
    time_now = millis();

    // Do increnment animation
    if (aniCounter < 30) {
      for (int i = 0; i < 11; i++)
      {
        if (WavePatterns[currentWavePattern][i] == 1) {
          int r = NormalWaterTile[i][0]+(((waveRgb[0]-NormalWaterTile[i][0])/30)*aniCounter);
          int g = NormalWaterTile[i][1]+(((waveRgb[1]-NormalWaterTile[i][1])/30)*aniCounter);
          int b = NormalWaterTile[i][2]+(((waveRgb[2]-NormalWaterTile[i][2])/30)*aniCounter); 
          leds[i].setRGB(r,g,b);
          FastLED.show();
        }
      }
    }

    // Do return animation
    if (aniCounter > 30 && aniCounter < 61) {
     for (size_t i = 0; i < 11; i++)
      {
        if (WavePatterns[currentWavePattern][i] == 1) {
          int r = waveRgb[0]+(((NormalWaterTile[i][0]-waveRgb[0])/30)*(aniCounter-30));
          int g = waveRgb[1]+(((NormalWaterTile[i][1]-waveRgb[1])/30)*(aniCounter-30));
          int b = waveRgb[2]+(((NormalWaterTile[i][2]-waveRgb[2])/30)*(aniCounter-30));
          leds[i].setRGB(r,g,b);
          FastLED.show();
        }
      } 
    }

    aniCounter ++; 
    if (aniCounter == 240) {
      aniCounter = 0;
      // Choose new wave animation Pattern
      currentWavePattern = random(3);
      Serial.print(currentWavePattern);
    }
  }

}

void setup() {
  // Uncomment/edit one of the following lines for your leds arrangement.
  // ## Clockless types ##
  //FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);  // GRB ordering is typical

  FastLED.setBrightness(40);
  fillPixel(0,11,220,20,60);

  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');
  delay(500);
    
  fillPixelWithPattern(0,11,NormalWaterTile);

  panelTileState[0] = NormalWater;


  // Serial.println();
  // Serial.print("MAC: ");
  // Serial.println(WiFi.macAddress());
  
  // WiFi.begin(ssid, password);             // Connect to the network
  // Serial.print("Connecting to ");
  // Serial.print(ssid); Serial.println(" ...");

  // int i = 0;
  // while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
  //   delay(1000);
  //   Serial.print(++i); Serial.print(' ');
  // }

  // Serial.println('\n');
  // Serial.println("Connection established!");  
  // Serial.print("IP address:\t");
  // Serial.println(WiFi.localIP());  

  // client.setServer(mqtt_server, 1883);
  // client.setCallback(callback);

  // client.subscribe(topic);

  // fillPixel(0,11,255,255,0);
}

void loop() {
  // confirm still connected to mqtt server
  // if (!client.connected()) {
  //   fillPixel(0,11,255,255,0);
  //   reconnect();
  // }
  // client.loop();
  animation();
}