#include <MiniCom.h>

MiniCom com;

void setup() {
  com.init();
  com.setInterval(100, check); // 0.1초 간격으로
}
void loop() {
  com.run();
}
void check() {
}