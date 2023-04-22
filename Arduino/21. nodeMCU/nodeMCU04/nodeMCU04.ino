#include <WifIMiniCom.h>
#include <PubSubClient.h>
# include <Led.h>

const char *ssid = "SK_WiFiGIGA7ECB_2.4G";
const char *password = "1701006267";
// pc의 ip 주소  무선 LAN 어댑터 Wi-Fi:
const char *mqtt_server = "192.168.35.245"; // mqtt broker ip address

WifiMiniCom com;

WiFiClient espClient;
PubSubClient client(espClient);
Led led(BUILTIN_LED);

int value = 0;

void callback(char *topic, byte *payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';
  // 확인용
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  Serial.println(buf);

  com.print(0, topic);
  com.print(1, buf);

  // 제어
  if(buf[0] == '1') {
    led.setValue(LOW);
  } 
  else {
    led.setValue(HIGH);
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP8266Client")) {  // 클라이언트 ID 중복 주의
      Serial.println("connected");

      client.publish("outTopic", "hello world");
      client.subscribe("inTopic");  // subscribe할 토픽 등록
    }
    else {  // 연결실패한 경우 5초 후 재시도
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void publish() {
  char msg[50];
  ++value;
  sprintf(msg, "hello world #%ld", value);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish("outTopic", msg);
}

void setup() {
  com.init(ssid, password);
  com.setInterval(2000, publish);  // 2초에 한번씩 value ++ 
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback); // 토픽 수신 시 호출할 함수 등록
}

void loop() {
  com.run();
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
