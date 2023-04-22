#include <Led.h>
# include "Button.h"

Button btn(2);
Led led(7);

Led leds[4] = {
  Led(8), Led(9), Led(10), Led(11)
};

int out_no = -1;

unsigned long old_time = 0;

void setup() {
  btn.setCallback(toggle);
  old_time = millis(); // 기동 순간의 시간
}

void loop() {
  btn.check();

  unsigned long current_time = millis(); // 현재 시간 측정
  if(current_time - old_time >= 1000) { // 지난 시간이 1초가 넘으면
    move_led();
    old_time = current_time; // old_time을 갱신
  }

  //move_led();
  //delay(1000);
}

void toggle() {
  led.toggle();
}

void move_led() {
  out_no = (++out_no) % 4;

  for(int n = 0; n < 4; n++) {
    leds[n].setValue(n == out_no);
  }
}