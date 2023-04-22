#include <ColorLed.h>

ColorLed leds(9, 10, 11);

void setup() {
  Serial.begin(115200);

}

void loop() {
  pwm_one_color();
  pwm_two_color();
  pwm_three_color();
}
