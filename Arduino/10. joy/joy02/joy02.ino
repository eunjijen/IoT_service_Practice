#include <Button.h>
#include <Analog.h>
#include <Minicom.h>

MiniCom com;
Analog x(A0);
Analog y(A1);
Button z(A2);

void check() {
  int dx, dy;
  boolean sw;

  dx = x.read();
  dy = y.read();
  sw = z.read();

  char buf[17];
  sprintf(buf, "%d, %d [%d]", dx, dy, sw);
  com.print(1, buf);
}

void setup() {
  com.init();
  com.setInterval(100, check);
  com.print(0, "[[Joystick]]");
}

void loop() {
  com.run();
}
