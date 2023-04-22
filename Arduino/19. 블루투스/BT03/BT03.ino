#include <BtMiniCom.h>
# include <Led.h>
# include <Servo.h>

void receive_msg(String msg);

Servo door;
Led led(8);
BtMiniCom com(13, 12, receive_msg);

void receive_msg(String msg) {
  String result = "ok";
  // 장치 제어
  if(msg == "on") {
    led.on();
  } else if (msg == "off") {
    led.off();    
  } else if(msg == "open") {
    door.write(90);
  } else if(msg == "close") {
    door.write(0);
  } else {
    result = "bad command: " + msg;
    com.print(1, result);
  }
  com.send(result);
}

void setup() {
  com.init();
  com.print(0, "[[Bluetooth]]");
  door.attach(3);
}

void loop() {
  com.run();
}
