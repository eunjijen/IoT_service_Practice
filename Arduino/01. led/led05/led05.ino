# include "Led.h"

Led leds[4] = { Led(3), Led(4), Led(5), Led(6)};
int out_no = 0; // 출력 값 출력 순서 번호(0-3)

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  for(int n = 0;n < 4;n++){ 
    if(n == out_no) {
      leds[n].on();
    } else {
      leds[n].off();
    }
  }
  out_no = (++out_no) % 4;
  delay(1000);
}
