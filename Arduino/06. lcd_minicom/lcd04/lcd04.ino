#include <LiquidCrystal_I2C.h>
// 이
uint8_t lee[8] = {
  0x00,
  0x01,
  0x0D,
  0x13,
  0x13,
  0x13,
  0x0D,
  0x01
};
// 은
uint8_t eun[8] = {
  0x04,
  0x0A,
  0x0A,
  0x04,
  0x1F,
  0x08,
  0x08,
  0x0F
};

// 지
uint8_t ji[8] = {
  0x00,
  0x1F,
  0x01,
  0x03,
  0x05,
  0x0D,
  0x13,
  0x01
};

// 하트
uint8_t heart[8] = {
  0x00,
  0x00,
  0x1B,
  0x1F,
  0x0E,
  0x04,
  0x00,
  0x00
};

LiquidCrystal_I2C lcd(0x27, 16, 2);  // 객체 생성

void setup() {
  lcd.init();
  lcd.backlight();
  
  lcd.createChar(0, lee);  // 이 패턴 코드 0으로 저장
  lcd.createChar(1, eun);  // 은 패턴 코드 1로 저장
  lcd.createChar(2, ji);
  lcd.createChar(3, heart);
}

void loop() {
  lcd.setCursor(0,0);
  lcd.print("Hello, Arduino!");

  lcd.setCursor(0,1);
  lcd.print("My name is ");

  lcd.write(0);
  lcd.write(1);
  lcd.write(2);
  lcd.write(3);
}
