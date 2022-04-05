#include <FastLED.h>
#include <ESP8266WiFi.h>        // Include the Wi-Fi library
#include <PubSubClient.h>

const char* ssid     = "AU-Gadget";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "augadget";     // The password of the Wi-Fi network

const char* mqtt_server = "REPLACE_WITH_YOUR_RPI_IP_ADDRESS"; // MQTT_Server


// How many leds in your strip?
#define NUM_LEDS 10 

// For led chips like WS2812, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
// Clock pin only needed for SPI based chipsets when not using hardware SPI
#define DATA_PIN 2 

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() {
  // Uncomment/edit one of the following lines for your leds arrangement.
  // ## Clockless types ##
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  //FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);  // GRB ordering is typical

  FastLED.setBrightness(40);
  for (int i = 0; i < 10; i++)
  {
    leds[i].setRGB(90,35,90);
    FastLED.show();
  }
  FastLED.show();

  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');
  delay(500);
    
 
  Serial.println();
  Serial.print("MAC: ");
  Serial.println(WiFi.macAddress());
  
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

  for (int i = 0; i < 10; i++)
  {
    leds[i].setRGB(102,178,255);
    FastLED.show();
  }
}

void loop() {
}
