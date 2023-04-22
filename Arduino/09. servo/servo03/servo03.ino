// 자동문
#include <Led.h>
#include <SimpleTimer.h>
#include <Servo.h>
#include <Button.h>
# include <Minicom.h>

Button btn(2);
Servo myServo;
MiniCom com;
Led led(8);

const int OPEN = 90;
const int CLOSE = 0;
const int servo_pin = 5;

char state = CLOSE;
int timer_id = -1;


void open() {
  myServo.write(OPEN);
  led.on();
  delay(100);
  led.off();
  com.print(1, "OPEN");
  state = OPEN;
}

void close() {
  timer_id = -1;
  myServo.write(CLOSE);
  com.print(1, "CLOSE");
  state = CLOSE;  // 상태변수 변경
}

void check() {
  SimpleTimer &timer  = com.getTimer();
  if(state == CLOSE) {  // 닫혀있는 경우 --> open
    open();
    timer_id = timer.setTimeout(3000, close); // 3초 지나면 close 호출
  }
  else {  // 열려 있는 경우 시간 연장
    timer.restartTimer(timer_id);  
  }
}

void setup() {
  com.init();
  com.print(0, "[[Door]]");
  com.print(1, "close");

  myServo.attach(servo_pin);
  myServo.write(CLOSE);

  btn.setCallback(check);
  
}

void loop() {
  btn.check();
  com.run();

}
