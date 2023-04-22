// 조이스틱 상태 시리얼 모니터 출력
const int x_joystick = A0; // x축 아날로그 연결핀
const int y_joystick = A1; // y축 아날로그 연결핀
const int z_sw = A2;  // z축 스위치 연결핀

void setup() {
  Serial.begin(115200);
  pinMode(z_sw, INPUT_PULLUP); // z축 스위치 연겨ㄹ핀 내부풀업 설정

}

void loop() {
  int dx, dy;
  boolean sw;

  dx = analogRead(x_joystick);
  dy = analogRead(y_joystick);
  sw = digitalRead(dx);

  // x축 방향 조이스틱 전압값 출력
  Serial.print("X-axis = ");
  Serial.println(dx);
  
 // y축 방향 조이스틱 전압값 출력
  Serial.print("Y-axis = ");
  Serial.println(dy);

// z축 스위치 상태 출력
  Serial.print("Z-swich = ");
  if(sw == 0) Serial.println("0(ON)");
  else Serial.println("1(OFF)");

  delay(2000);
}
