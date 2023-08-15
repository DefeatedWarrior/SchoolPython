#include "WiFi.h"

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

}

void loop() {
  int n = WiFi.scanNetworks();
    
    for (int i = 0; i < n; ++i) {
 
      delay(10);
      Serial.println(WiFi.SSID(i)+WiFi.RSSI(i));
    
    }
}