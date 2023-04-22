#include <MqttCom.h>
# include <ArduinoJson.h>

const char *ssid = "SK_WiFiGIGA7ECB_2.4G";
const char *password = "1701006267";
// pc의 ip 주소  무선 LAN 어댑터 Wi-Fi:
const char *mqtt_server = "192.168.35.245";

MqttCom com;

void callback(char *topic, byte *payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';

  StaticJsonDocument<256> doc;
  auto error = deserializeJson(doc, buf);
  if(error) {
    com.print(0, error.c_str());
    return;
  }

  int led = doc["led"].as<int>();
  const char* door = doc["door"];

  com.print(0, "led:", led);
  String str = "door:";
  str += door;
  com.print(1, str);
}

void setup() {
  com.init(ssid, password);
  com.setServer(mqtt_server, "iot/kim/control", callback);
}

void loop() {
  com.run();
}
