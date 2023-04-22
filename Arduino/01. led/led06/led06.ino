# include "Led.h"

Led leds[4] = { Led(3), Led(4), Led(5), Led(6)};

int out_no = 0; // 출력 값 출력 순서 번호(0-3)

void blink() {
    for (int i = 0; i<6; i++) {
      for(auto &led:leds) {
        led.toggle();
      }
      delay(500);
    }
}

void setup() {
 
}

void loop() {
  for(int n = 0; n < 4; n++){ 
    leds[n].setValue(n==out_no)
  }

  out_no = (++out_no) % 4;
  delay(1000);

  if(out_no == 0) {
    leds[3].off();
    blink();
  }
}
