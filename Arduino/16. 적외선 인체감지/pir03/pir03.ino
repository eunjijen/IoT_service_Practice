// 자옹문
# include <Minicom.h>
# include <Led.h>
# include <Servo.h>
# include <SimpleTimer.h>
# include "Pir.h"

MiniCom com;
Led led(8);
Pir pir(7);
Servo door;
int timer_id = -1;  // 현재 꺼져있음

void detect_on() {
  com.print(1, "Motion detected!");
  led.on();
  door.write(90);

  SimpleTimer &timer = com.getTimer();
  if(timer_id == -1) {  // 최초 감지
    timer_id = timer.setTimeout(8000, detect_off);  
  } else {
    timer.restartTimer(timer_id);
  }
}

void detect_off() {
  com.print(1, "Motion ended!");
  led.off();
  door.write(0);
  timer_id = -1;
}

void setup() {
  com.init();
  com.print(0, "[[Motion!]]");
  pir.setCallback(detect_on, NULL);
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
  pir.check();
}