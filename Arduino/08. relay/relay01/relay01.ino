#include <Minicom.h>

#include <Button.h>

Button btn(2);
MiniCom com;

const int relay_pin = 4;
boolean relay_out = LOW;

int timer_id = -1;

void blink() {
  relay_out = !relay_out; // 릴레이 제어핀 출력값 반전
  digitalWrite(relay_pin, relay_out); // 릴레이 제어핀 새 출력값 출력
}

void check() {
  if(timer_id == -1) { // blink 타이머 가동
    timer_id == com.setInterval(500, blink);
    com.print(1, "Blinking");
  } 
  else {  // blink 타이머 제거
    SimpleTimer &timer = com.getTimer();
    timer.deleteTimer(timer_id);
    timer_id = -1;
    relay_out = false;
    digitalWrite(relay_pin, relay_out);
    com.print(1, "");
  }
  relay_out = !relay_out;
  digitalWrite(relay_pin, relay_out);
}

void setup() {
  com.init();
  com.print(0, "[[Relay Ex]]");

  btn.setCallback(check);
  pinMode(relay_pin, OUTPUT);
}

void loop() {
  
  btn.check();
  com.run();
}
