# include <PWMLed.h>

PWMLed red(9);
PWMLed green(10);
PWMLed blue(11);

void setup() {
  Serial.begin(115200);
}

void loop() {
  one_color();
  two_color();
  three_color();
}

// LED 모두 끄기
void led_off(int d_time = 2000)
{
  delay(d_time);

  red.off();
  green.off();
  blue.off();

  Serial.println("-------------------------------------------------");
}

// LED 1개씩
void one_color() {
  Serial.println("R ON");
  red.on();
  led_off();

  Serial.println("G ON");
  green.on();
  led_off();

  Serial.println("B ON");
  blue.on();
  led_off();
}

// LED 2개씩 ON
void two_color() {
  Serial.println("R and G ON");
  red.on();
  green.on();
  led_off();

  Serial.println("G and B ON");
  green.on();
  blue.on();
  led_off();

  Serial.println("B and R ON");
  blue.on();
  red.on();
  led_off();
}

// LED 3개
void three_color() {
  Serial.println("R and G and B ON");
  red.on();
  green.on();
  blue.on();
  led_off();
}
