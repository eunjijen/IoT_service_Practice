// 블루투스 모듈 이름 및 PIN 의 변경

#include <SoftwareSerial.h>

SoftwareSerial BTSerial(13, 12); // SoftwareSerial(RX, TX)

void setup() {
  BTSerial.begin(9600);
  Serial.begin(9600);

}

void loop() {
  if (BTSerial.available()) {       
    Serial.write(BTSerial.read());  //블루투스측 내용을 시리얼모니터에 출력
  }
  if (Serial.available()) {         
    BTSerial.write(Serial.read());  //시리얼 모니터 내용을 블루추스 측에 WRITE
  }
}