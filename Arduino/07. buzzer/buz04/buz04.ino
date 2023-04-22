#include <Minicom.h>
#include <Button.h>
#include <Melody.h>
#include "pirates.h"

MiniCom com;
Button btn(2);

Melody melody(9, notes, durations, length);

void check() {
  bool bplay = melody.toggle(true);
  if(bplay) {
    com.print(0, "play");
  } else {
    com.print(0, "pause");
  }
}

void setup() {
  com.init();
  btn.setCallback(check);
  melody.play();
  com.print(0, "play");
}

void loop() {
  com.run();
  melody.run();
  btn.check();
}
