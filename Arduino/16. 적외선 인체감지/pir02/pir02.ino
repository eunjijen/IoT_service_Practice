// 현관문

# include <Minicom.h>
# include <Led.h>
# include <Servo.h>
# include "Pir.h"

MiniCom com;
Led led(8);
Pir pir(7);
Servo door;

void detect_on() {
  com.print(1, "Motion detected!");
  led.on();
  door.write(90);
}

void detect_off() {
  com.print(1, "Motion ended!");
  led.off();
  door.write(0);
}

void setup() {
  // put your setup code here, to run once:
  com.init();
  com.print(0, "[[Motion!]]");
  pir.setCallback(detect_on, detect_off);
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
  pir.check();
}