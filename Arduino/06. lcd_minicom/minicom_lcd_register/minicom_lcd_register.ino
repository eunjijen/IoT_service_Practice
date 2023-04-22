#include <PWMLed.h>
#include <Minicom.h>
#include <Analog.h>

PWMLed led(9);
Analog sensor(A0, 255, 0);
MiniCom com;

void check() {
  int bright = sensor.read();
  led.setValue(bright);
  com.print(1, "bright: ", bright);
}

void setup() {
  com.init();
  com.print(0, "[[MiniCom]]");
  com.setInterval(1000, check);
}

void loop() {
  com.run();

}
