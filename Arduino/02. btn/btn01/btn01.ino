#include <Led.h>

const int in_pu_sw_pin = 2; 
Led led(4);

void setup() {
 
  Serial.begin(9600);
  pinMode(in_pu_sw_pin, INPUT_PULLUP);
}

void loop() {
  boolean in_pu_sw;

  in_pu_sw = !digitalRead(in_pu_sw_pin); // 풀업 스위치 상태 읽기

  led.setValue(in_pu_sw);
 
}
