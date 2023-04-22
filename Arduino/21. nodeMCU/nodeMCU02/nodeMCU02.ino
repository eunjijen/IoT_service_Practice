# include <WifiMiniCom.h>

const char *ssid = "SK_WiFiGIGA7ECB_2.4G";
const char *password = "1701006267";

WifiMiniCom com;


void setup() {

  com.init(ssid, password);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
}