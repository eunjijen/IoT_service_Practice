#include <Led.h>
#include <WifiMiniCom.h>
// 조도 온도 습도를 측정
// lcd 1줄 T:, H:
// 2줄 I:
#include <MqttCom.h>
#include <Analog.h>
#include <DHT.h>

const char *ssid = "SK_WiFiGIGA7ECB_2.4G";
const char *password = "1701006267";
// pc의 ip 주소  무선 LAN 어댑터 Wi-Fi:
const char *mqtt_server = "192.168.35.245";    // mqtt broker ip address

MqttCom com;
Analog cds(A0, 100, 0);
DHT dht11(D7, DHT11);
Led led(9);

void publish() {
  int illu = cds.read();
  float humi, temp;
  humi = dht11.readHumidity();
  temp = dht11.readTemperature();

  com.print(0, "T:", temp, "H:", humi);
  com.print(1, "I:", illu);

  com.publish("iot/sensor/livingroom/illu", illu);
  // com.publish("iot/kim/sensor/livingroom/illu", illu);
  com.publish("iot/sensor/bedroom/temp", temp);
  com.publish("iot/sensor/kitchen/humi", humi);
}

void callback(char *topic, byte *payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';

  String msg = buf;
  if(msg == "on") {
    led.setValue(0);
  } 
  else if (msg == "off") {
    led.setValue(1);
  }
}

void setup() {
  com.init(ssid, password);
  // com.setServer(mqtt_server);  
  com.setServer(mqtt_server, "iot/control/led", callback);  
  com.setInterval(1000*10, publish);     // 10초 간격으로
  dht11.begin();
}

void loop() {
  com.run();
}
