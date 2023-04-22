#include <Analog.h>

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // 최대 16글자 출력
Analog sensor(A0, 1023, 0);

void setup() {
  lcd.init();
  lcd.backlight();
}

void loop() {
  char buf[17]; // 마지막에 null까지 포함해서 17글자
  int value = sensor.read();
  lcd.setCursor(0,0);
  // lcd.clear();

  sprintf(buf,"value: %4d", value); // 4자리 사용 digit 10진수 숫자
  // value값이 4자리에 들어가
  // string 출력 - formatting한 결과를 문자열에 담겠다
  lcd.print(buf);
}
