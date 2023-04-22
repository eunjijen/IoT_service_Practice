#include "WifIMiniCom.h"

WifiMiniCom::WifiMiniCom(int serial_bps, int lcd_addr)
    : MiniCom(serial_bps, lcd_addr)
{
}

void WifiMiniCom::init(const char *ssid, const char *password)
{
  MiniCom::init();

  WiFi.begin(ssid, password);
  print(0, "try to connect");
  Serial.println();

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print("."); // 연결되지 않으면 .을 계속 출력
  }

  print(0, "WiFi connected");
  print(1, WiFi.localIP().toString().c_str());
  Serial.println();
  Serial.println(WiFi.localIP());
}
