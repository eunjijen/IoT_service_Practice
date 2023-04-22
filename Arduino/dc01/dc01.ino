#include <BtMiniCom.h>
# include "Car.h" 

void receive_msg(String);

BtMiniCom com(13, 12, receive_msg);
Car car(6, 7, 5, 8, 9, 10);

void receive_msg(String msg) {
  String result = "ok: " + msg;

  if(msg == "forward") {
    car.setSpeed(120);
    car.forward();
  } 
  else if(msg == "backward") {
    car.setSpeed(120);
    car.backward();
  } 
  else if(msg == "turnLeft") {
    car.setSpeed(100);
    car.turnLeft();
  } 
  else if(msg == "turnRight") {
    car.setSpeed(100);
    car.turnRight();
  } 
  else if(msg == "stop") {
    car.stop();
  } 
  else {
    result = "bad command: " + msg;
  }
  com.send(result);
}

void setup() {
  com.init();
  car.stop();
}

void loop() {
  com.run();

}
