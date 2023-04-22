const int led_pin = 9; // LED 연결핀 (PWM 출력핀)

void setup() {
  // put your setup code here, to run once:
  pinMode(led_pin, OUTPUT); // PWM 출력 핀 출력 방향 설정
  digitalWrite(led_pin, 0); // LED OFF
}

void loop() {
  // put your main code here, to run repeatedly:
  int pwm_val;

  for (pwm_val = 0; pwm_val < 256; pwm_val += 5) {
    analogWrite(led_pin, pwm_val); // PWM 신호 출력
    delay(100);
  }

  digitalWrite(led_pin, 0); // LED OFF
  delay(2000);  // 2초 대기
}
