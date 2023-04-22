const int PULLUP_LED = 3;
const int PULLDOWN_LED = 4;

int state = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PULLUP_LED, OUTPUT); // 풀업 연결핀 출력 설정
  pinMode(PULLDOWN_LED, OUTPUT); // 풀다운 연결핀 출력 설정
}

void loop() {
  Serial.print("state value : ");
  Serial.println(state);

  digitalWrite(PULLDOWN_LED, state); // 풀다운 LED 연결핀 HIGH 출력
  digitalWrite(PULLUP_LED, state); // 풀업 LED 연결핀 HIGH 출력
 
  state = !state; // 현재 상태를 반전
  delay(500);

}
