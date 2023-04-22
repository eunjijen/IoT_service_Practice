# include <Minicom.h>
# include <Ultra.h>
# include <Servo.h>

Servo door;
MiniCom com;
Ultra ultra(5,6);

void notice_in() {
  com.print(1, "NOTICE IN");
  door.write(90);
}

void notice_out() {
  com.print(1, "NOTICE OUT");
  door.write(0);
}

void setup() {
  com.init();
  com.print(0, "[[Distance]]");
  int distance = pulseIn(5, HIGH) / 58;
  com.print(1, "Dist.(cm)=", distance);
  ultra.setThreshold(20, notice_in, notice_out);
  door.attach(3);
  door.write(0);
}

void loop() {
  com.run();
  ultra.run();
}
