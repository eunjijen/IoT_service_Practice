#include <Button.h>

Button btn(2);

const int relay_pin = 4;
boolean relay_out = LOW;

void check() {
  // put your setup code here, to run once:
  relay_out = !relay_out; // 릴레이 제어핀 출력값 반전
  digitalWrite(relay_pin, relay_out);
}

void setup() {
  // put your main code here, to run repeatedly:
  btn.setCallback(check);
  pinMode(relay_pin, OUTPUT);
}

void loop() {
  btn.check();
}