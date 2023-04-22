// 웹 서버

#include <WifIMiniCom.h>

const char *ssid = "SK_WiFiGIGA7ECB_2.4G";
const char *password = "1701006267";

WifiMiniCom com;
WiFiServer server(80);

void setup() {
  // put your setup code here, to run once:
  com.init(ssid, password);
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) {
    return;
  }

  //wait until the client sends some data
  Serial.println("new client");
  while(!client.available()) {
    delay(1); // 데이터 수신 대기
  }

  // read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();

  // return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("");

  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.print("Hello world!");
  client.println("</html>");
  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");
}
