# include <Led.h>
# include <Button.h>
# include <Minicom.h>

Led led(9);
MiniCom com;
Button btn(2);

const int tilt_pin = 4;
int count = 0;

void reset() {
  count = 0;
  com.print(1, "Count:", count);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(tilt_pin, INPUT);  // 기울기 스위치 입력 설정
  com.init();
  btn.setCallback(reset);
  com.print(0, "ManBoGi");
  com.print(1, "Count:", count);
}

void loop() {
  bool t_sw1, t_sw2;
  btn.check();

  t_sw1 = digitalRead(tilt_pin);  //  기울기 센서 첫 번째 상태 읽기
  delay(100);
  t_sw2 = digitalRead(tilt_pin); // 기울기 센서 두 번째 상태 읽기

  if(t_sw1 == LOW && t_sw2 == HIGH) {  // Tilt SW on --> Off 되는 순간
    count ++;
    com.print(1, "Count:", count);
  }
}
