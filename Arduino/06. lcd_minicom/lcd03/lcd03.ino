#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0,0);  // 커서 홈(0,0)
  lcd.print("1++++++++++23----------45*********67##########8");

  lcd.setCursor(0,1); // 커서 2행 1열(0, 1)
  lcd.print("1++++++++++23----------45*********67##########8");
}

void loop() {
  int n;

  for(n=0; n< 80; n++) {
    lcd.scrollDisplayLeft();
    delay(500);
  }
  delay(4000);

  for(n=0; n < 80; n++) {
    lcd.scrollDisplayRight();
    delay(500);
  }
  delay(4000);
}