# include <Minicom.h>

MiniCom com;

void setup() {
  com.init();
}

void loop() {
  int value = analogRead(A0);
  com.print(1, "val:", value);
  com.run();
}
