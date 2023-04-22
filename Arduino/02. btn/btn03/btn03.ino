#include <Led.h>

#define OFF 0
#define ON 1

const int sw_pin = 2;
Led led(8);
boolean led_st = OFF; // LED 초기 상태
int count = 0;  // 버튼 클릭 카운트

void setup() {
  Serial.begin(115200);
  pinMode(sw_pin, INPUT_PULLUP); // switch 연결핀 입력 설정
  led.setValue(led_st);

}

void loop() {
  boolean o_sw, n_sw;

  o_sw = !digitalRead(sw_pin);
  delay(10);
  n_sw = !digitalRead(sw_pin);

  if(o_sw == OFF && n_sw == ON) {
    count++;
    Serial.println(count);
    led_st = !led_st;
    led.setValue(led_st);
  }

}
