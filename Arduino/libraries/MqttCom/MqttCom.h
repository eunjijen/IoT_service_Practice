#pragma once

#include <WifiMiniCom.h>
#include <PubSubClient.h>

class MqttCom : public WifiMiniCom
{
protected:
  const char *server; // MQTT 브로커 IP 주소
  String client_id;   // 클라이언트(NodeMCU의 ID)
  WiFiClient espClient;
  PubSubClient client;

  const char *topic; // subscribe 토픽명
  // void (*callback)(char*, uint8_t*, unsigned int);
  MQTT_CALLBACK_SIGNATURE; // subscribe 콜백 함수 포인터, 변수명은 callback

public:
  MqttCom(int serial_bps = 115200, int lcd_addr = 0x27);
  void init(const char *ssid, const char *password, int no_lcd = false);
  void setServer(const char *server, const char *topic = NULL,
                 MQTT_CALLBACK_SIGNATURE = NULL);
  void reconnect();
  void run();

  void publish(const char *topic, const char *value);
  void publish(const char *topic, int value);
  void publish(const char *topic, float value);
};
